"""HPF Research Orchestrator v0 — evidence-collection pipeline.

Turns a research request into a session artifact:
plan -> collect -> extract -> draft findings.

Honest scope: no LLM. Extraction is mechanical (HTML -> text, paragraph
chunking, keyword-dense selection). Findings are DRAFTS requiring
adjudication. Nothing here mutates the corpus: sessions are operational
evidence records, not corpus knowledge. Corpus admission happens later,
through the normal authoring/validation pipeline, if the owner so decides.

Usage:
    python research.py --topic "..." --goal "..." [--depth quick|standard|deep]
        [--url https://... ...] [--import-md file.md --source-url https://...]
        [--dir sessions]

Stages:
    plan   - research question, keywords, depth
    collect- fetch URLs / import markdown
    extract- chunk text into evidence entries
    findings- rank evidence, emit draft candidate findings
"""

import argparse
import datetime
import html.parser
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

try:
    from connectors import EVIDENCE_CLASSES, plan_evidence_classes
    from connectors.community import validate_payload
except ImportError:
    EVIDENCE_CLASSES = ("primary", "code", "community", "scientific", "operational")

    def plan_evidence_classes(topic, depth, keywords):
        return {}

    def validate_payload(payload):
        return []

try:
    from watchlist import load, match_topic
except ImportError:
    def load(path=None):
        return {}

    def match_topic(topic, keywords, watchlist=None):
        return {"matched": [], "keyword_overlap": 0.0}

STAGES = [
    ("plan", "research question, keywords, depth"),
    ("collect", "sources fetched or imported"),
    ("extract", "text chunked into evidence entries"),
    ("findings", "draft candidate findings (not conclusions)"),
]

EVIDENCE_BUDGETS = {"primary": 40, "code": 10, "community": 20, "scientific": 25, "operational": 15}

EXCERPT_LIMIT = 1200

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with",
    "vs", "versus", "about", "what", "is", "are", "compare", "research",
    "it", "its", "how", "why", "which", "this", "that", "these", "those",
    "they", "them", "their", "we", "you", "your", "will", "can", "when",
}


class TextExtractor(html.parser.HTMLParser):
    """HTML -> text with real paragraph boundaries.

    Block elements emit a newline on BOTH start and end tags, so
    <p>a</p><p>b</p> produces "a\n\nb" — dense blog HTML keeps its
    paragraph structure instead of collapsing into one run of text.
    """

    BLOCK = ("p", "div", "li", "h1", "h2", "h3", "h4", "tr", "br", "section", "article", "blockquote", "pre", "table",
             "details", "summary", "figure", "figcaption", "aside", "main", "dl", "dt", "dd", "ol", "ul", "nav")

    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg", "head"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg", "head"):
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", "".join(self.parts)))


def html_to_text(raw: str) -> str:
    p = TextExtractor()
    p.feed(raw)
    return p.text().strip()


def fetch(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "HPF-Research-Orchestrator/0.1 (+research evidence collection)"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    return html_to_text(raw)


def classify_url(url: str) -> str:
    """Mechanical evidence-class inference from the URL host."""
    host = (url or "").lower()
    if any(d in host for d in ("github.com", "gitlab.com", "bitbucket.org")):
        return "code"
    if any(d in host for d in ("arxiv.org", "acm.org", "ieee.org", "scholar.google", "paper", "proceedings")):
        return "scientific"
    if any(d in host for d in ("reddit.com", "news.ycombinator.com", "stackoverflow.com", "discord", "reddit")):
        return "community"
    if any(d in host for d in ("benchmark", "report", "telemetry", "status", "metrics", "speedtest", "apdex")):
        return "operational"
    return "primary"


def is_boilerplate(text: str) -> bool:
    """True for page chrome that must never become evidence.

    Conservative phrase patterns: matches real chrome (subscribe boxes,
    footers, tag clouds, cookie banners, translation bars, search UI)
    while keeping genuine content that merely mentions the words.
    """
    t = " " + re.sub(r"\s+", " ", text.lower()).strip() + " "
    patterns = (
        r"selected tags",
        r"all tags",
        r"matching tags",
        r"no tags found",
        r"related posts?",
        r"related articles?",
        r"you may also like",
        r"more like this",
        r"table of contents",
        r"in this article",
        r"on this page",
        r"read more",
        r"continue reading",
        r"view all",
        r"opens? in a new tab",
        r"login opens",
        r"contact sales",
        r"sign up",
        r"start building",
        r"start for free",
        r"no credit card required",
        r"search is temporarily unavailable",
        r"subscribe",
        r"thanks for subscribing",
        r"check your inbox",
        r"never share your email",
        r"privacy choices",
        r"privacy policy",
        r"terms of use",
        r"terms of service",
        r"report security issues",
        r"cookie banner",
        r"accept cookies",
        r"cookie settings",
        r"we use cookies",
        r"your privacy",
        r"follow (us|on social media)",
        r"this post is also available in",
        r"post syndicated from",
        r"©\s*\d{4}",
        r"\.\.\.\s*manage consent",
        r"language switcher",
        r"switch to",
        r"copyright notice",
        r"all rights reserved",
    )
    for p in patterns:
        if re.search(p, t):
            return True
    return False


def split_paragraphs(text: str):
    """Split text into paragraphs, keeping only prose (sentence-bearing).

    Navigation chrome, TOC lists, boilerplate and menu fragments never
    become evidence. Returns (paragraphs, dropped_count).
    """
    parts = re.split(r"\n\s*\n+", text)
    out = []
    dropped = 0
    for p in parts:
        p = " ".join(p.split())
        if len(p) < 40:
            dropped += 1
            continue
        if "." not in p:
            dropped += 1
            continue
        if is_boilerplate(p):
            dropped += 1
            continue
        out.append(p)
    return out, dropped


def keep_paragraphs(paras: list, cls: str) -> list:
    """Evidence budget: no single source may flood the session."""
    return paras[: EVIDENCE_BUDGETS.get(cls, 20)]


def extract_source(text: str, cls: str, seen: set):
    """Turn collected text into kept paragraphs + per-source failure metrics.

    seen: session-level set of normalized kept excerpts (cross-source
    duplicate measurement — recorded, not removed). Returns (metrics,
    kept_paragraphs).
    """
    paras, dropped = split_paragraphs(text)
    kept = keep_paragraphs(paras, cls)
    truncated = sum(1 for p in kept if len(p) > EXCERPT_LIMIT)
    duplicates = 0
    for p in kept:
        norm = re.sub(r"\s+", " ", p.lower())[:200]
        if norm in seen:
            duplicates += 1
        else:
            seen.add(norm)
    lengths = [len(p) for p in kept]
    return {
        "paragraphs": len(paras),
        "evidence": len(kept),
        "chrome_dropped": dropped,
        "truncated": truncated,
        "duplicates": duplicates,
        "boilerplate_ratio": round(dropped / max(1, dropped + len(paras)), 3),
        "coverage": round(sum(lengths) / max(1, len(text)), 3),
        "avg_para_chars": round(sum(lengths) / max(1, len(lengths))),
        "largest_para_chars": max(lengths) if lengths else 0,
    }, kept


def extraction_health(sources: list) -> str:
    """Session-wide extraction-health line (longitudinal metric)."""
    kept_t = sum(s.get("evidence", 0) for s in sources if s.get("status") in ("fetched", "imported"))
    chrome = sum(s.get("chrome_dropped", 0) for s in sources if s.get("status") in ("fetched", "imported"))
    paras_t = sum(s.get("paragraphs", 0) for s in sources if s.get("status") in ("fetched", "imported"))
    dup = sum(s.get("duplicates", 0) for s in sources if s.get("status") in ("fetched", "imported"))
    trunc = sum(s.get("truncated", 0) for s in sources if s.get("status") in ("fetched", "imported"))
    avg = round(sum(s.get("avg_para_chars", 0) for s in sources if s.get("status") in ("fetched", "imported")) / max(1, kept_t))
    largest = max((s.get("largest_para_chars", 0) for s in sources if s.get("status") in ("fetched", "imported")), default=0)
    return (f"extraction health: boilerplate_ratio {round(chrome / max(1, paras_t), 3)}, "
            f"duplicate_ratio {round(dup / max(1, kept_t), 3)}, truncated {trunc}, "
            f"avg_para {avg} chars, largest_para {largest} chars")


def keywords(topic: str, depth: str) -> list:
    words = [w.lower() for w in re.findall(r"[A-Za-z0-9-]+", topic)]
    kw = [w for w in words if w not in STOPWORDS and len(w) > 1]
    if depth == "deep":
        kw.extend(["architecture", "architecture", "limitations", "performance", "security"])
    elif depth == "standard":
        kw.extend(["architecture", "performance", "limitations"])
    return sorted(set(kw))


def density(paragraph: str, kw: list) -> float:
    text = re.sub(r"https?://\S+|`[^`]*`|\[[^\]]*\]\([^)]*\)", "", paragraph.lower())
    return sum(text.count(k) for k in kw) / max(1, len(text))


def summary_of(s, sdir: Path = None) -> dict:
    duration_s = None
    if s.get("started") and s.get("finished"):
        try:
            a = datetime.datetime.fromisoformat(s["started"])
            b = datetime.datetime.fromisoformat(s["finished"])
            duration_s = max(0, round((b - a).total_seconds()))
        except (ValueError, TypeError):
            duration_s = None
    adjudicated = None
    if sdir is not None:
        adjf = sdir / "adjudication.json"
        if adjf.exists():
            try:
                adjudicated = json.loads(adjf.read_text(encoding="utf-8")).get("summary")
            except (json.JSONDecodeError, OSError):
                adjudicated = None
    return {
        "id": s.get("id"),
        "topic": s.get("topic"),
        "goal": s.get("goal"),
        "audience": s.get("audience"),
        "depth": s.get("depth"),
        "status": s.get("status"),
        "created": s.get("created"),
        "duration_s": duration_s,
        "sources": len(s.get("sources") or []),
        "evidence": len(s.get("evidence") or []),
        "findings": len(s.get("findings") or []),
        "community_signals": sum(1 for f in (s.get("findings") or []) if f.get("status") == "community_signal"),
        "adjudicated": adjudicated,
        "failed": sum(1 for x in (s.get("sources") or []) if x.get("status") == "failed"),
    }


def write_manifest(root: Path) -> int:
    entries = []
    for d in sorted(root.iterdir()):
        if not d.is_dir():
            continue
        sf = d / "session.json"
        if not sf.exists():
            continue
        try:
            entries.append(summary_of(json.loads(sf.read_text(encoding="utf-8")), d))
        except (json.JSONDecodeError, OSError):
            continue
    entries.sort(key=lambda e: e.get("created") or "", reverse=True)
    (root / "index.json").write_text(
        json.dumps({"schema": "hpf-sessions-manifest-v0", "sessions": entries}, indent=2),
        encoding="utf-8",
    )
    return len(entries)


def promote_session(sid: str, src_root: Path, exports_root: Path) -> int:
    src = src_root / sid
    if not src.is_dir() or not (src / "session.json").exists():
        print(f"! session not found: {sid}")
        return 2
    dst = exports_root / "sessions" / sid
    if dst.exists():
        print(f"! refused: {sid} already released (sessions are immutable once released)")
        return 3
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src / "session.json", dst / "session.json")
    if (src / "session.md").exists():
        shutil.copy2(src / "session.md", dst / "session.md")
    adj = src / "adjudication.json"
    if adj.exists():
        shutil.copy2(adj, dst / "adjudication.json")
    n = write_manifest(exports_root / "sessions")
    print(f"Released {sid} -> exports/sessions ({n} released sessions in manifest)")
    return 0


def make_session(topic, goal, audience, depth, sources, evidence, findings, activity, started, finished, plan, dirpath, watch=None, provenance=None):
    now = datetime.datetime.now(datetime.timezone.utc)
    sid = now.strftime("%Y-%m-%d-%H%M") + "-" + re.sub(r"[^a-z0-9-]+", "-", topic.lower()).strip("-")[:30]
    session = {
        "schema": "hpf-session-v0",
        "id": sid,
        "topic": topic,
        "goal": goal,
        "audience": audience,
        "depth": depth,
        "created": now.isoformat(),
        "started": started,
        "finished": finished,
        "activity": activity,
        "plan": plan,
        "watchlist": watch or {"matched": [], "keyword_overlap": 0.0},
        "provenance": provenance or {"events": []},
        "status": "draft",
        "stages": [{"name": n, "detail": d, "state": "done"} for n, d in STAGES],
        "sources": sources,
        "evidence": evidence,
        "findings": findings,
        "notes": (
            "Extraction v0 is mechanical: paragraphs, keyword density, truncation. "
            "Findings are DRAFT candidate findings requiring adjudication before any "
            "corpus admission. Sessions are operational evidence records."
        ),
    }
    out = Path(dirpath) / sid
    out.mkdir(parents=True, exist_ok=True)
    (out / "session.json").write_text(json.dumps(session, indent=2), encoding="utf-8")

    md = [f"# Research session: {topic}", "", f"Goal: {goal}", f"Audience: {audience} · Depth: {depth}",
          f"Status: {session['status']} · id: {sid}", "", "## Sources"]
    for s in sources:
        md.append(f"- [{s['title']}]({s['url']}) — {s['status']} ({s.get('chars', 0)} chars)")
    md.append("")
    md.append("## Findings (drafts)")
    for f in findings:
        md.append(f"- **{f['claim'][:180]}{'…' if len(f['claim']) > 180 else ''}**")
        md.append(f"  - sources: {', '.join(f['sources'])}")
        md.append(f"  - status: {f['status']} · method: {f['method']}")
    md.append("")
    md.append("## Evidence")
    for ev in evidence:
        md.append(f"- [{ev['id']}] {ev['excerpt'][:240]}{'…' if len(ev['excerpt']) > 240 else ''} ({ev['source']})")
    (out / "session.md").write_text("\n".join(md), encoding="utf-8")
    return sid, session


def main():
    ap = argparse.ArgumentParser(description="HPF Research Orchestrator v0")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--goal", default="")
    ap.add_argument("--audience", default="Internal", choices=["Internal", "Blog", "Whitepaper"])
    ap.add_argument("--depth", default="standard", choices=["quick", "standard", "deep"])
    ap.add_argument("--url", action="append", default=[], help="URL to fetch (repeatable)")
    ap.add_argument("--import-md", action="append", default=[], help="markdown/text file to import (repeatable)")
    ap.add_argument("--source-url", action="append", default=[], help="URL for the imported file (paired with --import-md)")
    ap.add_argument("--community-payload", action="append", default=[], help="community evidence payload JSON (see connectors/community.py)")
    ap.add_argument("--from-events", action="append", default=[], help="research event ids (evt-...) this session is seeded from (repeatable, comma-separated ok)")
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent / "sessions"))
    ap.add_argument("--sync-web", default="", help="copy sessions here and write sessions/index.json (e.g. website-hpf/sessions)")
    args = ap.parse_args()

    kw = keywords(args.topic, args.depth)
    sources = []
    evidence = []
    findings = []
    activity = []
    now = lambda: datetime.datetime.now(datetime.timezone.utc)

    stage = lambda n, d: print(f"[{n}] {d}")
    log = lambda msg: (activity.append({"ts": now().isoformat(), "msg": msg}), print(f"  ~ {msg}"))

    started = now().isoformat()
    log("Research started")

    stage("plan", f"keywords: {', '.join(kw) or '(none)'}")
    evidence_plan = plan_evidence_classes(args.topic, args.depth, kw)
    plan_lines = []
    for cls in EVIDENCE_CLASSES:
        weight, reason = evidence_plan.get(cls, ("low", "no rule matched"))
        plan_lines.append(f"{cls}={weight} ({reason})")
        log(f"Evidence class {cls}: {weight} — {reason}")
    watchlist = {}
    wl_ok = True
    try:
        watchlist = load()
    except (OSError, ValueError) as e:
        wl_ok = False
        log(f"Watchlist unavailable: {e}")
    watch = match_topic(args.topic, kw, watchlist) if wl_ok else {"matched": [], "keyword_overlap": 0.0}
    if watch["matched"]:
        log(f"Watchlist touches: {', '.join(watch['matched'])} (keyword overlap {watch['keyword_overlap']})")
    else:
        log("Watchlist: no watched entries touched by this topic")
    prov_events = []
    for raw in args.from_events:
        for eid in raw.split(","):
            eid = eid.strip()
            if not eid:
                continue
            if re.fullmatch(r"evt-[0-9a-f]{12}", eid):
                prov_events.append(eid)
            else:
                log(f"ignored malformed event id: {eid}")
    if prov_events:
        log(f"Provenance: seeded from {', '.join(prov_events)}")
    log(f"Research plan built: {len(kw)} keywords, depth {args.depth}")
    session_plan = {
        "keywords": kw,
        "depth": args.depth,
        "evidence_classes": {cls: evidence_plan.get(cls, ("low", ""))[0] for cls in EVIDENCE_CLASSES},
    }

    stage("collect", f"{len(args.url)} urls, {len(args.import_md)} imports, {len(args.community_payload)} community payloads")
    seen = set()
    for i, url in enumerate(args.url):
        try:
            text = fetch(url)
            title = url.split("/")[2] if len(url.split("/")) > 2 else url
            cls = classify_url(url)
            metrics, kept = extract_source(text, cls, seen)
            sources.append({"url": url, "title": title, "status": "fetched", "chars": len(text), "class": cls, **metrics})
            for para in kept:
                evidence.append({"id": f"ev-{len(evidence)+1}", "source": url, "excerpt": para[:EXCERPT_LIMIT], "class": cls})
            log(f"Collected {title} ({len(text)} chars, class {cls}: {metrics['evidence']}/{metrics['paragraphs']} paragraphs kept, {metrics['chrome_dropped']} chrome dropped, coverage {metrics['coverage']}, dup {metrics['duplicates']})")
        except Exception as e:
            sources.append({"url": url, "title": url, "status": "failed", "error": str(e), "class": classify_url(url)})
            log(f"Failed {url}: {e}")

    for i, path in enumerate(args.import_md):
        text = Path(path).read_text(encoding="utf-8")
        title = Path(path).stem
        url = args.source_url[i] if i < len(args.source_url) else f"file:{path}"
        metrics, kept = extract_source(text, "primary", seen)
        sources.append({"url": url, "title": title, "status": "imported", "chars": len(text), "class": "primary", **metrics})
        for para in kept:
            evidence.append({"id": f"ev-{len(evidence)+1}", "source": url, "excerpt": para[:EXCERPT_LIMIT], "class": "primary"})
        log(f"Imported {title} ({len(text)} chars, class primary: {metrics['evidence']}/{metrics['paragraphs']} paragraphs kept, {metrics['chrome_dropped']} dropped)")

    for path in args.community_payload:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        problems = validate_payload(payload)
        if problems:
            log(f"Community payload {Path(path).name} rejected: {', '.join(problems)}")
            continue
        sub = payload.get("subreddit", "unknown")
        thread = payload.get("thread", "")
        url = payload.get("url") or f"reddit://r/{sub}/comments/{thread}"
        comments = payload.get("comments") or []
        n = len([c for c in comments if c.get("text")])
        sources.append({
            "url": url, "title": f"r/{sub} community signal ({n} comments)", "status": "imported",
            "chars": sum(len(c.get("text", "")) for c in comments), "class": "community",
            "community": {"subreddit": sub, "thread": thread, "score": payload.get("score"), "comments": n},
        })
        for c in comments:
            text = (c.get("text") or "").strip()
            if len(text) > 80:
                evidence.append({
                    "id": f"ev-{len(evidence)+1}", "source": url, "excerpt": text[:600], "class": "community",
                    "community": {"score": c.get("score"), "author": c.get("author"), "url": c.get("url"), "date": c.get("date") or ""},
                })
        log(f"Community signal r/{sub}: {n} comments (class community)")

    stage("extract", f"{len(evidence)} evidence entries from {len(sources)} sources")
    log(f"Extracted {len(evidence)} evidence entries from {len(sources)} sources")
    for s in sources:
        if s.get("status") in ("fetched", "imported"):
            log(f"  coverage {s['title']}: {s.get('evidence', 0)} paragraphs kept, coverage {s.get('coverage', 0)}, {s.get('chrome_dropped', 0)} chrome dropped, {s.get('duplicates', 0)} duplicates")
    log(f"~ {extraction_health(sources)}")

    stage("findings", "keyword-density ranking (mechanical, draft only)")
    per_source = {}
    for ev in evidence:
        per_source.setdefault(ev["source"], []).append(ev)
    community_findings = 0
    for url, entries in per_source.items():
        ranked = sorted(entries, key=lambda e: density(e["excerpt"], kw), reverse=True)[:3]
        src = next((s for s in sources if s.get("url") == url), {})
        is_community = src.get("class") == "community" or any(e.get("class") == "community" for e in entries)
        for ev in ranked:
            if is_community:
                community_findings += 1
                status = "community_signal"
                community = {"class": "community", "frequency": len(entries)}
                sub = (src.get("community") or {}).get("subreddit")
                if sub:
                    community["subreddit"] = sub
            else:
                status = "needs_adjudication"
                community = None
            ev_urls = [e.get("community", {}).get("url") or e.get("source") or e.get("url") for e in ranked]
            dates = sorted({e.get("community", {}).get("date") or "" for e in ranked if e.get("community", {}).get("date")})
            f = {
                "id": f"f-{len(findings)+1}",
                "claim": ev["excerpt"][:400],
                "confidence": None,
                "status": status,
                "sources": [u for u in dict.fromkeys(ev_urls) if u],
                "evidence": [e["id"] for e in ranked],
                "method": "keyword-density-v0",
            }
            if dates:
                f["dates"] = dates
            if community:
                f["community"] = community
            findings.append(f)
    log(f"Drafted {len(findings)} candidate findings (keyword-density-v0), {community_findings} as community signals")

    finished = now().isoformat()
    log("Session artifact written")

    sid, session = make_session(args.topic, args.goal, args.audience, args.depth,
                                sources, evidence, findings, activity, started, finished, session_plan, args.dir,
                                watch=watch, provenance={"events": prov_events})
    print(f"\nSession {sid} written: {len(sources)} sources, {len(evidence)} evidence, {len(findings)} draft findings")
    print(f"  {Path(args.dir) / sid}")

    if args.sync_web:
        dst = Path(args.sync_web)
        dst.mkdir(parents=True, exist_ok=True)
        src_dir = Path(args.dir) / sid
        shutil.copytree(src_dir, dst / sid, dirs_exist_ok=True)
        n = write_manifest(dst)
        print(f"Synced to website sessions: {dst} ({n} sessions in manifest)")


if __name__ == "__main__":
    main()
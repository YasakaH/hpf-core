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

STAGES = [
    ("plan", "research question, keywords, depth"),
    ("collect", "sources fetched or imported"),
    ("extract", "text chunked into evidence entries"),
    ("findings", "draft candidate findings (not conclusions)"),
]

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with",
    "vs", "versus", "about", "what", "is", "are", "compare", "research",
}


class TextExtractor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg", "head"):
            self.skip += 1
        elif tag in ("p", "div", "li", "h1", "h2", "h3", "h4", "tr", "br", "section", "article"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg", "head"):
            self.skip = max(0, self.skip - 1)

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


def split_paragraphs(text: str):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 80]


def keywords(topic: str, depth: str) -> list:
    words = [w.lower() for w in re.findall(r"[A-Za-z0-9-]+", topic)]
    kw = [w for w in words if w not in STOPWORDS and len(w) > 1]
    if depth == "deep":
        kw.extend(["architecture", "architecture", "limitations", "performance", "security"])
    elif depth == "standard":
        kw.extend(["architecture", "performance", "limitations"])
    return sorted(set(kw))


def density(paragraph: str, kw: list) -> float:
    text = paragraph.lower()
    return sum(text.count(k) for k in kw) / max(1, len(paragraph))


def make_session(topic, goal, audience, depth, sources, evidence, findings, activity, started, finished, dirpath):
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
    log(f"Research plan built: {len(kw)} keywords, depth {args.depth}")

    stage("collect", f"{len(args.url)} urls, {len(args.import_md)} imports")
    for i, url in enumerate(args.url):
        try:
            text = fetch(url)
            title = url.split("/")[2] if len(url.split("/")) > 2 else url
            sources.append({"url": url, "title": title, "status": "fetched", "chars": len(text)})
            for para in split_paragraphs(text):
                evidence.append({"id": f"ev-{len(evidence)+1}", "source": url, "excerpt": para[:600]})
            log(f"Collected {title} ({len(text)} chars)")
        except Exception as e:
            sources.append({"url": url, "title": url, "status": "failed", "error": str(e)})
            log(f"Failed {url}: {e}")

    for i, path in enumerate(args.import_md):
        text = Path(path).read_text(encoding="utf-8")
        title = Path(path).stem
        url = args.source_url[i] if i < len(args.source_url) else f"file:{path}"
        sources.append({"url": url, "title": title, "status": "imported", "chars": len(text)})
        for para in split_paragraphs(text):
            evidence.append({"id": f"ev-{len(evidence)+1}", "source": url, "excerpt": para[:600]})
        log(f"Imported {title} ({len(text)} chars)")

    stage("extract", f"{len(evidence)} evidence entries from {len(sources)} sources")
    log(f"Extracted {len(evidence)} evidence entries from {len(sources)} sources")

    stage("findings", "keyword-density ranking (mechanical, draft only)")
    per_source = {}
    for ev in evidence:
        per_source.setdefault(ev["source"], []).append(ev)
    for url, entries in per_source.items():
        ranked = sorted(entries, key=lambda e: density(e["excerpt"], kw), reverse=True)[:3]
        for ev in ranked:
            findings.append({
                "id": f"f-{len(findings)+1}",
                "claim": ev["excerpt"][:400],
                "confidence": None,
                "status": "needs_adjudication",
                "sources": [ev["source"]],
                "method": "keyword-density-v0",
            })
    log(f"Drafted {len(findings)} candidate findings (keyword-density-v0)")

    finished = now().isoformat()
    log("Session artifact written")

    sid, session = make_session(args.topic, args.goal, args.audience, args.depth,
                                sources, evidence, findings, activity, started, finished, args.dir)
    print(f"\nSession {sid} written: {len(sources)} sources, {len(evidence)} evidence, {len(findings)} draft findings")
    print(f"  {Path(args.dir) / sid}")

    if args.sync_web:
        dst = Path(args.sync_web)
        dst.mkdir(parents=True, exist_ok=True)
        src_dir = Path(args.dir) / sid
        shutil.copytree(src_dir, dst / sid, dirs_exist_ok=True)
        ids = sorted(p.name for p in dst.iterdir() if p.is_dir())
        (dst / "index.json").write_text(
            json.dumps({"schema": "hpf-sessions-index-v0", "sessions": [{"id": i} for i in ids]}, indent=2),
            encoding="utf-8",
        )
        print(f"Synced to website sessions: {dst} ({len(ids)} sessions)")


if __name__ == "__main__":
    main()
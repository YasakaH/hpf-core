"""HPF Watchlist — shared service for the watchlist configuration.

The watchlist (config/watchlist.yaml) is operational configuration: a
maintained list of technologies/vendors/repos the programme cares about.
No discovery, no scoring, no automation. Every consumer (research
orchestrator today; future consumers) imports the SAME API here:

    load(path=None)                -> {section: [entry-dicts]}  (canonical)
    entries(watchlist=None)        -> flat list of normalized entries
    match_topic(topic, keywords)   -> {"matched": [ids], "coverage": float}

Matching is identifier-based, never substring-based: an entry matches a
topic when the topic contains one of its aliases as a word-bounded token,
or a session keyword equals an alias. This prevents false positives such
as "chrome" matching "chromedriver".

YAML is parsed with PyYAML when available and a minimal stdlib subset
parser otherwise (sections, `- id:` items with `aliases: [...]` and
`type:` — the watchlist's shape).
"""

import json
import re
import sys
from pathlib import Path

WATCHLIST_PATH = Path(__file__).resolve().parent / "config" / "watchlist.yaml"


def _parse_subset(text: str) -> dict:
    """Minimal YAML subset parser for the watchlist's shape."""
    topics = {}
    section = None
    item = None
    field = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- id:"):
            if section is None:
                raise ValueError("watchlist item before any section header")
            item = {"id": line[4:].strip()}
            topics.setdefault(section, []).append(item)
            field = None
            continue
        if line.startswith("aliases:"):
            if item is None:
                raise ValueError("aliases outside an item")
            rest = line[8:].strip()
            if rest.startswith("[") and rest.endswith("]"):
                item["aliases"] = [a.strip().strip("'\"") for a in rest[1:-1].split(",") if a.strip()]
            else:
                field = "aliases"
            continue
        if line.startswith("type:"):
            if item is None:
                raise ValueError("type outside an item")
            item["type"] = line[5:].strip()
            field = None
            continue
        if line.startswith("- ") and field == "aliases":
            item.setdefault("aliases", []).append(line[2:].strip())
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*$", line)
        if m and item is None:
            section = m.group(1)
            continue
        raise ValueError(f"unexpected watchlist line: {raw}")
    if not topics:
        raise ValueError("watchlist has no sections")
    return topics


def load(path: Path = None) -> dict:
    """Return {section: [{"id", "aliases", "type"}]} — canonical entries."""
    p = path or WATCHLIST_PATH
    text = p.read_text(encoding="utf-8")
    try:
        import yaml  # noqa: F401
        data = yaml.safe_load(text)
    except ImportError:
        data = _parse_subset(text)
    except Exception:
        raise
    topics = (data or {}).get("topics")
    if not isinstance(topics, dict) or not topics:
        raise ValueError("watchlist must define a 'topics' mapping")
    out = {}
    for section, items in topics.items():
        out[str(section)] = []
        for it in items:
            if isinstance(it, str):
                out[str(section)].append({"id": it, "aliases": [it], "type": ""})
                continue
            eid = it.get("id")
            if not eid:
                raise ValueError(f"watchlist entry without id in {section}")
            aliases = [str(a).lower() for a in (it.get("aliases") or [eid])]
            if eid.lower() not in aliases:
                aliases.insert(0, eid.lower())
            out[str(section)].append({"id": str(eid), "aliases": aliases, "type": str(it.get("type") or "")})
    return out


def entries(watchlist: dict = None) -> list:
    """Flat list of normalized entries: {id, aliases, type, section}."""
    w = watchlist if watchlist is not None else load()
    return [{"id": e["id"], "aliases": e["aliases"], "type": e["type"], "section": s}
            for s, es in w.items() for e in es]


def _alias_in_topic(alias: str, topic_lower: str, keywords: list) -> bool:
    if any(alias == k for k in keywords):
        return True
    pattern = r"(^|[^a-z0-9]+)" + re.escape(alias) + r"([^a-z0-9]+|$)"
    return re.search(pattern, topic_lower) is not None


def match_topic(topic: str, keywords: list, watchlist: dict = None) -> dict:
    """Boundary-aware, identifier-based matching.

    Returns {"matched": [entry ids], "coverage": fraction of keywords that
    matched any watchlist entry}. Coverage is keyword-level overlap, not a
    relevance judgement — it is honest by construction.
    """
    w = watchlist if watchlist is not None else load()
    topic_lower = " " + topic.lower() + " "
    kw = [str(k).lower() for k in (keywords or [])]
    matched = []
    covered_keywords = set()
    for e in entries(w):
        if any(_alias_in_topic(a, topic_lower, kw) for a in e["aliases"]):
            matched.append(e["id"])
            for a in e["aliases"]:
                for k in kw:
                    if a == k:
                        covered_keywords.add(k)
    coverage = round(len(covered_keywords) / max(1, len(kw)), 3) if kw else 0.0
    return {"matched": sorted(set(matched)), "coverage": coverage}


def watchlist_matches(keywords: list, watchlist: dict = None) -> list:
    """Back-compat: flat "section: id" strings for entries matching keywords."""
    w = watchlist if watchlist is not None else load()
    out = []
    for e in entries(w):
        if any(a == str(k).lower() for a in e["aliases"] for k in keywords):
            out.append(f"{e['section']}: {e['id']}")
    return out


def to_json(watchlist: dict = None) -> dict:
    return {"schema": "hpf-watchlist-v0", "topics": watchlist if watchlist is not None else load()}


def main():
    import argparse
    ap = argparse.ArgumentParser(description="HPF watchlist service")
    ap.add_argument("--check", action="store_true", help="validate the watchlist file")
    ap.add_argument("--out", default="", help="emit watchlist as JSON (e.g. website-hpf/data/watchlist.json)")
    args = ap.parse_args()
    try:
        w = load()
    except (OSError, ValueError) as e:
        print(f"! watchlist invalid: {e}")
        return 2
    if args.check:
        n = sum(len(v) for v in w.values())
        print(f"watchlist ok: {len(w)} sections, {n} entries")
        return 0
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(to_json(w), indent=2), encoding="utf-8")
    n = sum(len(v) for v in w.values())
    print(f"watchlist written: {out} ({len(w)} sections, {n} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

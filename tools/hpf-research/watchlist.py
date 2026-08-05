"""HPF Watchlist — shared service for the watchlist configuration.

The watchlist (config/watchlist.yaml) is operational configuration: a
maintained list of technologies/vendors/repos the programme cares about.
No discovery, no scoring, no automation. Every consumer (research
orchestrator today; publishing, website, future discovery) imports the
SAME API here:

    load(path=None)              -> {"schema": str, "topics": {section: [entries]}}
    entries(watchlist=None)      -> flat list of normalized entries
    match_topic(topic, keywords) -> {"matched": [ids], "coverage": float}

Schema: hpf-watchlist-v1. Entries carry stable vendor-independent ids
(tech.<domain>.<name>), a display `name`, explicit `aliases`, and `type`.
Loading validates: schema version, globally unique ids, aliases present
and unique, non-empty sections, required type. A violation raises
ValueError so every consumer fails fast; `--check` reports it nicely.

Matching is identifier-based, never substring-based. All aliases, names,
topic text and keywords are normalized (lowercase, non-alphanumerics ->
single space) and matched as word-bounded tokens: an entry matches when a
normalized alias (or its normalized name) occurs as a token sequence in
the normalized topic, or a normalized keyword equals an alias. This
prevents false positives such as "chrome" matching "chromedriver".

Coverage is the fraction of keywords that equal an alias of any matched
entry. It measures keyword overlap, NOT relevance or confidence — and it
depends on keyword generation, so treat it as a debugging metric: do not
compare coverage across sessions (chronicle entry 30).

YAML is parsed with PyYAML when available and a minimal stdlib subset
parser otherwise (schema, sections, `- id:` items with `name:`,
`aliases: [...]`/block list, `type:`).
"""

import json
import re
import sys
from pathlib import Path

WATCHLIST_PATH = Path(__file__).resolve().parent / "config" / "watchlist.yaml"
SCHEMA = "hpf-watchlist-v1"


def normalize(text: str) -> str:
    """Lowercase; every run of non-alphanumerics becomes a single space."""
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def _parse_subset(text: str) -> dict:
    """Minimal YAML subset parser for the watchlist's shape.

    Handles: `schema: <version>` (top-level scalar), `topics:` followed by
    section headers and `- id:` items with `name:`, `aliases: [...]` (or a
    block list) and `type:`.
    """
    data = {"schema": "", "topics": {}}
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
            data["topics"].setdefault(section, []).append(item)
            field = None
            continue
        if line.startswith("name:"):
            if item is None:
                raise ValueError("name outside an item")
            item["name"] = line[5:].strip()
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
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and item is None:
            key, rest = m.group(1), m.group(2).strip()
            if key == "schema" and rest:
                data["schema"] = rest.strip().strip("'\"")
                continue
            if key == "topics":
                section = None
                continue
            if section is not None and key not in ("schema", "topics"):
                section = key
                continue
        raise ValueError(f"unexpected watchlist line: {raw}")
    if not data["topics"]:
        raise ValueError("watchlist has no sections")
    return data


def _validate(schema: str, topics: dict) -> dict:
    """Canonicalize + validate. Raises ValueError on any violation."""
    if schema != SCHEMA:
        raise ValueError(f"watchlist schema {schema!r} != expected {SCHEMA!r}")
    if not isinstance(topics, dict) or not topics:
        raise ValueError("watchlist must define a non-empty 'topics' mapping")
    seen_ids = {}
    seen_aliases = {}
    out = {}
    for section, items in topics.items():
        section = str(section)
        if not items:
            raise ValueError(f"watchlist section {section!r} is empty")
        out[section] = []
        for it in items or []:
            if isinstance(it, str):
                it = {"id": it}
            eid = str(it.get("id") or "").strip()
            if not eid:
                raise ValueError(f"watchlist entry without id in {section}")
            if eid in seen_ids:
                raise ValueError(f"duplicate watchlist id {eid!r} (sections {seen_ids[eid]!r} and {section!r})")
            seen_ids[eid] = section
            raw_aliases = it.get("aliases") or []
            aliases = sorted({normalize(a) for a in raw_aliases if str(a).strip()})
            if not aliases:
                raise ValueError(f"watchlist entry {eid!r} has no aliases")
            for a in aliases:
                if a in seen_aliases:
                    raise ValueError(f"duplicate watchlist alias {a!r} (entry {seen_aliases[a]!r} vs {eid!r})")
                seen_aliases[a] = eid
            etype = str(it.get("type") or "").strip()
            if not etype:
                raise ValueError(f"watchlist entry {eid!r} has no type")
            name = str(it.get("name") or eid).strip()
            out[section].append({
                "id": eid,
                "name": name,
                "aliases": sorted(aliases),
                "type": etype,
            })
    return out


def load(path: Path = None) -> dict:
    """Return {"schema": str, "topics": {section: [entry-dicts]}} — validated."""
    p = Path(path) if path else WATCHLIST_PATH
    text = p.read_text(encoding="utf-8")
    try:
        import yaml  # noqa: F401
        data = yaml.safe_load(text)
    except ImportError:
        data = _parse_subset(text)
    except Exception:
        raise
    data = data or {}
    schema = str(data.get("schema") or "")
    topics = data.get("topics")
    return {"schema": schema, "topics": _validate(schema, topics)}


def entries(watchlist: dict = None) -> list:
    """Flat list of entries: {id, name, aliases, type, section}."""
    w = watchlist if watchlist is not None else load()
    return [dict(e, section=s) for s, es in w["topics"].items() for e in es]


def _token_in(alias: str, topic: str) -> bool:
    """Word-bounded token presence in a normalized topic (spaces separate)."""
    return re.search(r"(^| )" + re.escape(alias) + r"( |$)", topic) is not None


def _alias_in_topic(alias: str, name: str, topic_norm: str, keywords_norm: list) -> bool:
    if any(alias == k for k in keywords_norm):
        return True
    if _token_in(alias, topic_norm):
        return True
    return bool(name) and _token_in(name, topic_norm) and name != alias


def match_topic(topic: str, keywords: list, watchlist: dict = None) -> dict:
    """Identifier-based, boundary-aware matching.

    An entry matches when a normalized alias (or its normalized name)
    occurs as a word-bounded token sequence in the normalized topic, or a
    normalized keyword equals an alias. Returns
    {"matched": [entry ids], "coverage": float}.

    Coverage = fraction of keywords that equal an alias of a matched
    entry. It is keyword-level overlap, not a relevance or confidence
    judgement — and it depends on keyword generation, so do not compare
    coverage across sessions (chronicle entry 30).
    """
    w = watchlist if watchlist is not None else load()
    topic_norm = " " + normalize(topic) + " "
    kw_norm = [normalize(k) for k in (keywords or []) if normalize(k)]
    matched = []
    covered = set()
    for e in entries(w):
        name_norm = normalize(e["name"])
        if any(_alias_in_topic(a, name_norm, topic_norm, kw_norm) for a in e["aliases"]):
            matched.append(e["id"])
            for a in e["aliases"]:
                for k in kw_norm:
                    if a == k:
                        covered.add(k)
    coverage = round(len(covered) / max(1, len(kw_norm)), 3) if kw_norm else 0.0
    return {"matched": sorted(set(matched)), "coverage": coverage}


def watchlist_matches(keywords: list, watchlist: dict = None) -> list:
    """Back-compat: flat "section: id" strings for entries matching keywords."""
    w = watchlist if watchlist is not None else load()
    kw_norm = [normalize(k) for k in (keywords or [])]
    out = []
    for e in entries(w):
        if any(a == k for a in e["aliases"] for k in kw_norm):
            out.append(f"{e['section']}: {e['id']}")
    return out


def to_json(watchlist: dict = None) -> dict:
    """Serializable form: {"schema", "topics": {section: [entries]}}."""
    w = watchlist if watchlist is not None else load()
    return {"schema": w.get("schema", SCHEMA), "topics": w["topics"]}


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
    n = sum(len(v) for v in w["topics"].values())
    print(f"watchlist ok: {w['schema']}, {len(w['topics'])} sections, {n} entries")
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(to_json(w), indent=2), encoding="utf-8")
        print(f"watchlist written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

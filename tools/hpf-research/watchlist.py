"""HPF Watchlist loader — reads the watchlist configuration.

The watchlist (config/watchlist.yaml) is operational configuration: a
maintained list of technologies/vendors/repos the programme cares about.
No discovery, no scoring, no automation. The research orchestrator loads it
at plan time; this module is the single implementation of that load so the
orchestrator and any future consumer share the same reading.

YAML is parsed with PyYAML when available and a minimal stdlib subset
parser otherwise (sections + `- item` lists only — the watchlist's shape).
"""

import json
import re
import sys
from pathlib import Path

WATCHLIST_PATH = Path(__file__).resolve().parent / "config" / "watchlist.yaml"


def _parse_subset(text: str) -> dict:
    """Minimal YAML subset parser: comments, section headers, - item lists."""
    topics = {}
    section = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            if section is None:
                raise ValueError("watchlist item before any section header")
            topics.setdefault(section, []).append(line[2:].strip())
        else:
            m = re.match(r"^([A-Za-z0-9_-]+):\s*$", line)
            if not m:
                raise ValueError(f"unexpected watchlist line: {raw}")
            section = m.group(1)
    if not topics:
        raise ValueError("watchlist has no sections")
    return topics


def load_watchlist(path: Path = None) -> dict:
    """Return {section: [entries]} from the watchlist file."""
    p = path or WATCHLIST_PATH
    text = p.read_text(encoding="utf-8")
    try:
        import yaml  # noqa: F401
        data = yaml.safe_load(text)
    except ImportError:
        data = _parse_subset(text)
    except Exception:
        # PyYAML present but the file failed to parse: report, don't guess.
        raise
    topics = (data or {}).get("topics")
    if not isinstance(topics, dict) or not topics:
        raise ValueError("watchlist must define a 'topics' mapping")
    return {str(k): [str(v) for v in vals] for k, vals in topics.items()}


def watchlist_matches(topic_keywords: list, watchlist: dict) -> list:
    """Watched entries whose text overlaps the session keywords (either side)."""
    kw = [k.lower() for k in topic_keywords]
    out = []
    for section, entries in watchlist.items():
        for entry in entries:
            e = entry.lower()
            if any(k in e or e in k for k in kw):
                out.append(f"{section}: {entry}")
    return out


def main():
    ap = argparse_setup()
    args = ap.parse_args()
    if args.check:
        try:
            w = load_watchlist()
        except (OSError, ValueError) as e:
            print(f"! watchlist invalid: {e}")
            return 2
        n = sum(len(v) for v in w.values())
        print(f"watchlist ok: {len(w)} sections, {n} entries")
        return 0
    w = load_watchlist()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"schema": "hpf-watchlist-v0", "topics": w}, indent=2), encoding="utf-8")
    n = sum(len(v) for v in w.values())
    print(f"watchlist written: {out} ({len(w)} sections, {n} entries)")
    return 0


def argparse_setup():
    import argparse
    ap = argparse.ArgumentParser(description="HPF watchlist loader")
    ap.add_argument("--check", action="store_true", help="validate the watchlist file")
    ap.add_argument("--out", default="", help="emit watchlist as JSON (e.g. website-hpf/data/watchlist.json)")
    return ap


if __name__ == "__main__":
    sys.exit(main())

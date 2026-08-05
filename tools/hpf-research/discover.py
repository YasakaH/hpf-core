"""HPF Discover — manual, on-demand research-event suggestions.

Phases 2–4 of the discovery roadmap (chronicle entry 33): connectors
produce unified ResearchEvent[] objects (connectors.py, events.py), and
the opportunity queue remembers why an event was ignored so nothing is
shown twice. No cron, no scoring, no queue-based automation, no
autonomous publishing — the owner decides, HPF researches.

Provenance: activation evidence in chronicle entry 32 (Session 002 was
owner-supplied; Fara went undiscovered until the owner brought it).
Ranking/prioritization (Phase 5) is explicitly deferred until real usage
data exists.

Usage:
    python discover.py --static                     suggestion seed list
    python discover.py --events                     discover events (manual)
    python discover.py --events --out X             also write events JSON to X
    python discover.py --status <id> <status>       mark an event in the queue
    python discover.py --queue <path>               override queue file
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from connectors.discovery import discover_all
from watchlist import load

STATUSES = {"new", "ignored", "researched", "duplicate", "parked", "expired"}
QUEUE_PATH = Path(__file__).resolve().parent / "sessions" / "opportunities.json"


def load_queue(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            print(f"! queue unreadable, starting fresh: {path}")
    return {"statuses": {}}


def save_queue(queue: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(queue, indent=2), encoding="utf-8")


def static_suggestions(watchlist) -> list:
    """Suggestion seed list: every watched entry, section by section."""
    return [(section, entries) for section, entries in watchlist["topics"].items()]


def main():
    ap = argparse.ArgumentParser(description="HPF manual research-event suggestions")
    ap.add_argument("--static", action="store_true", help="suggestion seed list from the watchlist")
    ap.add_argument("--events", action="store_true", help="discover research events (manual, network)")
    ap.add_argument("--status", nargs=2, metavar=("EVENT_ID", "STATUS"), help="mark an event in the opportunity queue")
    ap.add_argument("--out", default="", help="write events JSON to this path")
    ap.add_argument("--queue", default=str(QUEUE_PATH), help="queue file path")
    args = ap.parse_args()

    queue_path = Path(args.queue)
    if args.status:
        evt_id, status = args.status
        if status not in STATUSES:
            print(f"! unknown status {status!r}; expected one of: {', '.join(sorted(STATUSES))}")
            return 2
        queue = load_queue(queue_path)
        queue.setdefault("statuses", {})[evt_id] = status
        save_queue(queue, queue_path)
        print(f"event {evt_id} marked {status}")
        return 0

    try:
        w = load()
    except (OSError, ValueError) as e:
        print(f"! watchlist unavailable: {e}")
        return 2

    if not args.static and not args.events:
        ap.error("choose --static or --events")

    if args.static:
        for section, entries in static_suggestions(w):
            print(f"\n{section}")
            for e in entries:
                srcs = " · ".join(f"{k}: {', '.join(v)}" for k, v in e["sources"].items()) if e.get("sources") else "no sources configured"
                print(f"  o {e['name']} ({e['type']}) — {srcs}")

    output = []
    if args.events:
        queue = load_queue(queue_path)
        statuses = queue.get("statuses", {})
        events = discover_all(w)
        print(f"\nresearch events ({len(events)})")
        for ev in events:
            status = statuses.get(ev["id"], "new")
            print(f"  [{status:10}] {ev['id']} {ev['technology']} {ev['event_type']}: {ev['title']} ({ev['date']}) {ev['link']}")
        output = [{**ev, "status": statuses.get(ev["id"], "new")} for ev in events]

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(),
            "events": output,
        }, indent=2), encoding="utf-8")
        print(f"\nevents written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())


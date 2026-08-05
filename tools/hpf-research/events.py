"""HPF Research Events — unified discovery output model (chronicle entry 33).

Every connector produces ResearchEvent[] — the same object shape regardless
of source. GitHub, docs, RSS, HN, Reddit are all producers of the same
object; consumers (today: discover.py; tomorrow: an opportunity queue, a
ranked list) never see connector-specific formats.

Schema: research-event-v0. No scoring: ranking is a LATER consumer of
events, explicitly gated on real usage data (Phase 5, chronicle entry 33).

Fields:
    id             deterministic across runs (stable identity for the queue)
    title          short title of the event (e.g. "v1.62.1")
    source         connector name (e.g. "github_releases")
    date           published date, YYYY-MM-DD
    event_type     fixed vocabulary (see EVENT_TYPES)
    technology     watchlist id (tech.<domain>.<name>)
    link           canonical URL
    summary        one-line human summary
    discovered_at  UTC ISO timestamp of when HPF saw it
"""

import hashlib
from datetime import datetime, timezone

EVENT_TYPES = {
    "release", "blog", "rfc", "paper", "issue", "breaking_change",
    "model", "benchmark", "security",
}

REQUIRED = ("id", "title", "source", "date", "event_type", "technology", "link")


def event_id(technology: str, event_type: str, date: str, link: str) -> str:
    """Deterministic, stable identity — survives re-discovery runs."""
    return "evt-" + hashlib.sha1(f"{technology}|{event_type}|{date}|{link}".encode("utf-8")).hexdigest()[:12]


def make_event(technology: str, event_type: str, title: str, date: str, link: str,
               summary: str = "", source: str = "") -> dict:
    """Build and validate a ResearchEvent."""
    ev = {
        "id": event_id(technology, event_type, date, link),
        "title": title,
        "source": source,
        "date": date,
        "event_type": event_type,
        "technology": technology,
        "link": link,
        "summary": summary,
        "discovered_at": datetime.now(timezone.utc).isoformat(),
    }
    return validate_event(ev)


def validate_event(ev: dict) -> dict:
    """Fail fast on malformed events. Returns the event."""
    for field in REQUIRED:
        if not ev.get(field):
            raise ValueError(f"event missing required field {field!r}")
    if ev["event_type"] not in EVENT_TYPES:
        raise ValueError(f"unknown event_type {ev['event_type']!r}")
    return ev

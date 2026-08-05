"""HPF discovery connectors — connectors produce ResearchEvent[] (Phase 3).

A discovery connector maps operational configuration (the watchlist's
`sources`, WHERE TO LOOK) to unified ResearchEvent[] objects (events.py).
Connectors run only when the owner invokes discover.py — nothing is
autonomous, no cron, no scheduling. New connectors register here and
return the SAME object shape; consumers never handle connector-specific
formats.

Today: github_releases. The reviewer's connector-registry config
separation (a dedicated file describing each connector's data sources,
separate from the watchlist) is deferred with this trigger: it is built
when a second connector needs configuration that does not fit the
watchlist's `sources` vocabulary (chronicle entry 33).
"""

import json
import urllib.error
import urllib.request

from events import make_event, validate_event

USER_AGENT = "hpf-discover (manual; no automation)"
GITHUB_API = "https://api.github.com/repos/{repo}/releases/latest"

REGISTRY = []


def register(name):
    """Decorator: register a connector function taking a watchlist."""
    def deco(fn):
        REGISTRY.append((name, fn))
        return fn
    return deco


def latest_release(repo: str) -> dict:
    """Fetch the latest GitHub release for a repo. Mechanical, no LLM."""
    req = urllib.request.Request(
        GITHUB_API.format(repo=repo),
        headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"repo": repo, "error": "no releases published (404)"}
        if e.code in (403, 429):
            return {"repo": repo, "error": "rate limited — wait or provide auth"}
        return {"repo": repo, "error": f"http {e.code}"}
    except (urllib.error.URLError, OSError) as e:
        return {"repo": repo, "error": str(e)}
    return {
        "repo": repo,
        "tag": data.get("tag_name", ""),
        "name": data.get("name") or data.get("tag_name", ""),
        "published_at": data.get("published_at", ""),
        "html_url": data.get("html_url", ""),
    }


@register("github_releases")
def github_releases(watchlist: dict) -> list:
    """Watchlist entries with sources.github_releases -> release events."""
    events = []
    for section, entries in watchlist["topics"].items():
        for e in entries:
            for repo in (e.get("sources") or {}).get("github_releases") or []:
                rel = latest_release(repo)
                if "error" in rel:
                    print(f"  ! {e['name']} ({repo}): {rel['error']}")
                    continue
                ev = make_event(
                    technology=e["id"],
                    event_type="release",
                    title=rel["tag"],
                    date=(rel["published_at"] or "")[:10],
                    link=rel["html_url"],
                    summary=f"{e['name']}: {rel['tag']} — {rel['name']}",
                    source="github_releases",
                )
                events.append(validate_event(ev))
    return events


def discover_all(watchlist: dict) -> list:
    """Run every registered connector, dedupe, sort newest first."""
    events = []
    for name, fn in REGISTRY:
        events.extend(fn(watchlist))
    seen = set()
    out = []
    for ev in events:
        if ev["id"] in seen:
            continue
        seen.add(ev["id"])
        out.append(ev)
    return sorted(out, key=lambda ev: ev["date"], reverse=True)


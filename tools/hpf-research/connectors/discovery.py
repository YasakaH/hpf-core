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
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

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
                    summary=f"{e['name']}: {rel['tag']} - {rel['name']}",
                    source="github_releases",
                )
                events.append(validate_event(ev))
    return events


# --- blog/RSS connector (second connector; validates the event model) ---

FEED_PATHS = ("rss.xml", "feed.xml", "atom.xml", "index.xml", "rss", "feed", "feeds/posts/default")


def _tag(el) -> str:
    return el.tag.rsplit("}", 1)[-1]


def _child_text(entry, name: str) -> str:
    for child in entry:
        if _tag(child) == name:
            return (child.text or "").strip()
    return ""


def _link_of(entry) -> str:
    for child in entry:
        if _tag(child) != "link":
            continue
        href = child.attrib.get("href")
        if href:
            return href.strip()
    return _child_text(entry, "link")


def _date_of(entry) -> str:
    for name in ("pubDate", "published", "updated"):
        text = _child_text(entry, name)
        if not text:
            continue
        try:
            if name == "pubDate":
                dt = parsedate_to_datetime(text)
            else:
                dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
            return dt.astimezone(timezone.utc).date().isoformat()
        except (ValueError, TypeError):
            continue
    return ""


def parse_feed(text: str, limit: int = 5) -> list:
    """Parse RSS 2.0 / Atom into [{title, link, date, summary}]. Stdlib only."""
    root = ET.fromstring(text)
    entries = []
    if _tag(root) == "feed":
        entries = [c for c in root if _tag(c) == "entry"]
    else:
        channel = next((c for c in root if _tag(c) == "channel"), None)
        if channel is not None:
            entries = [c for c in channel if _tag(c) == "item"]
    out = []
    for entry in entries[:limit]:
        link = _link_of(entry)
        title = _child_text(entry, "title")
        if not link or not title:
            continue
        out.append({
            "title": title,
            "link": link,
            "date": _date_of(entry),
            "summary": (_child_text(entry, "description") or _child_text(entry, "summary") or "")[:200],
        })
    return out


def _fetch(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _resolve_feed(url: str) -> str:
    """Already a feed URL, or probe common feed paths under a blog root."""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    u = url.rstrip("/")
    if u.endswith(FEED_PATHS):
        return u
    if ".xml" in u:
        return u
    for path in FEED_PATHS:
        candidate = f"{u}/{path}"
        try:
            head = _fetch(candidate)[:600].lower()
            if "<rss" in head or "<feed" in head or "<rdf" in head:
                return candidate
        except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
            continue
    return ""


@register("blog")
def blog(watchlist: dict) -> list:
    """Watchlist entries with sources.blog -> blog events from RSS/Atom feeds.

    Values may be a blog root (feed paths are probed) or a direct feed URL.
    Items without a parseable title or publication date are skipped honestly.
    """
    events = []
    for section, entries in watchlist["topics"].items():
        for e in entries:
            for url in (e.get("sources") or {}).get("blog") or []:
                feed = _resolve_feed(url)
                if not feed:
                    print(f"  ! {e['name']}: no RSS feed found at {url}")
                    continue
                try:
                    items = parse_feed(_fetch(feed), limit=3)
                except (urllib.error.URLError, urllib.error.HTTPError, OSError, ET.ParseError) as ex:
                    print(f"  ! {e['name']}: feed error ({feed}): {ex}")
                    continue
                for it in items:
                    if not it["date"] or not it["title"]:
                        continue
                    ev = make_event(
                        technology=e["id"],
                        event_type="blog",
                        title=it["title"][:120],
                        date=it["date"],
                        link=it["link"],
                        summary=it["summary"],
                        source="blog",
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


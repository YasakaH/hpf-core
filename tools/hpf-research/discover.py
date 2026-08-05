"""HPF Discover — minimal on-demand opportunity suggestions.

Manual only. No scheduling, no cron, no scoring, no queue, no autonomous
publishing. The owner runs it when topic selection starts; it reads the
watchlist (the knowledge seed) and, for entries with `github_releases`
sources, reports the latest published release. Output is a plain list of
suggestions — the owner chooses, HPF researches.

Provenance: chronicle entry 32. Activation evidence: Session 002's topic
and all primary sources were owner-supplied; Microsoft Fara (released
2026-07-22) went undiscovered by HPF until the owner brought it. That
fired activation trigger (2) of the parked Research Opportunity Engine
(entry 27). This tool is the minimal precursor, per the review: the full
engine (cadence, scoring, suggested-research queue, approval loop) stays
parked until measured evidence demands it. The `sources` data it consumes
is operational configuration on the watchlist itself, not engine
automation.

Usage:
    python discover.py --static             suggestion seed list from the watchlist
    python discover.py --releases           fetch latest GitHub releases (network)
    python discover.py --releases --out X   also write suggestions JSON to X
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from watchlist import load

USER_AGENT = "hpf-discover (manual; no automation)"
API = "https://api.github.com/repos/{repo}/releases/latest"


def static_suggestions(watchlist) -> list:
    """Suggestion seed list: every watched entry, section by section."""
    out = []
    for section, entries in watchlist["topics"].items():
        out.append((section, entries))
    return out


def latest_release(repo: str) -> dict:
    """Fetch the latest GitHub release for a repo. Mechanical, no LLM."""
    req = urllib.request.Request(
        API.format(repo=repo),
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


def main():
    ap = argparse.ArgumentParser(description="HPF manual opportunity suggestions")
    ap.add_argument("--static", action="store_true", help="suggestion seed list from the watchlist")
    ap.add_argument("--releases", action="store_true", help="fetch latest GitHub releases (network)")
    ap.add_argument("--out", default="", help="write suggestions JSON to this path")
    args = ap.parse_args()
    try:
        w = load()
    except (OSError, ValueError) as e:
        print(f"! watchlist unavailable: {e}")
        return 2

    if not args.static and not args.releases:
        ap.error("choose --static or --releases")

    suggestions = []
    if args.static:
        for section, entries in static_suggestions(w):
            print(f"\n{section}")
            for e in entries:
                srcs = " · ".join(f"{k}: {', '.join(v)}" for k, v in e["sources"].items()) if e.get("sources") else "no sources configured"
                print(f"  o {e['name']} ({e['type']}) — {srcs}")
            suggestions.append({"section": section, "entries": [e["id"] for e in entries]})

    if args.releases:
        print("\nlatest GitHub releases")
        results = []
        for section, entries in static_suggestions(w):
            for e in entries:
                repos = (e.get("sources") or {}).get("github_releases") or []
                for repo in repos:
                    rel = latest_release(repo)
                    results.append({"entry": e["id"], "section": section, **rel})
                    if "error" in rel:
                        print(f"  ! {e['name']} ({repo}): {rel['error']}")
                    else:
                        print(f"  o {e['name']}: {rel['tag']} — {rel['name']} ({rel['published_at'][:10]}) {rel['html_url']}")
        suggestions.append({"generated": datetime.now(timezone.utc).isoformat(), "releases": results})

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(suggestions, indent=2), encoding="utf-8")
        print(f"\nsuggestions written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

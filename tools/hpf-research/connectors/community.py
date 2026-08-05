"""Community Evidence Connector.

Gathers structured community signal from practitioner communities. The
connector only emits *structured payloads*; it never interprets them. HPF
labels everything it produces as `community_signal` — observation, not truth.

Payload schema (written to --out as JSON):

    {
      "source": "hackernews",
      "subreddit": "hacker-news",
      "thread": "query or story title",
      "score": 412,
      "url": "https://news.ycombinator.com/item?id=...",
      "comments": [
        {"text": "...", "score": 81, "author": "...", "url": "..."}
      ]
    }

Sources:

- v1a: Hacker News (Algolia API) — open, no auth, real practitioner signal.
- v1b: structured payload files (--payload) — produced by any community
  source (Reddit via a Devvit app, Stack Overflow, GitHub Discussions,
  Discord exports). The planner picks the source; HPF only consumes the
  schema.

The Devvit CLI was evaluated as a Reddit source: the current CLI
(0.13.x) is an app-development tool (init/publish/install) with no search
command, and its auth token is device-bound with an expiry. A Reddit source
would require building a custom Devvit app the owner publishes; until a real
research session fails without Reddit data, HN + payload files are the
working v1.
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PAYLOAD_SCHEMA = ("source", "subreddit", "thread", "score", "comments")

HN_API = "https://hn.algolia.com/api/v1/search_by_date"
USER_AGENT = "HPF-Research-Orchestrator/0.1 (+research evidence collection)"


def _get(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def hn_search(query: str, limit: int) -> list:
    """Top stories matching the query, with their text where available."""
    params = urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": limit})
    data = _get(f"{HN_API}?{params}")
    hits = []
    for h in data.get("hits") or []:
        hits.append({
            "title": h.get("title") or h.get("story_title") or "",
            "text": (h.get("story_text") or "")[:4000],
            "score": h.get("points") or 0,
            "author": h.get("author") or "",
            "url": f"https://news.ycombinator.com/item?id={h.get('objectID')}",
            "num_comments": h.get("num_comments") or 0,
            "date": (h.get("created_at") or "")[:10],
        })
    return hits


def hn_payload(query: str, hits: list) -> dict:
    comments = []
    for h in hits:
        text = (h["text"] or h["title"]).strip()
        if len(text) >= 80:
            comments.append({
                "text": text[:4000],
                "score": h["score"],
                "author": h["author"],
                "url": h["url"],
                "date": h["date"],
            })
    return {
        "source": "hackernews",
        "subreddit": "hacker-news",
        "thread": query,
        "score": sum(h["score"] for h in hits),
        "comments": comments,
    }


def validate_payload(payload: dict) -> list:
    problems = []
    for field in PAYLOAD_SCHEMA:
        if field not in payload:
            problems.append(f"missing field: {field}")
    if not isinstance(payload.get("comments"), list):
        problems.append("comments must be a list")
    return problems

def write_payload(payload: dict, out_path: Path) -> int:
    problems = validate_payload(payload)
    if problems:
        print("! invalid community payload:")
        for p in problems:
            print(f"  - {p}")
        return 8
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Community payload written: {out_path}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="HPF Community Evidence Connector")
    ap.add_argument("--source", default="hn", choices=["hn"])
    ap.add_argument("--query", default="")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--out", default="community-payload.json")
    ap.add_argument("--payload", default="", help="validate/normalize an existing payload file")
    args = ap.parse_args()

    if args.payload:
        payload = json.loads(Path(args.payload).read_text(encoding="utf-8"))
        sys.exit(write_payload(payload, Path(args.out)))

    if not args.query:
        print("! need --query (or --payload file.json)")
        sys.exit(2)

    try:
        hits = hn_search(args.query, args.limit)
    except Exception as e:
        print(f"! HN search failed: {e}")
        sys.exit(9)
    if not hits:
        print(f"! no HN hits for '{args.query}'; refusing to emit an empty or fabricated payload")
        sys.exit(10)
    sys.exit(write_payload(hn_payload(args.query, hits), Path(args.out)))


if __name__ == "__main__":
    main()

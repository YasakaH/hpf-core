# HPF Engineering Change Log

Implementation-level record of what was built, how, and with which test
outcomes. The Programme Chronicle (`HPF_RESEARCH_CHRONICLE.md`) records
decisions and governance only (separation policy: chronicle entry 33);
this log carries the engineering detail so the chronicle stays a decision
record, not a release log.

---

## Backfill — watchlist engineering, chronicle entries 29–32 (condensed)

Full decision context lives in the chronicle entries cited; this is the
implementation record.

- **Entry 29 (2026-08-05)** — `watchlist.yaml` + `tools/hpf-research/watchlist.py`:
  identifier-based matching (`id`/`aliases`/`type`, 24 entries, 3 sections),
  word-bounded alias matching, shared service API (`load`/`entries`/`match_topic`),
  session field `watchlist: {matched, coverage}`. test10 introduced.
- **Entry 30 (2026-08-05)** — schema `hpf-watchlist-v1`: vendor-independent
  canonical ids `tech.<domain>.<name>` + display `name`, alias normalization
  (lowercase, non-alphanumeric runs to single space), schema version enforced
  at load, fail-fast validation (duplicate ids, duplicate normalized aliases,
  missing aliases/type, empty sections), display name as match surface.
  test10 extended to 15 checks.
- **Entry 31 (2026-08-05)** — field `coverage` renamed `keyword_overlap`
  (name now states literally what the metric measures; no released session
  carried the old field). Watchlist declared v1-mature.
- **Entry 32 (2026-08-05)** — watchlist entries gained optional `sources`
  (WHERE TO LOOK; vocabulary: `github_releases`/`github`/`docs`/`blog`/`npm`/
  `pypi`/`hf`/`reddit`/`hackernews`, validated at load, non-empty string
  lists; entries without sources allowed). `tools/hpf-research/discover.py`
  added: manual `--static` (suggestion seed) and `--releases` (GitHub latest
  releases). Workbench watchlist view renders sources. test11 introduced.

---

## 2026-08-05 — Research Event model, discovery connector registry, opportunity queue

**Chronicle decision**: entry 33. Watchlist schema frozen again — no new
fields unless a real research session exposes a concrete need.

**Built** (executable infrastructure per entry 28 classification):

- `tools/hpf-research/events.py` — unified output model `research-event-v0`:
  `id` (deterministic `evt-<sha1 of technology|event_type|date|link>[:12]`),
  `title`, `source` (connector name), `date` (YYYY-MM-DD), `event_type`
  (vocabulary: release, blog, rfc, paper, issue, breaking_change, model,
  benchmark, security), `technology` (watchlist id), `link`, `summary`,
  `discovered_at`. `make_event()` + `validate_event()` fail fast. No scoring
  fields — ranking is a later consumer, gated on usage data.
- `tools/hpf-research/connectors/discovery.py` — connector registry
  (`REGISTRY`, `register(name)`, `discover_all(watchlist)` returning
  ResearchEvent[], deduped, newest-first). First connector: `github_releases`
  (was the `--releases` fetch in discover.py; moved here, same mechanical
  fetch, honest 404/rate-limit messages). Co-located with the existing
  evidence-connectors package (`connectors/community.py`); the package
  docstring documents both layers. Connector-registry CONFIG separation
  (a file describing connector data sources apart from the watchlist) is
  deferred with the trigger recorded in the chronicle: a second connector
  needing config beyond the watchlist `sources` vocabulary.
- `tools/hpf-research/discover.py` — refactored: `--releases` renamed
  `--events`; output shows event ids (so `--status` is usable), status
  annotation, and events JSON with `--out`. Opportunity queue:
  `--status <evt-id> <status>` (vocabulary: new, ignored, researched,
  duplicate, parked, expired) persisted in
  `tools/hpf-research/sessions/opportunities.json` (git-ignored working
  area); `--queue <path>` override for tests. An event never re-shows as
  `new` once the owner has dispositioned it.
- Printed strings switched to ASCII-safe separators (Windows console
  encoding mangles em-dashes/middots in redirected output).

**Tests** (workbench-test11.js, 13 checks, all green): static mode renders
sections/entries/sources without inventing priority or scores; event ids
deterministic and link-sensitive; validation rejects missing fields and
unknown event types; queue marks statuses and rejects unknown statuses;
`--events` completes end-to-end and reports honestly under rate-limit/404
(a live run during this round was rate-limited and degraded gracefully,
zero events, exit 0). Full suite (test4/8/9/10/11) green.

## 2026-08-05 — blog/RSS connector (model validation, chronicle entry 34)

**Chronicle decision**: entry 34. Infrastructure closed pending real usage.

**Built**: second discovery connector log in
	ools/hpf-research/connectors/discovery.py:

- parse_feed(text, limit) — RSS 2.0 + Atom parsing, stdlib only
  (xml.etree, email.utils.parsedate_to_datetime); namespaces stripped via
  local tag names; dates normalized to YYYY-MM-DD UTC; items without
  title/link/date skipped by the connector, not fabricated.
- _resolve_feed(url) — watchlist log: values may be a blog root
  (https:// prepended if scheme-less; common feed paths probed in order:
  rss.xml, feed.xml, atom.xml, index.xml, rss, feed, feeds/posts/default;
  first 600 chars sniffed for <rss/<feed/<rdf) or a direct feed URL
  (ends with a feed path or contains .xml).
- Emits ResearchEvent[] with event_type=blog, source=blog, summary
  truncated to 200 chars, title to 120.

No watchlist schema change (source values are free-form strings). No new
dependencies, no auth.

**Live validation** (2026-08-05): produced real blog events — Cloudflare
OS / Agent Access Model (08-05), OpenAI cyber-evaluations (08-04), WebKit
Safari 26.6 (07-27), Chrome agent-ready toolkit (06-22), Chromium
JetStream 3 (03-31) — alongside release events. Three feeds unresolved
(playwright.dev/blog, anthropic.com/research, blog.mozilla.org) reported
honestly; owner can switch those values to direct feed URLs later.
GitHub releases were rate-limited during the run; degradation was
per-connector and graceful.

**Fix during build**: _resolve_feed crashed with ValueError on
scheme-less watchlist values (unknown url type) — scheme prepended;
ValueError added to probe exception set. Console traceback confirmed the
crash path was caught before release.

**Tests**: test11 +2 offline checks (RSS 2.0 and Atom parse into event
fields) — 15 checks total, full suite green.

---

## Provenance capture (pre-Session-003 measurement, uncommitted until review)

Chronicle entry 34 declared discovery feature-complete for v1 and
requested one addition before Session 003: every accepted finding must
record which ResearchEvents produced it. This is measurement, not
infrastructure: it lets the record answer "which events became research,
which became findings, which were ignored".

- **`research.py`** — new `--from-events` repeatable flag (comma-separated
  values accepted). Values validated as `evt-[0-9a-f]{12}`; malformed ids
  logged and ignored. Collected into session field
  `provenance: {events: [...]}` via a new `provenance=None` parameter on
  `make_session(...)` (signature extended, call sites updated).
- **`adjudicate.py`** — adjudication artifact gains
  `provenance: session.provenance` (defaults `{"events": []}` for sessions
  that predate the field); review layer stays immutable — provenance is
  carried through, never rewritten.
- **`discover.py`** — new read-only `--report` (plus `--sessions <dir>`
  defaulting to repo `exports/sessions`, `--events-json` for enrichment):
  joins events → sessions → accepted findings. Each line prints queue
  status (default `new`), event id, optional enriched detail
  (technology/event_type/title), session id, topic, accepted-finding
  count. Summary dedupes per unique session (multi-event sessions were
  double-counting accepted findings — fixed in the same round). No writes
  to the queue or to sessions.

**Tests**: test12 introduced (offline) — 7 checks: report joins and
enriches, statuses honored, summary counts, adjudication provenance
carry-through, `make_session` provenance storage. test10 and test11
unchanged; full suite green (17 + 13 + 7).

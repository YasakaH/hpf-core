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

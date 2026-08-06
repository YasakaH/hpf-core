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

---

## Connector yield table (review round 7 follow-up, pre-freeze)

Reviewer's final pre-freeze request: the provenance report must also
compute connector yield automatically — a report derived from data
already collected, not new infrastructure.

- `discover.py --report` now prints a per-connector table after the
  summary when `--events-json` is provided:
  `Source | Events | Researched | Findings | Yield`.
- Semantics (documented in the change log, not the code):
  - **Events** — distinct events of that source in the events JSON
    (denominator = total discovered, including never-researched).
  - **Researched** — events of that source that seeded a session
    (provenance) or were marked `researched` in the queue.
  - **Findings** — accepted findings (approve/revise/add) of sessions the
    source's events seeded; counted per seeded session, so
    multi-connector sessions appear in each row they seeded (directional
    analysis, not a ledger).
  - **Yield** — findings / events.
- **Manual URLs** row: provenance events absent from the events JSON
  (owner-supplied seeds never produced by a connector). Their event
  counts are known only via provenance, so the manual denominator is
  "manual events used", not "all manual events ever".
- Without `--events-json`, the table prints `connector yield:
  unavailable (...)` — the report stays honest rather than inventing a
  source for unenriched events.

**Fix during validation**: manual row showed `Events 0, Researched 1` —
manual events (absent from the events JSON) were added to `used` but
never to the events list; the rows loop now appends unenriched events to
their source's event list. Test caught it via the fixture's manual event.

**Tests**: test12 +5 checks (yield table present, GitHub Releases row,
Blogs row, Manual URLs row, gated without `--events-json`) — 12 checks;
test10 (17) and test11 (13) rerun green. Real-data smoke: zero
provenance rows (all released sessions predate the field), clean exit.

This closes the discovery subsystem for v1. Next work is operational:
Sessions 003–020 through the pipeline, then the measured-friction review.

---

## Connector yield refinement (review round 8, pre-freeze)

Reviewer feedback round 8: the metric name `Yield` implies a 0–100%
conversion rate but the ratio is findings-per-event and can exceed 100%
(a single event can seed a session with several accepted findings).
Renamed and extended — the report remains derived from data already
consumed, no new infrastructure.

- **`Yield` → `F/Event`** (Findings/Event). Same semantics, honest name
  for a ratio that may exceed 100%. Section header note extended:
  "ratios may exceed 100%".
- **`Ignored` column added** — events of that source whose queue status
  is `ignored`. Uses the same queue file `--report` already reads.
- **`Sessions` + `S/Event` columns added** — distinct sessions the
  source's events seeded, and the sessions-per-event ratio. Answers
  "did this connector inspire research?" separately from "did it
  produce findings?" (F/Event).
- Table order: `Source | Events | Researched | Ignored | Sessions |
  Findings | S/Event | F/Event`. Multi-connector sessions still appear
  in each row they seeded (directional analysis; totals are NOT
  additive — unchanged from round 7, documented).

**Tests**: test12 fixture extended with a third event marked `ignored`
in the queue (never used); expectations updated for the renamed and new
columns; +1 check that the old `Yield` header is gone. test12 = 13
checks; test10 (17) and test11 (13) rerun green. Real-data smoke: clean
exit, zero provenance rows as expected.

Discovery subsystem is now closed for v1. Further analytical reports
(e.g. the full pipeline conversion report from connector → published
pack) are postponed until operational data from Sessions 003–020 makes
them meaningful.

---

## Extraction engineering round (Session 003 measurements, pre-Session-004)

Session 003's measurements pointed squarely at the extraction stage:
123 evidence entries with 70+ README chunks while the core article (the
Agent Access Model post) contributed one substantive paragraph; 8 of 15
drafts were navigation chrome; the reviewer had to add 7 findings that
were the article's substance. The reviewer directed one focused
engineering cycle on extraction before Session 004 — P0 items implemented
here; Claim Detection (P1) and semantic chunking (P3) staged next.

**Root-cause diagnosis** (two defects, not one):
1. `TextExtractor` emitted a newline only on block-element START tags, so
   `<p>a</p><p>b</p>` collapsed to `a b` — dense blog HTML had no
   blank-line paragraph separators. `split_paragraphs` then produced one
   giant paragraph per dense page and the 600-char excerpt truncation
   silently destroyed everything past the intro. The AAM post's body
   (five-component model, capability ceilings, multiplayer access
   control) was lost to this, not to "too much junk".
2. `split_paragraphs`' prose filter (len ≥ 40, contains ".") passed tag
   clouds, subscribe boxes, footers and translation bars ("1.1.1.1"
   contains a dot). READMEs with many blank lines flooded evidence while
   the budget-less loop kept every paragraph from every source.

**Fixes**:
- `TextExtractor` emits newlines on block-element END tags too →
  real paragraph boundaries; excerpt cap 600 → 1200 chars.
- `is_boilerplate(text)`: conservative phrase blocklist (subscribe,
  privacy choices, terms, tags, related posts, cookie banners,
  translation bars, search UI, © + year, contact sales, etc.) —
  paragraphs matching any pattern never become evidence.
- `EVIDENCE_BUDGETS` per class: primary 40, code 10, community 20,
  scientific 25, operational 15 — one source can no longer flood a
  session; `keep_paragraphs()` caps per source.
- **Source coverage metrics**: each source record gains `evidence`
  (paragraphs kept), `chrome_dropped`, and `coverage`
  (kept chars / collected chars); the extract stage prints a per-source
  coverage line. Live numbers after the fix (Session 003 URLs): AAM post
  coverage 0.309 (was: 1 substantive paragraph of a 45KB text — body
  lost), Cloudflare OS 0.334, Agents docs 0.358, Browser Run 0.415,
  README 0.069 at its 10-paragraph budget (was 70+ chunks).
- `watchlist.py`: `keyword_overlap` now counts the normalized display
  name as a match surface — a topic matching `tech.web.cloudflare` via
  its name "Cloudflare" (alias is "cloudflare anti-bot") no longer reads
  overlap 0.0 (verified 0.25 in the fixture). Bug confirmed: name was a
  documented match surface but excluded from the overlap calculation.
- `adjudicate.py`: **extraction-underperformance flag** — when reviewer
  adds exceed 3 findings, the adjudication artifact records
  `extraction_flag: {flagged, added_findings, threshold}` and a warning
  prints. Session 003 would have flagged: 7 adds. Session 002 would not
  have (5 adds > 3 — it would have flagged; threshold is a first cut).

**Tests**: test13 introduced (offline, 7 checks): paragraph boundaries
survive block HTML; boilerplate patterns dropped while genuine prose
mentioning the words is kept; per-source budgets cap evidence (code 10 /
primary 40); overlap counts name matches; extraction flag fires at 4
adds and stays quiet within threshold. test10 (17), test11 (13), test12
(13) rerun green.

**Recorded (document only, v2 feedback loop)**: SEO/keyword-tooling
direction — do NOT build around DataForSEO (self-hosted OpenSEO still
requires its API key; hosted openseo.so subsidizes costs as its business
model). The future SEO module should use free sources first (Google
Search Console API for own keywords/impressions/CTR, Google Trends,
autocomplete/PAA where terms permit, own crawler for competitor content,
Common Crawl) with commercial providers (DataForSEO, Ahrefs) as pluggable
backends later — consistent with the zero-cost operating constraint.

**Staged (P1/P3, not built this round)**: Claim Detection stage (heading/
list/code removal + assertion identification) and semantic chunking —
the next extraction round if Sessions 004–010 keep pointing at
extraction rather than discovery or publishing.

---

## Review round 10 — extraction failure taxonomy + measurement hardening (2026-08-05)

Review verdict: "excellent tactical engineering, not completed extraction
architecture" — the extraction subsystem is NOT closed. The review's
architectural recommendations (knowledge units, adaptive budgets,
boilerplate scoring, semantic overlap, confidence propagation, evidence
dedup, plugin extractors, claim-aware pipeline) were classified under
entry 28 and staged with triggers — building them now would violate the
measurement discipline (one extraction-round session of data). What WAS
implemented immediately is the measurement infrastructure the review
itself demanded: the failure taxonomy and observability that tell us WHY
extraction failed, not just that it did.

**Implemented (this round)**:
- **Failure taxonomy metrics per source** (`extract_source()` helper —
  extracted from the collect loops so it is testable; both URL and
  import loops use it, sharing one session-level `seen` set):
  - `truncated` — paragraphs cut by the EXCERPT_LIMIT (1200, now a
    constant);
  - `duplicates` — kept paragraphs whose normalized text already
    appeared in another source (cross-source duplication MEASURED, not
    removed — removal is staged, and this metric is its trigger);
  - `boilerplate_ratio` — dropped / (dropped + kept) per source;
  - `avg_para_chars`, `largest_para_chars`;
  - `paragraphs` (pre-filter count) added alongside existing
    evidence/chrome_dropped/coverage.
- **Session health line**: `extraction health: boilerplate_ratio X,
  duplicate_ratio Y, truncated N, avg_para N chars, largest_para N chars`
  printed in the extract stage and recorded in session activity —
  longitudinal regression signal.
- **Normalized extraction flag** (adjudicate.py): fires only when
  `adds > 3` AND `adds/accepted >= 0.35` — the review's point that raw
  counts conflate small and large sessions. The flag record now carries
  `added_findings`, `accepted_total`, `adds_accepted_ratio`, both
  thresholds, and `causes` — a reviewer-supplied failure taxonomy
  (`extraction_causes` field in decisions.json, vocabulary: missing_
  claims, duplicate_claims, truncated_claims, low_confidence_claims,
  boilerplate_leakage, coverage_loss, source_dominance, missing_urls,
  keyword_generation).
- **Block-tag hardening**: TextExtractor.BLOCK gained details, summary,
  figure, figcaption, aside, main, dl, dt, dd, ol, ul, nav — the review
  flagged the manual tag list as a maintenance burden; the list stays a
  single centralized tuple (the abstraction point), and these additions
  cover the structural elements that actually appear in current sources.
  Definition lists and table rows now split into separate units.

**Tests**: test14 introduced (12 checks, offline golden-corpus style):
dense-blog fixture keeps all paragraphs while footer boilerplate drops
with a recorded boilerplate_ratio; details/summary/dl/dt/dd/table
fixture yields separate units (3 sentence-bearing units — summary/dt
correctly dropped by the prose filter); 60-paragraph README-style
fixture capped at the code budget of 10; cross-source duplicate
measured via the shared seen set; >1200-char paragraph flagged
truncated; health-line format; flag stays quiet at ratio 0.333 (4/12)
and fires at 0.4 (4/10) with accepted_total and causes recorded.
test10-13 rerun green (17/13/13/7).

**Classified and staged (documented in chronicle entry 36), NOT built**:
1. Knowledge units as the pipeline primitive (paragraph → unit: list,
   table row, definition, code explanation, quote) — HIGH; trigger:
   the golden corpus or sessions 004-010 showing list/table/definition
   content loss (the new `truncated`/unit metrics are the instrument).
   Until then paragraphs remain the unit; the block-tag additions above
   are the cheap approximation.
2. Adaptive budgets (budget = f(claim density × source quality ×
   novelty × importance)) — needs claim detection first (P1); trigger:
   claim-detection stage exists.
3. Boilerplate scoring (link density, text density, sentence ratio,
   unique word ratio, navigation probability, DOM position, heading
   proximity → boilerplate_score 0-1) — trigger: is_boilerplate pattern
   count passes ~50 or golden corpus shows footer leakage. Pattern
   count today: ~45, including the Session 004 tagline class which is
   recorded as a pattern gap ("Design a beautiful and performant web
   with Chrome." / "Create the best experience...") — not added, per
   this round's scope discipline.
4. Semantic/concept-level overlap (concept IDs or embeddings instead of
   keyword equality) — trigger: a real session where normalized lexical
   overlap misleads despite the S003/S004 fixes.
5. Evidence confidence propagation (confidence/novelty/source authority
   on evidence → non-binary adjudication) — trigger: knowledge units.
6. Evidence deduplication before adjudication — trigger: the new
   duplicate_ratio metric exceeds ~0.15 in real sessions (S004 measured
   0.00 cross-source; the metric's first real data point).
7. Plugin extractor architecture (Extractor strategy interface:
   Html/Markdown/Pdf/Repository/ApiDoc) — trigger: a second content
   type beyond HTML/markdown import shows real demand.
8. Coverage → claim/knowledge coverage (accepted units / candidate
   units) — derivative of knowledge units; staged with item 1.

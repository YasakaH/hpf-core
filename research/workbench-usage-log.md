# Workbench Usage Log

Working note for the first weeks of daily Workbench use. Evidence collection,
not governance: recurring entries decide what the Workbench gains next.
A request earns implementation only if it keeps recurring during use.

For each friction point record:

| Date | Task | Left Workbench? | Missing Capability | Frequency |
|---|---|---|---|---|
| 2026-08-05 | Example: Inspect Cycle 012 predictions | Yes | Research view | #1 |
| 2026-08-07 | Example: Inspect Cycle 014 dossier | Yes | Research view | #2 |
| 2026-08-08 | Example: Validate object | No | — | — |

After a dozen sessions, patterns emerge. If entries repeatedly say "had to
open the dossier", the Research view has its evidence. If none do, it stays
unbuilt.

## Usage discipline (working-note refinement, 2026-08-04)

The Workbench is the primary interface for HPF: everything previously done via
VS Code, terminal, JSON inspection, or ad hoc scripts goes through it. The
infrastructure phase is closed; the next improvements come from this log, not
from the deployment stack.

Owner-directed redesign 2026-08-04: the workbench was reoriented from
ontology-browser to research-first (Home = research prompt; Research hub =
intended investigations; ontology/schema details moved to Diagnostics). Log
entries should therefore record departures against the new interface, and any
recurring "had to open the dossier / terminal" gap becomes evidence under the
new layout.

For every departure from the Workbench, ask:

> "Could I reasonably have stayed inside the Workbench?"

- Repeatedly "no" for the same reason → evidence for the next feature.
- Mostly "yes" → the operational-interface goal is achieved.

First workbench review after 20-30 logged sessions.

## Community evidence review (recurring operational check, 2026-08-05)

Now that the Community Evidence Connector is live (v1a: Hacker News / Algolia
API; Devvit/Reddit deferred — the 0.13.x CLI has no search command and its
auth is device-bound), each session that used community evidence gets a short
recurring check — not governance, a signal for whether the connector is
contributing or adding noise:

| Question | Example answer |
|---|---|
| Did community evidence reveal anything not in official documentation? | Yes — repeated reports of browser fingerprinting failures. |
| Did it change the conclusions? | No / Partially / Yes |
| Was it validated elsewhere? | GitHub Issues, benchmarks, vendor docs, etc. |

Only repeated "yes, and it changed the outcome" answers justify building more
community connectors (HN, Stack Overflow, GitHub Discussions, Discord
exports). Connectors are added only when a real research session failed
without them — never preemptively.

Suggested first community-heavy research topic: "Web automation pain points"
(recurring practitioner signals: Playwright detection, CAPTCHA escalation,
Cloudflare blocking, proxy rotation, browser fingerprinting, session
persistence, rate limiting) — then compare against official documentation.

## Inaugural community-heavy session (2026-08-05)

Session `2026-08-05-0455-web-automation-pain-points-202` (released to
`exports/sessions/`): "Web automation pain points (2026)". Evidence classes:
primary (playwright.dev intro, developer.chrome.com/devtools), code
(github.com/nodriver), community (4 HN payloads, 23 comments). 7 sources, 62
evidence, 21 draft findings, 12 community signals.

Community evidence review answers:

| Question | Answer |
|---|---|
| Did community evidence reveal anything not in official documentation? | Yes — official docs describe *how* to automate; HN describes *what breaks* (Cloudflare gating on Tor/"bad" IPs, captcha escalation, fingerprinting failures, RAM cost of headless fleets). |
| Did it change the conclusions? | Partially — community_signal findings are drafts; conclusions still need adjudication. |
| Was it validated elsewhere? | Not yet — the HN claims are single-source signals; cross-checking against GitHub issues/benchmarks is the adjudication step. |

Connector behavior notes (mechanical, verified during the run):
- Empty result sets refuse to emit a payload (exit 10) rather than fabricate.
- URL hosts now infer evidence class (github.com → code; docs/primary default);
  previously the planner's `code: high` was recorded but nothing was collected
  as code — fixed during this session.
- Evidence-class plan is honest: `scientific: high` was planned but no
  scientific source was collected (none existed for this topic); the manifest
  counts only what exists.

## First full session review (2026-08-05) — Session 001

`2026-08-05-0512-web-automation-pain-points-202` was the first session
reviewed end-to-end before any deployment (the reviewer's rule: no release
until a genuinely valuable research artifact exists). The review layer is a
separate `adjudication.json` next to `session.json` — the mechanical record
stays immutable; the review layer records what a reviewer decided. Written by
`tools/hpf-research/adjudicate.py` (same immutability discipline: refuses to
overwrite).

Review outcome (21 draft findings → 7 revised, 14 rejected, 1 added):

- **Rejected (14)** fell into three honest buckets: restatements of official
  docs/nav chrome (f-1..f-3, f-7..f-9), code-source README blurbs with no
  extracted claim (f-4..f-6), and product pitches / query drift (f-11, f-14,
  f-18, f-19, f-21). ~9 of the original 21 were not findings at all.
- **Revised (7)** survived because the pain-point claim inside the pitch was
  independently corroborated: paid-API-vs-headless-fleet + RAM cost (f-10,
  two occurrences), stealth at scale (f-12), fingerprinting counter-tooling
  (f-13), geo-flagging + signal breadth (f-15), missing official APIs
  (f-16), Cloudflare Under-Attack captcha ~90% failure (f-17, score 161 —
  the anchor), site-operator bot traffic (f-20).
- **Added (1)**: f-22, the contradiction finding — official docs present
  automation as supported practice while community reports systematic
  anti-bot blocking. Synthesized by the reviewer, kept as a draft
  (`needs_adjudication`, confidence null) — it does not graduate
  automatically.

Pipeline defects this review exposed and fixed (same run):

1. **`github.com/nodriver` was not a repo** — the fetch returned GitHub
   homepage nav ("PROGRAMS / Security Lab / BY INDUSTRY") and the pipeline
   turned nav menus into findings. Real repo is
   `github.com/ultrafunkamsterdam/nodriver`. Fix: correct URL + prose filter.
2. **Findings were severed from evidence** — findings carried a fake
   `reddit://r/...` pseudo-URL; real HN thread URLs/scores existed only in
   evidence. Fix: findings now carry `evidence` ids, real source URLs, and
   `dates` (HN `created_at` now flows through the connector payload).
3. **Plan dishonesty** — `depth=deep` forced `scientific: high` for a
   non-research topic, contradicting the planner's own rule text in the
   activity log. Fix: deep raises breadth, not relevance — off-topic classes
   stay `low` and the plan records that.
4. **`duration_s` in the manifest was always None** (dead expression) — fixed.
5. **Pseudo-source URLs** — findings now link out to real HN items;
   community sources render as links in the workbench.

Workbench gained: adjudication rendering (per-finding decision badges,
revised claims replace originals, rejected dimmed but retained, added
findings shown with `adjudication-synthesis-v0` method), manifest
`adjudicated` counts. All smoke tests pass (test4 manifest lazy-load,
test5 community UI, test6 adjudication render).

Review checklist kept for future sessions: research plan intent, evidence
quality (thread/score/occurrences/date), claim extraction (finding vs
restatement), community signal discipline (nothing graduates), contradictions
(docs vs community divergence), corpus impact, publish pack quality.

## Publishing Compiler (2026-08-05) — the downstream subsystem

Reviewer direction: adjudication is now a first-class, mandatory stage —
never compile drafts. `tools/hpf-research/publish.py` renders an ADJUDICATED
session into a publish pack:

```
Session -> Review -> Accepted Findings -> Compiler
NEVER Draft Findings -> Compiler
```

- Refuses to compile a session with no review layer (exit 2).
- Accepted findings only: approve / revise (revised claim) / add.
  Rejected findings are counted, never rendered (verified: 0 leaks).
- Output `exports/publish/<session-id>/` (immutable, exit 3 on overwrite):
  `publish-pack.json` + six renders (comparison, article, LinkedIn, X thread,
  FAQ, documentation). Every claim carries status, confidence (null),
  sources, evidence ids, dates.
- Release workflow assembles `exports/publish` → `website-hpf/publish`.
- Workbench: Publish view lists reviewed sessions + compiled packs (no more
  "draft findings" as publishable); pack detail route shows renders and
  accepted claims. UI copy renamed "adjudicated" → "Research Review".

First pack: `2026-08-05-0512-web-automation-pain-points-202` — 8 accepted
(7 revised + 1 contradiction added), 14 rejected excluded, 6 renders.

Pipeline now: Research → Evidence → Draft Findings → Research Review →
Accepted Findings → Publishing Compiler → Website / Social / Documentation.
The open question the reviewer set for HPF: can it consistently produce
accepted findings that require minimal rewriting before publication?

## Feature freeze + roadmaps (2026-08-05, after v1 release)

"Release HPF Workbench" dispatched and completed (all 10 steps, Cloudflare
Pages deploy OK). Architecture phase declared over; v1 feature-frozen:

- Allowed: bug fixes; new connectors only if a session fails without them;
  better extraction/adjudication/publishing quality; performance.
- Not allowed without repeated evidence: dashboards, workflow pages,
  navigation, governance, architecture.

Roadmap A (Research Engine): consistent high-quality adjudicated findings.
Roadmap B (Publishing Compiler): record per-session editing minutes per
render (Blog/LinkedIn/X/Documentation) — trend must go down.

Research Yield KPI: draft findings -> accepted findings. Session 001: 21 -> 8
(38%). Track stability across sessions; do NOT maximize.

Session 001 is the regression test: after any planner/connector/extraction/
adjudication/publishing change, re-run the identical session and compare
evidence, drafts, accepted findings, pack quality. Improvements that worsen
accepted findings or add unsupported claims are regressions.

## Operation phase (2026-08-05, development phase closed)

Platform declared complete enough for its intended purpose; feedback loops
(Research -> Review -> Publish -> Measure -> Improve) are now the driver.

Daily routine:
1. Choose research topic
2. Run HPF
3. Review findings
4. Generate publish packs
5. Publish (if ready)
6. Log friction

KPI set complete (no additions until weeks of data): Research Yield,
Editing Time, Usage Log friction, Regression Session 001. Owner dashboard
card deferred until 30-50 sessions. Priorities: run real research daily,
publish from HPF not ad hoc prompts, measure editing time honestly, improve
only what repeatedly slows work.


## Session 002 — Microsoft Fara vs Nodriver (2026-08-05)

Topic: "Microsoft Fara vs Nodriver: architecture, capabilities, and future of
AI browser automation" (Blog, deep). Goal includes Technology Maturity
assessment: production readiness, community adoption, maintenance activity,
breaking changes, vendor commitment, migration risk.

Run: 4 URLs fetched (microsoft/fara, ultrafunkamsterdam/nodriver, MS Learn
Foundry browser automation tool, HF Fara1.5-9B model card), 2 community
payloads (HN "Fara AI browser" 127 pts / 8 comments, "nodriver" 2 pts /
6 comments), 330 evidence entries, 18 draft findings (6 community signals).

Friction:
- HN search_by_date is story-title search: "Fara AI browser" returns mostly
  unrelated show-HN submissions; only 1-2 hits relevant (Puppeteer->Nodriver
  story, proxy-rotation post). "Fara1.5" returned 0 comments. Connector
  behaved honestly (refused empty payloads, exit 10). Community signal for
  this topic is thin — reddit connector would help but stays blocked.
- DeepWiki shows strong Fara repo documentation (5-browser-automation,
  quick-start) — not fetched; DeepWiki mirrors the repo, low added value.
- Keyword-density findings are heavy with code snippets (clone/install
  commands) — adjudication will filter most.
- Session id truncated to 30 chars ("...-arc").

## Job Status Contract (2026-08-05) — the awareness gap

Reviewer observation: HPF knows only what starts inside HPF. The publishing
engine holds state HPF never sees (Article Started / Draft Complete). Fix is
NOT coupling HPF to consumer internals — a shared, implementation-independent
Job Status Contract, the export-contract principle in reverse:

    Publishing -> status record -> exports/jobs/ -> HPF reads only that

Contract hpf-job-status-v0: id, type (research|publishing|marketing|website),
owner, status (queued|running|drafting|review|ready|done|blocked|cancelled),
started, updated, progress (free-form), research_session, outputs.

- tools/hpf-research/jobs.py: update/list/check; refuses unknown status/type
  (exit 2), unreadable existing record (exit 3), invalid record (exit 4);
  check exits 1 on any invalid record.
- exports/jobs/<id>.json + index.json (registry, committed).
- Workbench: Pipeline view (#/pipeline) — per-session chain Research ->
  Publishing -> Website -> Marketing with status badges, owner, progress,
  outputs. Read-only; HPF never writes consumer state.
- Release workflow assembles exports/jobs -> website-hpf/jobs.

First truthful records: research-001/publish-001/website-001 done;
research-002 done (18 drafts awaiting review); publish-002 queued
(awaiting research review).

## Session 002 — adjudication (2026-08-05)

Reviewer decision: Promising, not yet publishable. Core claim had to be
adjudicated before any pack.

Outcome: 1 approve, 4 revise, 13 reject, 5 add = 10 accepted of 18 drafts
(Research Yield 56%; raw draft survival 28% — 5 of 18 drafts survived
review unchanged or revised, the rest were restatements/code samples/
off-topic HN hits).

Decisive review question answered by synthesis f-19: Fara is a vision-first
AI computer-use LAYER (model, screenshots, pixel-grounded actions, harness
required), Nodriver is a CDP browser DRIVER (successor of
undetected-chromedriver, WAF resistance). Different classes, not successor.

Reviewer guidance recorded:
- No further Job Status Contract changes until publishing jobs have flowed
  through it (defer owner-vs-state separation and dependencies).
- Evidence uniqueness ratio (330 entries vs unique observations) noted as a
  candidate quality metric — not built.
- Article must organize around abstraction layers (AI decides vs developer
  decides), not feature-by-feature.
- Community volume caveat: report as "limited discussion", never consensus.
- No publish pack yet — waiting for framing approval.

## Session 002 — publish pack compiled (2026-08-05)

Framing decision (reviewer-directed): evidence supported the "different
layers" reading, so the compiler produced:

    Microsoft Fara vs Nodriver: Different Layers of the Browser Automation
    Stack

publish.py gained --title (publication title override; defaults to session
topic) — a publishing-quality change, allowed under the v1 freeze. Pack
records publication_title separately from session topic.

Pack: 10 accepted / 13 rejected excluded / LEAK none. Claims f-1, f-11,
f-12, f-13, f-16, f-19, f-20, f-21, f-22, f-23. Six renders. publish-002
job -> done (pack compiled, framing approved). Site publish/ synced.

Editing-time metric for this pack: NOT YET MEASURED — first honest reading
when the owner edits the article.

## Measurements — editing time + rejection reasons (2026-08-05)

Editing time is now THE most important HPF metric: "How many minutes does an
expert need before they're comfortable pressing Publish?"

Session 002 editing-time table (to be filled by the owner, honestly, during
the first edit pass):

| Render        | Editing Time | Notes                                |
| ------------- | -----------: | ------------------------------------ |
| Article       |        ? min | Architecture framing, flow, wording  |
| Comparison    |        ? min | Accuracy/completeness                |
| LinkedIn      |        ? min | Tone and hook                        |
| X thread      |        ? min | Compression and readability          |
| FAQ           |        ? min | Usually minimal edits                |
| Documentation |        ? min | Technical precision                  |

Rejection-reason categorization (first two data points, 27 rejects):

| Reason                  | S001 | S002 | Total |
| ----------------------- | ---: | ---: | -----:|
| Restated documentation  |    6 |    7 |    13 |
| Off-topic               |    2 |    4 |     6 |
| Marketing language      |    4 |    0 |     4 |
| Duplicate finding       |    1 |    1 |     2 |
| Navigation chrome       |    1 |    0 |     1 |
| Weak evidence/relevance |    0 |    1 |     1 |

Signal: the extraction stage's dominant failure is restatement (docs
installs, code samples, README blurbs) — that is the extraction roadmap.

Benchmarks:
- Session 001: regression benchmark (engine changes must not degrade it).
- Session 002: CLASSIFICATION benchmark — engine changes must not collapse
  the AI computer-use / browser framework / browser driver distinction.

Roadmap B objective: reduce median manual editing time by improving
compilation WITHOUT changing accepted findings. Compiler effort next:
section ordering, transitions, comparison tables, narrative flow, evidence
citations, uncertainty handling.

### Why-editing breakdown (added 2026-08-05, reviewer suggestion)

Editing time alone is an opaque number — two articles can both take 20
minutes for different reasons. Record WHY, per pack, alongside the totals.

Session 002 article edit categories (to fill during first edit pass):

| Edit Category        | Minutes |
| -------------------- | ------: |
| Structure/order      |       ? |
| Technical accuracy   |       ? |
| Evidence/citations   |       ? |
| Narrative flow       |       ? |
| Grammar/style        |       ? |
| TOTAL                |       ? |

Interpretation rule: if ~70% of time is narrative flow, improve the
compiler; if mostly evidence/citations, the problem is upstream in
research or adjudication.

No further metrics until 20-30 sessions of data accumulate.

## Research Opportunity Engine — PARKED (2026-08-05)

Architect proposal: scheduled discovery (cron) -> opportunity scoring ->
suggested-research queue -> owner approval; cookbook staleness as signal.
Design (cadence 6h/12h/daily/weekly/monthly; scorecard domain +40, vendor
+20, stars +15, HN +15, researched -50, duplicate -100) recorded in
chronicle entry 27.

PARKED per the measurement-driven rule (entry 26). No measured weakness yet
points to a discovery gap: Session 002's thin HN signal was connector query
quality, not missed opportunities.

Activation triggers (any one):
1. Owner logs topic-selection friction N times.
2. A materially important development goes undiscovered.
3. Cookbook staleness measured and shown to impact readers.
4. Post-20-30-sessions: a queue would have changed which sessions ran.

## Watchlist implemented (2026-08-05) — operational configuration

Reviewer correction: watchlist was operational configuration, not a
document-only idea. Decision-classification rule adopted (chronicle 28):

- Governance only -> document only
- Deferred architecture -> document only
- Operational configuration -> IMPLEMENT IMMEDIATELY
- Executable infrastructure -> IMPLEMENT IMMEDIATELY
- Production feature -> implement only if activated

Implemented:
- tools/hpf-research/config/watchlist.yaml (3 sections, 26 entries)
- tools/hpf-research/watchlist.py (load/validate/emit JSON; PyYAML or
  stdlib subset parser)
- research.py plan stage loads watchlist, logs watchlist_matches into the
  session plan (integration verified: Playwright/Nodriver topic matched 7
  entries)
- Workbench #/research/watched read-only view; release workflow assembles
  data/watchlist.json
- test9 green; full suite green

No discovery, no cron, no scoring. The parked Research Opportunity Engine
will seed from this list if the measurements ever earn it.

## Watchlist refinement (2026-08-05) — identifier-based matching, session persistence

Engineering review (8.5-9/10) findings addressed:

1. Substring matching fixed: entries now use id/aliases/type metadata
   (24 entries, 3 sections). match_topic() is boundary-aware + keyword
   equality only. Verified: 'chrome' no longer matches 'chromedriver';
   'cdp' -> chrome-devtools-protocol via alias; 'undetected chromedriver'
   matches via aliases.
2. Shared API: watchlist.load()/entries()/match_topic() — every consumer
   imports the same service (research.py today; compiler/website/engine
   later).
3. Session persistence: session.json carries top-level
   'watchlist': {matched: [...], coverage: <keyword overlap fraction>}.
   Queryable later without rebuilding. coverage is keyword overlap, NOT
   relevance/confidence — honest by construction.
4. DEFERRED: priority/sources/rss/reddit seed metadata — belongs to the
   parked Research Opportunity Engine, not this config.

Tests: test10 (matching algorithm) new + green; test9/4/8 green; syntax
clean. Note: 'coverage' was named deliberately instead of 'confidence' —
it measures keyword overlap, not certainty.

## Watchlist schema v1 (2026-08-05) — stable ids, normalization, validation

Reviewer round 2 (9.7-9.8/10): five long-term maintainability refinements.
Classified under decision-classification rule (entry 28):

- Implemented (operational config / infrastructure):
  - Stable vendor-independent canonical ids tech.<domain>.<name> + display
    'name' field (vendor transfers never rewrite history).
  - Alias normalization at load: everything normalized to lowercase with
    non-alphanumeric runs collapsed to single space; matching on one
    surface. 'playwright-python' = 'playwright python' = 'playwright_python'.
  - schema: hpf-watchlist-v1 at top of YAML, enforced at load, emitted by
    to_json(). Future schema changes versioned, not guessed.
  - Startup validation failing fast: duplicate ids / duplicate normalized
    aliases / missing aliases / missing type / empty sections -> ValueError;
    --check for CI. Config drift cannot be silent.
  - Matching now also uses normalized display name as a match surface
    (topic "Selenium" matches entry whose alias is "selenium webdriver").
- Documented only (measurement note): coverage depends on keyword
  generation -> treat as a debugging metric, NEVER compare across sessions
  unless keyword generation is frozen. Recorded in watchlist.py docstring.

Tests: test10 extended to 15 checks (8 matching + schema + 6 validation
rejections) all PASS; test9 (names in chips, ids as titles) PASS; test4/8
green. watchlist.json regenerated.

## Watchlist declared v1-mature (2026-08-05) — focus shifts to operations

Review round 3: production-quality verdict (10/9.6/9.5/9.5/9.7/9 rating
table), directive: STOP investing engineering time in the watchlist
unless a real research session exposes a concrete defect.

- Implemented (one surgical fix): session field 'coverage' renamed to
  'keyword_overlap' — old name invited cross-session comparison that the
  docs forbid; new name says exactly what it measures. Migration-free:
  no released session carries the field. match_topic() return shape,
  session plan field, plan log, workbench row, test10 updated; release
  JSON shape unaffected.
- Documented only (deferred architecture, not for v1; recorded in
  chronicle entry 31 with activation conditions): hierarchical matching,
  entry lifecycle, entry relationships, immutable ids + canonical paths,
  weighted aliases.
- Recorded do-not-build list (belongs to parked Opportunity Engine):
  priorities, RSS URLs, discovery scheduling, scoring, tags, dashboards,
  watch statistics, heatmaps.
- Focus shift: 20-30 real sessions for the measurement framework;
  editing-time data for Roadmap B; extraction (Research Yield ~56%) and
  adjudication (restatements/duplicates/marketing) improvement.

## Discovery activation (2026-08-05) — sources + discover.py

Review round 4: direction correction. The parked Research Opportunity
Engine (entry 27) is earning activation. Evidence (verified in records,
not asserted): Session 002's topic and all four primary URLs were
owner-supplied; Fara (released 2026-07-22) went undiscovered until the
owner brought it. Fires trigger (2).

Built (classification: operational config + minimal precursor; full
engine stays parked):
- watchlist entries gained 'sources' (WHERE TO LOOK): fixed vocabulary
  github_releases/docs/blog/npm/pypi/hf/reddit/hackernews, validated at
  load (unknown keys, non-list values rejected). Inert data; nothing
  runs against it autonomously. Corrects entries 29-30 deferral —
  reclassified on activation evidence.
- tools/hpf-research/discover.py: manual, on-demand, no cron/scoring/
  queue. --static prints suggestion seed list from watchlist;
  --releases fetches latest GitHub releases for configured repos and
  prints today's opportunities; --out writes JSON. Live run surfaced
  Stagehand browse@0.9.6, Puppeteer browsers v3.1.0, Foundry
  dotnet-1.17.0 unprompted.
- Workbench watchlist view renders sources per entry.

Not built (recorded): connector expansion (feature freeze: only when a
session fails without them), extraction/drafting improvements (await the
20-30 session measurement record). Allocation rule adopted: every change
must help discover better research / produce better findings / reduce
publishing edits, else it waits.

Tests: test10 +2 source-validation checks (17 PASS); test11 new:
discover --static (6 checks) + live --releases smoke, all PASS.

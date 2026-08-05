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


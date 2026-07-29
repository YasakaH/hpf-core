# Benchmark Impact Assessment — Browser State

## Questions Directly Affected

| QID | Mode | Question | Previous Dependency | New Knowledge Available |
|---|---|---|---|---|
| E04 | explain | What is a browser session lifecycle? | session-lifecycle-concept (18 lines) | Expanded with CDP events, WebDriver comparison, failure taxonomy |
| T01 | troubleshoot | Why do sessions expire unexpectedly? | session-lifecycle-concept (generic) | Session lifecycle states + specific failure causes with probabilities |
| T04 | troubleshoot | Why does the browser crash after multiple navigations? | No Crash knowledge object | Navigation lifecycle failure modes + crash recovery patterns |
| C01 | compare | CDP vs WebDriver | cdp-concept, webdriver-concept | Session lifecycle observability comparison table |
| C03 | compare | Selenium vs Playwright | playwright-concept, selenium-concept | Session lifecycle management comparison table |
| DS04 | design | Design a session management system | session-lifecycle-concept + 4 objects | Session lifecycle state machine, pool vs single vs per-op approaches |

## Questions Indirectly Affected

| QID | Mode | Question | Why |
|---|---|---|---|
| C06 | compare | Browser profile vs fresh session | Session lifecycle refresh implications clearer with state machine |
| D04 | decide | Should I implement health checks? | Readiness levels + session states enable better health check design |
| D05 | decide | Should I use a fresh browser profile per session? | Session lifecycle trade-offs (overhead vs isolation) clearer |
| DS03 | design | Design a retry mechanism for CDP operations | Navigation lifecycle failure modes inform retry-able vs not |
| T05 | troubleshoot | Why is data extraction missing content? | Navigation lifecycle explains content availability timing |

## M2 Improvement Priority Mapping

The new knowledge objects align with these improvement-priority deficiencies:

| Priority | Deficiency | New Knowledge Contribution |
|---|---|---|
| P1 | Compare evidence synthesis | Compare sections added to session-lifecycle-concept + navigation-lifecycle + readiness-model |
| P2 | Decision justification | Decide/design sections with approaches, trade-offs, recommendations |
| P3 | Knowledge object schema reuse | Objects now have structured Compare/Troubleshoot/Design sections |
| P5 | Narrow retrieval | 3 new knowledge objects expand retrieval pool for Browser State questions |

**Recommended next M2 cycle**: Re-benchmark E04, T01, T04, C01, C03, DS04 after the engine update to measure whether richer knowledge objects improve scores without engine changes. If scores improve, the hypothesis that P3 (schema reuse) is the root cause of P1-P2 is supported.

## Current Baseline Scores (run_002)

| QID | HPF | RAG | Winner |
|---|---|---|---|
| E04 | 65.0 | 54.8 | DISAGREEMENT |
| T01 | 53.0 | 86.8 | RAG |
| T04 | 53.0 | 39.0 | DISAGREEMENT |
| C01 | 27.2 | 70.2 | RAG |
| C03 | 18.8 | 78.0 | RAG |
| DS04 | 70.8 | 70.0 | DISAGREEMENT |

---

*Research Cycle 001 — 2026-07-29*

# Benchmark Impact Assessment — Browser Memory

## Questions Directly Affected

| QID | Mode | Question | Previous Dependency | New Knowledge Available |
|---|---|---|---|---|
| D05 | decide | Should I use a fresh browser profile per session? | browser-profiles-concept (18 lines) | Expanded to 150+ lines with structured decision factors, comparison criteria, trade-off table |
| C06 | compare | Browser profile vs fresh session | browser-profiles-concept (generic) | Structured comparison across 5 dimensions with per-dimension scoring |
| E05 | explain | Why do browser profiles matter? | browser-profiles-concept (18 lines) | Full profile component breakdown, isolation semantics, detection implications |
| D06 | decide | Should I use anti-detection techniques? | anti-detection-principle | Profile-based fingerprinting persistence, storage-based tracking surface |
| T01 | troubleshoot | Why do sessions expire unexpectedly? | session-lifecycle-concept | Cache/storage corruption as root cause, profile bloat as degradation factor |
| C05 | compare | Exponential backoff vs fixed backoff | retry-pattern (indirect) | Memory pressure influence on retry strategy selection |

## Questions Indirectly Affected

| QID | Mode | Question | Why |
|---|---|---|---|
| D04 | decide | Should I implement health checks? | Memory metrics should be part of health check probes |
| DS04 | design | Design a session management system | Session rotation strategy informed by memory pressure patterns |
| T04 | troubleshoot | Why does browser crash after multiple navigations? | OOM is an alternative root cause to navigation failure |
| DS03 | design | Design a retry mechanism for CDP operations | OOM-related failures should not be retried in same session |
| C01 | compare | CDP vs WebDriver | Memory monitoring capability is a comparison dimension |

## M2 Improvement Priority Mapping

| Priority | Deficiency | New Knowledge Contribution |
|---|---|---|
| P1 | Compare evidence synthesis | Browser profiles concept now has structured compare criteria across 5 dimensions |
| P2 | Decision justification | browser-profiles-concept has structured decision factors with supporting/contradictory/weight |
| P3 | Knowledge object schema reuse | All 3 objects use structured field names consumable by reasoner without inference |
| P5 | Narrow retrieval | 3 new knowledge objects (browser-storage, memory-pressure; expanded browser-profiles-concept) |

**Key improvement from Cycle 001**: HPF objects now expose structured fields per reasoning mode (compare: `comparison_criteria`, troubleshoot: `failure_modes` with typed sub-fields, decide: `decision_factors`, design: `approaches` with pros/cons/best_for, `pitfalls`, `best_practices`). This reduces the inference burden on the reasoner.

## Current Baseline Scores (run_002)

| QID | HPF | RAG | Winner |
|---|---|---|---|
| D05 | 49.2 | 76.2 | DISAGREEMENT |
| C06 | 45.0 | 86.5 | RAG |
| E05 | 78.0 | 74.8 | DISAGREEMENT |
| D06 | 64.0 | 88.0 | RAG |
| T01 | 53.0 | 86.8 | RAG |
| C05 | 76.8 | 69.8 | DISAGREEMENT |

---

*Research Cycle 002 — 2026-07-29*

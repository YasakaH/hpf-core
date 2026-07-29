# Research Cycle 002 — Browser Memory

## Summary

| Item | Count |
|---|---|
| Research dossier pages | 1 (dossier.md, 180 lines) |
| Canonical concepts added | 3 (browser-profile, browser-storage, memory-pressure) |
| Canonical concepts expanded | 0 |
| HPF knowledge objects added | 2 (browser-storage, memory-pressure) |
| HPF knowledge objects expanded | 1 (browser-profiles-concept, 18→170 lines) |
| Benchmark questions directly affected | 6 (D05, C06, E05, D06, T01, C05) |
| Benchmark questions indirectly affected | 5 (D04, DS04, T04, DS03, C01) |
| Book perspectives updated | 3 (Perspectives A, B, C) |
| Public artifacts | 1 (Why Clearing Cookies Isn't Enough) |
| Open questions recorded | 9 |

## Effort Distribution

| Phase | Estimated Effort | Notes |
|---|---|---|
| Research dossier | 35% | Profile anatomy and storage taxonomy consumed most time |
| Canonical concepts | 15% | Clean mapping from dossier to concepts |
| HPF knowledge objects | **35%** | Structured field design was the bottleneck (intentional quality focus) |
| Benchmark impact | 5% | Straightforward after Cycle 001 established the pattern |
| Book outline notes | 5% | Derived from concepts |
| Public artifact | 5% | Extracted one actionable insight |

## Quality Assessment

| Output | Quality | Issues |
|---|---|---|
| Research dossier | High | Profile storage taxonomy is comprehensive; memory pressure section thinner |
| Canonical concepts | High | Implementation-independent, well-defined relationships |
| HPF knowledge objects | **High** (improved) | Structured fields per mode (compare: comparison_criteria, troubleshoot: failure_modes with typed fields, decide: decision_factors, design: approaches/pitfalls/best_practices). Reasoner can consume without inference. |
| Benchmark impact | High | Clear mapping to existing questions |
| Book notes | High | Appropriate level; Perspective C getting useful framing |
| Public artifact | High | Self-contained, publishes actionable debugging insight |
| Open questions | High | 9 legitimate gaps |

## Quality Improvement from Cycle 001

HPF objects moved from prose-under-headings to structured semantic fields:

**Cycle 001 approach** (session-lifecycle-concept):
```
## Compare Section
(prose paragraphs under headings)
```

**Cycle 002 approach** (browser-profiles-concept):
```
## Compare Section
- dimension: detection_risk
- fresh_profile: {value: low, reason: ...}
- persistent_profile: {value: medium-to-high, reason: ...}
- tradeoff_table:
  - criterion: detection_risk, winner: fresh_profile, importance: critical
```

This structure is directly consumable by the reasoner — each field name maps to a reasoning mode's expected input. The renderer can read `failure_modes[*].observable_evidence` without parsing prose.

## Key Finding

The structured field approach adds ~2x development time per HPF object but eliminates the inference gap. For Cycle 003 (Browser Perception), maintain this quality bar. The trade-off is acceptable because objects are created once and consumed by all downstream outputs (HPF, books, blogs).

---

*2026-07-29*

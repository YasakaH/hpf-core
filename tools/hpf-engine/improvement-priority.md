# Improvement Priority — Evidence Analysis Only

This document ranks observed behavioural deficiencies by evidence weight. No implementation. No recommended sprints.

## Prioritisation Criteria

- **Evidence mass**: Number of benchmark questions exhibiting the behaviour
- **Score impact**: Measured gap between HPF and RAG on affected questions
- **Systemic depth**: Whether the behaviour is a symptom of a deeper architectural issue
- **Independence**: Whether the behaviour can be isolated and validated independently

---

## P1 — Compare evidence synthesis

**Evidence**: 6/6 compare tasks affected. Average HPF 48.5 vs RAG 72.2 (-23.7 gap). All 6 tasks show the same pattern: HPF produces repetitive criteria, placeholder values, and missing trade-off reasoning.

**Behavioural description**: When asked to compare two entities, HPF produces a structured table with hardcoded generic criteria. The comparison does not reflect entity-specific differences. Scores are repetitive or contain placeholders ("varies"). Trade-off analysis and recommendation are generic.

**Questions exhibiting this**: C01, C02, C03, C04 (won by explain fallback), C05 (disagreement, saved by explain fallback), C06.

**Notable exception**: C04 (CSS selectors vs XPath) — HPF won because it fell back to explain mode. The sole retrieved object (selector-strategy-pattern) happened to contain good explanatory content. Confirms the compare template, not the knowledge, is the bottleneck.

---

## P2 — Decision justification

**Evidence**: 6/6 decide tasks affected. Average HPF 46.8 vs RAG 73.9 (-27.1 gap). All 6 tasks show low actionability scores (avg 3.7 vs RAG's 7.8).

**Behavioural description**: When asked a "should I" question, HPF produces a claim with supporting and contradictory evidence, but the evidence is shallow (drawn from generic prose, not structured decision data). Risks are generic. Recommendations lack specificity.

**Questions exhibiting this**: D01, D02, D03, D04, D05, D06.

**Dimension breakdown** (HPF vs RAG):
- technical_correctness: 6.3 vs 8.0 (-1.7)
- completeness: 5.0 vs 8.2 (-3.2)
- reasoning_quality: 5.8 vs 7.5 (-1.7)
- actionability: 3.7 vs 7.8 (-4.1) ← **largest single-dimension gap across all modes**

---

## P3 — Knowledge object schema not reusable across modes

**Evidence**: 16/30 questions (all compare, decide, troubleshoot, design). Current schema stores prose narratives with optional mode-specific sections. Only 4/14 objects have any mode-specific sections. Engine depends on sections that mostly don't exist.

**Behavioural description**: Knowledge objects are written as documentation (prose narratives) rather than structured semantic records. Each reasoning mode requires specific data shapes that the objects don't provide. The engine's templates attempt to extract mode-specific content from prose, producing generic or empty output.

**Questions exhibiting this**: All C-series, D-series, DS-series, and T-series. Only E-series (explain) is unaffected because explain maps to the prose narrative naturally.

**Architectural note**: This is distinct from P1 and P2. P1 and P2 are symptoms of different user-facing capabilities (compare vs decide). P3 is the shared root cause — the knowledge objects lack the structural semantics that all modes (except explain) need.

---

## P4 — Judge ambiguity / rubric sensitivity

**Evidence**: 10/30 questions where judges disagreed. 5 of 10 classified as rubric ambiguity — Mistral consistently penalizes breadth without depth, Llama consistently penalizes depth without breadth.

**Behavioural description**: The dual-judge system disagrees on 1/3 of questions. Most disagreements trace to different weighting of the 6 scoring dimensions, not genuine quality differences. This means the current average scoring is sensitive to which judges are used.

**Questions exhibiting this**: C05, D01, D05, DS01, DS02, DS04, E04, E05, E06, T04.

---

## P5 — Narrow retrieval for non-explain modes

**Evidence**: 16/30 questions. HPF retrieves avg 3.1 objects per question vs RAG's 10.3. In decide mode, HPF retrieves avg 2.0 objects vs RAG's 14.

**Behavioural description**: The max-per-entity scoring strategy works well for explain (where precision matters) but starves compare/decide/design/troubleshoot modes that benefit from broader context.

**Interaction with P3**: Even with broad retrieval, the templates would struggle because objects lack structured sections. P5 is downstream of P3.

---

## P6 — No fallback strategy for thin retrieval

**Evidence**: 8/30 questions with ≤2 retrieved objects. HPF doesn't adapt — it produces the same template with shorter content.

**Behavioural description**: When retrieval returns <2 objects, HPF proceeds with the same template. Contrast with compare→explain fallback (which exists) but no equivalent for decide, troubleshoot, or design.

**Questions exhibiting this**: C04 (saved by existing explain fallback), C05 (saved by existing explain fallback), D02 (1 object), D03 (1 object), D04 (1 object), D06 (2 objects), DS02 (1 object), T02 (1 object), T06 (1 object).

---

## P7 — Hallucination from dynamic entity extraction

**Evidence**: 5/30 questions. T04 (hallucination_penalty=2) is worst case.

**Behavioural description**: Dynamic entity extraction picks up terms like "crash" that match no knowledge object. The engine still retrieves based on these entities, producing off-topic or hallucinated content.

**Questions exhibiting this**: E01, E02, E07, E08, T04.

---

## Summary

| Priority | Behavioural Deficiency | Evidence | Score Gap |
|---|---|---|---|
| P1 | Compare evidence synthesis | 6/6 tasks | -23.7 |
| P2 | Decision justification | 6/6 tasks | -27.1 |
| P3 | Knowledge object schema not reusable | 16/30 questions | Systemic |
| P4 | Judge ambiguity / rubric sensitivity | 10/30 questions | Measurement |
| P5 | Narrow retrieval for non-explain modes | 16/30 questions | Indirect |
| P6 | No fallback strategy for thin retrieval | 8/30 questions | Indirect |
| P7 | Hallucination from entity extraction | 5/30 questions | Small |

**Key relationship**: P3 (knowledge schema) is the architectural root cause of which P1 (compare) and P2 (decide) are the most visible symptoms. P4 is a measurement concern, not a behavioural one. P5 and P6 are downstream of P3. P7 is independent.

This document will be updated when evidence from subsequent benchmark runs changes the priority ordering. No implementation decisions are recorded here.

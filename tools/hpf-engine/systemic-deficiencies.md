# Systemic Deficiencies — Aggregate Analysis

## Method

22 isolated mistakes observed across 30 benchmark questions → grouped into 9 recurring behaviours → aggregated into 3 systemic deficiencies.

---

## Isolated Mistakes (22)

Observed from judge rationales, trace data, and score patterns:

1. C01 — HPF compare repetitive, lacks depth, has placeholders
2. C02 — HPF compare repetitive, "varies" placeholder, lacks depth
3. C03 — HPF compare incomplete, no meaningful comparison
4. C04 — HPF fell back to explain (only HPF win in compare)
5. C05 — HPF fell back to explain (disagreement — saved by explain quality)
6. C06 — HPF compare incomplete, repetitive, lacks depth
7. D01 — HPF vague, incomplete, has placeholders
8. D02 — HPF vague, lacks substance despite correct technical content
9. D03 — HPF vague, unspecific, lacks meaningful content
10. D04 — HPF vague, lacks depth, scores low on actionability
11. D05 — HPF vague, lacks practical value (per Mistral)
12. D06 — HPF actionability score low (4 vs 9)
13. DS01 — HPF actionability score low (4 vs 9 per Llama)
14. DS02 — HPF incomplete, lacks depth (per Mistral); actionability low (per Llama)
15. DS03 — HPF low actionability (scores 4 from both judges)
16. DS04 — HPF actionability low (6 vs 9 per Llama)
17. E04 — HPF structured but narrow (disagreement)
18. E05 — HPF lacking clarity (Mistral: 7 vs B's 9)
19. E06 — HPF lacking actionability (6 vs 8 per Llama)
20. T01 — HPF incomplete, lacks concrete steps
21. T04 — HPF hallucinated content (per Mistral, hallucination_penalty=2)
22. T05 — HPF lower actionability (4 vs 9 per Llama)

---

## Recurring Behaviours (9)

### Behaviour 1: Compare mode produces template soup
**Evidence**: C01, C02, C03, C06 all show repetitive scoring, placeholder text ("varies"), and generic criteria that don't reflect the actual comparison. C04 and C05 only "won" because they fell back to explain mode.

**Frequency**: 6/6 compare questions affected.

### Behaviour 2: Low actionability across all modes
**Evidence**: HPF's actionability scores average 3.7 in decide, 4.3 in design, 5.2 in troubleshoot, 7.1 in explain. RAG's actionability scores are consistently 2-4 points higher.

**Frequency**: 18/30 questions show HPF actionability ≤ RAG actionability.

### Behaviour 3: Narrow retrieval limits answer breadth
**Evidence**: HPF retrieves avg 3.1 objects per question. RAG consults avg 10.3. In decide mode (avg 2.0 objects), this is most damaging.

**Frequency**: Present in every question. Most visible in D-series (decide).

### Behaviour 4: Explain mode outperforms other modes
**Evidence**: Explain mode scores (avg 74.6) beat every other mode. The explain template (definition + mechanics + examples + limitations) maps directly to knowledge object structure.

**Frequency**: 7/8 explain questions score above 65.0.

### Behaviour 5: No fallback strategy when retrieval is thin
**Evidence**: When 1-2 objects are retrieved (C04, C05, D02, D03, D04), HPF doesn't adapt its strategy — it just produces a shorter answer from the same template.

**Frequency**: All cases with ≤2 retrieved objects (8 questions).

### Behaviour 6: Knowledge objects lack structured sections
**Evidence**: Only 4/14 objects have Compare/Decide/Troubleshoot/Design sections beyond the base. The engine relies on these sections that don't exist.

**Frequency**: Affects all compare, decide, troubleshoot, and design mode questions.

### Behaviour 7: Actionability dimension is systematically weak
**Evidence**: Actionability is HPF's lowest-scoring dimension across all modes (avg 5.1 vs RAG's 7.4). The gap is largest in decide (-4.1) and design (-2.8).

**Frequency**: Every question.

### Behaviour 8: Hallucination in specific edge cases
**Evidence**: T04 had hallucination_penalty=2 for HPF, the worst across all questions. E01, E02, E07, E08 also had lower hallucination scores for HPF.

**Frequency**: 5/30 questions affected, primarily when entity extraction picks up loosely related concepts.

### Behaviour 9: Output length correlates with scores
**Evidence**: HPF avg output 683 chars vs RAG's 763. Shorter HPF answers (D02: 349, D04: 344, C04: 388) get penalized on completeness and actionability.

**Frequency**: Present across all modes but most visible in decide (HPF avg 441 vs RAG's 863).

---

## Systemic Deficiencies (3)

### Deficiency 1: Template-Driven Architecture Without Content Awareness

- **Behaviours**: 1 (compare template soup), 4 (explain overperformance), 6 (missing sections), 9 (length correlation)
- **Root cause**: HPF uses fixed mode-specific templates that assume knowledge objects have corresponding structured sections. When those sections don't exist, the template generates generic, repetitive, or placeholder-filled output. Explain mode works because its template aligns with the natural prose structure of all knowledge objects.
- **Evidence**: Compare mode loses 5/6 times because objects lack `## Compare` sections. Explain mode wins 6/8 because every object has narrative prose that maps to definition/mechanics/examples/limitations.
- **Hypothesis**: Adding structured sections to knowledge objects would fix this deficiency.
- **Validation path**: Add `## Compare`, `## Decide`, `## Troubleshoot`, `## Design` sections to 2-3 objects, rerun benchmark on affected questions, compare scores.

### Deficiency 2: Retrieval Over-Narrowing

- **Behaviours**: 3 (narrow retrieval), 5 (no fallback strategy), 2 (low actionability)
- **Root cause**: HPF's max-per-entity scoring aggressively narrows retrieval to the best-matching objects. While this improves precision for explain questions, it starves compare/decide/design modes that benefit from breadth. Once retrieval narrows to 1-2 objects, the templates have insufficient raw material to produce comprehensive answers.
- **Evidence**: Decide mode retrieves avg 2.0 objects (RAG uses 14). Compare mode often fails to retrieve both entities being compared.
- **Hypothesis**: Mode-specific retrieval strategies would fix this — e.g., compare mode should retrieve N objects per entity, design mode should bias toward pattern objects.
- **Validation path**: Implement mode-aware retrieval with broader recall for compare/decide/design modes. Rerun benchmark on affected 16 questions.

### Deficiency 3: Actionability Blind Spot

- **Behaviours**: 2 (low actionability), 7 (systematic weakness), 9 (length correlation)
- **Root cause**: HPF's templates prioritize structured explanation over actionable guidance. The 6-dimension scoring rubric penalizes this systematically. Actionability is the dimension with the largest HPF-RAG gap (-2.3 avg, -4.1 in decide). The templates never include explicit "what to do next" or "how to implement" sections.
- **Evidence**: Every question shows HPF actionability ≤ RAG. No HPF template produces anything like "steps to implement" or "actionable recommendations."
- **Hypothesis**: Adding an "actionable steps" section to every template would close the actionability gap.
- **Validation path**: Add actionability-focused paragraphs to 2-3 templates. Rerun benchmark on 6 representative questions (1 per mode).

---

## Deficiency Interdependence

Deficiencies 1 (template) and 2 (retrieval) are independent — fixing either helps without the other. Deficiency 3 (actionability) depends on 1 — even with broader retrieval, the templates still won't produce actionable output. Fix order: 1 → 3 → 2.

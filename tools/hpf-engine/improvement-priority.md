# Improvement Priority — Ranked with Evidence

## Prioritisation Criteria

- **Impact**: Score improvement expected (high/medium/low)
- **Effort**: Implementation complexity (high/medium/low)
- **Evidence**: How many benchmark questions support this change
- **Attribution confidence**: Can we isolate the effect of this single change?

---

## Priority 1: Knowledge Object Section Expansion

| | |
|---|---|
| **Impact** | High |
| **Effort** | Medium |
| **Evidence** | 16/30 questions (all compare, decide, troubleshoot, design) |
| **Attribution** | High — specific questions map to specific objects |

**What**: Add `## Compare`, `## Decide`, `## Troubleshoot`, and `## Design` sections to all 14 knowledge objects. Each section must contain actual structured data (criteria with scores, supporting/contradictory claims, likely causes with probabilities, design approaches).

**Evidence**: 
- Compare mode loses 5/6 times because objects lack explicit compare data (compare-mode-analysis.md)
- Decide mode avg actionability is 3.7 vs RAG's 7.8 (decision-mode-analysis.md)
- Only 4/14 objects have any structured sections beyond base narrative

**Hypothesis**: Adding structured sections will transform compare mode from template-soup to data-driven comparison, and give decide/design/troubleshoot modes the raw material they need.

**Implementation**: 
1. Pick 2-3 objects with the most cross-references (e.g., playwright-concept, selenium-concept, anti-detection-principle)
2. Add `## Compare`, `## Decide`, `## Troubleshoot`, `## Design` sections
3. Rerun benchmark on affected questions

**Validation questions**: C01 (CDP vs WebDriver), C03 (Selenium vs Playwright), D01 (Should I migrate from Selenium?), T03 (Why does scraper get blocked?), DS01 (Design resilient scraper)

**Expected improvement**: Compare mode avg from 48.5 → ~65. Decide mode avg from 32.2 → ~50.

---

## Priority 2: Actionability Layer in All Templates

| | |
|---|---|
| **Impact** | High |
| **Effort** | Low |
| **Evidence** | 30/30 questions |
| **Attribution** | Medium — actionability is one of 6 dimensions |

**What**: Add an "actionable guidance" section to the end of every template. For explain: "practical implications." For compare: "migration considerations." For decide: "implementation steps." For troubleshoot: "fix procedure." For design: "build checklist."

**Evidence**: 
- Actionability is HPF's lowest dimension across ALL modes (-2.3 avg gap, -4.1 in decide)
- Every single HPF answer scores lower on actionability than the RAG equivalent

**Hypothesis**: A simple "what to do next" footer on every template will close the actionability gap by 1-2 points.

**Implementation**: 
1. Add one paragraph to each of the 5 formatters in renderer.py
2. Rerun benchmark on 6 representative questions (1 per mode)

**Validation questions**: E01 (CDP explanation — actionability), C01 (compare — actionability), D02 (HTTP 429 — actionability), T02 (flaky selectors — diagnostic steps), DS03 (CDP retry mechanism — build guidance)

**Expected improvement**: All modes gain +1.5 to +2.5 on actionability dimension.

---

## Priority 3: Mode-Aware Retrieval Strategy

| | |
|---|---|
| **Impact** | Medium |
| **Effort** | High |
| **Evidence** | 16/30 questions (all compare, decide, troubleshoot, design) |
| **Attribution** | Low — confounding with template changes |

**What**: Replace uniform max-per-entity scoring with mode-specific retrieval configs:
- **explain**: Keep current max-per-entity (precision-focused)
- **compare**: Retrieve N objects per entity, bias toward objects with `## Compare` sections
- **decide**: Broaden recall (lower match thresholds), prefer objects with `## Decide` sections
- **troubleshoot**: Retrieve by symptom/entity mapping
- **design**: Bias toward pattern-type objects

**Evidence**: 
- Decide mode retrieves avg 2.0 objects vs RAG's 14
- Compare mode sometimes retrieves only 1 entity's objects (C04, C05)
- Narrow retrieval is invisible in explain mode (which wins 6/8) but cripples other modes

**Hypothesis**: Mode-aware retrieval will increase average retrieved objects from 3.1 to 5-6 for compare/decide/design modes, providing more raw material for templates.

**Implementation**: 
1. Add `mode` parameter to `retriever.retrieve()` 
2. Define mode-specific scoring configs
3. Adjust max-per-entity and minimum thresholds per mode

**Validation questions**: All 6 compare, all 6 decide, all 4 design, all 6 troubleshoot questions.

**Expected improvement**: Compare mode avg from 48.5 → ~58. Decide mode avg from 32.2 → ~42.

---

## Priority 4: Hallucination Guard for Entity Extraction

| | |
|---|---|
| **Impact** | Low |
| **Effort** | Low |
| **Evidence** | 5/30 questions |
| **Attribution** | High — hallucination_penalty is explicit |

**What**: Add confidence filtering to dynamic entity extraction. If extracted entity has <0.5 match confidence to any known concept, exclude it or flag it in the output.

**Evidence**: T04 (browser crash) hallucinated because "crash" was dynamically extracted but no knowledge object covers crash causes. E01/E02/E07/E08 had lower hallucination scores for HPF.

**Implementation**: 
1. Add confidence threshold to `question_analyzer.extract()`
2. Filter out low-confidence dynamic entities

**Expected improvement**: T04 hallucination_penalty from 2 → 4. Marginal overall score gain.

---

## Priority 5: Length-Normalised Scoring Analysis

| | |
|---|---|
| **Impact** | Low (analysis only) |
| **Effort** | Low |
| **Evidence** | 30/30 questions |
| **Attribution** | N/A — diagnostic |

**What**: Analyse whether the scoring rubric systematically penalises shorter answers. If completeness scores correlate with answer length (r > 0.5), the rubric may need adjustment for human evaluation.

**Evidence**: HPF avg output 683 chars vs RAG's 763. D02 (HPF: 349 chars, score 31.0) vs D02 (RAG: 863 chars, score 62.5).

---

## Priority Ordering Rationale

1. **Section expansion first** — Without data in the objects, no template or retrieval change can produce good answers. This is the bottleneck.
2. **Actionability layer second** — Low effort, high impact, independent of other changes. Can be done in parallel with section expansion.
3. **Mode-aware retrieval third** — Only valuable after objects have the sections to retrieve. Otherwise broad retrieval just pulls in more irrelevant content.
4. **Hallucination guard fourth** — Lower impact but easy to do.
5. **Length-correlation analysis** — Informational, not an implementation.

## Recommended Sprint

| Week | Work | Validation |
|---|---|---|
| 1 | Add sections to 3 objects + actionability layer | Run 6-question subset benchmark |
| 2 | Analyse results, expand sections to all 14 objects | Full 30-question benchmark |
| 3 | Mode-aware retrieval implementation | Full 30-question benchmark |
| 4 | Hallucination guard + length analysis | Full 30-question benchmark |

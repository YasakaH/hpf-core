# Disagreement Analysis — run_002

10 of 30 questions had split verdicts between Mistral Small and NVIDIA Llama. Each case classified below.

## Classification Categories

- **Rubric ambiguity**: Judges applied different weights to the 6 scoring dimensions
- **Model variance**: Judges reached opposite conclusions from similar reasoning
- **HPF behavioural issue**: HPF's structured output caused systematic scoring divergence
- **RAG behavioural issue**: RAG's free-form output caused systematic scoring divergence
- **Prompt ambiguity**: The evaluation prompt led to inconsistent interpretations
- **Genuine tie**: Answers are genuinely comparable in quality

---

## 1. C05 — Exponential backoff vs fixed backoff (compare)

- **Mistral → RAG** (broader context, practical details)
- **Llama → HPF** (more accurate, comprehensive)
- **Classification: Rubric ambiguity**
- Mistral valued breadth and practicality; Llama valued accuracy. Both valid. The `argument_keys` show HPF fell back to explain mode (no compare section), producing a definition-only answer. RAG gave a broader compare.

## 2. D01 — Should I migrate from Selenium? (decide)

- **Mistral → RAG** (actionable, complete)
- **Llama → HPF** (more accurate, comprehensive about Selenium)
- **Classification: Rubric ambiguity**
- HPF retrieved only 2 objects (selenium-concept, webdriver-concept). RAG consulted all 14. Mistral penalized HPF's brevity; Llama preferred its focused accuracy.

## 3. D05 — Should I use a fresh browser profile per session? (decide)

- **Mistral → RAG** (detailed, accurate, actionable)
- **Llama → HPF** (focused on specific stages, relevant)
- **Classification: Rubric ambiguity**
- HPF retrieved 5 objects; RAG consulted 14. Mistral penalized HPF for vagueness (scored 1/9 on actionability). Llama preferred HPF's focused relevance.

## 4. DS01 — Design a resilient scraper (design)

- **Mistral → HPF** (detailed, technically accurate, fewer hallucinations)
- **Llama → RAG** (comprehensive, well-structured)
- **Classification: Rubric ambiguity**
- HPF retrieved 3 objects with anti-detection, blocking, and selectors. RAG consulted all 14. Mistral penalized RAG for hallucination (score 3 vs 5). Llama preferred RAG's broader coverage.

## 5. DS02 — Build a production download pipeline (design)

- **Mistral → HPF** (detailed, technically accurate, actionable)
- **Llama → RAG** (clear, actionable, strong technical correctness)
- **Classification: Model variance**
- HPF retrieved 1 object (download-pipeline-pattern); RAG consulted 14. Mistral scored RAG poorly (3 completeness, 2 actionability). Llama scored HPF poorly (4 actionability). Both judges acknowledge quality but diverge on which is better.

## 6. DS04 — Design a session management system (design)

- **Mistral → HPF** (detailed, actionable, fewer gaps)
- **Llama → RAG** (comprehensive, accurate)
- **Classification: Rubric ambiguity**
- Mistral scored RAG low (5 completeness, 5 reasoning) while Llama scored HPF low (4 actionability). Same pattern as DS01/DS02 — Mistral penalizes breadth without depth, Llama penalizes depth without breadth.

## 7. E04 — What is a browser session lifecycle? (explain)

- **Mistral → HPF** (direct, structured, relevant)
- **Llama → RAG** (more accurate, actionable, detection techniques)
- **Classification: HPF behavioural issue**
- HPF directly addressed the question with session-lifecycle-concept. RAG's answer drifted into detection techniques (off-topic). Mistral correctly identified relevance. Llama's rationale shows it preferred RAG's broader but less relevant content — suggests the rubric doesn't penalize tangential content enough.

## 8. E05 — Why do browser profiles matter? (explain)

- **Mistral → HPF** (deeper technical context, reasoning about bot detection)
- **Llama → RAG** (clear, comprehensive, informative, actionable)
- **Classification: Rubric ambiguity**
- HPF explained browser profiles in the context of anti-detection. RAG gave a general explanation. Both valid framing; judges differ on which framing is more valuable.

## 9. E06 — What is anti-detection in browser automation? (explain)

- **Mistral → HPF** (comprehensive, technically accurate)
- **Llama → RAG** (more accurate, comprehensive, actionable advice)
- **Classification: Model variance**
- Near-total disagreement despite close scores. Both judges claim the other answer is less accurate. Suggests scoring is near the decision boundary; no clear winner.

## 10. T04 — Why does the browser crash after multiple navigations? (troubleshoot)

- **Mistral → RAG** (technically correct, hallucination-free, well-structured)
- **Llama → HPF** (comprehensive, multiple causes, actionable)
- **Classification: Model variance**
- Mistral heavily penalized HPF for hallucinated/nonsensical content (hallucination_penalty=2). Llama scored HPF well on technical_correctness (9) and completeness (8). Suggests HPF had some hallucinated content that Mistral caught but Llama missed, or vice-versa.

---

## Summary

| Category | Count | Cases |
|---|---|---|
| Rubric ambiguity | 5 | C05, D01, D05, DS01, DS04 |
| Model variance | 3 | DS02, E06, T04 |
| HPF behavioural issue | 1 | E04 |
| RAG behavioural issue | 0 | — |
| Prompt ambiguity | 0 | — |
| Genuine tie | 0 | — |

**Key insight**: Most disagreements stem from rubric ambiguity (5/10) — Mistral consistently penalizes vagueness/breadth, Llama consistently penalizes lack of comprehensiveness. Only E04 shows a clear HPF behavioural issue (off-topic RAG answer not penalized by the rubric). The 3 model variance cases are near the decision boundary and likely noise.

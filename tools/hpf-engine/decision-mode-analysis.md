# Decision Mode Analysis — Why Decide Mode Scores Low

## Summary

| QID | Question | HPF avg | RAG avg | Winner | Gap |
|---|---|---|---|---|---|
| D01 | Should I migrate from Selenium? | 64.2 | 73.8 | DISAGREEMENT | -9.6 |
| D02 | Should I retry on HTTP 429? | 31.0 | 62.5 | HPF | -31.5 |
| D03 | Should I use data-testid selectors? | 47.8 | 88.5 | RAG | -40.7 |
| D04 | Should I implement health checks? | 24.8 | 54.5 | HPF | -29.7 |
| D05 | Should I use fresh profile per session? | 49.2 | 76.2 | DISAGREEMENT | -27.0 |
| D06 | Should I use anti-detection techniques? | 64.0 | 88.0 | RAG | -24.0 |

HPF won 2, RAG won 2, 2 disagreements. But average HPF (46.8) < average RAG (73.9) by a wide margin.

---

## Root Cause Analysis

### 1. Knowledge Gap: Only 1-2 objects per question

| QID | HPF objects retrieved | RAG objects consulted |
|---|---|---|
| D01 | 2 (selenium-concept, webdriver-concept) | 14 |
| D02 | 1 (retry-pattern) | 14 |
| D03 | 1 (selector-strategy-pattern) | 14 |
| D04 | 1 (health-check-pattern) | 14 |
| D05 | 5 (session-lifecycle, browser-profiles, health-check, playwright, retry) | 14 |
| D06 | 2 (anti-detection-principle, blocking-rate-limiting-principle) | 14 |

HPF retrieves a narrow set of directly matching objects (avg 2.0). RAG consults all 14 objects every time. For a "should I" question, RAG has access to 7x more information to build supporting/contradictory arguments.

### 2. Structural Gap: Objects lack `## Decide` sections

HPF's decide mode extracts:
- `claim` — inferred from question
- `supporting` — from object text, but no structured `## Decide` section
- `contradictory` — from object text
- `risks` — from object text
- `recommendation` — from object text

Only 4 of 14 objects have a `## Decide` section. The rest rely on generic prose extraction, which produces vague supporting/contradictory claims.

**Example**: For D02 "Should I retry on HTTP 429?", HPF retrieved only retry-pattern. The retry-pattern object explains *how* retries work but doesn't discuss *whether* to retry on 429 specifically. HPF's decide mode generated a generic claim with weak support. RAG consulted all 14 objects and found relevant content about rate limiting, blocking detection, and session management.

### 3. Template Rigidity

The decide template always produces:
```
## Decision: {claim}
### Supporting Evidence
### Contradictory Evidence
### Risks
### Recommendation
```

This works when objects have explicit decision-relevant content. When they don't, the sections are filled with:
- Vague generalities from the object's prose
- Missing contradictory evidence (only 1 object → no counter-perspective)
- A recommendation that doesn't weigh tradeoffs

### 4. Answer Length Correlation

| QID | HPF length | RAG length | HPF score |
|---|---|---|---|
| D01 | 533 | 863 | 64.2 |
| D02 | 349 | 863 | 31.0 |
| D03 | 361 | 863 | 47.8 |
| D04 | 344 | 863 | 24.8 |
| D05 | 480 | 863 | 49.2 |
| D06 | 578 | 863 | 64.0 |

RAG always produces 863 chars (full context window). HPF's output is shorter (avg 441 vs 863). Length correlates with completeness scores. HPF's shorter answers are penalized on the completeness dimension.

### 5. Dimension-Level Breakdown

Looking at judge scores for decide questions:

| Dimension | HPF avg | RAG avg | Gap |
|---|---|---|---|
| technical_correctness | 6.3 | 8.0 | -1.7 |
| completeness | 5.0 | 8.2 | -3.2 |
| reasoning_quality | 5.8 | 7.5 | -1.7 |
| actionability | 3.7 | 7.8 | -4.1 |
| clarity | 6.8 | 7.7 | -0.9 |
| hallucination_penalty | 4.3 | 4.8 | -0.5 |

**Actionability is the biggest gap (-4.1)**. HPF's structured decision output is generic and doesn't give specific, actionable guidance. RAG's free-form answers provide concrete steps.

---

## Conclusion

Decide mode suffers from a **knowledge gap** (too few objects per question) and **framework gap** (objects lack structured Decide sections). The actionability deficit (-4.1) is the most damaging single dimension gap across all modes.

Without expanding knowledge objects to include `## Decide` sections with explicit supporting/contradictory claims and risk analysis, HPF cannot compete with RAG's ability to synthesize decision guidance from the full domain.

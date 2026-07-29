# Compare Mode Analysis — Why RAG Wins 4/6

## Summary

| QID | Question | HPF avg | RAG avg | Winner | Gap |
|---|---|---|---|---|---|
| C01 | CDP vs WebDriver | 27.2 | 70.2 | RAG | -43.0 |
| C02 | Playwright vs nodriver | 36.8 | 84.2 | RAG | -47.4 |
| C03 | Selenium vs Playwright | 18.8 | 78.0 | RAG | -59.2 |
| C04 | CSS selectors vs XPath | 86.2 | 64.2 | HPF | +22.0 |
| C05 | Exponential backoff vs fixed backoff | 76.8 | 69.8 | DISAGREEMENT | +7.0 |
| C06 | Browser profile vs fresh session | 45.0 | 86.5 | RAG | -41.5 |

HPF won 1, RAG won 4, 1 disagreement.

---

## C01 — CDP vs WebDriver (RAG won)

- **HPF retrieved**: webdriver-concept, cdp-concept, + 3 extras
- **HPF output**: 1283 chars, mode=compare, criteria+scoring+tradeoffs+recommendation
- **RAG consulted**: 7 objects, 654 chars
- **Mistral**: "Answer A [RAG] provides accurate, actionable, well-structured details... Answer B [HPF] is repetitive, lacks depth, contains placeholders"
- **Llama**: "Answer A [RAG] provides more accurate and relevant information... Answer B [HPF] is overly simplistic and inaccurate"
- **Root cause**: HPF's compare template produced repetitive scoring across hardcoded criteria without extracting meaningful differences from the objects. RAG gave a direct, practical comparison.

## C02 — Playwright vs nodriver (RAG won)

- **HPF retrieved**: nodriver-concept, playwright-concept (2 objects, correct)
- **HPF output**: 1656 chars — longest HPF compare answer
- **RAG consulted**: 2 objects, 517 chars
- **Mistral**: "Answer A [RAG] provides accurate, detailed, well-structured information... Answer B [HPF] is repetitive, lacks depth, contains placeholders ('varies')"
- **Llama**: "Answer A [RAG] provides clear and accurate comparison... Answer B [HPF] fails to provide meaningful information"
- **Root cause**: Despite retrieving the correct 2 objects, HPF's evidence_builder couldn't extract meaningful compare data from knowledge objects that lacked `## Compare` sections. The `argument_keys` show it fell into criteria+scoring+tradeoffs template, but the objects didn't have the data to fill them properly.

## C03 — Selenium vs Playwright (RAG won, biggest gap)

- **HPF retrieved**: playwright-concept, selenium-concept, webdriver-concept
- **HPF output**: 1533 chars
- **RAG consulted**: 3 objects, 849 chars
- **Mistral**: "Answer A [RAG] provides accurate, detailed, well-structured information... Answer B [HPF] is repetitive, incomplete, lacks meaningful content"
- **Llama**: "Answer A [RAG] provides clear and accurate comparison... Answer B [HPF] fails to provide any meaningful comparison"
- **Root cause**: Same structural failure as C02. Neither playwright-concept nor selenium-concept has a `## Compare` section. HPF's compare mode relies on knowledge objects having explicit compare data, but they don't. The template generates empty or placeholder-filled output.

## C04 — CSS selectors vs XPath (HPF won)

- **HPF retrieved**: selector-strategy-pattern (1 object)
- **HPF output**: 388 chars, **fell back to explain mode** (argument_keys: target/definition/core_mechanics/examples/limitations)
- **RAG consulted**: 1 object, 153 chars
- **Mistral**: "Answer B [HPF] provides more structured, detailed, actionable comparison with clear examples"
- **Llama**: "Answer B [HPF] provides more comprehensive information and better supports its claims"
- **Why HPF won**: Fallback to explain mode actually worked here. selector-strategy-pattern had good explain content. RAG's output was too short (153 chars). The explain-formatted answer for a compare question was actually better than RAG's minimal compare.

## C05 — Exponential backoff vs fixed backoff (Disagreement)

- **HPF retrieved**: retry-pattern (1 object), fell back to explain mode
- **HPF output**: 534 chars, explain-formatted
- **RAG consulted**: 2 objects, 488 chars
- **Mistral → RAG**, **Llama → HPF**
- Near-tie. HPF's explain fallback produced a decent answer covering backoff mechanics. RAG was broader. Both close in quality.

## C06 — Browser profile vs fresh session (RAG won)

- **HPF retrieved**: session-lifecycle-concept, browser-profiles-concept + 3 extras
- **HPF output**: 1519 chars, mode=compare with criteria+scoring+tradeoffs+recommendation
- **RAG consulted**: 12 objects, 863 chars
- **Mistral**: "Answer B [RAG] provides accurate, detailed, actionable insights. Answer A [HPF] is incomplete, repetitive, lacks depth."
- **Llama**: "Answer B [RAG] provides more accurate and actionable information."
- **Root cause**: Again, objects lacked `## Compare` sections, so HPF's template generated generic scoring with placeholder content. RAG drew from 12 objects and synthesized a practical comparison.

---

## Systemic Failure Identified

**The compare template requires data that the knowledge objects don't provide.**

HPF's evidence_builder.build() for compare mode expects objects to have `## Compare` sections with criteria, scores, and tradeoffs. Of the 14 knowledge objects, only 4 have sections beyond the base (compare/decide/troubleshoot/design). When those sections are missing, the template produces:

1. Hardcoded generic criteria that don't reflect the actual comparison
2. Placeholder or repetitive scoring values
3. Missing tradeoff analysis

RAG wins on compare because it synthesizes across all objects in the domain, extracting relevant differences even from unrelated content.

**Evidence**: C04 (the one HPF won) is the exception — HPF fell back to explain mode, and the single retrieved object did have good content. This confirms the compare template is the problem, not the retrieval or knowledge base.

## Recommended Fix

Dynamic criteria generation from retrieved objects instead of hardcoded template. Extract entity-specific attributes from each object's prose and construct comparison dimensions dynamically.

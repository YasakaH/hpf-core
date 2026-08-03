# Attribution Assessment

## Identity
- id: attribution-assessment
- type: decision
- title: Attribution Assessment for Midnight Foundry
- tags: [attribution, state-affiliated, professional contract, competing hypotheses, language artifacts, UTC+8, K7 evidence, unresolved]
- entities: [attribution, state-affiliated hypothesis, professional contract hypothesis, K7 relatedness, competing hypotheses]
- concepts: [midnight-foundry-campaign, k7-overlap, hammer-b-variant, open-analytical-questions]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The leading hypothesis attributes the activity to a state-affiliated group, supported by language artifacts in Hammer-B, operational hours aligned with UTC+8, procurement-linked targeting, and the dismissal of the K7 link by some analysts."
  certainty: medium
  evidence: Source material pack §8; leading-hypothesis reading
  scope: cross-domain
- claim: "The competing hypothesis holds that the intrusions are contract work by a professional group possibly related to K7, supported by the infrastructure overlap, operational cleanliness, and the shared tooling comment string."
  certainty: medium
  evidence: Source material pack §8; competing-hypothesis reading
  scope: cross-domain
- claim: "Both hypotheses remain open; the evidence is insufficient to choose between them with confidence."
  certainty: high
  evidence: Source material pack §8
  scope: cross-domain

## Decision Factors
- factor: operational_hours
  question: "Do the observed operational hours indicate a specific time zone?"
  supporting: "Hours align with UTC+8"
  contradictory: "Hours could fit other explanations"
  weight: medium
- factor: language_artifacts
  question: "What do the Hammer-B code comments indicate?"
  supporting: "Consistent with a specific East Asian language family"
  contradictory: "Reading is recorded, not demonstrated"
  weight: medium
- factor: infrastructure_overlap
  question: "What does the K7 infrastructure overlap indicate?"
  supporting: "One VPS in a previously K7-used IP range"
  contradictory: "A single overlap; no other links found"
  weight: medium
- factor: targeting_consistency
  question: "Is the procurement-linked targeting consistent with state collection priorities?"
  supporting: "Defense supply-chain targeting, procurement timing"
  contradictory: "Correlation, not demonstrated intent"
  weight: medium
- factor: operational_cleanliness
  question: "How does operational cleanliness bear on the hypotheses?"
  supporting: "Cleaner than typical state campaigns"
  contradictory: "Cleanliness is not hypothesis-decisive"
  weight: low

## Relationships
- concept: midnight-foundry-campaign
  relationship: linked_to
  description: "The assessment concerns the campaign."
- concept: k7-overlap
  relationship: linked_to
  description: "The K7 links are weighed as the strongest competing evidence."
- concept: hammer-b-variant
  relationship: linked_to
  description: "The language artifacts are weighed for the state-affiliated reading."
- concept: open-analytical-questions
  relationship: constrained_by
  description: "The unresolved assessment is constrained by the open questions."

## Tradeoffs
- dimension: attribution_specificity_vs_certainty
  options:
    specific_attribution: "Named-actor claims focus the response but stand on thinner evidence"
    general_attribution: "General origin claims stay within the evidence but guide response less"
  importance: high

## Constraints
- constraint: "The assessment records both hypotheses and their evidence; it does not resolve them."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Hold both hypotheses in tracking systems with the evidence each side cites."
  rationale: "The source concludes the evidence is insufficient."
  evidence_level: high

## Recommendations
- recommendation: "Keep both attribution hypotheses open in tracking systems, each with its supporting evidence listed."
  context: analysis
  certainty: strong
  rationale: "The source's conclusion is that the evidence is insufficient."
- recommendation: "Record what evidence would move each hypothesis before acting on either."
  context: analysis
  certainty: moderate
  rationale: "The assessment is unresolved by design."

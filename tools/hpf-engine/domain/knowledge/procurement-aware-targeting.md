# Procurement-Aware Targeting

## Identity
- id: procurement-aware-targeting
- type: pattern
- title: Procurement-Aware Targeting Pattern
- tags: [targeting pattern, procurement timing, defense supply chain, funded program, lure sourcing, unexplained]
- entities: [procurement timing, funded procurement program, procurement-aware lures, supply chain targeting]
- concepts: [victim-set, spearphishing-initial-access, attribution-assessment]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "In all four compromises, access was obtained within two weeks of the victim becoming part of a funded procurement program visible in public procurement notices."
  certainty: high
  evidence: Source material pack §2
  scope: cross-domain
- claim: "The lure content references real procurement documents that would be visible only to someone with prior access to the procurement process or to the relevant procurement feeds."
  certainty: high
  evidence: Source material pack §3
  scope: cross-domain
- claim: "The sourcing of the procurement-aware lure content is unexplained; it may imply a separate, earlier compromise of a procurement entity that has never been observed."
  certainty: low
  evidence: Source material pack §9.5; analyst hypothesis
  scope: cross-domain
- claim: "The procurement-linked timing is consistent with state collection priorities, but the source records this as an analytical reading, not a demonstrated fact."
  certainty: medium
  evidence: Source material pack §8
  scope: cross-domain

## Relationships
- concept: victim-set
  relationship: linked_to
  description: "The pattern correlates with compromise timing across the victim set."
- concept: spearphishing-initial-access
  relationship: linked_to
  description: "Procurement-aware content informs the tailored lure templates."
- concept: attribution-assessment
  relationship: linked_to
  description: "Targeting consistency is weighed as evidence in the attribution assessment."

## Failure Modes
- name: correlation_overread
  description: "Procurement-timing correlation is treated as demonstrated targeting intent rather than a recorded correlation."
  likelihood: medium
  observable_evidence: "Attribution arguments that cite timing as proof of state collection priorities without the source's own caveats"
  detection: "Fact-vs-reading audit on timing claims"
  recovery: "Record the correlation as an observable and the state-collection reading as an interpretation"
  retryable: true

## Constraints
- constraint: "The timing correlation is an observed pattern, not evidence of intent."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Record procurement timing as an observable and label the collection-priority reading as interpretation."
  rationale: "The source itself keeps the correlation and the reading separate."
  evidence_level: high

## Recommendations
- recommendation: "Track procurement-linked timing as a targeting observable, distinct from any attribution reading built on it."
  context: analysis
  certainty: strong
  rationale: "The correlation is pack-attested; the intent reading is not."

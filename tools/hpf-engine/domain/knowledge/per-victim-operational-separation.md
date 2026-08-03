# Per-Victim Operational Separation

## Identity
- id: per-victim-operational-separation
- type: pattern
- title: Per-Victim Operational Separation Pattern
- tags: [operational separation, per-victim isolation, distinct C2, lure tailoring, tool overlap, cross-victim exception]
- entities: [per-victim separation, operational compartmentalization, distinct C2, minimal tool overlap]
- concepts: [spearphishing-initial-access, dropper, cluster-1-c2-infrastructure, cluster-2-staging-infrastructure]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The intrusions are professionally separated: distinct command-and-control infrastructure per victim, fresh spearphishing lures per company, and minimal tool overlap between victim networks."
  certainty: high
  evidence: Source material pack §1, §5
  scope: cross-domain
- claim: "Per-victim separation has exactly one observed exception: the module host served Hammer-B modules to both Victim B and Victim D."
  certainty: high
  evidence: Source material pack §5
  scope: cross-domain
- claim: "The separation profile is an observed pattern of the intrusions; the source does not establish that it was deliberate."
  certainty: medium
  evidence: Source material pack §1; reading of the record
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The separation profile characterizes the campaign."
- concept: spearphishing-initial-access
  relationship: linked_to
  description: "Fresh lures per company manifest the separation."
- concept: dropper
  relationship: linked_to
  description: "Unique single-use droppers manifest the separation."
- concept: cluster-1-c2-infrastructure
  relationship: linked_to
  description: "Per-victim callback domains manifest the separation."
- concept: cluster-2-staging-infrastructure
  relationship: linked_to
  description: "The module host is the separation's one exception."

## Failure Modes
- name: intent_inferred
  description: "The observed separation is read as proof of deliberate compartmentalization."
  likelihood: medium
  observable_evidence: "Operator-intent claims built from the separation profile"
  detection: "Fact-vs-reading audit on separation claims"
  recovery: "Record the separation as an observable and deliberation as a reading"
  retryable: true

## Constraints
- constraint: "Separation claims are restricted to the observed profile; operator intent is not asserted."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Track the separation profile as an observable, and the exception as part of the profile."
  rationale: "The profile is pack-attested; its single exception is part of the record."
  evidence_level: high

## Recommendations
- recommendation: "Record the per-victim separation and its single exception as one observable profile."
  context: analysis
  certainty: strong
  rationale: "The profile and the exception are both pack-attested."

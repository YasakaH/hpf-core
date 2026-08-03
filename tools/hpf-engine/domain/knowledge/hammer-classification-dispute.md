# Hammer Family Classification Dispute

## Identity
- id: hammer-classification-dispute
- type: decision
- title: Hammer One-Family-vs-Two Classification Dispute
- tags: [classification, one family vs two, analyst disagreement, malware repository, lineage note, open question]
- entities: [hammer family count, one-family reading, two-family reading, shared lineage note]
- concepts: [hammer-backdoor-family, hammer-a-variant, hammer-b-variant, open-analytical-questions]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The one-family reading holds that Hammer-A and Hammer-B are two builds of one family because the core logic and C2 protocol framing are shared."
  certainty: high
  evidence: Source material pack §4, §9.2
  scope: cross-domain
- claim: "The two-family reading holds that the loader and encryption layer are functionally distinct capabilities, and B's module system has no equivalent in A."
  certainty: high
  evidence: Source material pack §4, §9.2
  scope: cross-domain
- claim: "The evidence is insufficient to choose between the readings; the classification remains open."
  certainty: high
  evidence: Source material pack §4, §9.2
  scope: cross-domain
- claim: "The repository's handling — two artifacts with a shared lineage note — is a provisional decision that preserves both readings."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain

## Decision Factors
- factor: shared_core_and_framing
  question: "Do the builds share enough core logic and protocol framing to count as one family?"
  supporting: "Shared core logic; shared C2 protocol framing; shared download path"
  contradictory: "Functional capability gap in loader and encryption"
  weight: high
- factor: capability_distinctiveness
  question: "Are the loader and encryption layer distinctive enough to constitute a separate family?"
  supporting: "B's module system has no A equivalent; encrypted callbacks are a distinct capability"
  contradictory: "The capabilities extend a shared core rather than replacing it"
  weight: high
- factor: repository_practice
  question: "How does the tracking system hold the artifacts?"
  supporting: "Two artifacts, shared lineage note — a conservative non-resolution"
  contradictory: "The repository entry pre-commits to artifact granularity"
  weight: medium

## Relationships
- concept: hammer-backdoor-family
  relationship: linked_to
  description: "The dispute is about the family object's own identity."
- concept: hammer-a-variant
  relationship: linked_to
  description: "Hammer-A's profile is one side of the dispute."
- concept: hammer-b-variant
  relationship: linked_to
  description: "Hammer-B's profile is the other side of the dispute."
- concept: open-analytical-questions
  relationship: linked_to
  description: "The dispute is open question 2 of the campaign."

## Tradeoffs
- dimension: family_granularity_vs_openness
  options:
    one_family: "Simpler, respects the shared core, but pre-commits the open question"
    two_families: "Respects the capability difference, but pre-commits the opposite"
  importance: high

## Constraints
- constraint: "The dispute object records both readings; it does not resolve them."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Mirror the repository's provisional handling when the classification is contested."
  rationale: "Two artifacts with a lineage note preserve both readings without pre-committing."
  evidence_level: high

## Recommendations
- recommendation: "Keep the family count open in tracking systems and record which reading each downstream claim assumes."
  context: analysis
  certainty: strong
  rationale: "The classification propagates to malware, infrastructure, and attribution claims."

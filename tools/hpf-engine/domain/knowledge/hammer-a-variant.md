# Hammer-A Variant

## Identity
- id: hammer-a-variant
- type: concept
- title: Hammer-A Variant
- tags: [hammer-A, HTTP POST, callbacks, toolchain, victims A and C, service persistence]
- entities: [hammer-A, hammer variant, HTTP callback build]
- concepts: [hammer-backdoor-family, hammer-classification-dispute]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Hammer-A was observed on Victims A and C and compiled with a particular toolchain."
  certainty: high
  evidence: Source material pack §4, Hammer-A
  scope: cross-domain
- claim: "Hammer-A uses HTTP POST callbacks and persists via service registration."
  certainty: high
  evidence: Source material pack §4, Hammer-A
  scope: cross-domain
- claim: "Hammer-A has no module loader; the loader and encryption layer of Hammer-B have no equivalent in A."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain

## Relationships
- concept: hammer-backdoor-family
  relationship: part_of
  description: "Hammer-A is a build of the shared family core."
- concept: victim-set
  relationship: observed_on
  description: "Hammer-A was observed on Victims A and C."
- concept: hammer-classification-dispute
  relationship: linked_to
  description: "Hammer-A's capability profile is one side of the one-family-vs-two question."

## Observations
- observation: "The variant's callback and persistence mechanics are distinguishable from Hammer-B's, which is what keeps the family count contested."
  confidence: high
  source: Source material pack §4

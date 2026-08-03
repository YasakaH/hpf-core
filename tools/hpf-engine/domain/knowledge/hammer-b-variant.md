# Hammer-B Variant

## Identity
- id: hammer-b-variant
- type: concept
- title: Hammer-B Variant
- tags: [hammer-B, HTTPS, encrypted callbacks, module loader, in-memory loading, language artifacts, victims B and D]
- entities: [hammer-B, hammer variant, encrypted callback build, module loader]
- concepts: [hammer-backdoor-family, cluster-2-staging-infrastructure, attribution-assessment]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Hammer-B was observed on Victims B and D: the same core as Hammer-A with encrypted HTTPS callbacks and an added in-memory module loader."
  certainty: high
  evidence: Source material pack §4, Hammer-B
  scope: cross-domain
- claim: "The loader retrieves additional modules in-memory from the campaign's module host."
  certainty: high
  evidence: Source material pack §4, §5
  scope: cross-domain
- claim: "Two malformed code comments in Hammer-B are consistent with a specific East Asian language family — a reading recorded as attribution input, not a demonstrated fact."
  certainty: medium
  evidence: Source material pack §4, §8
  scope: cross-domain

## Relationships
- concept: hammer-backdoor-family
  relationship: part_of
  description: "Hammer-B is a build of the shared family core."
- concept: victim-set
  relationship: observed_on
  description: "Hammer-B was observed on Victims B and D."
- concept: cluster-2-staging-infrastructure
  relationship: loads_from
  description: "Hammer-B loads modules from the Cluster 2 module host."
- concept: attribution-assessment
  relationship: linked_to
  description: "Hammer-B's language artifacts are weighed in the attribution assessment."

## Observations
- observation: "The module loader and encryption layer are the functionally distinct capabilities behind the two-family reading."
  confidence: high
  source: Source material pack §4

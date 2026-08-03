# Hammer Backdoor Family

## Identity
- id: hammer-backdoor-family
- type: concept
- title: Hammer Backdoor Family
- tags: [backdoor, C2, service registration, host information collection, fixed-interval polling, command set, one-family-vs-two dispute]
- entities: [hammer backdoor, backdoor family, c2 poller, service registration, command set]
- concepts: [hammer-a-variant, hammer-b-variant, hammer-classification-dispute, cluster-1-c2-infrastructure, persistence-pattern]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Hammer is a backdoor observed on all four victims: it registers as a service, collects host information, polls a C2 domain at fixed intervals, and supports a small command set."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain
- claim: "Hammer-A and Hammer-B share the core logic and C2 protocol framing that unify the builds."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain
- claim: "Whether Hammer is one family or two is contested: the loader and encryption layer of Hammer-B are functionally distinct, and B's module system has no equivalent in A."
  certainty: high
  evidence: Source material pack §4, §9.2
  scope: cross-domain
- claim: "The malware repository holds the builds as two artifacts with a shared lineage note — a provisional handling, not a resolution."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain

## Relationships
- concept: dropper
  relationship: installed_by
  description: "The Hammer family is installed by the dropper family."
- concept: victim-set
  relationship: observed_on
  description: "The Hammer family was observed on all four victims."
- concept: cluster-1-c2-infrastructure
  relationship: phones_home_to
  description: "Hammer variants phone home to Cluster 1 callback sinks."
- concept: persistence-pattern
  relationship: linked_to
  description: "Hammer persists on servers via service registration."
- concept: hammer-classification-dispute
  relationship: linked_to
  description: "The family's own identity is the subject of the classification dispute."
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The Hammer family is shared campaign tooling."

## Observations
- observation: "The family object carries only the shared core; the variant mechanics that fuel the dispute live in the variant objects."
  confidence: high
  source: Source material pack §4

## Constraints
- constraint: "Family-level claims cover the shared core only; variant-specific capability claims are carried by the variant objects."
  type: invariant
  scope: cross-domain
- constraint: "The family object does not resolve the one-family-vs-two classification."
  type: invariant
  scope: cross-domain

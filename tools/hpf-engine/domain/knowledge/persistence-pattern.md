# Persistence Pattern

## Identity
- id: persistence-pattern
- type: pattern
- title: Persistence Pattern
- tags: [persistence, scheduled tasks, WMI event subscriptions, service registration, workstations, servers]
- entities: [persistence, scheduled tasks, WMI event subscriptions, service registration]
- concepts: [hammer-backdoor-family, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Persistence on non-domain workstations used scheduled tasks and WMI event subscriptions."
  certainty: high
  evidence: Source material pack §6
  scope: cross-domain
- claim: "Persistence on servers used service registration for the Hammer backdoor."
  certainty: high
  evidence: Source material pack §6
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The persistence pattern is part of the campaign's operating picture."
- concept: hammer-backdoor-family
  relationship: linked_to
  description: "Service registration anchors the Hammer backdoor on servers."

## Observations
- observation: "The persistence mechanisms differ by host class — service registration on servers, scheduled tasks and WMI on workstations."
  confidence: high
  source: Source material pack §6

## Constraints
- constraint: "Persistence claims cover the documented mechanisms only; movement and collection are separate objects."
  type: invariant
  scope: cross-domain

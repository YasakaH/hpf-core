# Dropper

## Identity
- id: dropper
- type: concept
- title: First-Stage Dropper Family
- tags: [dropper, loader, first-stage, single-use, shared download logic, per-campaign compile]
- entities: [dropper, first-stage loader, download logic, single-use binaries]
- concepts: [spearphishing-initial-access, hammer-backdoor-family, per-victim-operational-separation]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The droppers are small, single-use first-stage loader binaries: unique per victim, compiled per campaign, and never reused."
  certainty: high
  evidence: Source material pack §4, droppers
  scope: cross-domain
- claim: "The shared download logic across all four victims is the droppers' only identifying artifact; they contain no other identifying artifacts."
  certainty: high
  evidence: Source material pack §3, §4
  scope: cross-domain
- claim: "The droppers stage the Hammer backdoor family after execution."
  certainty: high
  evidence: Source material pack §3, §4
  scope: cross-domain

## Relationships
- concept: spearphishing-initial-access
  relationship: delivered_by
  description: "The dropper is delivered by the spearphishing lures."
- concept: hammer-backdoor-family
  relationship: installed_by
  description: "The dropper stages the Hammer backdoor."
- concept: per-victim-operational-separation
  relationship: linked_to
  description: "Per-victim single-use binaries manifest the separation profile."
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The dropper family is shared across the campaign."

## Observations
- observation: "Because the droppers are unique per victim and per campaign, they carry no lineage signal beyond the shared download logic."
  confidence: high
  source: Source material pack §4

## Constraints
- constraint: "Dropper-specific claims are limited to the loader stage; lure mechanics and the backdoor payload belong to their own objects."
  type: invariant
  scope: cross-domain

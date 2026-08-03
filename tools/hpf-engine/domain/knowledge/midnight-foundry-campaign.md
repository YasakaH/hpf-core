# Midnight Foundry Campaign

## Identity
- id: midnight-foundry-campaign
- type: concept
- title: Midnight Foundry Intrusion Campaign
- tags: [intrusion campaign, working designation, aerospace defense supply chain, spearphishing, RDP lateral movement, staged exfiltration, professional separation]
- entities: [midnight foundry, intrusion campaign, working designation, cluster of intrusions, aerospace contractors]
- concepts: [victim-set, per-victim-operational-separation, attribution-assessment, open-analytical-questions]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Midnight Foundry is the working designation for a cluster of intrusions observed between January and October of the reporting year against four aerospace and defense contractors in three countries."
  certainty: high
  evidence: Source material pack §1, §2
  scope: cross-domain
- claim: "The intrusions combine spearphishing, custom backdoors, lateral movement over RDP, and staged exfiltration, with professionally separated operations across victims."
  certainty: high
  evidence: Source material pack §1, §6, §7
  scope: cross-domain
- claim: "Whether Midnight Foundry is one campaign, several intrusion sets, or two operational phases is an open question the source material does not resolve."
  certainty: medium
  evidence: Source material pack §9.1; analyst disagreement recorded in the pack
  scope: cross-domain
- claim: "No operational impact has been confirmed at any victim; the observed activity was consistent with persistent collection."
  certainty: high
  evidence: Source material pack §2
  scope: cross-domain

## Relationships
- concept: victim-set
  relationship: part_of
  description: "The victim set is part of the campaign's scope — the four compromises define the campaign's observed span."
- concept: per-victim-operational-separation
  relationship: part_of
  description: "The per-victim separation profile is part of the campaign's operating picture."
- concept: attribution-assessment
  relationship: linked_to
  description: "The campaign is the subject of the unresolved attribution assessment."
- concept: open-analytical-questions
  relationship: part_of
  description: "The campaign carries the five open analytical questions that structure analyst disagreement."

## Observations
- observation: "The record groups four professionally separated intrusions under one umbrella designation while preserving the per-victim separation as its defining feature."
  confidence: high
  source: Source material pack §1, §5
- observation: "The campaign's own boundary (one or several) is the first of five open questions, so any representation that fixes the campaign as a single object is a decision, not a reading of the record."
  confidence: medium
  source: Source material pack §9.1

## Constraints
- constraint: "Campaign-level claims are restricted to umbrella-level facts; per-victim and per-tool detail is carried by the objects that own it."
  type: invariant
  scope: cross-domain
- constraint: "The campaign object records the open boundary question; it does not resolve it."
  type: invariant
  scope: cross-domain

# Exfiltration Pattern

## Identity
- id: exfiltration-pattern
- type: pattern
- title: Exfiltration Pattern
- tags: [exfiltration, encrypted archives, FTP staging, single external IP, small batches, interrupted, volume thresholds]
- entities: [exfiltration, encrypted archives, FTP staging, data-volume thresholds]
- concepts: [cluster-2-staging-infrastructure, collection-pattern, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "On Victims A, B, and D, files were compressed into encrypted archives, uploaded to the staging host, and retrieved over FTP sessions originating from a single external IP per victim."
  certainty: high
  evidence: Source material pack §7
  scope: cross-domain
- claim: "Exfiltration occurred in small batches over weeks — behavior consistent with an attempt to stay under data-volume thresholds, a reading the source records rather than proves."
  certainty: medium
  evidence: Source material pack §7
  scope: cross-domain
- claim: "Victim C's exfiltration channel was interrupted before completion, and the Rivet stealer's collected data was not recovered."
  certainty: high
  evidence: Source material pack §7
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The exfiltration pattern is part of the campaign's operating picture."
- concept: cluster-2-staging-infrastructure
  relationship: linked_to
  description: "Exfiltration uses the Cluster 2 staging hosts."
- concept: collection-pattern
  relationship: linked_to
  description: "Exfiltration draws on the collection pattern's output."

## Failure Modes
- name: completeness_assumed
  description: "Staging-host presence is read as exfiltration completion when the channel may have been interrupted."
  likelihood: medium
  observable_evidence: "Completeness claims that ignore the interrupted Victim C channel"
  detection: "Per-victim channel audit"
  recovery: "Record per-victim channel status as observed"
  retryable: true

## Constraints
- constraint: "The pattern records the observed channel behavior; volume-threshold intent is a labeled reading."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Record exfiltration channel status per victim, including interruption."
  rationale: "Completion differs per victim and is pack-attested per victim."
  evidence_level: high

## Recommendations
- recommendation: "Track exfiltration completeness per victim rather than as a campaign-wide status."
  context: analysis
  certainty: strong
  rationale: "Three channels completed; one was interrupted."

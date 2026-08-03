# Collection Pattern

## Identity
- id: collection-pattern
- type: pattern
- title: Collection Pattern
- tags: [collection, engineering workstations, CAD files, sensor-test data, programmatic collection, manual selection]
- entities: [collection, engineering workstations, CAD files, sensor-test data, file selection]
- concepts: [rivet-stealer, exfiltration-pattern, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Collection focused on engineering workstations, CAD files, and sensor-test data, with the Rivet stealer the only custom collection tool, on Victim C."
  certainty: high
  evidence: Source material pack §6, §7, Appendix B
  scope: cross-domain
- claim: "The collection focus is consistent with programmatic rather than opportunistic collection — a reading the source records, not a demonstrated fact."
  certainty: medium
  evidence: Source material pack §6
  scope: cross-domain
- claim: "Collection activity was consistent with persistent collection; no confirmed operational impact resulted."
  certainty: high
  evidence: Source material pack §2, §6
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The collection pattern is part of the campaign's operating picture."
- concept: rivet-stealer
  relationship: linked_to
  description: "Rivet feeds the collection pattern on Victim C."
- concept: exfiltration-pattern
  relationship: linked_to
  description: "The collection pattern feeds the exfiltration channel."

## Failure Modes
- name: opportunistic_misreading
  description: "The recorded collection focus is read as proof of programmatic intent rather than as an observed focus."
  likelihood: medium
  observable_evidence: "Intent claims built from the collection focus without the source's caveat"
  detection: "Fact-vs-reading audit on collection claims"
  recovery: "Record the focus as an observable and programmatic intent as a reading"
  retryable: true

## Constraints
- constraint: "The pattern records the observed collection focus; intent readings are labeled as interpretations."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Keep the collection focus observable separate from the programmatic-intent reading."
  rationale: "The source states the focus; the intent reading is its own claim."
  evidence_level: high

## Recommendations
- recommendation: "Record collection targets (workstation class, file classes) as observables independent of any intent assessment."
  context: analysis
  certainty: strong
  rationale: "The targets are pack-attested; the intent is not."

# Rivet Stealer

## Identity
- id: rivet-stealer
- type: concept
- title: Rivet Credential and Data Stealer
- tags: [stealer, credentials, clipboard, document harvesting, victim C, code-signing comment, K7 lineage]
- entities: [rivet stealer, credential stealer, code-signing comment string, K7 tooling]
- concepts: [k7-overlap, collection-pattern, victim-set]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Rivet is a credential and data stealer observed on Victim C only, harvesting browser credentials, clipboard contents, and documents matching file-name patterns."
  certainty: high
  evidence: Source material pack §4, Rivet
  scope: cross-domain
- claim: "Rivet's code contains a code-signing comment string byte-identical to a string in tooling used two years earlier by the unrelated financially motivated cluster K7."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain
- claim: "Whether the string indicates shared tool lineage, shared authors, or stolen or borrowed code is unknown."
  certainty: medium
  evidence: Source material pack §4; unresolved interpretation
  scope: cross-domain
- claim: "Rivet's collected data was not recovered because Victim C's exfiltration channel was interrupted."
  certainty: high
  evidence: Source material pack §7
  scope: cross-domain

## Relationships
- concept: victim-set
  relationship: observed_on
  description: "Rivet was observed on Victim C only."
- concept: k7-overlap
  relationship: linked_to
  description: "Rivet carries the byte-identical code-signing comment linking it to K7 tooling."
- concept: collection-pattern
  relationship: part_of
  description: "Rivet is the campaign's only custom collection tool."

## Observations
- observation: "The stealer's lineage link is the record of a string match; the interpretation of that match is explicitly open."
  confidence: high
  source: Source material pack §4

## Constraints
- constraint: "The Rivet object records the string match; the lineage interpretation is carried as an open question, not a fact."
  type: invariant
  scope: cross-domain

# Victim Set

## Identity
- id: victim-set
- type: concept
- title: Aerospace Defense Supply-Chain Victim Set
- tags: [victims, victimology, aerospace, defense suppliers, secondary suppliers, procurement-linked timing, compromise timeframe]
- entities: [victim set, victims A-D, aerospace contractors, secondary suppliers, procurement programs]
- concepts: [midnight-foundry-campaign, procurement-aware-targeting]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The four victims are mid-sized aerospace or defense suppliers in three regions: aircraft subassemblies (North America), avionics (Europe), propulsion components (North America), and sensor systems (East Asia)."
  certainty: high
  evidence: Source material pack §2, table
  scope: cross-domain
- claim: "All four are secondary suppliers in larger defense supply chains, and each was compromised within two weeks of becoming part of a funded procurement program."
  certainty: high
  evidence: Source material pack §2
  scope: cross-domain
- claim: "Compromise timeframes ran January through October, with each victim's first access two weeks before its first observed C2 contact."
  certainty: high
  evidence: Source material pack §2, Appendix C
  scope: cross-domain
- claim: "No confirmed operational impact; the observed activity at each victim was consistent with persistent collection."
  certainty: high
  evidence: Source material pack §2
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The victim set defines the campaign's observed span."
- concept: procurement-aware-targeting
  relationship: linked_to
  description: "Compromise timing correlates with funded-procurement entry for all four victims."

## Observations
- observation: "Grouping the four victims as one set preserves the source's shared victimology claims; per-victim specifics remain available in the timeline tables."
  confidence: high
  source: Source material pack §2, Appendix C
- observation: "Whether the set should be one group or four individual victims is a defensible boundary difference; the source consistently writes them as a group."
  confidence: medium
  source: Source material pack §2

## Constraints
- constraint: "Shared victimology claims are asserted at the set level only; nothing in this object attributes means of access or tooling to specific victims."
  type: invariant
  scope: cross-domain

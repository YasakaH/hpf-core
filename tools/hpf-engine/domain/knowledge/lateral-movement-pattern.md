# Lateral Movement Pattern

## Identity
- id: lateral-movement-pattern
- type: pattern
- title: Lateral Movement Pattern
- tags: [lateral movement, RDP, Mimikatz, password spray, living-off-the-land, enumeration, no domain-wide compromise]
- entities: [lateral movement, RDP, Mimikatz, password spraying, LoLBins]
- concepts: [midnight-foundry-campaign, rivet-stealer, victim-set]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "RDP was the primary lateral movement mechanism, with credentials obtained via Mimikatz usage observed once (Victim A) and password-spraying against local admin accounts (Victim C)."
  certainty: high
  evidence: Source material pack §6
  scope: cross-domain
- claim: "Living-off-the-land binaries (PowerShell, WMIC, sc.exe) were used for enumeration; no custom tooling was observed in lateral movement except the Rivet stealer on Victim C."
  certainty: high
  evidence: Source material pack §6
  scope: cross-domain
- claim: "No domain-wide compromise was observed at any victim; the operators appeared to work within specific engineering workstations and file shares."
  certainty: high
  evidence: Source material pack §6
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The lateral movement pattern is part of the campaign's operating picture."
- concept: rivet-stealer
  relationship: linked_to
  description: "Rivet was the only custom tool enlisted in lateral movement."

## Failure Modes
- name: domain_wide_assumed
  description: "Lateral movement is treated as evidence of domain-wide intent despite the recorded absence of domain-wide compromise."
  likelihood: medium
  observable_evidence: "Confident domain-dominance claims on per-workstation observations"
  detection: "Scope audit of movement claims"
  recovery: "Record movement scope per victim as observed"
  retryable: true

## Constraints
- constraint: "Movement claims are scoped to the observed per-victim behavior; no claim asserts domain-wide activity."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Record lateral movement scope per victim rather than as a campaign-wide behavior."
  rationale: "The source documents workstation-and-share scope at each victim."
  evidence_level: high

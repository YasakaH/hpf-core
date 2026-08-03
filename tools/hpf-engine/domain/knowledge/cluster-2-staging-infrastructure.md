# Cluster 2 Staging Infrastructure

## Identity
- id: cluster-2-staging-infrastructure
- type: concept
- title: Cluster 2 Staging Infrastructure
- tags: [staging, module hosting, exfil staging, VPS, cross-victim overlap, K7 IP range, encrypted archives]
- entities: [cluster 2, staging infrastructure, module host, exfil staging host]
- concepts: [hammer-b-variant, k7-overlap, exfiltration-pattern, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Cluster 2 is the staging cluster: two file-staging hosts and three VPS endpoints used for exfil staging and module hosting, plus appendix module and archival hosts."
  certainty: high
  evidence: Source material pack §5, Appendix A
  scope: cross-domain
- claim: "The module host is the only cross-victim infrastructure overlap observed: it served Hammer-B modules to both Victim B and Victim D."
  certainty: high
  evidence: Source material pack §5
  scope: cross-domain
- claim: "One Cluster 2 VPS sits in an IP range previously used by K7 infrastructure — the single strongest piece of evidence in the competing-hypothesis debate."
  certainty: high
  evidence: Source material pack §5
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "Cluster 2 is the campaign's staging infrastructure."
- concept: hammer-b-variant
  relationship: linked_to
  description: "The module host serves Hammer-B modules."
- concept: exfiltration-pattern
  relationship: linked_to
  description: "Cluster 2 hosts the staging for the exfiltration pattern."
- concept: k7-overlap
  relationship: linked_to
  description: "The K7-used IP range hosting a Cluster 2 VPS is one observed link."

## Observations
- observation: "The single cross-victim infrastructure overlap sits here, not in the C2 cluster — the separation profile is violated exactly once, on the module host."
  confidence: high
  source: Source material pack §5

## Constraints
- constraint: "Cluster 2 claims cover the staging hosts only; the C2 cluster is a separate object."
  type: invariant
  scope: cross-domain

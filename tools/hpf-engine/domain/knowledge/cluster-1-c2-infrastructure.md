# Cluster 1 C2 Infrastructure

## Identity
- id: cluster-1-c2-infrastructure
- type: concept
- title: Cluster 1 C2 Infrastructure
- tags: [C2, domains, VPS, callbacks, privacy registration, redirectors, DNS glue, lure infrastructure, per-victim separation]
- entities: [cluster 1, C2 infrastructure, callback sinks, redirectors, DNS glue, lure infrastructure]
- concepts: [hammer-backdoor-family, per-victim-operational-separation, unassigned-hosts, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Cluster 1 is the primary C2 cluster: five domains registered through a privacy service with hosting in two providers, and four VPS endpoints, plus relays, DNS glue, lure infrastructure, and one suspected host from the appendix."
  certainty: high
  evidence: Source material pack §5, Appendix A
  scope: cross-domain
- claim: "Hammer variants phone home to Cluster 1 sinks; each victim observed a different callback domain."
  certainty: high
  evidence: Source material pack §5, §6
  scope: cross-domain
- claim: "One appendix host (telemetry-12) is a suspected C2 with no confirmed callback."
  certainty: high
  evidence: Source material pack §5, Appendix A
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "Cluster 1 is the campaign's primary C2 infrastructure."
- concept: hammer-backdoor-family
  relationship: linked_to
  description: "Hammer variants phone home to Cluster 1 sinks."
- concept: unassigned-hosts
  relationship: linked_to
  description: "The unassigned hosts share SSL certificate reuse with Cluster 1."
- concept: per-victim-operational-separation
  relationship: linked_to
  description: "Per-victim callback domains manifest the separation profile."

## Observations
- observation: "The cluster boundary includes functionally mixed hosts (relays, DNS, lure infrastructure) grouped by the source's cluster assignment rather than by a single role."
  confidence: medium
  source: Source material pack §5, Appendix A

## Constraints
- constraint: "Cluster 1 claims cover the assigned hosts only; staging and unassigned hosts are separate objects."
  type: invariant
  scope: cross-domain

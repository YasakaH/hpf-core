# Unassigned Hosts

## Identity
- id: unassigned-hosts
- type: concept
- title: Unassigned Hosts
- tags: [unassigned, SSL certificate reuse, unknown role, disputed membership, open question]
- entities: [unassigned hosts, skunk-09, skunk-10, SSL certificate reuse]
- concepts: [cluster-1-c2-infrastructure, open-analytical-questions, midnight-foundry-campaign]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "Two hosts (skunk-09 and skunk-10) share SSL certificate reuse with Cluster 1 but have an unknown active role."
  certainty: high
  evidence: Source material pack §5, Appendix A
  scope: cross-domain
- claim: "Analysts disagree on whether the unassigned hosts belong to the campaign at all."
  certainty: high
  evidence: Source material pack §5, §9.3
  scope: cross-domain

## Relationships
- concept: cluster-1-c2-infrastructure
  relationship: linked_to
  description: "The hosts share SSL certificate reuse with Cluster 1."
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The hosts' membership in the campaign is disputed."
- concept: open-analytical-questions
  relationship: linked_to
  description: "Host membership is open question 3."

## Observations
- observation: "SSL reuse is the only observed connection; it does not resolve the hosts' role or membership."
  confidence: high
  source: Source material pack §5

## Constraints
- constraint: "The object records the observed reuse and the disputed membership; it does not assign the hosts."
  type: invariant
  scope: cross-domain

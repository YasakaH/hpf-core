# K7 Overlap

## Identity
- id: k7-overlap
- type: concept
- title: K7 Overlap Links
- tags: [K7, financially motivated, code lineage, IP-range overlap, competing hypothesis, unrelated cluster]
- entities: [K7 cluster, financially motivated group, code-signing string, IP range overlap]
- concepts: [rivet-stealer, cluster-2-staging-infrastructure, attribution-assessment, open-analytical-questions]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "K7 is an unrelated financially motivated cluster that has never been linked to state-sponsored activity."
  certainty: high
  evidence: Source material pack §4, §5
  scope: cross-domain
- claim: "Two links between Midnight Foundry and K7 are observed: the byte-identical code-signing string in Rivet, and one Cluster 2 VPS endpoint in an IP range previously used by K7 infrastructure."
  certainty: high
  evidence: Source material pack §4, §5
  scope: cross-domain
- claim: "No other link between Midnight Foundry and K7 has been found."
  certainty: high
  evidence: Source material pack §4
  scope: cross-domain
- claim: "The infrastructure overlap is the strongest piece of evidence in the competing-hypothesis debate."
  certainty: high
  evidence: Source material pack §5
  scope: cross-domain

## Relationships
- concept: rivet-stealer
  relationship: linked_to
  description: "The byte-identical string in Rivet is one observed link."
- concept: cluster-2-staging-infrastructure
  relationship: linked_to
  description: "The K7-used IP range hosting a Cluster 2 VPS is the other observed link."
- concept: attribution-assessment
  relationship: linked_to
  description: "The overlap is weighed as the strongest competing-hypothesis evidence."
- concept: open-analytical-questions
  relationship: linked_to
  description: "The significance of the overlap is open question 4."

## Observations
- observation: "The overlap object records the observed links only; whether they mean shared lineage, shared authors, or coincidence is left to the attribution assessment."
  confidence: high
  source: Source material pack §4, §8

## Constraints
- constraint: "Overlap claims are restricted to the two observed links; no claim here asserts a relationship between the actors themselves."
  type: invariant
  scope: cross-domain

# Open Analytical Questions

## Identity
- id: open-analytical-questions
- type: decision
- title: Open Analytical Questions for Midnight Foundry
- tags: [open questions, one-vs-many, family count, host membership, K7 overlap, lure sourcing, analyst disagreement]
- entities: [open questions, unresolved questions, analyst disagreement, tracking implications]
- concepts: [midnight-foundry-campaign, hammer-classification-dispute, unassigned-hosts, k7-overlap, spearphishing-initial-access]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "The source lists five open analytical questions: one campaign or several intrusion sets; Hammer one family or two; unassigned-host membership; K7 overlap significance; and lure-content sourcing as possible evidence of a separate access."
  certainty: high
  evidence: Source material pack §9
  scope: cross-domain
- claim: "None of the five questions is resolved by the source material; each carries attached analyst disagreement."
  certainty: high
  evidence: Source material pack §9
  scope: cross-domain
- claim: "The open questions matter for how the activity is organized in knowledge bases and tracking systems."
  certainty: high
  evidence: Source material pack §1, §9
  scope: cross-domain

## Relationships
- concept: midnight-foundry-campaign
  relationship: part_of
  description: "The open questions belong to the campaign's record."
- concept: hammer-classification-dispute
  relationship: linked_to
  description: "Question 2 is the Hammer family-count dispute."
- concept: unassigned-hosts
  relationship: linked_to
  description: "Question 3 concerns the unassigned hosts' membership."
- concept: k7-overlap
  relationship: linked_to
  description: "Question 4 concerns the K7 overlap's significance."
- concept: spearphishing-initial-access
  relationship: linked_to
  description: "Question 5 concerns the lure-content sourcing."
- concept: attribution-assessment
  relationship: linked_to
  description: "The open questions constrain the attribution assessment."

## Constraints
- constraint: "The object records the questions as open; it resolves none of them."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Track the five open questions explicitly so representation decisions do not silently pre-commit their answers."
  rationale: "Each question maps to a boundary or classification the source leaves open."
  evidence_level: high

## Recommendations
- recommendation: "Represent each open question at the object whose boundary it contests, and consolidate them as a campaign-level open-question list."
  context: analysis
  certainty: moderate
  rationale: "Both forms appear in the three independent decompositions; the consolidated form preserves the source's explicit list."

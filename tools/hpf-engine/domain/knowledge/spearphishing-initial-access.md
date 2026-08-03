# Spearphishing Initial Access

## Identity
- id: spearphishing-initial-access
- type: pattern
- title: Spearphishing Initial Access Pattern
- tags: [spearphishing, initial access, PDF exploit, macro document, tailored lures, lookalike domain, dropper download]
- entities: [spearphishing, initial access, request-for-quote lure, security questionnaire lure, lookalike sender domains]
- concepts: [dropper, procurement-aware-targeting, per-victim-operational-separation, victim-set]
- domain: threat-analysis
- version: 1.0
- research_cycle: "015"

## Claims
- claim: "All four intrusions began with spearphishing, in two lure styles: a PDF request-for-quote exploiting a now-patched reader vulnerability (Victims A and B) and a macro-enabled Word security questionnaire (Victims C and D)."
  certainty: high
  evidence: Source material pack §3
  scope: cross-domain
- claim: "Lures were individually tailored per company — different templates, different prime-contractor personas, different sender infrastructure — with the sender domain spoofed via lookalike registrations."
  certainty: high
  evidence: Source material pack §3
  scope: cross-domain
- claim: "The lures share one underlying behavior: they download the same first-stage dropper family across all four victims."
  certainty: high
  evidence: Source material pack §3
  scope: cross-domain
- claim: "Lure content references real procurement documents whose sourcing is unexplained."
  certainty: high
  evidence: Source material pack §3, §9.5
  scope: cross-domain

## Relationships
- concept: victim-set
  relationship: linked_to
  description: "The pattern was delivered to the victim set."
- concept: dropper
  relationship: linked_to
  description: "The pattern stages the shared dropper family."
- concept: procurement-aware-targeting
  relationship: linked_to
  description: "Lure content draws on procurement-aware material."
- concept: per-victim-operational-separation
  relationship: linked_to
  description: "Tailored lures per company exemplify the per-victim separation profile."

## Failure Modes
- name: template_reuse_assumed
  description: "Per-company tailoring is treated as evidence of a single orchestrator without the source's recorded uncertainty."
  likelihood: medium
  observable_evidence: "Confident single-operator claims built on lure variety"
  detection: "Fact-vs-reading audit on tailoring claims"
  recovery: "Record tailoring as an observable and the orchestration reading as an interpretation"
  retryable: true

## Constraints
- constraint: "The pattern describes access mechanics; loader internals belong to the dropper object."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Separate the tailoring observable from the single-operator reading it invites."
  rationale: "The source documents the tailoring, not its cause."
  evidence_level: high

## Recommendations
- recommendation: "Track the two lure styles and their per-company variants as distinct observables."
  context: analysis
  certainty: strong
  rationale: "The styles and tailoring are pack-attested."
- recommendation: "Attribute the unexplained lure sourcing to a separate potential access only as a hypothesis."
  context: analysis
  certainty: moderate
  rationale: "The source records the possibility as open, not demonstrated."

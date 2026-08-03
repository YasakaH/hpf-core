# Real-Time Guarantee

## Identity
- id: real-time-guarantee
- type: concept
- title: Real-Time Guarantee
- tags: [real-time systems, guarantees, deadlines, validity conditions, temporal correctness]
- entities: [real-time guarantee, timing guarantee, deadline guarantee, temporal correctness, verification]
- concepts: [deadline, schedulability-analysis, worst-case-execution-time, type-safety, data-integrity]

## Claims
- claim: "A real-time guarantee is a scoped claim — a statement that timing requirements will be met under stated conditions."
  certainty: high
  evidence: Cross-domain comparison (guarantee objects 009-010)
  scope: cross-domain
- claim: "The guarantee's validity is bound by its conditions — deadline, load, and model assumptions qualify the claim."
  certainty: high
  evidence: Schedulability analysis practice
  scope: cross-domain
- claim: "A real-time guarantee is the fourth guarantee object — joining type-safety (009), data-integrity (010), and atomicity (010) — the guarantee-object motif at n=4."
  certainty: high
  evidence: Cross-domain comparison (guarantee objects 009-010)
  scope: cross-domain
- claim: "The guarantee is established by analysis and verified by runtime — it is a claim with evidence, not an observation."
  certainty: high
  evidence: Cross-domain comparison (verification objects 009)
  scope: cross-domain
- claim: "Temporal correctness is not a separate kind of correctness — it is logical correctness plus a validity condition on completion."
  certainty: high
  evidence: Tier 1 deadline resolution (completion <= T)
  scope: cross-domain

## Relationships
- concept: deadline
  relationship: bounded_by
  description: "A real-time guarantee is bounded by deadlines — the timing requirement is the constraint."
- concept: schedulability-analysis
  relationship: established_by
  description: "A real-time guarantee is established by schedulability analysis — the evidence for the claim."
- concept: worst-case-execution-time
  relationship: rests_on
  description: "A real-time guarantee rests on WCET — the estimate bounds the analysis."
- concept: type-safety
  relationship: analogous_to
  description: "A real-time guarantee is analogous to type safety — a scoped guarantee object — the Cycle 009 cross-domain link."
- concept: data-integrity
  relationship: analogous_to
  description: "A real-time guarantee is analogous to data integrity — a scoped guarantee object — the Cycle 010 cross-domain link."

## Tradeoffs
- dimension: guarantee_strength_vs_capacity
  options:
    strong_guarantee:
      value: certainty
      rationale: "Strong guarantees need headroom but waste capacity."
    tight_guarantee:
      value: efficiency
      rationale: "Tight guarantees are efficient but leave no margin."
  importance: high
- dimension: scope_breadth_vs_depth
  options:
    broad_guarantee:
      value: coverage
      rationale: "Broad guarantees cover more but are weaker per claim."
    narrow_guarantee:
      value: strength
      rationale: "Narrow guarantees are strong but cover less."
  importance: high

## Failure Modes
- name: guarantee_invalidated
  description: "The guarantee's conditions stop holding — the claim is void even though no single step failed."
  likelihood: medium
  observable_evidence: "Misses despite guarantee; condition violations; drift"
  detection: "Condition audits; guarantee re-verification"
  recovery: "Re-establish under current conditions; repair the drift"
  retryable: true
- name: guarantee_erosion
  description: "The guarantee silently weakens as assumptions decay — the claim outlives its conditions."
  likelihood: medium
  observable_evidence: "Growing miss probability; analysis/runtime divergence"
  detection: "Guarantee audits; assumption review"
  recovery: "Re-analyse; re-scope; repair the erosion"
  retryable: true
- name: false_confidence
  description: "A guarantee is believed stronger than its conditions allow — the scope is misread as broader."
  likelihood: medium
  observable_evidence: "Surprise failures outside the guarantee's actual scope"
  detection: "Scope review; expectation audit"
  recovery: "Restate the scope; align expectations"
  retryable: true

## Observations
- observation: "The guarantee-object motif now spans four objects — scoped claim + invariants + failure modes + verification evidence — the strongest motif in the catalogue."
  confidence: high
  source: Cross-domain comparison (guarantee objects 009-010)
- observation: "The guarantee is a claim under conditions — the strongest real-time guarantee is still bound by stated conditions."
  confidence: high
  source: Schedulability analysis practice
- observation: "Temporal correctness is validity on completion — the unification hypothesis extends to guarantees."
  confidence: high
  source: Tier 1 deadline resolution

## Constraints
- constraint: "A real-time guarantee is valid only under its stated conditions — deadline, load, and model assumptions bound the claim."
  type: invariant
  scope: cross-domain
- constraint: "A guarantee outside its scope is a false promise — scope precision is part of the claim."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "State the guarantee's conditions with the guarantee."
  rationale: "Unstated conditions are unverified claims."
  evidence_level: high
- heuristic: "Re-verify guarantees when the system changes."
  rationale: "Erosion is silent invalidation."
  evidence_level: high

## Recommendations
- recommendation: "Model real-time guarantees as scoped claims with conditions."
  context: modelling
  certainty: strong
  rationale: "The guarantee object is a claim under conditions, not a promise."
- recommendation: "Verify the guarantee's conditions continuously."
  context: operations
  certainty: strong
  rationale: "Conditions drift; guarantees expire with them."
- recommendation: "Keep the guarantee-object pattern as the fourth instantiation."
  context: modelling
  certainty: strong
  rationale: "n=4 strengthens the motif; optional composition preserves it."

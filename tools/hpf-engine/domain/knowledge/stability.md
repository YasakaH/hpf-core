# Stability

## Identity
- id: stability
- type: concept
- title: Stability
- tags: [stability, closed-loop correctness, lyapunov, boundedness, verification]
- entities: [stability, stability condition, Lyapunov function, boundedness, envelope]
- concepts: [feedback-control, closed-loop-guarantee, physical-state, formal-verification, schedulability-analysis]

## Claims
- claim: "Stability is the closed-loop correctness property — bounded response to bounded disturbance over time."
  certainty: high
  evidence: Control theory
  scope: cross-domain
- claim: "Stability is demonstrated, not claimed — analysis (Lyapunov conditions), simulation, and test provide the evidence."
  certainty: high
  evidence: Verification practice (P4 — stability as verification pattern)
  scope: cross-domain
- claim: "A stability condition is a constraint — boundedness and convergence are invariants governing state evolution."
  certainty: high
  evidence: Cross-domain comparison (constraints as invariants)
  scope: cross-domain
- claim: "Stability claims are valid under stated conditions — the plant model and operating envelope bound the claim, exactly as all verification claims."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "Stability joins the verification family — claim + evidence + constraints, where verification does not become ontology."
  certainty: high
  evidence: Verification family watch (Cycle 012 — fifth member at this tier)
  scope: cross-domain

## Relationships
- concept: feedback-control
  relationship: constrains
  description: "Stability constrains feedback control — the gain and response live within the stability boundary."
- concept: closed-loop-guarantee
  relationship: supports
  description: "Stability supports closed-loop-guarantee — the guarantee rests on stability evidence."
- concept: formal-verification
  relationship: analogous_to
  description: "Stability is analogous to formal verification — demonstrated correctness under stated conditions — the Cycle 009 cross-domain link."
- concept: schedulability-analysis
  relationship: analogous_to
  description: "Stability is analogous to schedulability analysis — a feasibility claim evidenced by analysis — the Cycle 011 cross-domain link."
- concept: physical-state
  relationship: governs
  description: "Stability governs physical state — boundedness constrains how state may evolve."

## Tradeoffs
- dimension: responsiveness_vs_stability_margin
  options:
    fast_loop:
      value: responsiveness
      rationale: "Fast loops respond quickly."
    wide_margin:
      value: robustness
      rationale: "Wide margins survive model error and disturbance."
  importance: high
- dimension: envelope_vs_performance
  options:
    wide_envelope:
      value: safety
      rationale: "Wide envelopes cover more operating conditions."
    tight_envelope:
      value: performance
      rationale: "Tight envelopes allow aggressive performance."
  importance: high

## Failure Modes
- name: instability
  description: "The loop diverges — bounded disturbance produces unbounded response."
  likelihood: low
  observable_evidence: "Divergent oscillation; envelope exit; runaway behaviour"
  detection: "Stability monitoring; oscillation detection; envelope checks"
  recovery: "Re-tune; enter safe posture; re-verify the analysis"
  retryable: true
- name: marginal_stability
  description: "The loop sits at the stability boundary — a small model error or disturbance pushes it over."
  likelihood: medium
  observable_evidence: "Sustained oscillation; sensitivity to small changes; borderline margins"
  detection: "Margin measurement; sensitivity analysis; boundary checks"
  recovery: "Widen the margin; reduce gain; re-verify"
  retryable: true
- name: envelope_exit
  description: "The system leaves its verified operating envelope — the stability claim's stated conditions no longer hold."
  likelihood: medium
  observable_evidence: "Operation outside verified conditions; unmodelled behaviour; degraded margins"
  detection: "Envelope monitoring; condition checks; margin tracking"
  recovery: "Return to envelope; re-verify; restrict operations"
  retryable: true

## Observations
- observation: "Stability resolved as verification pattern — demonstrated, not claimed; the verification family (equivalence-checking 009, formal-verification 009, benchmark-validity 008, schedulability-analysis 011) gains its fifth member at this tier."
  confidence: high
  source: P4 test (Cycle 012)
- observation: "The Lyapunov condition is a constraint on state evolution — stability is invariants over dynamics, not a new property type."
  confidence: high
  source: Control theory
- observation: "Epistemic Distance at stability claims is 2–3 — the property is demonstrated over a model, at the same distance as the belief it constrains."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "Stability is the boundary between verification and guarantee families — demonstrated by the first, scoped by the second."
  confidence: high
  source: Cross-domain comparison (009-011)

## Constraints
- constraint: "Stability is a claim under stated conditions — the plant model and operating envelope bound it."
  type: invariant
  scope: cross-domain
- constraint: "A stability demonstration is an artifact of evidence — it verifies, it does not construct."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Demonstrate stability before claiming it."
  rationale: "Stability is not asserted — it is evidenced by analysis, simulation, and test."
  evidence_level: high
- heuristic: "Measure the margin, not the fact of stability."
  rationale: "Marginal stability fails at the first disturbance; the margin is the honest quantity."
  evidence_level: high

## Recommendations
- recommendation: "Represent stability as claim + constraints + evidence — never as a stability construct."
  context: modelling
  certainty: strong
  rationale: "Stability is the verification pattern: demonstrated correctness under stated conditions."
- recommendation: "Bound every stability claim with its operating envelope."
  context: engineering
  certainty: strong
  rationale: "The envelope is the stated condition — outside it, the claim does not hold."
- recommendation: "Re-verify stability when the plant model changes."
  context: operations
  certainty: strong
  rationale: "Model change invalidates the demonstration — the evidence artifact must be regenerated."

# Closed-Loop Guarantee

## Identity
- id: closed-loop-guarantee
- type: concept
- title: Closed-Loop Guarantee
- tags: [closed-loop guarantee, guarantee, safety, scoped claim, control]
- entities: [guarantee, closed loop, operating envelope, verification evidence]
- concepts: [feedback-control, stability, cyber-physical-system, type-safety, data-integrity, real-time-guarantee]

## Claims
- claim: "A closed-loop guarantee is the scoped claim that the loop holds its specified behaviour under stated conditions — the fifth guarantee object."
  certainty: high
  evidence: Guarantee-object motif (009-012)
  scope: cross-domain
- claim: "The guarantee structure is unchanged: scoped claim + invariants + failure modes + verification evidence — joining type-safety (009), data-integrity (010), atomicity (010), and real-time-guarantee (011)."
  certainty: high
  evidence: Cross-domain comparison (guarantee-object motif at n=5)
  scope: cross-domain
- claim: "The guarantee is valid only under its conditions — plant model, envelope, measurement quality, and timing bound the claim."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "The guarantee is verified, not assumed — stability analysis, simulation, and test are the evidence."
  certainty: high
  evidence: Verification family (P3/P4)
  scope: cross-domain
- claim: "The guarantee-object motif reaches n=5 across five engineering categories — composition, not coincidence."
  certainty: high
  evidence: Guarantee-object motif (type-safety 009, data-integrity 010, atomicity 010, real-time-guarantee 011, closed-loop-guarantee 012)
  scope: cross-domain

## Relationships
- concept: feedback-control
  relationship: guaranteed_by
  description: "Feedback control is guaranteed by closed-loop-guarantee — the scoped claim holds the loop to its behaviour."
- concept: stability
  relationship: depends_on
  description: "Closed-loop-guarantee depends on stability — the guarantee rests on demonstrated stability."
- concept: type-safety
  relationship: analogous_to
  description: "Closed-loop-guarantee is analogous to type safety — the scoped guarantee structure — the Cycle 009 cross-domain link."
- concept: data-integrity
  relationship: analogous_to
  description: "Closed-loop-guarantee is analogous to data integrity — invariants + failure modes — the Cycle 010 cross-domain link."
- concept: real-time-guarantee
  relationship: analogous_to
  description: "Closed-loop-guarantee is analogous to real-time guarantee — the temporal scoping — the Cycle 011 cross-domain link."

## Tradeoffs
- dimension: guarantee_strength_vs_envelope
  options:
    strong_guarantee:
      value: assurance
      rationale: "Strong guarantees bind tightly."
    wide_envelope:
      value: coverage
      rationale: "Wide envelopes cover more conditions."
  importance: high
- dimension: verification_depth_vs_cost
  options:
    deep_verification:
      value: evidence_quality
      rationale: "Deep verification demonstrates more."
    light_verification:
      value: speed
      rationale: "Light verification reaches the field faster."
  importance: medium

## Failure Modes
- name: guarantee_overreach
  description: "The guarantee claims more than its conditions support — the scoped claim exceeds the evidence."
  likelihood: medium
  observable_evidence: "Claims beyond the envelope; verification gaps; unstated conditions"
  detection: "Guarantee audits; condition review; evidence-vs-claim comparison"
  recovery: "Narrow the claim; widen verification; restate conditions"
  retryable: true
- name: envelope_exit
  description: "Operation leaves the stated conditions — the guarantee silently ceases to hold."
  likelihood: medium
  observable_evidence: "Operation outside verified conditions; unmodelled behaviour; degraded margins"
  detection: "Envelope monitoring; condition checks; guarantee audits"
  recovery: "Return to envelope; re-verify; declare the guarantee out of scope"
  retryable: true
- name: verification_gap
  description: "The guarantee is asserted where the evidence is missing — analysis, simulation, and test do not cover the claim."
  likelihood: medium
  observable_evidence: "Claims without demonstration; untested corners; analysis/runtime divergence"
  detection: "Evidence coverage review; verification audits; gap analysis"
  recovery: "Close the gap; narrow the claim; add verification"
  retryable: true

## Observations
- observation: "The closed-loop guarantee is the fifth guarantee object — the motif now spans five engineering categories (009-012)."
  confidence: high
  source: Guarantee-object motif (n=5)
- observation: "The guarantee depends on the verification family — stability is demonstrated evidence; the guarantee is the scoped claim over it."
  confidence: high
  source: P3/P4 test (Cycle 012)
- observation: "Epistemic Distance at the guarantee is 2–3 — the claim sits over the model chain, bound by the same conditions as the belief."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "Guarantee overreach is the characteristic failure — the scoped claim grows faster than the evidence."
  confidence: high
  source: Cross-domain comparison (guarantee objects 009-011)

## Constraints
- constraint: "The closed-loop guarantee is valid only under its stated conditions — envelope and model bound it."
  type: invariant
  scope: cross-domain
- constraint: "A guarantee without verification evidence is a claim, not a guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Scope the guarantee to the verified envelope."
  rationale: "The guarantee is a claim; the envelope is its stated condition."
  evidence_level: high
- heuristic: "Audit the claim against the evidence."
  rationale: "Guarantee overreach grows when claims and evidence diverge."
  evidence_level: high

## Recommendations
- recommendation: "Represent the closed-loop guarantee as scoped claim + invariants + failure modes + verification evidence."
  context: modelling
  certainty: strong
  rationale: "The guarantee-object structure holds at n=5 — composition, not a new type."
- recommendation: "State the envelope with the guarantee."
  context: engineering
  certainty: strong
  rationale: "An unstated condition is an unbounded claim."
- recommendation: "Re-verify the guarantee when the plant model or envelope changes."
  context: operations
  certainty: strong
  rationale: "The evidence artifact must regenerate with its conditions."

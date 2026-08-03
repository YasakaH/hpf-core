# Safety Case

## Identity
- id: safety-case
- type: pattern
- title: Safety Case
- tags: [safety case, certification, argument, assurance, safety]
- entities: [safety case, argument, evidence, certification standard, assurance claim]
- concepts: [cyber-physical-system, closed-loop-guarantee, formal-verification, stability, autonomy-decision]

## Claims
- claim: "A safety case is an artifact of evidence — claim + evidence + argument structure, exactly as a proof is an artifact of evidence."
  certainty: high
  evidence: Certification practice (ISO 26262, IEC 61508, DO-178C)
  scope: cross-domain
- claim: "The safety case is the sixth verification-family member — claim + evidence + constraints, joining equivalence-checking, formal-verification, benchmark-validity, schedulability-analysis, and stability."
  certainty: high
  evidence: Verification family candidate (009-012)
  scope: cross-domain
- claim: "The argument is a relationship structure — evidence links to claims through stated conditions, not a new evidence type."
  certainty: high
  evidence: Cross-domain comparison (relationships as structure)
  scope: cross-domain
- claim: "A safety case is valid only under its stated conditions — environment, configuration, and assumptions bound the claim."
  certainty: high
  evidence: Cross-domain comparison (validity conditions 008-011)
  scope: cross-domain
- claim: "Certification standards are constraint sets over evidence — the case demonstrates the claim, it does not construct it."
  certainty: high
  evidence: Certification practice (P3)
  scope: cross-domain

## Relationships
- concept: cyber-physical-system
  relationship: serves
  description: "The safety case serves the cyber-physical system — the assurance claim over the deployed system."
- concept: closed-loop-guarantee
  relationship: supports
  description: "The safety case supports closed-loop-guarantee — the case is the evidence structure behind the guarantee."
- concept: formal-verification
  relationship: analogous_to
  description: "The safety case is analogous to formal verification — demonstrated correctness under stated conditions — the Cycle 009 cross-domain link."
- concept: stability
  relationship: analogous_to
  description: "The safety case is analogous to stability — claim + evidence + constraints — the Cycle 012 cross-domain link."
- concept: autonomy-decision
  relationship: constrains
  description: "The safety case constrains autonomy-decision — the assurance envelope bounds what the system may decide."

## Tradeoffs
- dimension: evidence_depth_vs_cost
  options:
    deep_evidence:
      value: assurance
      rationale: "Deep evidence demonstrates more."
    light_evidence:
      value: speed_to_field
      rationale: "Light evidence reaches the field faster."
  importance: high
- dimension: assurance_vs_flexibility
  options:
    rigid_case:
      value: certification
      rationale: "Rigid cases certify a fixed configuration."
    flexible_case:
      value: adaptability
      rationale: "Flexible cases accommodate change."
  importance: medium

## Failure Modes
- name: evidence_gap
  description: "The case asserts where evidence is missing — the claim outruns the demonstration."
  likelihood: medium
  observable_evidence: "Claims without backing; untested corners; argument over empty evidence"
  detection: "Evidence coverage review; case audits; claim-evidence tracing"
  recovery: "Close the gap; narrow the claim; add verification"
  retryable: true
- name: unstated_assumption
  description: "The case rests on conditions that were never stated — the claim silently exceeds its validity."
  likelihood: medium
  observable_evidence: "Conditions outside the case; assumptions discovered after the fact; surprise failures"
  detection: "Assumption review; condition audits; change impact analysis"
  recovery: "State the assumptions; re-scope the claim; re-verify"
  retryable: true
- name: invalidated_case
  description: "The system changed without the case being regenerated — the evidence artifact no longer matches its claim."
  likelihood: medium
  observable_evidence: "Configuration drift; claims over old states; case/implementation divergence"
  detection: "Change tracking; case refresh audits; configuration comparison"
  recovery: "Regenerate the case; re-verify; freeze the configuration"
  retryable: true

## Observations
- observation: "The safety case resolved as the sixth verification-family member — certification pressure collapsed into claim + evidence + constraints, exactly as a proof did (009)."
  confidence: high
  source: P3 test (Cycle 012)
- observation: "Certification standards behave as constraint sets over evidence — the case demonstrates, it does not construct."
  confidence: high
  source: Certification practice
- observation: "Epistemic Distance at the safety case is 2–3 — the case argues over the model chain, at the same distance as the guarantees it supports."
  confidence: high
  source: Epistemic Distance metric (Cycle 012)
- observation: "The invalidated case is the certification form of assumption drift — evidence decays when the claim's conditions change."
  confidence: high
  source: Cross-domain comparison (guarantee erosion 011)

## Constraints
- constraint: "A safety case demonstrates a claim under stated conditions — it verifies, it does not construct."
  type: invariant
  scope: cross-domain
- constraint: "An argument without evidence is an assertion, not a case."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Trace every claim to its evidence."
  rationale: "An evidence gap is the case's characteristic failure — tracing finds it."
  evidence_level: high
- heuristic: "State every assumption the case stands on."
  rationale: "An unstated assumption is an unbounded condition."
  evidence_level: high

## Recommendations
- recommendation: "Represent the safety case as claim + evidence + constraints — the argument is a relationship structure."
  context: modelling
  certainty: strong
  rationale: "The verification family candidate holds at n=6 — the case is an artifact of evidence."
- recommendation: "Regenerate the case when the system changes."
  context: engineering
  certainty: strong
  rationale: "An invalidated case is an evidence artifact that no longer matches its claim."
- recommendation: "Treat certification standards as constraint sets over evidence, not as authority."
  context: operations
  certainty: strong
  rationale: "The standard bounds the demonstration; the evidence must actually carry the claim."

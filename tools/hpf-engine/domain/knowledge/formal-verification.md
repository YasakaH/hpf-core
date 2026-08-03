# Formal Verification

## Identity
- id: formal-verification
- type: concept
- title: Formal Verification
- tags: [formal verification, proof, theorem proving, machine-checked proof, verification, correctness]
- entities: [formal verification, proof, proof obligation, theorem prover, specification, machine-checked proof]
- concepts: [compiler-correctness, type-safety, equivalence-checking, program-semantics, type-system]

## Claims
- claim: "Formal verification is the machine-checked establishment of a property — a proof artifact whose every step is checked by a machine."
  certainty: high
  evidence: Verification practice, theorem prover usage
  scope: cross-domain
- claim: "A proof is an artifact of evidence — proof obligations, specifications, and machine-checked derivations are the evidence structure, not a new knowledge kind."
  certainty: high
  evidence: Formal methods practice
  scope: cross-domain
- claim: "Verification is bounded by specification correctness — a verified system is correct only with respect to what the specification states (garbage in, verified garbage out)."
  certainty: high
  evidence: Verification experience, specification bug analyses
  scope: cross-domain
- claim: "Machine-checked proofs are the strongest evidence engineering has — they eliminate the possibility of proof error, not the possibility of specification error."
  certainty: high
  evidence: Formal methods research and practice
  scope: cross-domain
- claim: "Verification cost scales with system complexity — verification investment is a decision about which properties deserve proof."
  certainty: high
  evidence: Verification engineering practice
  scope: cross-domain

## Relationships
- concept: compiler-correctness
  relationship: verifies
  description: "Formal verification verifies compiler correctness — verified compilers prove semantic preservation."
- concept: type-safety
  relationship: verifies
  description: "Formal verification verifies type safety — soundness theorems are proven, not tested."
- concept: equivalence-checking
  relationship: uses
  description: "Formal verification uses equivalence checking — before/after comparisons are verification tasks."
- concept: program-semantics
  relationship: requires
  description: "Formal verification requires program semantics — a property is meaningful only against a formal model of meaning."
- concept: type-system
  relationship: verifies
  description: "Formal verification verifies the type system — rule soundness is a proof target."

## Tradeoffs
- dimension: verification_depth_vs_cost
  options:
    deep_verification:
      value: assurance
      rationale: "Full verification of critical properties gives the strongest assurance but dominates engineering time."
    targeted_verification:
      value: affordability
      rationale: "Verifying the riskiest properties focuses cost but leaves other properties unproven."
  importance: high
- dimension: specification_strength_vs_tractability
  options:
    strong_specifications:
      value: guarantees
      rationale: "Strong specifications promise more but are harder to prove and easier to get wrong."
    weak_specifications:
      value: tractability
      rationale: "Weak specifications are easier to verify but guarantee less of what users assume."
  importance: high

## Failure Modes
- name: specification_error
  description: "The specification misstates the intended property — verification succeeds against the wrong target and the system is 'verified' but wrong."
  likelihood: medium
  observable_evidence: "Verified systems failing in practice; proofs that do not match intent; spec-review findings"
  detection: "Specification review; property elicitation; counterexample analysis"
  recovery: "Correct the specification; re-verify; validate specs against intent"
  retryable: true
- name: verification_gap
  description: "The verification covers only part of the system — unverified components or assumptions break the overall guarantee."
  likelihood: medium
  observable_evidence: "Verified components failing through unverified interactions; trust-boundary violations; assumption mismatches"
  detection: "Trust boundary analysis; assumption auditing; composition review"
  recovery: "Close the gap; verify the boundary; document assumptions"
  retryable: true
- name: proof_system_unsoundness
  description: "The prover or logic admits a false derivation — a machine-checked proof that is not actually valid."
  likelihood: low
  observable_evidence: "Proofs of false statements; logic inconsistencies; prover bugs"
  detection: "Prover audits; logic consistency research; cross-prover checking"
  recovery: "Patch the logic or prover; re-check dependent proofs"
  retryable: true

## Observations
- observation: "Machine-checked proof eliminates proof error but not specification error — the specification is the residual risk."
  confidence: high
  source: Formal methods practice
- observation: "Verification effort concentrates at trust boundaries — the components whose failure voids everything else."
  confidence: high
  source: Verification engineering experience
- observation: "Verified compilers remain rare because the cost curve is steep — the decision to verify is economic, not technical."
  confidence: high
  source: Verified compiler projects

## Constraints
- constraint: "A verified property holds only under the stated assumptions and specification — verification does not transcend its own inputs."
  type: invariant
  scope: cross-domain
- constraint: "Proofs must be machine-checked to count as verification — human proof checking reintroduces exactly the error class being eliminated."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: verification_target
  question: "Which properties and components deserve proof-level assurance?"
  supporting: "Targeted verification concentrates cost where failure is most costly."
  contradictory: "Unverified components can void the verified ones through boundary interactions."
  weight: high
- factor: proof_tractability
  question: "Can the specification be expressed and proved within the available logic and effort?"
  supporting: "Tractable specifications are verified completely."
  contradictory: "Overambitious specifications stall verification or produce weak proofs."
  weight: high
- factor: cost_assurance_tradeoff
  question: "What assurance is the verification budget buying, relative to other correctness channels?"
  supporting: "Proof is the strongest evidence; differential testing is the cheapest channel."
  contradictory: "Verification spending can exceed the value of the guarantee it buys."
  weight: high

## Heuristics
- heuristic: "Treat the specification as the risk — the property you state is the property you get."
  rationale: "Specification error is the residual failure mode after proof is eliminated."
  evidence_level: high
- heuristic: "Verify at trust boundaries first."
  rationale: "Assurance concentrates where failure voids other guarantees."
  evidence_level: high

## Recommendations
- recommendation: "Verify only with machine-checked proofs."
  context: verification_policy
  certainty: strong
  rationale: "Human proof checking reintroduces the error class verification exists to remove."
- recommendation: "Review specifications as carefully as code."
  context: verification_governance
  certainty: strong
  rationale: "The specification is the residual risk; it deserves code-grade review."
- recommendation: "Choose verification targets by failure cost, not by proof convenience."
  context: investment_decision
  certainty: strong
  rationale: "Verification is an investment; its returns are measured in voided failure classes."

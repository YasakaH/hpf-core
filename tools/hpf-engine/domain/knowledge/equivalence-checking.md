# Equivalence Checking

## Identity
- id: equivalence-checking
- type: concept
- title: Equivalence Checking
- tags: [compilers, equivalence checking, semantic equivalence, before-after comparison, verification, testing]
- entities: [equivalence checking, semantic equivalence, equivalence relation, observation model, before-after comparison]
- concepts: [program-semantics, compiler-optimization, compiler-correctness, formal-verification, constant-folding, dead-code-elimination]

## Claims
- claim: "Equivalence checking is the mechanical comparison of two programs — determining whether their observable behaviour matches under a stated observation model."
  certainty: high
  evidence: Equivalence checking research and practice
  scope: cross-domain
- claim: "Equivalence is a relation defined over semantics, not syntax — two differently-shaped programs can be equivalent; two similar ones may not be."
  certainty: high
  evidence: Program equivalence research
  scope: cross-domain
- claim: "Equivalence is always relative to an observation model — equivalence under input-output behaviour is not equivalence under full behavioural observation."
  certainty: high
  evidence: Program equivalence theory, compiler engineering experience
  scope: cross-domain
- claim: "Equivalence checking is the verification channel for transformations — before/after comparison is how optimization correctness is mechanically established."
  certainty: high
  evidence: Compiler verification practice
  scope: cross-domain
- claim: "A checker can be wrong in both directions — false positives (claiming equivalence where behaviour differs) and false negatives (rejecting true equivalence) are distinct failure classes."
  certainty: high
  evidence: Equivalence checking implementation practice
  scope: cross-domain

## Relationships
- concept: program-semantics
  relationship: based_on
  description: "Equivalence checking is based on program semantics — equivalence is a relation over meaning."
- concept: compiler-optimization
  relationship: verifies
  description: "Equivalence checking verifies compiler optimizations — before/after comparison validates transformations."
- concept: compiler-correctness
  relationship: verifies
  description: "Equivalence checking verifies compiler correctness — transformation preservation is checked mechanically."
- concept: formal-verification
  relationship: used_by
  description: "Equivalence checking is used by formal verification — equivalence proofs are verification tasks."
- concept: constant-folding
  relationship: verifies
  description: "Equivalence checking verifies constant folding — folded values must equal evaluated expressions."
- concept: dead-code-elimination
  relationship: verifies
  description: "Equivalence checking verifies dead code elimination — removed code must be unobservable."

## Tradeoffs
- dimension: checking_completeness_vs_tractability
  options:
    complete_checking:
      value: certainty
      rationale: "Complete checking decides all cases but is intractable for large programs."
    approximate_checking:
      value: scalability
      rationale: "Approximate checking scales but leaves equivalence undecided."
  importance: high
- dimension: observation_strength_vs_checking_freedom
  options:
    fine_observation:
      value: fidelity
      rationale: "Fine observation models catch subtle behavioural differences but reject legal aggressive optimizations."
    coarse_observation:
      value: transformation_freedom
      rationale: "Coarse observation models permit more transformations but admit differences users may observe."
  importance: high

## Failure Modes
- name: false_positive
  description: "The checker declares equivalence where behaviour differs — an unsound verdict lets a miscompilation pass."
  likelihood: medium
  observable_evidence: "Checked transformations later producing different behaviour; checker soundness gaps; edge-case divergences"
  detection: "Checker audits; adversarial equivalence pairs; differential re-testing"
  recovery: "Fix the checker's abstraction; strengthen the equivalence relation; re-run verification"
  retryable: true
- name: false_negative
  description: "The checker rejects true equivalence — sound transformations are flagged, blocking valid optimizations."
  likelihood: medium
  observable_evidence: "Optimizations rejected by checking; spurious equivalence failures; verification blockage"
  detection: "False-negative triage; checker precision analysis; acceptance criteria review"
  recovery: "Widen the equivalence relation; improve checker precision; document rejected classes"
  retryable: true
- name: observation_model_mismatch
  description: "The checker's observation model differs from the language's — equivalence is decided under the wrong behavioural relation."
  likelihood: medium
  observable_evidence: "Checker verdicts disagreeing with semantic review; equivalence disputes; model drift"
  detection: "Model review; equivalence criteria audits; cross-checker comparison"
  recovery: "Align observation models; document the relation; re-verify affected pairs"
  retryable: true

## Observations
- observation: "Equivalence checking converts correctness from a hope into a checkable artifact — before/after comparison is the workhorse of transformation verification."
  confidence: high
  source: Compiler verification practice
- observation: "Every equivalence dispute in practice reduces to an observation model dispute."
  confidence: high
  source: Compiler engineering experience
- observation: "Checker soundness, not coverage, is the critical property — false positives are correctness failures, false negatives are opportunities lost."
  confidence: high
  source: Equivalence checking practice

## Constraints
- constraint: "Equivalence verdicts are valid only under a stated observation model — an unstated model makes every verdict untestable."
  type: invariant
  scope: cross-domain
- constraint: "A checker must never claim equivalence falsely — false positives violate the verification contract."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "State the observation model before designing the checker."
  rationale: "The relation is the checker's contract; everything else is engineering."
  evidence_level: high
- heuristic: "Audit false positives as correctness defects, false negatives as precision issues."
  rationale: "The two directions have opposite severity and opposite fixes."
  evidence_level: high

## Recommendations
- recommendation: "Define the equivalence relation and its observation model explicitly."
  context: checker_design
  certainty: strong
  rationale: "An explicit relation makes verdicts meaningful and auditable."
- recommendation: "Prefer unsoundness-by-silence over false claims — reject rather than wrongly accept."
  context: verification_policy
  certainty: strong
  rationale: "A false positive validates a miscompilation; a false negative only blocks an opportunity."
- recommendation: "Re-verify checked transformations when the observation model changes."
  context: change_management
  certainty: strong
  rationale: "Old verdicts under a new relation are stale evidence."

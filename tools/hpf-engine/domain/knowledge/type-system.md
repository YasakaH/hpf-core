# Type System

## Identity
- id: type-system
- type: concept
- title: Type System
- tags: [compilers, types, static analysis, type checking, soundness, formal rules]
- entities: [type system, type, type rule, type checker, type annotation, kind system]
- concepts: [abstract-syntax-tree, type-safety, program-semantics, compiler-correctness, formal-verification, equivalence-checking]

## Claims
- claim: "A type system is a set of formal rules assigning types to program terms — the rules determine which programs are well-typed."
  certainty: high
  evidence: Type theory literature, programming language design
  scope: cross-domain
- claim: "Type checking is decidable static analysis — the checker decides well-typedness without executing the program."
  certainty: high
  evidence: Type checker implementation practice, type theory
  scope: cross-domain
- claim: "A sound type system guarantees that well-typed programs cannot exhibit the runtime failure classes its safety theorem covers."
  certainty: high
  evidence: Type safety research (progress and preservation theorems)
  scope: cross-domain
- claim: "Type rules trade expressiveness against checking power — richer type systems detect more classes of errors but complicate the checker and the language."
  certainty: high
  evidence: Programming language design experience
  scope: cross-domain
- claim: "Type system soundness holds only within its stated scope — unsafe constructs, dynamic escapes, and untrusted annotations can pierce the guarantee."
  certainty: high
  evidence: Unsafe code practice, soundness hole incidents
  scope: cross-domain

## Relationships
- concept: abstract-syntax-tree
  relationship: annotates
  description: "The type system annotates the AST — type information is attached to syntax nodes during checking."
- concept: type-safety
  relationship: guarantees
  description: "The type system guarantees type safety — soundness of the rules is the source of the safety property."
- concept: program-semantics
  relationship: constrains
  description: "The type system constrains program semantics — well-typedness restricts which behaviours a program can have."
- concept: compiler-correctness
  relationship: must_preserve
  description: "Compiler correctness must preserve type soundness — generated code must not introduce new runtime failure classes."
- concept: formal-verification
  relationship: verified_by
  description: "The type system is verified by formal verification — soundness and safety are proven, not tested."
- concept: equivalence-checking
  relationship: relied_upon_by
  description: "Equivalence checking relies on the type system — typed terms make behaviour comparison tractable."

## Tradeoffs
- dimension: expressiveness_vs_checking_power
  options:
    rich_types:
      value: error_detection
      rationale: "Expressive type systems catch more failure classes statically but complicate the language and the checker."
    simple_types:
      value: accessibility
      rationale: "Simple type systems are easy to learn and check but push more failure classes to runtime."
  importance: high
- dimension: soundness_strictness_vs_practicality
  options:
    strict_soundness:
      value: guarantee
      rationale: "Strict soundness yields a clean safety theorem but requires conservative rejection of some valid programs."
    pragmatic_unsoundness:
      value: flexibility
      rationale: "Pragmatic escapes (unsafe blocks, casts) increase flexibility but puncture the guarantee."
  importance: high

## Failure Modes
- name: unsoundness_hole
  description: "The type system admits an escape — unsafe constructs or unsound rules let ill-typed behaviour reach runtime."
  likelihood: medium
  observable_evidence: "Runtime type errors in supposedly type-safe code; soundness counterexamples; crashes in safe code"
  detection: "Soundness proofs; adversarial typing examples; runtime type instrumentation"
  recovery: "Close the escape; restrict unsafe constructs; repair the rule set"
  retryable: true
- name: checker_divergence
  description: "The type checker and the type rules diverge — the implementation checks something other than the documented rules."
  likelihood: medium
  observable_evidence: "Accepted programs the rules forbid; rejected programs the rules allow; spec-vs-implementation drift"
  detection: "Rule conformance test suites; specification audits; differential checking"
  recovery: "Re-align implementation with rules; test against the specification"
  retryable: true
- name: inference_ambiguity
  description: "Type inference fails or over-commits — the checker cannot infer types or infers unintended ones, producing confusing errors or wrong annotations."
  likelihood: medium
  observable_evidence: "Inference failure cascades; misleading diagnostics; unintended inferred types"
  detection: "Type inference test cases; diagnostic review; annotation requirement analysis"
  recovery: "Add explicit annotations; refine inference; improve error context"
  retryable: true

## Observations
- observation: "Type checking catches whole failure classes at compile time — soundness is a static guarantee, not a runtime probability."
  confidence: high
  source: Programming language practice
- observation: "Type system complexity is the dominant cost of language evolution — rule changes ripple through the checker, diagnostics, and tooling."
  confidence: high
  source: Language design experience
- observation: "Most practical soundness holes come from deliberate escape hatches, not from proof errors in the core rules."
  confidence: high
  source: Unsafe code and soundness hole analyses

## Constraints
- constraint: "Type rules are invariants — every rule must hold for every program, or the system's guarantee is void."
  type: invariant
  scope: cross-domain
- constraint: "Type safety holds only within the typed core — unsafe constructs and runtime escapes are outside the guarantee."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Treat type rules as a specification to be checked against, not a description of the implementation."
  rationale: "Rule-implementation drift is how soundness holes are born."
  evidence_level: high
- heuristic: "Make escape hatches visible and rare."
  rationale: "Pragmatic unsoundness is tolerable only where it is auditable."
  evidence_level: high

## Recommendations
- recommendation: "Define the type system's safety claim explicitly, including its scope and escape hatches."
  context: language_design
  certainty: strong
  rationale: "A scoped guarantee is honest; an unstated scope is a soundness hole."
- recommendation: "Test the checker against the type rules, including negative tests for forbidden programs."
  context: compiler_testing
  certainty: strong
  rationale: "Checker divergence is invisible to positive test suites."
- recommendation: "Track unsoundness reports as correctness failures, not feature requests."
  context: governance
  certainty: strong
  rationale: "Each escape erodes the guarantee the whole type system exists to provide."

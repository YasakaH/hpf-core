# Type Safety

## Identity
- id: type-safety
- type: concept
- title: Type Safety
- tags: [compilers, type safety, soundness, guarantees, progress, preservation, safe languages]
- entities: [type safety, soundness, progress property, preservation property, safe language, runtime failure]
- concepts: [type-system, program-semantics, compiler-correctness, formal-verification, equivalence-checking, dead-code-elimination]

## Claims
- claim: "Type safety is a language guarantee: well-typed programs cannot exhibit the runtime failure classes the safety theorem covers."
  certainty: high
  evidence: Type theory literature, safe language practice
  scope: cross-domain
- claim: "Type safety decomposes into progress and preservation — a well-typed program either steps to a well-typed program or is a value, and no type error is reachable."
  certainty: high
  evidence: Type safety research (progress and preservation)
  scope: cross-domain
- claim: "Type safety is a property of the type system and the runtime together — the guarantee holds only where both halves are sound."
  certainty: high
  evidence: Type safety practice, unsoundness incident analyses
  scope: cross-domain
- claim: "The guarantee is scoped — unsafe constructs, dynamic escapes, and runtime boundaries are outside the safety claim."
  certainty: high
  evidence: Unsafe code practice, FFI boundaries
  scope: cross-domain
- claim: "Type safety is enforced at compile time — the type checker rejects ill-typed programs before they can run."
  certainty: high
  evidence: Compiler implementation practice
  scope: cross-domain

## Relationships
- concept: type-system
  relationship: guaranteed_by
  description: "Type safety is guaranteed by the type system — soundness of the rules is the source of the guarantee."
- concept: program-semantics
  relationship: defined_over
  description: "Type safety is defined over program semantics — the guarantee is about behaviour, not syntax."
- concept: compiler-correctness
  relationship: must_preserve
  description: "Compiler correctness must preserve type safety — code generation cannot introduce new runtime failure classes."
- concept: formal-verification
  relationship: verifiable_by
  description: "Type safety is verifiable by formal verification — soundness is proved, not tested."
- concept: equivalence-checking
  relationship: bounded_by
  description: "Type safety bounds equivalence checking — the guarantee defines which failure classes the checker may ignore."
- concept: dead-code-elimination
  relationship: enabled_by
  description: "Type safety enables aggressive dead code elimination — the guarantee makes removal of unobservable code safe."

## Tradeoffs
- dimension: guarantee_strength_vs_language_power
  options:
    strong_guarantees:
      value: safety
      rationale: "Strong safety covers more failure classes but forces the language to restrict some expressiveness."
    flexible_language:
      value: expressiveness
      rationale: "Flexible languages permit more programs but push more failure classes to runtime or unsafe code."
  importance: high
- dimension: scoped_soundness_vs_uniformity
  options:
    small_unsafe_core:
      value: auditable_guarantee
      rationale: "A small, visible unsafe core keeps the safety claim honest and auditable."
    pervasive_escape_hatches:
      value: pragmatism
      rationale: "Widespread escape hatches are pragmatic but make the guarantee diffuse and hard to audit."
  importance: high

## Failure Modes
- name: soundness_hole
  description: "A language or runtime construct breaks the safety theorem — a well-typed program reaches a type error at runtime."
  likelihood: medium
  observable_evidence: "Runtime type errors in safe code; safety counterexamples; crashes from typed constructs"
  detection: "Soundness proofs; adversarial counterexample hunting; runtime instrumentation"
  recovery: "Repair the construct; close the escape; re-prove affected theorems"
  retryable: true
- name: unsound_optimization
  description: "An optimizer exploits type assumptions the language does not guarantee — optimization changes behaviour for programs outside the assumed type facts."
  likelihood: low
  observable_evidence: "Optimized builds behaving differently; wrong code in safe programs; optimizer violations of language rules"
  detection: "Differential testing; semantics audits of optimizations; formal checks of transformation legality"
  recovery: "Constrain the optimization to guaranteed type facts; regression-test the assumption"
  retryable: true
- name: guarantee_scope_erosion
  description: "The safety claim's scope expands informally — code written at escape hatches (unsafe blocks, FFI) drifts into the 'safe' zone without the guarantee."
  likelihood: medium
  observable_evidence: "Safe code depending on unsafe internals; crashes traced through unsafe boundaries; scope confusion in audits"
  detection: "Unsafe code audits; boundary instrumentation; scope documentation review"
  recovery: "Enforce boundary discipline; document the guarantee's edges; audit escape sites"
  retryable: true

## Observations
- observation: "Type safety converts a class of runtime failures into compile-time rejections — the guarantee is static, not statistical."
  confidence: high
  source: Safe language practice
- observation: "Safety claims are only as strong as their scope — every practical language fences its guarantee with escape hatches."
  confidence: high
  source: Language design experience
- observation: "Optimizers are a recurring source of safety violations — they assume type facts the language does not actually promise."
  confidence: high
  source: Compiler bug analyses

## Constraints
- constraint: "The safety guarantee is scoped — unsafe constructs and runtime boundaries are outside it by definition."
  type: invariant
  scope: cross-domain
- constraint: "Compile-time rejection must be decidable — the checker must decide well-typedness without executing the program."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "State the safety theorem and its scope before designing the escape hatches."
  rationale: "A scoped guarantee is auditable; an unstated scope is a slow-motion soundness hole."
  evidence_level: high
- heuristic: "Audit optimizer assumptions against the guarantee's scope."
  rationale: "Optimizer type assumptions are where safety claims silently erode."
  evidence_level: high

## Recommendations
- recommendation: "Define the safety theorem, its proof strategy, and its scope as a first-class artifact."
  context: language_design
  certainty: strong
  rationale: "The guarantee is the product; everything else is detail."
- recommendation: "Keep escape hatches small, visible, and audited."
  context: language_governance
  certainty: strong
  rationale: "Unstated scope erosion is how safety claims become fiction."
- recommendation: "Test optimizations against the guarantee's boundary, not just its happy path."
  context: testing
  certainty: strong
  rationale: "Unsound optimizations are safety violations with a performance costume."

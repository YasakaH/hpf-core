# Compiler Correctness

## Identity
- id: compiler-correctness
- type: concept
- title: Compiler Correctness
- tags: [compilers, correctness, miscompilation, semantic preservation, verification, reliability]
- entities: [compiler correctness, miscompilation, semantic preservation, compiler bug, wrong-code, differential testing]
- concepts: [program-semantics, intermediate-representation, type-safety, formal-verification, equivalence-checking, optimization-pass, debug-vs-release-modes]

## Claims
- claim: "Compiler correctness is semantic preservation — the compiler is correct if every program it compiles behaves per the source's semantics."
  certainty: high
  evidence: Compiler correctness research and practice
  scope: cross-domain
- claim: "Miscompilation is the correctness failure mode — a compiler defect that produces wrong behaviour for correct source, distinct from rejecting valid input."
  certainty: high
  evidence: Compiler bug analyses, miscompilation research
  scope: cross-domain
- claim: "Compiler correctness is never established by testing alone — the input space is unbounded and the failure modes are rare and input-specific."
  certainty: high
  evidence: Compiler testing research (differential testing findings)
  scope: cross-domain
- claim: "Correctness evidence accumulates from multiple channels — differential testing, conformance suites, formal verification, and real-world volume."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain
- claim: "Correctness is relative to a stated observation model — the compiler preserves the observable behaviour the language defines, not unspecified behaviour."
  certainty: high
  evidence: Language specification practice
  scope: cross-domain

## Relationships
- concept: program-semantics
  relationship: preserves
  description: "Compiler correctness preserves program semantics — semantic preservation is the correctness definition."
- concept: intermediate-representation
  relationship: constrains
  description: "Compiler correctness constrains IR design — representation gaps make correct compilation unachievable."
- concept: type-safety
  relationship: must_preserve
  description: "Compiler correctness must preserve type safety — generated code cannot break the safety guarantee."
- concept: formal-verification
  relationship: supported_by
  description: "Compiler correctness is supported by formal verification — verified compilers prove semantic preservation."
- concept: equivalence-checking
  relationship: verified_by
  description: "Compiler correctness is verified by equivalence checking — before/after comparison validates transformations."
- concept: optimization-pass
  relationship: depends_on
  description: "Compiler correctness depends on pass correctness — each pass must preserve semantics."
- concept: debug-vs-release-modes
  relationship: affected_by
  description: "Compiler correctness is affected by debug vs release modes — different optimization postures change the observable behaviour contract."

## Tradeoffs
- dimension: correctness_assurance_vs_engineering_cost
  options:
    formal_verification:
      value: proof
      rationale: "Fully verified compilers offer the strongest guarantee but cost years of verification effort."
    evidence_accumulation:
      value: pragmatic_assurance
      rationale: "Testing, fuzzing, and differential testing are affordable but never exhaustive."
  importance: high
- dimension: optimization_freedom_vs_behavioural_fidelity
  options:
    aggressive_optimization:
      value: performance
      rationale: "Aggressive optimization exploits the observation model's freedom but surprises users who assumed more behaviour."
    behavioural_fidelity:
      value: predictability
      rationale: "Conservative behaviour preservation is predictable but leaves performance on the table."
  importance: high

## Failure Modes
- name: miscompilation
  description: "A compiler defect changes program behaviour — correct source produces wrong machine code, usually rare and input-specific."
  likelihood: medium
  observable_evidence: "Wrong results in optimized builds; behaviour differing across compiler versions; rare crashes in production"
  detection: "Differential testing across levels and versions; random program generation; user bug reports"
  recovery: "Reproduce at minimal optimization; bisect passes; fix the transformation; regression test"
  retryable: true
- name: wrong_code_generation
  description: "Back-end defects produce machine code that violates the target semantics — bad instruction selection, scheduling, or register allocation."
  likelihood: medium
  observable_evidence: "Target-specific wrong behaviour; ABI violations; crashes only on specific architectures"
  detection: "Target-specific differential testing; ABI conformance tests; assembly review"
  recovery: "Fix the back-end rule; add target-specific tests; re-verify ABI contracts"
  retryable: true
- name: rejection_of_valid_program
  description: "The compiler rejects correct source — a soundness-conservative or buggy front end refuses valid programs."
  likelihood: medium
  observable_evidence: "Compile errors on conforming code; false positives in diagnostics; standards-conformance failures"
  detection: "Conformance test suites; standard-example regression; user reports"
  recovery: "Fix the rejecting rule; align with the standard; regression test"
  retryable: true

## Observations
- observation: "Differential testing is the most effective practical miscompilation detector — comparing outputs across optimization levels and versions."
  confidence: high
  source: Compiler testing research and practice
- observation: "Compiler bugs cluster in optimizations — transformations are where semantic preservation is hardest and least tested per line."
  confidence: high
  source: Compiler bug analyses
- observation: "Real-world volume finds bugs fuzzing cannot — production diversity remains a correctness channel."
  confidence: high
  source: Compiler engineering experience

## Constraints
- constraint: "The compiler must preserve the source's defined behaviour — divergence is a correctness failure regardless of how rarely it triggers."
  type: invariant
  scope: cross-domain
- constraint: "Correctness claims are valid under the language's observation model — unspecified behaviour is outside the preservation obligation."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Differential-test every optimization level and version pair."
  rationale: "Divergence between configurations is the cheapest miscompilation signal."
  evidence_level: high
- heuristic: "Treat miscompilation reports as top-priority defects, not reliability issues."
  rationale: "Wrong code silently corrupts every program that hits it; rejections are loud, miscompilations are not."
  evidence_level: high

## Recommendations
- recommendation: "Run differential testing continuously across optimization levels and releases."
  context: compiler_engineering
  certainty: strong
  rationale: "It is the highest-yield correctness channel available."
- recommendation: "Formalize the observation model the compiler is allowed to change."
  context: compiler_governance
  certainty: strong
  rationale: "Behavioural surprises are observation-model disagreements."
- recommendation: "Verify high-value transformations with equivalence checking before release."
  context: verification
  certainty: strong
  rationale: "Targeted verification covers the transformations most likely to miscompile."

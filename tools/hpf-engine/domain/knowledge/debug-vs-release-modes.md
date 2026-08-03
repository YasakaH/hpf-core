# Debug vs Release Modes

## Identity
- id: debug-vs-release-modes
- type: decision
- title: Debug vs Release Modes
- tags: [compilers, build modes, debug builds, release builds, assertions, optimization levels]
- entities: [debug mode, release mode, build posture, assertion, debug info, optimization level]
- concepts: [compiler-optimization, optimization-tradeoffs, build-systems, compiler-correctness, compiler-performance]

## Claims
- claim: "Debug and release are different build postures — debug optimizes for diagnosability, release for delivered performance."
  certainty: high
  evidence: Build engineering practice
  scope: cross-domain
- claim: "The modes differ in behaviour, not just speed — assertion removal, optimization legality, and debug-info presence change observable behaviour."
  certainty: high
  evidence: Compiler and build engineering experience, incident analyses
  scope: cross-domain
- claim: "Assertion removal is a correctness hazard — behaviour checked in debug builds is unguarded in release, making release-only failures possible."
  certainty: high
  evidence: Release-only bug analyses
  scope: cross-domain
- claim: "The behaviour gap between modes is a knowledge gap — code validated in debug mode is a different program in release mode."
  certainty: high
  evidence: Testing practice, release engineering experience
  scope: cross-domain
- claim: "Mode divergence is a decision, not an accident — the gap can be deliberately widened or narrowed per the product's risk profile."
  certainty: high
  evidence: Build policy practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: configured_by
  description: "Debug and release modes configure compiler optimization — the postures set optimization level and legality."
- concept: optimization-tradeoffs
  relationship: instantiates
  description: "Debug vs release modes instantiate optimization tradeoffs — the canonical posture tradeoff."
- concept: build-systems
  relationship: produced_by
  description: "Debug and release modes are produced by build systems — both postures are build products."
- concept: compiler-correctness
  relationship: affected_by
  description: "Compiler correctness is affected by mode — each posture carries its own behaviour contract."
- concept: compiler-performance
  relationship: differentiates
  description: "Debug vs release modes differentiate compiler performance — the two postures optimize different axes."

## Tradeoffs
- dimension: diagnosability_vs_performance
  options:
    debug_fidelity:
      value: diagnosability
      rationale: "Debug fidelity makes issues diagnosable but ships slow, instrumented code."
    release_performance:
      value: delivered_speed
      rationale: "Release performance ships fast code but with reduced diagnosability."
  importance: high
- dimension: assertion_coverage_vs_runtime_cost
  options:
    full_assertions:
      value: detection
      rationale: "Assertions catch invariant violations early but cost runtime in production."
    no_assertions:
      value: speed
      rationale: "Removed assertions run fast but let invariant violations go undetected."
  importance: high

## Failure Modes
- name: release_only_bug
  description: "Behaviour validated in debug fails in release — the mode change altered the program, not just its speed."
  likelihood: high
  observable_evidence: "Failures that only reproduce in release builds; assertion-protected invariants violated in release; optimized-only wrong behaviour"
  detection: "Mode differential testing; release-mode test suites; assertion-gap analysis"
  recovery: "Test release mode directly; keep critical assertions; narrow the behaviour gap"
  retryable: true
- name: assertion_dependence
  description: "Code relies on assertions for correctness — removing them in release deletes the guard the program depended on."
  likelihood: medium
  observable_evidence: "Release crashes on paths debug exercised; assumptions enforced only by assertions; UB surfacing in release"
  detection: "Assertion-dependence review; release-mode fuzzing; assumption auditing"
  recovery: "Convert critical guards to checked behaviour; validate assumptions in release; correct the code"
  retryable: true
- name: debug_only_behaviour
  description: "Code behaves differently in debug mode — debug-only branches or instrumentation mask or change real behaviour."
  likelihood: medium
  observable_evidence: "Debug passes while release fails; debug-only paths hiding bugs; environment-dependent test results"
  detection: "Mode differential testing; debug-path review; test-matrix analysis"
  recovery: "Test both modes; reduce debug-only behaviour; align test environments"
  retryable: true

## Observations
- observation: "Release-only bugs are the standard cost of mode divergence — every project with distinct modes pays it."
  confidence: high
  source: Release engineering incident analyses
- observation: "The mode gap is a decision surface — products that audit it deliberately control their risk; products that ignore it inherit it."
  confidence: high
  source: Build policy practice
- observation: "Testing in one mode validates one program — mode coverage is part of test coverage."
  confidence: high
  source: Testing practice

## Constraints
- constraint: "Each mode is a distinct program — debug and release builds must be validated separately."
  type: invariant
  scope: cross-domain
- constraint: "Assertion removal must not delete behaviour the program depends on — guards are code, and their removal is a code change."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: optimization_level
  question: "What optimization level does each mode carry, and what behaviour is it allowed to change?"
  supporting: "Deliberate levels make the mode's behaviour contract explicit."
  contradictory: "Undocumented levels hide the behaviour gap until it surfaces as a release-only bug."
  weight: high
- factor: assertion_policy
  question: "Which assertions survive into release, and which are removed?"
  supporting: "Selective retention keeps critical guards in production."
  contradictory: "Full removal saves runtime but deletes the program's protection."
  weight: high
- factor: debug_info_retention
  question: "How much debug information does the shipped artifact retain?"
  supporting: "Retained debug info makes production issues diagnosable."
  contradictory: "Full debug info costs size and can expose internals."
  weight: medium
- factor: environment_fidelity
  question: "Do test environments run the same mode as production?"
  supporting: "Mode-faithful testing validates the deployed program."
  contradictory: "Dev-mode testing validates a different program than production runs."
  weight: high

## Heuristics
- heuristic: "Test release mode directly, not just debug."
  rationale: "Each mode is a program; testing one validates one."
  evidence_level: high
- heuristic: "Audit the assertion policy per invariant, not globally."
  rationale: "Invariants differ in cost; so does their protection."
  evidence_level: high

## Recommendations
- recommendation: "Define the behaviour contract of each mode explicitly — what is optimized, what is removed, what is retained."
  context: build_governance
  certainty: strong
  rationale: "An explicit contract makes mode divergence auditable."
- recommendation: "Keep critical assertions in release."
  context: release_engineering
  certainty: strong
  rationale: "The cheapest failure detection is the guard that survives."
- recommendation: "Run release-mode tests in the release configuration as part of the release process."
  context: release_process
  certainty: strong
  rationale: "Mode-faithful testing is the only validation of the deployed program."

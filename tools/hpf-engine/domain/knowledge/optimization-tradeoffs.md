# Optimization Tradeoffs

## Identity
- id: optimization-tradeoffs
- type: decision
- title: Optimization Tradeoffs
- tags: [compilers, optimization, tradeoffs, decision factors, compile time, binary size, debuggability]
- entities: [optimization tradeoff, optimization aggressiveness, compile-time budget, binary size, debuggability, decision]
- concepts: [compiler-optimization, compiler-performance, build-systems, debug-vs-release-modes, equivalence-checking]

## Claims
- claim: "Optimization is a decision problem — every optimization posture trades generated-code quality against compile time, binary size, and debuggability."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain
- claim: "The optimization posture is chosen per context — release builds optimize differently from debug builds, and shipping contexts weight the axes differently."
  certainty: high
  evidence: Build engineering practice
  scope: cross-domain
- claim: "Tradeoffs are explicit when chosen, implicit when defaulted — an unexamined default still makes a tradeoff, just an unaudited one."
  certainty: high
  evidence: Build configuration practice, incident analyses
  scope: cross-domain
- claim: "Debuggability is the tradeoff dimension most often ignored — optimized builds that users must debug become a correctness-equivalent cost."
  certainty: high
  evidence: Debugging practice, production incident analyses
  scope: cross-domain
- claim: "Tradeoff decisions are reversible only when measurement exists — without performance and compile-time tracking, decisions cannot be audited or rolled back rationally."
  certainty: high
  evidence: Engineering measurement practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: decides_over
  description: "Optimization tradeoffs decide over compiler optimizations — which transformations run and how aggressively."
- concept: compiler-performance
  relationship: shapes
  description: "Optimization tradeoffs shape compiler performance — the chosen posture determines the measured outcome."
- concept: build-systems
  relationship: configures
  description: "Optimization tradeoffs configure build systems — postures are build configuration decisions."
- concept: debug-vs-release-modes
  relationship: defines
  description: "Optimization tradeoffs define debug vs release modes — the two postures are the canonical tradeoff instantiations."
- concept: equivalence-checking
  relationship: bounded_by
  description: "Optimization tradeoffs are bounded by equivalence checking — aggressive postures must still preserve behaviour."

## Tradeoffs
- dimension: runtime_speed_vs_binary_size
  options:
    speed_first:
      value: runtime_performance
      rationale: "Speed-first optimization produces fast code but larger binaries through inlining and specialization."
    size_first:
      value: footprint
      rationale: "Size-first optimization produces small binaries but leaves runtime performance on the table."
  importance: high
- dimension: build_speed_vs_output_quality
  options:
    fast_builds:
      value: iteration_speed
      rationale: "Fast builds accelerate development loops but ship slower code."
    quality_output:
      value: shipped_performance
      rationale: "Heavy optimization ships faster code but slows every build, including CI."
  importance: high

## Failure Modes
- name: defaulted_tradeoff
  description: "The optimization posture is decided by default rather than choice — the tradeoff exists but nobody owns it."
  likelihood: medium
  observable_evidence: "Unexplained release performance differences; tradeoff complaints with no decision owner; config archaeology"
  detection: "Build config audits; decision documentation review; posture review"
  recovery: "Record posture decisions; assign ownership; document tradeoffs"
  retryable: true
- name: debuggability_collapse
  description: "The optimization posture destroys the ability to debug shipped code — optimized builds are unreadable or unreproducible."
  likelihood: medium
  observable_evidence: "Unreadable optimized traces; missing debug info; release-only bugs that resist diagnosis"
  detection: "Debug-ability checks; trace readability review; incident analysis"
  recovery: "Retain debug info selectively; provide symbolised builds; rebalance the posture"
  retryable: true
- name: tradeoff_reversal
  description: "A posture decision is reversed without re-measurement — the new tradeoff is chosen on preference, not evidence."
  likelihood: medium
  observable_evidence: "Performance changes without measurement; posture flip-flops; regression disputes"
  detection: "Change-review audits; measurement-before-change checks"
  recovery: "Measure before deciding; compare against baselines; record the evidence"
  retryable: true

## Observations
- observation: "Tradeoff decisions without measurement are preference decisions wearing engineering clothes."
  confidence: high
  source: Engineering decision practice
- observation: "Debug/release divergence is the most common tradeoff failure — the postures differ more than their names suggest."
  confidence: high
  source: Build engineering incident analyses
- observation: "Tradeoff ownership is the difference between auditable engineering and config archaeology."
  confidence: high
  source: Engineering governance practice

## Constraints
- constraint: "Every optimization posture is a tradeoff — choosing 'default' chooses a tradeoff, not a way to avoid one."
  type: invariant
  scope: cross-domain
- constraint: "Posture changes require measurement — a tradeoff decision without evidence is reversible only by accident."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: optimization_aggressiveness
  question: "How aggressively should the compiler optimize, given the build's purpose?"
  supporting: "Aggressive postures maximise shipped performance."
  contradictory: "Aggressive optimization costs compile time, size, and debuggability."
  weight: high
- factor: compile_time_budget
  question: "What compile-time cost is acceptable for this build's users (developers, CI)?"
  supporting: "Budgeted compile time keeps development and CI fast."
  contradictory: "Tight budgets force conservative optimization postures."
  weight: high
- factor: binary_size_target
  question: "Does the delivery context impose a binary-size constraint?"
  supporting: "Size targets protect constrained deployments."
  contradictory: "Size-first postures trade away runtime performance."
  weight: medium
- factor: debuggability_requirement
  question: "Will the users of this build need to debug it, and how much fidelity do they need?"
  supporting: "Debug-fidelity builds make production issues diagnosable."
  contradictory: "Full fidelity costs performance and size in the shipped artifact."
  weight: high

## Heuristics
- heuristic: "Choose postures per context, not globally."
  rationale: "Debug, release, and delivery variants have different tradeoff weightings."
  evidence_level: high
- heuristic: "Record the decision and its evidence."
  rationale: "An owned decision is auditable; a defaulted one is archaeology."
  evidence_level: high

## Recommendations
- recommendation: "Make optimization posture an explicit decision with a recorded owner and evidence."
  context: build_governance
  certainty: strong
  rationale: "Unexamined defaults are tradeoffs without owners."
- recommendation: "Measure before changing posture."
  context: change_management
  certainty: strong
  rationale: "Evidence-based tradeoff decisions are reversible; preference-based ones are political."
- recommendation: "Never let debug/release divergence become a debugging tax on production issues."
  context: release_engineering
  certainty: strong
  rationale: "The cheapest time to preserve diagnosability is at posture choice."

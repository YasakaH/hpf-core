# Compiler Performance

## Identity
- id: compiler-performance
- type: concept
- title: Compiler Performance
- tags: [compilers, performance, benchmarks, generated code, compile time, measurement]
- entities: [compiler performance, generated code quality, benchmark, compile time, performance regression, measurement]
- concepts: [compiler-optimization, optimization-tradeoffs, build-systems, optimization-pass, debug-vs-release-modes]

## Claims
- claim: "Compiler performance has two axes — the quality of the generated code and the cost of compilation itself (time, memory)."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain
- claim: "Generated-code performance is measured by benchmarks — the instruments define what 'fast' means, and benchmark validity bounds the measurement."
  certainty: high
  evidence: Benchmarking practice and methodology
  scope: cross-domain
- claim: "Performance is a distribution, not a point — benchmark noise, hardware variation, and input dependence make single-number claims misleading."
  certainty: high
  evidence: Measurement methodology, benchmark design research
  scope: cross-domain
- claim: "Optimizations trade axes against each other — faster generated code can cost compile time, binary size, or debuggability."
  certainty: high
  evidence: Compiler engineering practice
  scope: cross-domain
- claim: "Performance regressions are detectable only with disciplined measurement — without baselines and noise control, regressions hide in the noise."
  certainty: high
  evidence: Performance engineering practice
  scope: cross-domain

## Relationships
- concept: compiler-optimization
  relationship: driven_by
  description: "Compiler performance drives optimization — generated-code quality is the optimization objective."
- concept: optimization-tradeoffs
  relationship: informed_by
  description: "Compiler performance informs optimization tradeoffs — measurement feeds the tradeoff decisions."
- concept: build-systems
  relationship: constrained_by
  description: "Compiler performance is constrained by build systems — compile-time budgets and incremental expectations bound optimization work."
- concept: optimization-pass
  relationship: affected_by
  description: "Compiler performance is affected by pass pipelines — pass count and cost dominate compile time."
- concept: debug-vs-release-modes
  relationship: differentiated_by
  description: "Compiler performance is differentiated across debug and release modes — the two postures optimize different axes."

## Tradeoffs
- dimension: generated_code_quality_vs_compile_time
  options:
    quality_focus:
      value: runtime_performance
      rationale: "Heavy optimization produces fast code but slow builds."
    speed_focus:
      value: fast_builds
      rationale: "Light optimization keeps builds fast but leaves runtime performance on the table."
  importance: high
- dimension: measurement_precision_vs_overhead
  options:
    rigorous_measurement:
      value: detection_power
      rationale: "Rigorous benchmark control catches real regressions but costs setup and machine time."
    lightweight_measurement:
      value: speed
      rationale: "Lightweight measurement is cheap but cannot distinguish regressions from noise."
  importance: high

## Failure Modes
- name: performance_regression
  description: "A change slows generated code or compilation — the compiler's output quality degrades without a correctness failure to signal it."
  likelihood: medium
  observable_evidence: "Benchmark declines; compile-time increases; user-visible slowdowns after compiler updates"
  detection: "Continuous benchmark baselines; compile-time tracking; performance tests on release candidates"
  recovery: "Bisect the change; revert or fix the regression; add regression tests"
  retryable: true
- name: benchmark_noise_obscuring
  description: "Measurement noise hides real changes — regressions and improvements are indistinguishable from environmental variation."
  likelihood: medium
  observable_evidence: "Non-reproducible benchmark results; conclusions flipping between runs; chasing noise"
  detection: "Noise analysis; repeated-run statistics; controlled environments"
  recovery: "Improve experimental control; use statistical comparisons; longer measurement windows"
  retryable: true
- name: benchmark_gaming
  description: "Optimizations tune to the benchmark rather than real workloads — measured performance improves while real performance does not."
  likelihood: medium
  observable_evidence: "Benchmark wins without real-world gains; workload regression reports despite benchmark gains; benchmark overfitting"
  detection: "Workload diversity checks; benchmark rotation; production comparison"
  recovery: "Diversify benchmarks; validate against real workloads; rotate instruments"
  retryable: true

## Observations
- observation: "Compile-time regressions accumulate silently — each change is affordable alone, and only cumulative measurement reveals the trend."
  confidence: high
  source: Compiler engineering practice
- observation: "Benchmark validity is the ceiling on performance knowledge — an invalid instrument makes every measurement misleading."
  confidence: high
  source: Benchmarking methodology
- observation: "Performance and correctness compete for the same engineering budget — the highest-risk optimizer changes are exactly those that improve benchmarks."
  confidence: high
  source: Compiler engineering experience

## Constraints
- constraint: "Performance claims are valid only within the benchmark's validity — the instrument bounds the claim."
  type: invariant
  scope: cross-domain
- constraint: "Optimization must not trade correctness for performance — a faster miscompilation is still a miscompilation."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Track compile time cumulatively across changes."
  rationale: "Silent accumulation is the failure mode; cumulative tracking is the detection."
  evidence_level: high
- heuristic: "Treat benchmark improvements as hypotheses until validated on real workloads."
  rationale: "Benchmark gaming is the standard way performance work goes wrong."
  evidence_level: high

## Recommendations
- recommendation: "Maintain continuous benchmark baselines with noise controls."
  context: performance_governance
  certainty: strong
  rationale: "Regressions are invisible without a baseline and noise discipline."
- recommendation: "Validate performance changes against diverse real workloads, not just benchmarks."
  context: change_management
  certainty: strong
  rationale: "Instruments lie; workloads do not."
- recommendation: "Never accept a correctness risk for a benchmark gain."
  context: engineering_policy
  certainty: strong
  rationale: "Performance is measured; correctness is guaranteed. The trade is never symmetric."

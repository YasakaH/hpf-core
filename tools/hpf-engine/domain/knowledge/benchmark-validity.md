# Benchmark Validity

## Identity
- id: benchmark-validity
- type: concept
- title: Benchmark Validity
- tags: [machine learning, benchmarks, evaluation, measurement, contamination, leaderboards, validity]
- entities: [benchmark, benchmark validity, leaderboard, benchmark score, contamination, evaluation scope]
- concepts: [generalization, training-data, hallucination, metric-selection, human-evaluation, alignment]

## Claims
- claim: "A benchmark is a measurement instrument — its score is evidence about the model only within the benchmark's scope."
  certainty: high
  evidence: Evaluation methodology literature
  scope: cross-domain
- claim: "Benchmark scores are upper bounds on demonstrated performance, not ground truth about capability."
  certainty: high
  evidence: Evaluation research, benchmark audits
  scope: cross-domain
- claim: "Benchmark contamination — benchmark content in training data — inflates scores and invalidates the measurement."
  certainty: high
  evidence: Contamination research, leaderboard audits
  scope: cross-domain
- claim: "Benchmark validity decays — benchmarks saturate as models train on them and their ability to discriminate capability diminishes."
  certainty: high
  evidence: Benchmark saturation research
  scope: cross-domain
- claim: "Benchmarks are proxies for capability — they measure proxy tasks and inherit the proxy's blind spots."
  certainty: high
  evidence: Evaluation methodology literature
  scope: cross-domain

## Relationships
- concept: generalization
  relationship: estimates
  description: "Benchmarks estimate generalization — the score is evidence about unseen-data performance within scope."
- concept: training-data
  relationship: contaminated_by
  description: "Benchmark validity is contaminated by training data — benchmark content in training invalidates the score."
- concept: hallucination
  relationship: measures
  description: "Benchmarks measure hallucination — hallucination rates are benchmark evidence, scope-bound like all scores."
- concept: metric-selection
  relationship: governed_by
  description: "Benchmark design is governed by metric selection — the metric determines what the benchmark demonstrates."
- concept: human-evaluation
  relationship: complements
  description: "Benchmarks complement human evaluation — automated measurement and human judgement cover different qualities."
- concept: alignment
  relationship: evaluates
  description: "Benchmarks evaluate alignment — alignment claims are only as strong as the benchmarks measuring them."

## Tradeoffs
- dimension: benchmark_power_vs_scope
  options:
    narrow_benchmark:
      value: precision
      rationale: "Narrow benchmarks measure one capability precisely but miss adjacent behaviours."
    broad_benchmark:
      value: coverage
      rationale: "Broad benchmarks cover many capabilities but measure each shallowly."
  importance: high
- dimension: static_vs_live_benchmarks
  options:
    static_benchmark:
      value: comparability
      rationale: "Fixed benchmarks stay comparable across models but saturate and leak over time."
    live_benchmark:
      value: freshness
      rationale: "Updated benchmarks resist saturation but break comparability with past results."
  importance: high

## Failure Modes
- name: benchmark_leakage
  description: "Benchmark content enters training data — the model is scored on content it has seen, inflating the measurement."
  likelihood: high
  observable_evidence: "Scores far above fresh-data performance; performance collapse on new variants; contamination patterns in training corpora"
  detection: "Contamination audits; variant testing; n-gram overlap analysis between training data and benchmark"
  recovery: "Decontaminate training data; maintain benchmark exclusion lists; use held-out fresh variants"
  retryable: true
- name: benchmark_saturation
  description: "The benchmark stops discriminating — models score at the ceiling and the benchmark no longer measures capability differences."
  likelihood: high
  observable_evidence: "Scores clustering at ceiling; rank changes driven by noise; no capability signal in score differences"
  detection: "Score distribution analysis; discriminative power measurement; error-profile review"
  recovery: "Retire or renew saturated benchmarks; shift to harder or live variants"
  retryable: true
- name: proxy_mismatch
  description: "The benchmark measures a proxy that diverges from the intended capability — high scores coexist with real-task failure."
  likelihood: medium
  observable_evidence: "High benchmark scores with poor task-matched performance; benchmark wins that do not transfer to deployment"
  detection: "Task-matched validation; proxy-criterion correlation analysis"
  recovery: "Design task-matched benchmarks; validate proxy against the real task"
  retryable: true

## Observations
- observation: "Contamination is widespread and inflates reported scores on popular benchmarks."
  confidence: high
  source: Contamination audits, leaderboard analyses
- observation: "Benchmark scores systematically overstate production performance."
  confidence: high
  source: Deployment studies, evaluation audits
- observation: "Leaderboard rankings frequently diverge from task-appropriate evaluation results."
  confidence: high
  source: Independent evaluation comparisons

## Constraints
- constraint: "A benchmark score is evidence only within the benchmark's stated scope."
  type: invariant
  scope: cross-domain
- constraint: "A benchmark whose content has entered training data can no longer measure the model."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Check contamination before trusting any benchmark score."
  rationale: "Contamination silently converts measurement into memorization demonstration."
  evidence_level: high
- heuristic: "Report benchmark scope with every score — the number is meaningless without its instrument."
  rationale: "Scope is the validity condition of the measurement."
  evidence_level: high
- heuristic: "Prefer benchmarks whose task matches the deployment task over famous benchmarks."
  rationale: "Task match determines transfer; fame does not."
  evidence_level: high

## Recommendations
- recommendation: "Treat benchmarks as measurement instruments with stated scope, not as capability verdicts."
  context: evaluation
  certainty: strong
  rationale: "Instrument framing keeps score interpretation disciplined."
- recommendation: "Keep benchmark content out of training data by exclusion list and audit."
  context: data_governance
  certainty: strong
  rationale: "Contamination is the dominant silent invalidation of model evidence."
- recommendation: "Complement static benchmarks with task-matched, fresh evaluation at deployment time."
  context: deployment
  certainty: strong
  rationale: "Static scores age and saturate; deployment-time measurement restores validity."

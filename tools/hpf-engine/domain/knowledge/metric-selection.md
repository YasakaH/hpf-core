# Metric Selection

## Identity
- id: metric-selection
- type: concept
- title: Metric Selection
- tags: [machine learning, metrics, evaluation, precision, recall, F1, accuracy, aggregation]
- entities: [metric selection, evaluation metric, accuracy, precision, recall, F1, aggregate metrics]
- concepts: [benchmark-validity, generalization, confidence-calibration, distribution-shift, human-evaluation, alignment]

## Claims
- claim: "Metric choice determines what an evaluation demonstrates — different metrics measure different properties of the same predictions."
  certainty: high
  evidence: Evaluation methodology literature
  scope: cross-domain
- claim: "Metrics are not interchangeable — accuracy, precision, recall, calibration, and coverage answer different questions about the same model."
  certainty: high
  evidence: Evaluation practice and research
  scope: cross-domain
- claim: "Metric selection is a decision under tradeoffs — the choice encodes which error type the evaluator finds costlier."
  certainty: high
  evidence: Decision-theoretic evaluation literature
  scope: cross-domain
- claim: "Aggregate metrics hide per-segment structure — a good average can mask systematically failing segments."
  certainty: high
  evidence: Fairness and robustness evaluation research
  scope: cross-domain
- claim: "The metric must match the deployment loss — a mismatch between evaluation metric and real cost produces harmful optimization."
  certainty: high
  evidence: Objective mismatch research, Goodhart's law applications
  scope: cross-domain

## Relationships
- concept: benchmark-validity
  relationship: composes
  description: "Metric selection composes with benchmark validity — the metric is part of the measurement instrument."
- concept: generalization
  relationship: estimates
  description: "Metric selection shapes generalization estimates — different metrics report different faces of generalization."
- concept: confidence-calibration
  relationship: evaluates
  description: "Metric selection evaluates calibration — calibration metrics are a deliberate choice, not a default."
- concept: distribution-shift
  relationship: masks
  description: "Aggregate metric selection masks distribution shift — good averages hide segment degradation."
- concept: human-evaluation
  relationship: contrasts_with
  description: "Metric selection contrasts with human evaluation — automated metrics substitute for judgement only where validated."
- concept: alignment
  relationship: expresses_objectives
  description: "Metric selection expresses objectives — the chosen metric operationalizes what alignment means to optimize."

## Tradeoffs
- dimension: aggregate_vs_segmented_metrics
  options:
    aggregate:
      value: simplicity
      rationale: "Single numbers are comparable and communicable but hide failing segments."
    segmented:
      value: fidelity
      rationale: "Per-segment metrics reveal structure but multiply reporting complexity."
  importance: high
- dimension: precision_vs_recall
  options:
    precision_optimised:
      value: false_positive_avoidance
      rationale: "Optimizing precision minimizes false alarms at the cost of missed positives."
    recall_optimised:
      value: false_negative_avoidance
      rationale: "Optimizing recall minimizes missed positives at the cost of false alarms."
  importance: high

## Failure Modes
- name: metric_mismatch
  description: "The evaluation metric diverges from the deployment objective — the model optimizes what is measured, not what matters."
  likelihood: high
  observable_evidence: "Good evaluation scores with poor realized outcomes; teams optimizing measured proxies that harm real objectives"
  detection: "Objective-usage mapping; realized-vs-measured outcome comparison"
  recovery: "Derive metrics from deployment loss; validate metric against realized cost"
  retryable: true
- name: aggregate_mask
  description: "Aggregate metrics conceal segment failures — small high-risk segments fail inside good averages."
  likelihood: high
  observable_evidence: "Good overall scores with concentrated failure segments; complaints from segment users; bias discovered later"
  detection: "Segment-level reporting; failure concentration analysis"
  recovery: "Require segment breakdowns; gate on worst-segment performance"
  retryable: true
- name: metric_chasing
  description: "The metric itself becomes the target — the model is tuned to the metric rather than the capability, and gains stop transferring."
  likelihood: medium
  observable_evidence: "Metric gains without task gains; evaluation overfitting; declining fresh-data performance"
  detection: "Fresh-data validation; metric-capability correlation checks"
  recovery: "Rotate or diversify metrics; validate on untouched data; penalize evaluation overfitting"
  retryable: true

## Observations
- observation: "Leaderboard metrics frequently diverge from deployment-relevant measures."
  confidence: high
  source: Evaluation comparisons, deployment studies
- observation: "Accuracy masks rare-class failures in many production systems."
  confidence: high
  source: Imbalanced learning research, incident analyses
- observation: "Changing the metric can reverse evaluation conclusions about which model is better."
  confidence: high
  source: Evaluation methodology studies

## Constraints
- constraint: "A metric is evidence only about the property it measures."
  type: invariant
  scope: cross-domain
- constraint: "Evaluation must not be tuned to the metric — optimizing the measurement corrupts the measurement."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: deployment_objective_match
  question: "Does the metric reflect the deployment loss the system will actually incur?"
  supporting: "Metrics derived from the deployment objective align optimization with realized outcomes."
  contradictory: "Metrics chosen by convention ignore the real cost structure and optimize the wrong thing."
  weight: high
- factor: error_type_cost
  question: "Which error type — false positive or false negative — is costlier in deployment?"
  supporting: "Precision-prioritizing metrics are correct when false positives are the costly error."
  contradictory: "Recall-prioritizing metrics are correct when misses are the costly error."
  weight: high
- factor: segment_sensitivity
  question: "Can segment failures hide inside the aggregate metric?"
  supporting: "Segmented metrics are required when failure concentration across segments is plausible."
  contradictory: "Aggregates suffice when segments are homogeneous and equally covered."
  weight: medium

## Heuristics
- heuristic: "Select metrics from the deployment loss, not from convention."
  rationale: "The deployment objective defines what should be measured."
  evidence_level: high
- heuristic: "Always pair aggregate metrics with segment breakdowns."
  rationale: "Averages are where failures hide."
  evidence_level: high
- heuristic: "Treat metric choice as a documented decision, not a default."
  rationale: "Documented choices are auditable; defaults encode unexamined assumptions."
  evidence_level: high

## Recommendations
- recommendation: "Define evaluation metrics from the deployment objective and the cost of each error type."
  context: evaluation_design
  certainty: strong
  rationale: "Metric-objective match is the precondition for optimization to improve outcomes."
- recommendation: "Report segment-level performance alongside every aggregate metric."
  context: reporting
  certainty: strong
  rationale: "Segments are where silent failures concentrate."
- recommendation: "Document the rationale for every selected metric, including what it excludes."
  context: governance
  certainty: strong
  rationale: "Documentation exposes the tradeoff choices encoded in measurement."

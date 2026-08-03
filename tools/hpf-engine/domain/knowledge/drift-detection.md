# Drift Detection

## Identity
- id: drift-detection
- type: pattern
- title: Drift Detection
- tags: [machine learning, drift detection, monitoring, reference distribution, PSI, statistical tests, alerting]
- entities: [drift detection, drift metric, reference distribution, PSI, KS test, alert threshold]
- concepts: [distribution-shift, model-monitoring, retraining-decisions, confidence-calibration, training-data, generalization]

## Claims
- claim: "Drift detection is the practice of measuring divergence between a reference and current distribution — it converts 'the world changed' into measurable evidence."
  certainty: high
  evidence: Drift detection literature, ML operations practice
  scope: cross-domain
- claim: "Drift detection must distinguish signal from routine fluctuation — statistical tests require severity thresholds to mean anything."
  certainty: high
  evidence: Statistical process control, drift research
  scope: cross-domain
- claim: "Drift detection is only useful when tied to response — detection without a decision channel is noise."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain
- claim: "Detection methods trade sensitivity against noise tolerance — no method detects all real shift without some false alarms."
  certainty: high
  evidence: Drift detection method comparisons
  scope: cross-domain
- claim: "Drift detection evidence decays — thresholds and reference windows age as the world moves."
  certainty: high
  evidence: Monitoring practice
  scope: cross-domain

## Relationships
- concept: distribution-shift
  relationship: measures
  description: "Drift detection measures distribution shift — the metric is the measurable face of shift."
- concept: model-monitoring
  relationship: composes
  description: "Drift detection composes with model monitoring — drift metrics are a monitoring channel."
- concept: retraining-decisions
  relationship: triggers
  description: "Drift detection triggers retraining decisions — verified drift is the evidence-based trigger."
- concept: confidence-calibration
  relationship: protects
  description: "Drift detection protects calibration — early detection prevents prolonged miscalibration."
- concept: training-data
  relationship: references
  description: "Drift detection references training data — the reference distribution comes from training."
- concept: generalization
  relationship: guards
  description: "Drift detection guards generalization — detecting shift preserves the validity boundary of generalization claims."

## Tradeoffs
- dimension: detection_sensitivity_vs_noise
  options:
    high_sensitivity:
      value: early_warning
      rationale: "Sensitive detection catches shift early but triggers on routine fluctuation."
    high_tolerance:
      value: stability
      rationale: "Tolerant detection avoids false alarms but misses early shift."
  importance: high
- dimension: statistical_vs_operational_signal
  options:
    statistical_methods:
      value: rigor
      rationale: "Statistical tests are principled but flag many practically irrelevant differences."
    operational_signals:
      value: relevance
      rationale: "Outcome-based signals are decision-relevant but react later than distribution tests."
  importance: medium

## Failure Modes
- name: silent_miss
  description: "Shift below the detection threshold degrades the model — the detector never fires."
  likelihood: high
  observable_evidence: "Gradual performance decline with no alerts; degradation concentrated in unmonitored segments"
  detection: "Threshold validation against realized degradation; segment-level detection"
  recovery: "Lower thresholds on decision-relevant dimensions; segment detection; outcome-coupled signals"
  retryable: true
- name: false_alarm_storms
  description: "Over-sensitive detection floods the response channel — every routine fluctuation triggers retraining."
  likelihood: high
  observable_evidence: "Frequent spurious alerts; retraining triggered by noise; alert fatigue"
  detection: "Alert-to-verified-shift ratio; retraining outcome analysis"
  recovery: "Raise severity thresholds; require confirmation metrics; couple alerts to decision cost"
  retryable: true
- name: reference_decay
  description: "The reference distribution ages — detection compares against a baseline the world has legitimately left."
  likelihood: medium
  observable_evidence: "Permanent alert state; detection meaningless against stale reference; confusion about baseline validity"
  detection: "Reference review; alert-state duration analysis"
  recovery: "Deliberately renew reference on verified regime change; document reference validity"
  retryable: true

## Observations
- observation: "Drift metrics lead visible performance decay — detection is possible before user-visible failure."
  confidence: high
  source: ML monitoring practice
- observation: "Common statistical tests (PSI, KS) flag many practically irrelevant differences in production."
  confidence: high
  source: Drift detection practice
- observation: "Most teams detect drift only after incidents, when monitoring is absent or untuned."
  confidence: high
  source: ML operations reviews

## Constraints
- constraint: "Drift detection is only meaningful against a fixed reference — a moving baseline cannot detect change."
  type: invariant
  scope: cross-domain
- constraint: "Detection without response capacity is noise — the detector and the decision channel must be designed together."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Fix the reference distribution and defend it — renewal is a deliberate decision, not an accident."
  rationale: "The reference defines what counts as drift."
  evidence_level: high
- heuristic: "Tie alert thresholds to retraining cost, not to statistical significance alone."
  rationale: "The threshold that matters is where response cost meets degradation cost."
  evidence_level: high
- heuristic: "Validate detection quality against realized degradation, not against test-set claims."
  rationale: "Detection evidence earns its trust from production outcomes."
  evidence_level: high

## Recommendations
- recommendation: "Detect drift at decision-relevant granularity — segments, not just global distributions."
  context: monitoring_design
  certainty: strong
  rationale: "Global detection hides the segments where degradation concentrates."
- recommendation: "Pair every drift detector with a response workflow — detection without response is noise."
  context: operations_design
  certainty: strong
  rationale: "The decision channel is what makes detection evidence."
- recommendation: "Renew the reference distribution deliberately on verified regime change, never on routine fluctuation."
  context: operational_ml
  certainty: strong
  rationale: "Reference decay silently destroys detection validity."

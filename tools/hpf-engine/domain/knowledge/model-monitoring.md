# Model Monitoring

## Identity
- id: model-monitoring
- type: pattern
- title: Model Monitoring
- tags: [machine learning, monitoring, observability, telemetry, production, degradation, MTTR]
- entities: [model monitoring, telemetry, observability, degradation detection, production metrics, alerting]
- concepts: [distribution-shift, confidence-calibration, uncertainty-estimation, retraining-decisions, deployment-risk, hallucination]

## Claims
- claim: "Model monitoring is the continuous observation of deployed model behaviour and its context — it is the evidence channel that keeps deployed knowledge valid."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain
- claim: "Monitoring detects degradation signals (performance, distribution, input anomalies) before users experience failure."
  certainty: high
  evidence: ML monitoring practice, incident analyses
  scope: cross-domain
- claim: "Monitoring is bounded by what is instrumented — unobserved dimensions degrade silently."
  certainty: high
  evidence: Observability practice, incident analyses
  scope: cross-domain
- claim: "Monitoring produces evidence for decisions (retraining, rollback, escalation) — its value is realized in the decisions it informs."
  certainty: high
  evidence: ML operations practice
  scope: cross-domain
- claim: "Monitoring is itself a system with failure modes — missing telemetry, alert fatigue, and stale thresholds degrade it silently."
  certainty: high
  evidence: Incident analysis of monitoring failures
  scope: cross-domain

## Relationships
- concept: distribution-shift
  relationship: detects
  description: "Model monitoring detects distribution shift — drift metrics are monitoring signals."
- concept: confidence-calibration
  relationship: tracks
  description: "Model monitoring tracks calibration — ongoing ECE measurement detects calibration decay."
- concept: uncertainty-estimation
  relationship: validates
  description: "Model monitoring validates uncertainty estimates — realized outcomes check estimated uncertainty."
- concept: retraining-decisions
  relationship: informs
  description: "Model monitoring informs retraining decisions — degradation evidence is the retraining trigger."
- concept: deployment-risk
  relationship: reduces
  description: "Model monitoring reduces deployment risk — observability converts unknown risk into managed risk."
- concept: hallucination
  relationship: detects
  description: "Model monitoring detects hallucination — production hallucination is a monitoring signal, not only a benchmark metric."

## Tradeoffs
- dimension: telemetry_coverage_vs_cost
  options:
    full_instrumentation:
      value: visibility
      rationale: "Complete telemetry sees every degradation dimension but costs storage, compute, and maintenance."
    essential_signals_only:
      value: efficiency
      rationale: "Minimal telemetry is cheap but leaves blind dimensions."
  importance: high
- dimension: alert_sensitivity_vs_fatigue
  options:
    high_sensitivity:
      value: early_detection
      rationale: "Sensitive alerts catch degradation early but flood operators with noise."
    high_thresholds:
      value: attention_preservation
      rationale: "High thresholds keep alerts meaningful but delay detection."
  importance: high

## Failure Modes
- name: telemetry_blindspot
  description: "Degradation occurs on an unmonitored dimension — the failure is invisible to the monitoring system."
  likelihood: high
  observable_evidence: "Incidents discovered by users, not monitoring; post-incident analysis reveals missing signals"
  detection: "Coverage audits against decision-relevant dimensions; incident retrospection"
  recovery: "Instrument decision-relevant dimensions; map telemetry to risk surface"
  retryable: true
- name: alert_fatigue
  description: "Alert volume exceeds operator capacity — genuine alerts drown in routine noise."
  likelihood: high
  observable_evidence: "Alerts ignored or auto-dismissed; long alert response times; genuine degradation missed in noise"
  detection: "Alert-to-action ratio; response time metrics; alert review"
  recovery: "Tune thresholds; tier alerts by severity; automate routine responses"
  retryable: true
- name: monitoring_drift
  description: "The monitoring system itself ages — thresholds, references, and alert logic go stale against the changing system."
  likelihood: medium
  observable_evidence: "Stale thresholds flagging nothing or everything; monitoring review backlog; alert logic referencing old behaviour"
  detection: "Monitoring system review; threshold validation against current behaviour"
  recovery: "Refresh thresholds on model update; periodic monitoring audit"
  retryable: true

## Observations
- observation: "Monitoring signals lead visible performance decay — degradation is detectable before users experience failure."
  confidence: high
  source: ML monitoring practice, incident analyses
- observation: "Most production incidents show pre-cursor signals in hindsight that were not instrumented."
  confidence: high
  source: Incident post-mortems
- observation: "Monitoring maturity correlates with reduced mean time to recovery."
  confidence: high
  source: ML operations surveys

## Constraints
- constraint: "A deployed model's validity cannot be assessed beyond what is monitored."
  type: invariant
  scope: cross-domain
- constraint: "Monitoring evidence is only as fresh as the last valid observation — stale telemetry is not evidence."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Instrument decision-relevant dimensions first — monitor what changes decisions."
  rationale: "Monitoring value is realized through decisions; coverage without decision relevance is noise."
  evidence_level: high
- heuristic: "Pair every alert threshold with a review date."
  rationale: "Thresholds age with the system; scheduled review prevents monitoring drift."
  evidence_level: high
- heuristic: "Treat the monitoring system as part of the system — test it, version it, review it."
  rationale: "An untested monitoring system is a false safety net."
  evidence_level: high

## Recommendations
- recommendation: "Instrument distribution, performance, and business outcome dimensions jointly."
  context: observability_design
  certainty: strong
  rationale: "Single-dimension monitoring misses the degradation patterns that matter."
- recommendation: "Refresh thresholds and references whenever the model is retrained or redeployed."
  context: operational_ml
  certainty: strong
  rationale: "Old monitoring logic invalidates the evidence channel for the new model."
- recommendation: "Make monitoring feed an explicit decision channel — alerts must map to actions."
  context: operations_design
  certainty: strong
  rationale: "Monitoring without a decision channel is noise."

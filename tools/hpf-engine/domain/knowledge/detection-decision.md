# Detection Decision

## Identity
- id: detection-decision
- type: decision
- title: Detection Decision on Incomplete Reconstruction
- tags: [detection, decision, artifact analysis, incomplete reconstruction, response, confidence]
- entities: [detection decision, detection call, respond decision, flag decision]
- concepts: [reconstruction-confidence, competing-hypotheses, incomplete-evidence, threat-detection, artifact]

## Claims
- claim: "The detection decision is whether the reconstruction supports acting on the artifact — a decision taken on claims whose ground truth is still withheld."
  certainty: high
  evidence: Adversarial analysis practice
  scope: cross-domain
- claim: "Detection decisions are made under incomplete reconstruction — the reading set is open, the intent claim is derived, and the decision is made anyway."
  certainty: high
  evidence: Decision practice under uncertainty
  scope: cross-domain
- claim: "The decision is qualified by the reconstruction's confidence — the decision-maker inherits the evidence chain's qualification, and the decision inherits the chain's limits."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "The detection decision prices what the reconstruction does not know — the decision's condition is openness, not completeness."
  certainty: high
  evidence: Decision analysis practice
  scope: cross-domain
- claim: "False negatives and false positives are asymmetric under concealment — the artifact was designed against detection, and the decision must price that design."
  certainty: high
  evidence: Concealment design analysis, detection practice
  scope: cross-domain

## Relationships
- concept: reconstruction-confidence
  relationship: qualified_by
  description: "The detection decision is qualified by reconstruction confidence — the decision inherits the chain's qualification."
- concept: competing-hypotheses
  relationship: informed_by
  description: "The detection decision is informed by competing hypotheses — the open reading set is the decision's evidence context."
- concept: incomplete-evidence
  relationship: constrained_by
  description: "The detection decision is constrained by incomplete evidence — the capture bounds what the decision can know."
- concept: threat-detection
  relationship: serves
  description: "The detection decision serves threat detection — the call is what detection becomes when it decides."
- concept: artifact
  relationship: applies_to
  description: "The detection decision applies to the artifact — the call is about the object under analysis."

## Tradeoffs
- dimension: detection_threshold_vs_alarm_load
  options:
    low_threshold:
      value: coverage
      rationale: "Low thresholds catch more but flood the analyst with false alarms."
    high_threshold:
      value: precision
      rationale: "High thresholds stay quiet but let concealed artifacts through."
  importance: high
- dimension: decision_speed_vs_reconstruction_completeness
  options:
    act_early:
      value: tempo
      rationale: "Early decisions respond while the artifact is still active."
    reconstruct_first:
      value: fidelity
      rationale: "Complete reconstructions decide better but decide late."
  importance: high

## Failure Modes
- name: detection_paralysis
  description: "The open reading set blocks the decision — the analyst waits for a reconstruction the artifact is designed to prevent."
  likelihood: medium
  observable_evidence: "Detection calls deferred past the decision window; 'we can't know yet' as a standing state"
  detection: "Decision-latency review; per-candidate resolution checks"
  recovery: "Time-box the reconstruction; decide with explicit residual qualification"
  retryable: true
- name: confidence_inheritance_error
  description: "The decision's qualification is not inherited — the decision-maker acts with more certainty than the chain supports."
  likelihood: high
  observable_evidence: "Decisive responses on weak chains; decisions more confident than their evidence; qualification dropped at the decision layer"
  detection: "Chain-to-decision audit; confidence consistency review"
  recovery: "Attach the chain's qualification to the decision; recalibrate"
  retryable: true
- name: concealment_priced_in_forgotten
  description: "The designed-against-detection factor is dropped — the decision prices ordinary risk but not the artifact's design intent."
  likelihood: medium
  observable_evidence: "Detection calls that treat the artifact as if it were not designed to evade; false negatives on concealed artifacts"
  detection: "Design-state review; factor-completeness audit"
  recovery: "Include the concealment design in the decision's evidence; re-run the decision"
  retryable: true

## Observations
- observation: "The decision's openness is carried in its factors — the open reconstruction is priced factor by factor, and the record shows the incompleteness with the call."
  confidence: high
  source: Decision analysis practice
- observation: "The decision inherits the chain's limits — the reconstruction's qualification is the decision's qualification, and losing it at the decision layer is the characteristic failure."
  confidence: high
  source: Decision analysis practice
- observation: "Concealment is priced as decision content — the designed-against-detection asymmetry is carried inside the decision's own factors."
  confidence: high
  source: Decision analysis practice

## Constraints
- constraint: "A detection decision inherits its evidence chain's qualification — the decision cannot be more certain than the reconstruction it stands on."
  type: invariant
  scope: cross-domain
- constraint: "The concealment design is part of the detection decision's evidence — the artifact was designed against being caught, and the decision prices it."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: reconstruction_confidence
  question: "What is the confidence in the reconstruction this decision depends on?"
  supporting: "Calibrated reconstruction confidence justifies decisive detection."
  contradictory: "Uncalibrated confidence justifies nothing the chain does not carry."
  weight: high
- factor: concealment_design
  question: "How strongly was the artifact designed against detection?"
  supporting: "Concealment analysis prices the asymmetry between false negatives and false positives."
  contradictory: "Ignoring the concealment design prices the artifact as if it were not designed."
  weight: high
- factor: decision_window
  question: "What does delaying the decision cost versus what does deciding early cost?"
  supporting: "Window analysis time-boxes reconstruction against the artifact's activity."
  contradictory: "Decisions past the window are decisions about a past artifact."
  weight: high
- factor: false_positive_stakes
  question: "What does a false positive detection cost the organisation?"
  supporting: "Visible false-positive costs discipline the threshold."
  contradictory: "Invisible false-positive costs inflate the threshold toward false negatives."
  weight: high

## Heuristics
- heuristic: "Decide with the chain's qualification attached."
  rationale: "The decision inherits the chain; dropping the inheritance is the failure."
  evidence_level: high
- heuristic: "Price the concealment design in every detection call."
  rationale: "The artifact was built to evade; evasiveness is evidence."
  evidence_level: high

## Recommendations
- recommendation: "Record the reconstruction's openness with every detection call."
  context: analysis
  certainty: strong
  rationale: "The decision inherits the chain; recording its openness keeps the inheritance honest."
- recommendation: "Attach the evidence chain's qualification to every detection decision."
  context: operations
  certainty: strong
  rationale: "Carrying the chain's confidence into the decision is the discipline."
- recommendation: "Time-box reconstruction against the decision window."
  context: operations
  certainty: strong
  rationale: "The artifact is designed to outlast patience; the window is part of the decision."

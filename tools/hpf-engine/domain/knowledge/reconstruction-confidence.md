# Reconstruction Confidence

## Identity
- id: reconstruction-confidence
- type: concept
- title: Reconstruction Confidence
- tags: [confidence, reconstruction, interpretation, artifact analysis, qualification, inference]
- entities: [reconstruction confidence, interpretive confidence, confidence in a reading, reconstruction certainty]
- concepts: [confidence, inference-from-behavior, competing-hypotheses, belief-state, probabilistic-outputs]

## Claims
- claim: "Confidence in a reconstruction is confidence attached to an interpretation of an inference — the claim in the analysis furthest removed from direct observation."
  certainty: high
  evidence: Analysis methodology
  scope: cross-domain
- claim: "Confidence in a reading must reflect the inference's distance, not the analyst's fluency — the longer the evidential chain, the harder honest confidence must work."
  certainty: high
  evidence: Calibration practice, cognitive bias research
  scope: cross-domain
- claim: "Confidence in a reading and confidence in an observation are anchored differently — conflating them is the analysis's characteristic corruption."
  certainty: high
  evidence: Calibration practice, analysis methodology
  scope: cross-domain
- claim: "The object of confidence in a reconstruction is the reading, never the artifact's hidden nature — the analyst is confident about a claim, and the claim is about the artifact."
  certainty: high
  evidence: Claim-audit discipline, analysis methodology
  scope: cross-domain
- claim: "Overconfidence is the reconstruction's characteristic failure — fluency is the analyst's most convincing substitute for evidence."
  certainty: high
  evidence: Calibration research, overconfidence case studies
  scope: cross-domain

## Relationships
- concept: confidence
  relationship: anchored_in
  description: "Reconstruction confidence is anchored in confidence — the same confidence discipline covers observations and readings."
- concept: inference-from-behavior
  relationship: qualifies
  description: "Reconstruction confidence qualifies behavioural inference — the reading carries the confidence."
- concept: competing-hypotheses
  relationship: applies_to
  description: "Reconstruction confidence applies to the reading set — each candidate carries its own qualification."
- concept: belief-state
  relationship: analogous_to
  description: "Reconstruction confidence is analogous to belief-state confidence — confidence grows the more inferential steps the claim stands from direct observation, and both fail by overconfidence."
- concept: probabilistic-outputs
  relationship: analogous_to
  description: "Reconstruction confidence is analogous to probabilistic outputs — both are estimates of truth-bearing over uncertain evidence, and both must be calibrated against evidence."

## Tradeoffs
- dimension: decisive_reconstruction_vs_honest_confidence
  options:
    decisive_reading:
      value: actionability
      rationale: "Decisive reconstructions act with force but risk acting on overconfidence."
    honest_confidence:
      value: calibration
      rationale: "Honest confidence stays calibrated but reads as indecisive."
  importance: high
- dimension: confidence_in_readings_vs_confidence_in_evidence
  options:
    reading_focused:
      value: conclusion
      rationale: "Reading-focused confidence makes the conclusion's strength visible."
    evidence_focused:
      value: foundation
      rationale: "Evidence-focused confidence keeps the analyst honest about the base."
  importance: high

## Failure Modes
- name: fluency_overconfidence
  description: "The analyst's confidence tracks the smoothness of the reading rather than the strength of its evidence — the reading is fluent, confident, and ungrounded."
  likelihood: high
  observable_evidence: "Confident reconstructions on thin evidence; fluency correlating with certainty; over-read analyses"
  detection: "Calibration audits; evidence-to-confidence matching; second-reader review"
  recovery: "Re-anchor confidence in evidence; widen the reading set; treat fluency as a bias flag"
  retryable: true
- name: confidence_destination_confusion
  description: "The analyst qualifies the wrong object — confidence about the evidence is recorded as confidence about the reading, or worse, about the artifact."
  likelihood: medium
  observable_evidence: "Records where evidence strength and reading confidence are conflated; claims whose confidence outruns their cited evidence"
  detection: "Claim-audit discipline; per-claim evidence-to-confidence mapping"
  recovery: "Attach each confidence to its claim; separate evidence quality from reading confidence"
  retryable: true
- name: underconfidence
  description: "Confidence never rises with evidence — the analyst remains tentative long after the record discriminates."
  likelihood: medium
  observable_evidence: "Fully discriminative evidence met with persistent hedging; conclusions deferred past their evidence"
  detection: "Confidence-vs-discrimination review; decision latency"
  recovery: "Raise confidence with the evidence; re-run calibration"
  retryable: true

## Observations
- observation: "Confidence attaches to claims at three positions on the evidential chain — to an observation, to a belief, to an interpretation of an inference — each written as certainty on a claim."
  confidence: high
  source: Calibration practice, analysis methodology
- observation: "Observation-anchored and interpretation-anchored confidence differ in what the claim states and what the evidence supports — the distinction lives in the record itself."
  confidence: high
  source: Calibration practice, analysis methodology
- observation: "Fluency is the reconstruction's overconfidence engine — the analyst's confidence is measured by how well the story reads, not by how well it is supported."
  confidence: high
  source: Calibration research, analysis practice
- observation: "The interpretation-anchored claim is where the analyst's knowledge finally matches the modelled system's — both are qualified claims about an unobserved truth."
  confidence: high
  source: Epistemic symmetry observation

## Constraints
- constraint: "Confidence qualifies the claim it is attached to — the object of reconstruction confidence is the reading, never the artifact's hidden nature."
  type: invariant
  scope: cross-domain
- constraint: "Fluency is not confidence — confidence is calibrated to evidence strength, and a reading's smoothness is never grounds for it."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Anchor every reconstruction confidence to its evidence, never to its fluency."
  rationale: "Fluency is the analyst's property; evidence is the claim's."
  evidence_level: high
- heuristic: "Separate what is observed from what is inferred in every confidence statement."
  rationale: "Separating the observed from the inferred keeps confidence honest; conflating them is the failure."
  evidence_level: high

## Recommendations
- recommendation: "Record reconstruction confidence in the same form as any claim confidence — a reading gets no special scale."
  context: modelling
  certainty: strong
  rationale: "Separate scales break comparability — the reading's confidence must sit on the same record as the evidence it rests on."
- recommendation: "Record confidence destination explicitly — say what the confidence is about."
  context: analysis
  certainty: strong
  rationale: "Destination confusion is the quiet corruptor of reconstruction records."
- recommendation: "Calibrate interpretation-anchored confidence against evidence strength before acting on it."
  context: analysis
  certainty: strong
  rationale: "Overconfident readings are the reconstruction's signature failure — the same failure belief-state analysis records."

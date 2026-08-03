# Inference from Behaviour

## Identity
- id: inference-from-behavior
- type: concept
- title: Inference from Behaviour
- tags: [inference, behaviour, artifact analysis, interpretation, semantics, evidence]
- entities: [inference from behaviour, behavioural inference, reading, interpretation step, what the artifact does]
- concepts: [artifact, behavioral-observation, surface-ambiguity, observable-evidence, belief-state, perception-uncertainty]

## Claims
- claim: "Inferring what the artifact does from what it is observed doing is an inference step — behaviour is evidence, and the step from evidence to function is never given by the evidence itself."
  certainty: high
  evidence: Behavioural analysis methodology
  scope: cross-domain
- claim: "The inference is a claim about the artifact one inference beyond the observation it is built on."
  certainty: high
  evidence: Behavioural analysis methodology
  scope: cross-domain
- claim: "Every behavioural inference is conditional — it holds only under the observation conditions that produced its evidence."
  certainty: high
  evidence: Behavioural analysis practice; conditionality of observation
  scope: cross-domain
- claim: "The same behaviour supports multiple inferences — behavioural evidence underdetermines function, exactly as the surface does."
  certainty: high
  evidence: Competing-hypothesis practice in analysis
  scope: cross-domain
- claim: "Inference quality is a function of evidence, not of fluency — a smooth reading is not a grounded reading."
  certainty: high
  evidence: Cognitive bias research, analysis practice
  scope: cross-domain

## Relationships
- concept: behavioral-observation
  relationship: derived_from
  description: "Inference from behaviour is derived from behavioural observation — the trace is the inference's evidence."
- concept: artifact
  relationship: describes
  description: "Inference from behaviour describes the artifact — the reading is a claim about what the artifact does."
- concept: surface-ambiguity
  relationship: constrained_by
  description: "Inference from behaviour is constrained by surface ambiguity — the reading cannot outrun the gap between surface and semantics."
- concept: observable-evidence
  relationship: based_on
  description: "Inference from behaviour is based on observable evidence — the record bounds every reading."
- concept: belief-state
  relationship: analogous_to
  description: "Inference from behaviour is analogous to belief state — an internal model of an unobserved truth, carried by confidence."
- concept: perception-uncertainty
  relationship: subject_to
  description: "Inference from behaviour is subject to perception uncertainty — the observer's instrument limits what the evidence can carry."

## Tradeoffs
- dimension: inferential_reach_vs_confidence
  options:
    deep_reading:
      value: insight
      rationale: "Deep readings reach the artifact's function sooner but stand on weaker evidence."
    shallow_reading:
      value: honesty
      rationale: "Shallow readings stay close to the evidence but leave function unknown."
  importance: high
- dimension: single_reading_vs_reading_set
  options:
    committed_reading:
      value: actionability
      rationale: "A single committed reading is actionable but risks being the wrong one."
    reading_set:
      value: fidelity
      rationale: "A reading set stays faithful to the evidence but delays conclusions."
  importance: high

## Failure Modes
- name: over_interpretation
  description: "The reading exceeds its evidence — confidence in the inference is higher than the observation supports."
  likelihood: high
  observable_evidence: "Smooth confident readings on thin evidence; conclusions that outrun the trace; fluency mistaken for grounding"
  detection: "Evidence-to-claim audits; per-claim evidence checks; second-reader review"
  recovery: "Demote the reading to its evidence; qualify by what the observation could support"
  retryable: true
- name: under_inference
  description: "The analyst stops at the evidence — the reading is never made and the artifact's function stays unclaimed."
  likelihood: medium
  observable_evidence: "Records of behaviour without any reading; analysis that documents but never concludes"
  detection: "Conclusion-completeness review; per-object claim coverage"
  recovery: "Force the reading explicitly with its qualification"
  retryable: true
- name: circular_inference
  description: "The conclusion is built on the reading it is meant to support — the inference's own output becomes its input."
  likelihood: medium
  observable_evidence: "Readings justified by earlier readings of the same evidence; conclusions that reference themselves"
  detection: "Evidence-source review; claim-dependency mapping"
  recovery: "Ground each inference in observation; mark derived claims as derived"
  retryable: true

## Observations
- observation: "Inference from behaviour is the first claim whose inferential gap is structural — the analyst now states what the artifact does, having seen only what it did."
  confidence: high
  source: Behavioural analysis methodology
- observation: "Fluency tracks with wrongness — the smoothest reading is often the over-read one."
  confidence: high
  source: Cognitive bias research
- observation: "The inference step is where the analyst's own knowledge enters the chain — this is the point at which the modeler's position matches the modelled system's."
  confidence: high
  source: Analysis practice

## Constraints
- constraint: "A behavioural inference is valid only under the observation it is derived from — the reading inherits the trace's conditions."
  type: invariant
  scope: cross-domain
- constraint: "The inference never closes the surface/semantics gap by itself — a reading is a claim, not a fact."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Mark derived claims as derived — every reading cites the observation it stands on."
  rationale: "Derivation discipline keeps the inferential gap visible."
  evidence_level: high
- heuristic: "Distrust fluent readings on thin evidence."
  rationale: "Fluency is a property of the analyst, not of the evidence."
  evidence_level: high

## Recommendations
- recommendation: "Mark every behaviour→function reading as derived — the reading stands one step beyond its observation."
  context: analysis
  certainty: strong
  rationale: "Derivation discipline keeps the inferential gap visible."
- recommendation: "Ground every reading in its observation and record the conditions."
  context: analysis
  certainty: strong
  rationale: "Derived claims without their evidence are circular claims."
- recommendation: "Keep the reading set open until evidence discriminates."
  context: analysis
  certainty: strong
  rationale: "Underdetermination is the rule; premature commitment is the failure."

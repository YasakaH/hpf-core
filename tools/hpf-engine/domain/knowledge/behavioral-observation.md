# Behavioural Observation

## Identity
- id: behavioral-observation
- type: concept
- title: Behavioural Observation of Artifacts
- tags: [observation, behaviour, artifact analysis, execution trace, telemetry, evidence]
- entities: [behavioural observation, execution trace, behavioural log, activity sequence, monitored behaviour]
- concepts: [artifact, observable-evidence, threat-detection, perception-uncertainty, incomplete-evidence]

## Claims
- claim: "Behavioural observation is the record of what an artifact does when executed or engaged — the action sequence is the analyst's primary window on the artifact."
  certainty: high
  evidence: Malware analysis and sandboxing practice
  scope: cross-domain
- claim: "Behaviour is observed, not read — an execution trace is a sequence of recorded actions, and interpretation of the sequence is a separate step."
  certainty: high
  evidence: Behavioural analysis methodology
  scope: cross-domain
- claim: "Observed behaviour is conditional — the same artifact behaves differently across environments, inputs, and conditions of observation."
  certainty: high
  evidence: Sandboxing and behavioural analysis practice
  scope: cross-domain
- claim: "Observation changes the observed — an artifact aware of being watched may behave differently than one that is not."
  certainty: high
  evidence: Anti-analysis practice; observer-effect in instrumented execution
  scope: cross-domain
- claim: "A behavioural record is a sequence of recorded actions — individual events compose into the behaviour."
  certainty: high
  evidence: Event-level logging and trace analysis practice
  scope: cross-domain

## Relationships
- concept: artifact
  relationship: describes
  description: "Behavioural observation describes the artifact — behaviour is the artifact in action."
- concept: observable-evidence
  relationship: produces
  description: "Behavioural observation produces observable evidence — the trace becomes the record."
- concept: threat-detection
  relationship: feeds
  description: "Behavioural observation feeds threat detection — observed behaviour is what detection telemetry looks for."
- concept: perception-uncertainty
  relationship: constrained_by
  description: "Behavioural observation is constrained by perception uncertainty — the observer's instrumentation has its own limits and blind spots."
- concept: incomplete-evidence
  relationship: subject_to
  description: "Behavioural observation is subject to incomplete evidence — the capture may miss phases of behaviour entirely."

## Tradeoffs
- dimension: capture_breadth_vs_capture_fidelity
  options:
    broad_capture:
      value: completeness
      rationale: "Wide capture records more behaviour phases but degrades fidelity and volume of noise."
    deep_capture:
      value: clarity
      rationale: "Focused capture produces clean high-fidelity records but can miss behaviour outside the focus."
  importance: high
- dimension: instrumented_vs_natural_environment
  options:
    instrumented:
      value: observability
      rationale: "Instrumented environments make behaviour visible but are detectable and change it."
    natural_environment:
      value: authenticity
      rationale: "Natural environments produce authentic behaviour but hide it from the observer."
  importance: high

## Failure Modes
- name: observation_bias
  description: "The analyst sees what the instrumentation watches — behaviour outside the instrumented surface is invisible to the record."
  likelihood: high
  observable_evidence: "Trace records that systematically miss behaviour classes; conclusions shaped by what was measured"
  detection: "Instrumentation coverage review; comparison against independent observation channels"
  recovery: "Map instrumented vs uninstrumented surface; qualify claims by what the capture could see"
  retryable: true
- name: observation_condition_dependence
  description: "Behaviour recorded under one condition is treated as behaviour under all conditions — the record inherits its environment."
  likelihood: high
  observable_evidence: "Behaviour observed in the sandbox that never occurs in the wild; environment-specific action patterns"
  detection: "Multi-environment capture; condition recording with each trace"
  recovery: "Record environment conditions as qualification on the observation; re-run under alternative conditions"
  retryable: true
- name: instrumentation_interference
  description: "The instrument changes what it measures — hooks, breakpoints, and monitors that the artifact detects and evades."
  likelihood: medium
  observable_evidence: "Clean traces of apparently benign behaviour on known-malicious artifacts; artifacts that stall or exit when instrumented"
  detection: "Cross-instrument comparison; detection-of-instrumentation checks"
  recovery: "Use less detectable instrumentation; treat instrumented traces as confidence-qualified"
  retryable: true

## Observations
- observation: "Behavioural observation is the least contested evidence in artifact analysis — the record is factual even when its meaning is not."
  confidence: high
  source: Behavioural analysis methodology
- observation: "The conditionality of behaviour is the analyst's permanent problem — every trace answers 'under what conditions was this seen?', not 'what is this artifact?'."
  confidence: high
  source: Sandboxing practice
- observation: "Observation bias compounds downstream — the trace is the evidence, and its blind spots become the analysis's blind spots."
  confidence: high
  source: Instrumentation coverage practice
- observation: "The observer effect is measurable — artifacts behave differently when they detect the observer, and the difference is itself evidence."
  confidence: high
  source: Anti-analysis practice observations

## Constraints
- constraint: "A behavioural record is valid only under its observation conditions — environment, instrumentation, and inputs are part of the record."
  type: invariant
  scope: cross-domain
- constraint: "Observation does not exhaust behaviour — unobserved phases are unknown, not absent."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Record conditions with every trace — an observation without its environment is unqualified."
  rationale: "Conditionality is intrinsic to behaviour; a trace answers a conditional question."
  evidence_level: high
- heuristic: "Treat instrumented observation as qualified observation — the instrument is part of the evidence."
  rationale: "Observation changes the observed; declaring the instrumentation keeps the change visible."
  evidence_level: high

## Recommendations
- recommendation: "Record behaviour at event granularity — a trace is a sequence of atomic actions."
  context: analysis
  certainty: strong
  rationale: "Event-level records are re-analysable; behaviour summaries are not."
- recommendation: "Cross-check behaviour across observation conditions before drawing conclusions."
  context: analysis
  certainty: strong
  rationale: "Single-condition traces conflate the artifact with its environment."
- recommendation: "Qualify every behavioural claim by its capture conditions."
  context: analysis
  certainty: strong
  rationale: "The condition is part of the evidence; claims without it are overclaims."

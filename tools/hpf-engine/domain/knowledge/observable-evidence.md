# Observable Evidence

## Identity
- id: observable-evidence
- type: concept
- title: Observable Evidence from Artifacts
- tags: [evidence, observation, capture, provenance, artifact analysis, telemetry]
- entities: [observable evidence, captured signal, raw record, byte capture, timestamped event, evidence object]
- concepts: [artifact, behavioral-observation, confidence, incomplete-evidence, likelihood, threat-detection]

## Claims
- claim: "Observable evidence is the recorded signal the artifact yields — bytes, strings, hashes, timestamps, event sequences, and files touched, as captured."
  certainty: high
  evidence: Malware analysis and digital forensics practice
  scope: cross-domain
- claim: "Evidence records observation, not meaning — the same evidence record supports multiple interpretations, and interpretation is a separate step."
  certainty: high
  evidence: Evidence-based analysis methodology
  scope: cross-domain
- claim: "Evidence is qualified by its provenance — who captured it, how, when, and what was done to it between capture and analysis."
  certainty: high
  evidence: Digital forensics and evidence-handling practice
  scope: cross-domain
- claim: "The absence of recorded evidence is not evidence about the artifact — a clean capture is a statement about the capture, not about the artifact's behaviour."
  certainty: high
  evidence: Forensics practice; incomplete-evidence principles
  scope: cross-domain
- claim: "Evidence quality varies with capture conditions — contaminated, incomplete, or selection-biased captures degrade every claim built on them."
  certainty: high
  evidence: Evidence-handling standards, capture practice
  scope: cross-domain

## Relationships
- concept: behavioral-observation
  relationship: produced_by
  description: "Observable evidence is produced by behavioural observation — the trace becomes the record."
- concept: artifact
  relationship: originates_from
  description: "Observable evidence originates from the artifact — the signal comes from the captured object."
- concept: confidence
  relationship: qualified_by
  description: "Observable evidence is qualified by confidence — claims about its authenticity and provenance carry the qualification."
- concept: incomplete-evidence
  relationship: subject_to
  description: "Observable evidence is subject to incomplete evidence — the capture is a sample, never the whole artefact."
- concept: likelihood
  relationship: informs
  description: "Observable evidence informs likelihood — the record updates the estimate of what the artifact is."
- concept: threat-detection
  relationship: feeds
  description: "Observable evidence feeds threat detection — captured signals are what detection telemetry consumes."

## Tradeoffs
- dimension: capture_fidelity_vs_volume
  options:
    high_fidelity:
      value: precision
      rationale: "High-fidelity capture preserves detail but produces volume and slows analysis."
    selective_capture:
      value: tractability
      rationale: "Selective capture stays analysable but risks missing the detail that matters."
  importance: high
- dimension: evidence_preservation_vs_operational_use
  options:
    preserve_pristine:
      value: integrity
      rationale: "Pristine preservation keeps evidence admissible and re-analysable."
    use_in_analysis:
      value: progress
      rationale: "Working the evidence directly progresses analysis but consumes and contaminates it."
  importance: high

## Failure Modes
- name: contaminated_capture
  description: "The record includes what the analyst added — noise, instrumentation artifacts, or modification from handling the sample."
  likelihood: medium
  observable_evidence: "Records containing the analyst's own actions; hashes that change between captures; impossible event sequences"
  detection: "Capture-chain audit; working-copy discipline that isolates the pristine original"
  recovery: "Re-capture from the pristine original; record the contamination if re-capture is impossible"
  retryable: true
- name: provenance_loss
  description: "The chain of custody is broken — capture time, handler, method, or modification history is lost."
  likelihood: medium
  observable_evidence: "Missing custody records; undocumented modifications; unverifiable capture metadata"
  detection: "Chain-of-custody review; capture-time documentation discipline"
  recovery: "Record the provenance gap explicitly; qualify affected claims accordingly"
  retryable: false
- name: selection_bias_in_capture
  description: "What was captured is a sample chosen by the capture process — the record over-represents what the instrumentation noticed."
  likelihood: high
  observable_evidence: "Conclusion sets shaped by captured surfaces; evidence classes systematically absent from records"
  detection: "Coverage mapping of the capture process; comparison against independent channels"
  recovery: "Map the capture's selection surface; qualify conclusions by what the capture could see"
  retryable: true

## Observations
- observation: "The observable evidence is the only ground truth the analysis has — everything else in the cycle is inference built on this record."
  confidence: high
  source: Evidence-based analysis methodology
- observation: "Interpretation splits cleanly from the record — two analysts with the same evidence can hold different readings without disagreeing about the evidence."
  confidence: high
  source: Competing-hypothesis practice in analysis
- observation: "Provenance degrades first — the record survives analysis; the account of its capture rarely does."
  confidence: high
  source: Digital forensics practice
- observation: "Capture selection bias is the hidden driver of conclusions — what the instrumentation noticed shapes what the analysis concludes."
  confidence: high
  source: Telemetry coverage practice

## Constraints
- constraint: "Observable evidence records observation, not meaning — meaning is inference, never part of the record."
  type: invariant
  scope: cross-domain
- constraint: "A clean capture is evidence about the capture, not about the artifact — absence of signal is not absence of behaviour."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Separate the record from the reading — keep raw evidence intact and interpretations labelled as interpretations."
  rationale: "The record is re-analysable only if it survives its own analysis."
  evidence_level: high
- heuristic: "Document capture conditions as evidence, not as footnote."
  rationale: "Provenance is qualification; it belongs to the claim it supports."
  evidence_level: high

## Recommendations
- recommendation: "Treat provenance as part of the evidence — capture context qualifies every claim built on the record."
  context: analysis
  certainty: strong
  rationale: "Provenance is qualification; it belongs to the claim it supports."
- recommendation: "Preserve a pristine working copy and analyse the copy."
  context: operations
  certainty: strong
  rationale: "Contamination is irreversible; the pristine original is the recovery path."
- recommendation: "Record capture selection explicitly — what the capture could see is part of every conclusion built on it."
  context: analysis
  certainty: strong
  rationale: "Selection bias is the quiet driver of wrong conclusions."

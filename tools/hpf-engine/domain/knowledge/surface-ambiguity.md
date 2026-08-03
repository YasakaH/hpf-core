# Surface Ambiguity

## Identity
- id: surface-ambiguity
- type: concept
- title: Surface Ambiguity of Artifacts
- tags: [ambiguity, observable surface, artifact analysis, interpretation, hypotheses, concealment]
- entities: [surface ambiguity, observable ambiguity, ambiguous surface, surface compatibility, inconclusive observation]
- concepts: [artifact, observable-evidence, incomplete-evidence, confidence, threat-detection]

## Claims
- claim: "The observable surface of an artifact is ambiguous — the same surface is compatible with multiple candidate purposes, and the surface alone does not decide between them."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Ambiguity at the surface is often designed — concealment produces surfaces engineered to support plausible innocent readings."
  certainty: high
  evidence: Concealment and obfuscation practice
  scope: cross-domain
- claim: "Ambiguity is not resolved by more observation alone — additional surface evidence narrows, but the gap between surface and semantics is structural."
  certainty: high
  evidence: Analysis methodology; incompleteness of observational evidence
  scope: cross-domain
- claim: "Ambiguity is a property of the surface as perceived — the artifact is a single object; the plurality of readings lives in the evidence, not in the artifact."
  certainty: high
  evidence: Epistemic framing in analysis practice
  scope: cross-domain
- claim: "Premature commitment is the characteristic response to ambiguity — analysis that fixes one reading early trades correctness for closure."
  certainty: high
  evidence: Cognitive bias research, analysis practice
  scope: cross-domain

## Relationships
- concept: artifact
  relationship: characterises
  description: "Surface ambiguity characterises the artifact's presentation — the surface admits multiple readings."
- concept: observable-evidence
  relationship: constrained_by
  description: "Surface ambiguity is constrained by observable evidence — the record bounds which readings are plausible."
- concept: incomplete-evidence
  relationship: amplified_by
  description: "Surface ambiguity is amplified by incomplete evidence — the less the capture shows, the wider the readings."
- concept: confidence
  relationship: reduces
  description: "Surface ambiguity reduces confidence — ambiguous evidence cannot ground confident claims."
- concept: threat-detection
  relationship: blinds
  description: "Surface ambiguity blinds threat detection — artifacts that read as innocent evade the telemetry that looks for threats."

## Tradeoffs
- dimension: decisive_reading_vs_open_hypotheses
  options:
    commit_early:
      value: closure
      rationale: "Early commitment produces decisive analysis quickly but risks locking a wrong reading."
    hold_open:
      value: fidelity
      rationale: "Holding hypotheses open stays faithful to the evidence but delays resolution."
  importance: high
- dimension: surface_depth_vs_resolution_speed
  options:
    exhaustive_surface:
      value: coverage
      rationale: "Exhaustive surface work maximises what the surface yields but spends time the adversary also uses."
    resolve_quickly:
      value: tempo
      rationale: "Quick resolution reaches an answer faster but risks missing the clue on the surface."
  importance: high

## Failure Modes
- name: premature_commitment
  description: "The analysis fixes on the first plausible reading and interprets later evidence to fit it."
  likelihood: high
  observable_evidence: "Early verdicts that survive evidence contradicting them; analyses that stop collecting once a reading holds"
  detection: "Hypothesis-review discipline; second-reader checks; commitment timestamps"
  recovery: "Re-open the reading set; treat the committed reading as one candidate among several"
  retryable: true
- name: ambiguity_denial
  description: "The surface is treated as semantics — 'it looks like X' becomes 'it is X' without behavioural confirmation."
  likelihood: high
  observable_evidence: "Conclusions cited from surface inspection alone; metadata read as intent; surface spoofing accepted"
  detection: "Evidence-source audit; the surface/semantics distinction applied to every claim"
  recovery: "Demote surface-only claims to qualified observation; require behavioural confirmation"
  retryable: true
- name: hypothesis_paralysis
  description: "Awareness of ambiguity prevents resolution — the analyst waits for evidence that cannot distinguish the readings."
  likelihood: medium
  observable_evidence: "Open reading sets without resolution progress; 'we can't know' as a stopping state"
  detection: "Resolution-latency tracking; per-hypothesis evidence checklists"
  recovery: "Time-box resolution; document what evidence would decide; decide with explicit residual ambiguity"
  retryable: true

## Observations
- observation: "The surface/semantics gap is the central structural fact of artifact analysis — the reading is never given by the surface."
  confidence: high
  source: Adversarial artifact analysis practice
- observation: "Designed ambiguity is cheap for the designer — a plausible innocent surface costs less than robust concealment and works as often."
  confidence: high
  source: Concealment practice
- observation: "Premature commitment is the failure mode the analyst is most prone to — ambiguity invites closure."
  confidence: high
  source: Cognitive bias research
- observation: "Ambiguity lives in the evidence, not the artifact — the artifact is one object; the plurality of readings is epistemic."
  confidence: high
  source: Epistemic framing in analysis practice

## Constraints
- constraint: "The observable surface does not determine semantics — identical surfaces can serve different purposes, and this gap is structural."
  type: invariant
  scope: cross-domain
- constraint: "A claim grounded in the surface alone is a qualified observation, never a conclusion — surface-derived certainty is false certainty."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Hold the reading set open until behaviour confirms or eliminates readings."
  rationale: "Surface ambiguity is resolved by action, not by looking harder at the surface."
  evidence_level: high
- heuristic: "Treat surface-only conclusions as hypotheses, whatever their confidence."
  rationale: "The surface is presentation; presentation is authored."
  evidence_level: high

## Recommendations
- recommendation: "Treat the surface/semantics gap as structural — the gap is not closed by looking harder at the surface."
  context: analysis
  certainty: strong
  rationale: "Ambiguity is a property of evidence under concealment, resolved by behaviour, never by more surface inspection."
- recommendation: "Record candidate readings explicitly with the evidence that supports each."
  context: analysis
  certainty: strong
  rationale: "Explicit reading sets make commitment visible and revisable."
- recommendation: "Require behavioural confirmation before a reading becomes a claim."
  context: analysis
  certainty: strong
  rationale: "Surface-only claims are the spoofing failure's doorway."

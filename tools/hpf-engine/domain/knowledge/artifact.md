# Artifact Under Analysis

## Identity
- id: artifact
- type: concept
- title: Artifact Under Analysis
- tags: [artifact, analysis, reverse engineering, forensics, adversarial, observable surface]
- entities: [artifact, sample, specimen, captured object, binary, firmware, evidence object]
- concepts: [incomplete-evidence, attacker-capability, threat-detection, confidence, incident-response]

## Claims
- claim: "An artifact is a manufactured object whose provenance is suspect or unknown — a binary, firmware image, or captured device presented to analysis without a trusted account of what it is."
  certainty: high
  evidence: Malware analysis and digital forensics practice
  scope: cross-domain
- claim: "The artifact presents itself through two channels only: its observable surface and its behaviour — everything else about it is inference."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Artifacts of adversarial origin are deliberately separated from their own description — the thing itself is present; the account of what it does is withheld."
  certainty: high
  evidence: Obfuscation and concealment practice; adversarial engineering literature
  scope: cross-domain
- claim: "The artifact's true purpose is a property the analyst does not directly access — it exists in the design intent of an absent creator."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "An artifact is evidence — its legal and operational significance depends on preserved provenance, not on the analyst's reading of it."
  certainty: high
  evidence: Digital forensics practice, evidence-handling standards
  scope: cross-domain

## Relationships
- concept: incomplete-evidence
  relationship: constrained_by
  description: "Analysis of the artifact is constrained by incomplete evidence — the artifact reveals only what it permits to be observed."
- concept: attacker-capability
  relationship: describes
  description: "The artifact describes attacker capability in material form — what the attacker can build is present in what the artifact is."
- concept: threat-detection
  relationship: challenges
  description: "The artifact challenges threat detection — an artifact designed to evade observation defeats the telemetry that would catch it."
- concept: confidence
  relationship: requires
  description: "Claims about the artifact require confidence — every statement about it is qualified by the strength of the observation behind it."
- concept: incident-response
  relationship: informs
  description: "The artifact informs incident response — analysis of a captured object directs containment and eradication."

## Tradeoffs
- dimension: surface_triage_vs_deep_analysis
  options:
    surface_triage:
      value: speed
      rationale: "Surface triage answers 'is this worth investigating' quickly and cheaply."
    deep_analysis:
      value: fidelity
      rationale: "Deep analysis recovers the artifact's true behaviour but costs time the adversary also uses."
  importance: high
- dimension: engagement_depth_vs_observation_risk
  options:
    shallow_engagement:
      value: safety
      rationale: "Minimal engagement avoids detection by the artifact — sandboxes that are noticed are escaped."
    deep_engagement:
      value: insight
      rationale: "Deep engagement produces real behaviour, but observed artefacts may behave differently under observation."
  importance: high

## Failure Modes
- name: artifact_misidentification
  description: "The analyst treats the artifact as a known object it is not — the reading is confident and wrong."
  likelihood: medium
  observable_evidence: "Analysis conclusions contradicted by later behaviour; confident attribution that collapses under deeper inspection"
  detection: "Independent second reading; hypothesis discipline that does not lock a verdict"
  recovery: "Re-open the analysis; treat prior identification as one candidate among several"
  retryable: true
- name: surface_spoofing
  description: "The artifact presents a crafted surface that supports the conclusion the designer wanted — fake strings, fake metadata, misleading structure."
  likelihood: medium
  observable_evidence: "Surface clues that are 'too clean'; metadata that matches an innocent narrative exactly"
  detection: "Cross-check surface claims against behaviour; treat conveniently legible surfaces as suspect"
  recovery: "Move analysis to behaviour and semantics; never conclude from surface alone"
  retryable: true
- name: provenance_loss
  description: "The artifact's capture history is lost or contaminated — where it came from, who handled it, and what was done to it are unknown."
  likelihood: medium
  observable_evidence: "Missing custody records; samples modified in transit; unverifiable capture chain"
  detection: "Chain-of-custody review; capture-time documentation"
  recovery: "Re-capture if possible; if not, record the provenance gap as a qualification on every claim"
  retryable: false

## Observations
- observation: "The observable surface is the only part of the artifact the analyst can touch directly — everything else is recovered, never given."
  confidence: high
  source: Adversarial artifact analysis practice
- observation: "Artifacts designed against analysis treat the analyst as an adversary — their structure anticipates being read."
  confidence: high
  source: Obfuscation and concealment practice
- observation: "Provenance is the weakest link in the chain — the artifact's journey to the analyst is the most frequently lost information."
  confidence: high
  source: Digital forensics practice
- observation: "The artifact's designer and the analyst model each other — the artifact is the intersection of two analyses."
  confidence: high
  source: Adversarial analysis practice

## Constraints
- constraint: "The observable surface is not the semantics — an artifact's appearance never certifies what it does."
  type: invariant
  scope: cross-domain
- constraint: "Every claim about an artifact carries a provenance condition — claims without capture context are unqualified."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Conclude from behaviour, never from surface — surface is presentation, behaviour is action."
  rationale: "Presentation is authored by the adversary; behaviour is what the artifact actually does."
  evidence_level: high
- heuristic: "Treat conveniently legible surfaces as suspect."
  rationale: "An artifact that reads exactly like its cover story is often built to read exactly that way."
  evidence_level: medium

## Recommendations
- recommendation: "Separate the artifact from the account of it — record what is observed and what is inferred distinctly."
  context: analysis
  certainty: strong
  rationale: "The distinction is the discipline that prevents surface spoofing from becoming a false conclusion."
- recommendation: "Preserve provenance at capture time — the artifact's history is evidence about the artifact."
  context: operations
  certainty: strong
  rationale: "Provenance loss damages every downstream claim; capture context is captured evidence."
- recommendation: "Keep the surface/semantics distinction explicit in every analysis record."
  context: analysis
  certainty: strong
  rationale: "The distinction is the discipline that prevents surface spoofing from becoming a false conclusion."

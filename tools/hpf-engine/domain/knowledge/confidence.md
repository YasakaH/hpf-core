# Confidence

## Identity
- id: confidence
- type: concept
- title: Confidence in Security Judgement
- tags: [security, uncertainty, confidence, evidence, judgement, risk]
- entities: [confidence, certainty, evidence quality, judgement, uncertainty, epistemic confidence]
- concepts: [likelihood, incomplete-evidence, risk-acceptance, threat-detection]

## Claims
- claim: "Confidence is a property of a security judgement, not of the system being judged — it qualifies the quality of the evidence and reasoning behind a claim."
  certainty: high
  evidence: Security risk analysis literature, epistemic practice
  scope: cross-domain
- claim: "Confidence can be high even when certainty is low — a well-evidenced probabilistic judgement can carry high confidence in its own reliability."
  certainty: high
  evidence: Risk analysis literature, decision science
  scope: cross-domain
- claim: "Confidence degrades with evidence quality, evidence age, and conflicting signals — stale intelligence produces lower confidence conclusions."
  certainty: high
  evidence: Intelligence analysis literature (CIA analysis of competing hypotheses)
  scope: cross-domain
- claim: "Security decisions made without expressed confidence levels mask the true uncertainty of the underlying judgement."
  certainty: high
  evidence: Risk management literature, incident post-mortems
  scope: cross-domain
- claim: "Confidence is not transferable between contexts — high confidence in one environment does not imply high confidence in a different deployment."
  certainty: high
  evidence: Security assessment practice
  scope: cross-domain

## Relationships
- concept: likelihood
  relationship: qualifies
  description: "Confidence qualifies how reliable the likelihood estimate is — a likelihood without confidence is an assertion without epistemic grounding."
- concept: incomplete-evidence
  relationship: limited_by
  description: "Incomplete evidence reduces confidence — confidence should scale with evidence completeness."
- concept: risk-acceptance
  relationship: informs
  description: "Confidence in the risk assessment directly informs whether accepting the risk is defensible."
- concept: threat-detection
  relationship: affects
  description: "Confidence in detection results determines whether alerts are actioned or dismissed — low-confidence detections are frequently ignored."

## Tradeoffs
- dimension: confidence_threshold_vs_responsiveness
  options:
    high_threshold:
      value: accuracy
      rationale: "Only act on high-confidence judgements — fewer false actions but slower response to real threats."
    low_threshold:
      value: responsiveness
      rationale: "Act on lower-confidence judgements — faster response but more false positives and wasted effort."
  importance: high
- dimension: expressed_vs_implicit_confidence
  options:
    expressed:
      value: transparency
      rationale: "Explicit confidence levels expose uncertainty to decision makers and enable calibration."
    implicit:
      value: simplicity
      rationale: "Unstated confidence is simpler but hides the true reliability of the judgement."
  importance: high

## Failure Modes
- name: confidence_miscalibration
  description: "Confidence does not track actual judgement accuracy — overconfidence or underconfidence relative to the true reliability of the evidence."
  likelihood: high
  observable_evidence: "Repeated incorrect high-confidence judgements; surprise when confident assertions fail; team consistently surprised by incident outcomes"
  detection: "Calibration audits — compare expressed confidence with actual outcome accuracy over time"
  recovery: "Retrain on calibration data; require evidence-tying for high-confidence claims; second-opinion reviews"
  retryable: false
- name: confidence_paralysis
  description: "Decision makers refuse to act because no judgement reaches the required confidence threshold."
  likelihood: medium
  observable_evidence: "Delayed security actions; unresolved risk items; decisions deferred repeatedly pending 'more evidence'"
  detection: "Track decision latency; monitor risk item ageing; review meetings where no decision is reached"
  recovery: "Lower threshold for reversible actions; require explicit 'decide with current confidence' checkpoints; time-box evidence gathering"
  retryable: true
- name: false_confidence_transfer
  description: "Confidence from one context is incorrectly applied to a different context — a well-understood environment's confidence applied to an unfamiliar deployment."
  likelihood: medium
  observable_evidence: "Security assessments rely on experience from different environments; vulnerabilities dismissed because 'we've never seen this fail'"
  detection: "Peer review of security assessments; context audit of confidence rationale"
  recovery: "Require context-specific evidence for confidence claims; separate confidence statements from rationale"
  retryable: false

## Observations
- observation: "Security practitioners systematically overestimate their confidence in vulnerability assessments — calibration audits consistently show overconfidence."
  confidence: high
  source: Security research, calibration studies
- observation: "Confidence expressions in security reports ('likely', 'probably', 'may') are interpreted inconsistently by different readers."
  confidence: high
  source: Intelligence community research, communication studies
- observation: "Teams that explicitly calibrate confidence (tracking accuracy vs expressed confidence) improve judgement quality within months."
  confidence: medium
  source: Decision science literature, intelligence analysis practice

## Constraints
- constraint: "Confidence cannot exceed the quality of the underlying evidence — high confidence on weak evidence is a contradiction, not a judgement."
  type: invariant
  scope: cross-domain
- constraint: "Confidence is always time-bound — evidence ages, environments change, and confidence must decay accordingly."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Express confidence on a fixed scale (high/medium/low) with an explicit rationale — consistency enables calibration."
  rationale: "A fixed scale with rationale allows comparing judgements across time and teams."
  evidence_level: high
- heuristic: "Tie every high-confidence claim to specific evidence — untethered high confidence is assertion, not analysis."
  rationale: "High confidence is only useful if the decision maker can audit the evidence behind it."
  evidence_level: high
- heuristic: "Require the same confidence threshold for action as for inaction — most teams act asymmetrically."
  rationale: "Teams act quickly on high-confidence threats but also 'act' by ignoring low-confidence ones; both should meet the same bar."
  evidence_level: medium

## Recommendations
- recommendation: "Include an explicit confidence statement with rationale in every security risk assessment."
  context: security_assessment
  certainty: strong
  rationale: "Confidence with rationale makes uncertainty auditable and enables calibration over time."
- recommendation: "Audit confidence calibration quarterly — compare expressed confidence against actual outcomes."
  context: security_operations
  certainty: strong
  rationale: "Uncalibrated confidence is worse than no confidence because it creates false assurance."
- recommendation: "Act on high-impact low-confidence threats with reversible, low-cost mitigations rather than ignoring them."
  context: risk_management
  certainty: strong
  rationale: "Low confidence does not mean low impact — reversible mitigations capture the upside of responding without overcommitting."

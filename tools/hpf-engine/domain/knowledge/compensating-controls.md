# Compensating Controls

## Identity
- id: compensating-controls
- type: pattern
- title: Compensating Controls
- tags: [security, compensating controls, compliance, risk, mitigation, alternative controls]
- entities: [compensating control, alternative control, compensating measure, control substitution, mitigation alternative]
- concepts: [risk-acceptance, residual-risk, defense-in-depth, vulnerability-management, threat-detection]

## Claims
- claim: "A compensating control is an alternative control that reduces risk to an acceptable level when the required primary control cannot be implemented."
  certainty: high
  evidence: Compliance frameworks (PCI DSS, ISO 27001), security literature
  scope: cross-domain
- claim: "Compensation is valid only when the alternative control demonstrably achieves an equivalent or better risk reduction — intent alone is insufficient."
  certainty: high
  evidence: Compliance framework guidance, audit practice
  scope: cross-domain
- claim: "Compensating controls are accepted on the basis of effectiveness evidence, not equivalence of mechanism — the risk outcome must match, not the control type."
  certainty: high
  evidence: Compliance audit practice, risk management literature
  scope: cross-domain
- claim: "Compensation is distinct from acceptance — compensation actively reduces risk via an alternative; acceptance tolerates the residual without an alternative."
  certainty: high
  evidence: Risk management standards, compliance guidance
  scope: cross-domain
- claim: "Compensating controls are most defensible when paired with enhanced detection and monitoring of the compensated risk."
  certainty: high
  evidence: Audit practice, security operations literature
  scope: cross-domain

## Relationships
- concept: risk-acceptance
  relationship: distinguishes_from
  description: "Compensation actively reduces risk via an alternative control; acceptance tolerates residual risk without substitution."
- concept: residual-risk
  relationship: reduces
  description: "Compensating controls lower residual risk when primary controls cannot be implemented."
- concept: defense-in-depth
  relationship: contributes_to
  description: "Compensation contributes to depth by adding a control where the primary layer is absent."
- concept: vulnerability-management
  relationship: applies_to
  description: "Vulnerabilities without patches are the classic compensation scenario — compensating controls bridge the unpatched window."
- concept: threat-detection
  relationship: enhances
  description: "Detection enhancement is the most common compensating control — monitoring what cannot be prevented."

## Tradeoffs
- dimension: compensation_effectiveness_vs_equivalence_strictness
  options:
    outcome_based:
      value: flexibility
      rationale: "Accept any alternative that measurably reduces risk to an acceptable level — flexible, requires evidence."
    mechanism_based:
      value: certainty
      rationale: "Require the same class of control — certain equivalence but eliminates valid alternatives."
  importance: high
- dimension: permanent_vs_temporary_compensation
  options:
    temporary:
      value: remediation_path
      rationale: "Bridge a remediation window with a time-boxed alternative — clear accountability but expires."
    permanent:
      value: lasting_fit
      rationale: "Structural alternatives that remain long-term — stable but must be maintained indefinitely."
  importance: high

## Failure Modes
- name: cosmetic_compensation
  description: "A nominal alternative control is presented without evidence of equivalent risk reduction."
  likelihood: high
  observable_evidence: "Compensating controls lacking effectiveness evidence; audits rejecting compensation as cosmetic"
  detection: "Control evidence audit; effectiveness measurement review"
  recovery: "Require measurable effectiveness evidence; replace cosmetic controls with real alternatives"
  retryable: false
- name: compensation_decay
  description: "Compensating control degrades over time — monitoring gaps appear, the alternative control ages without maintenance."
  likelihood: high
  observable_evidence: "Compensated risk rising despite control present; control health metrics declining; no maintenance ownership"
  detection: "Compensation health monitoring; periodic effectiveness re-validation"
  recovery: "Assign maintenance ownership; re-validate effectiveness on schedule; escalate decaying compensations"
  retryable: true
- name: compensation_as_acceptance
  description: "A compensating control is claimed where no real alternative exists — the 'compensation' is actually acceptance in disguise."
  likelihood: medium
  observable_evidence: "Compensating controls that do not reduce risk; governance records showing compensation without effect"
  detection: "Effectiveness audit; risk reduction measurement comparison"
  recovery: "Reclassify as acceptance; pursue genuine alternatives; implement detection-only compensation if that is all that exists"
  retryable: false

## Observations
- observation: "Compensation quality is the most variable element of control frameworks — auditors see both rigorous alternatives and cosmetic substitutions."
  confidence: high
  source: Compliance audit practice, security assessment experience
- observation: "Detection-based compensation is the most widely accepted class — organisations compensate for unpreventable risk with monitoring."
  confidence: high
  source: Compliance practice, security operations
- observation: "Temporary compensations frequently become permanent — remediation windows slip and the 'temporary' control remains."
  confidence: high
  source: Audit findings, remediation tracking data

## Constraints
- constraint: "Compensation without effectiveness evidence is not compensation — it is a claim."
  type: invariant
  scope: cross-domain
- constraint: "Compensation cannot reduce risk below what the compensated exposure allows — some residual always remains."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Prefer detection-and-response compensation for unpreventable risks — monitoring is the most defensible alternative."
  rationale: "When prevention is impossible, detection and response bound the damage — the accepted compensation class."
  evidence_level: high
- heuristic: "Require measurable effectiveness evidence for every compensating control, reviewed on a schedule."
  rationale: "Effectiveness evidence is the line between compensation and cosmetics."
  evidence_level: high
- heuristic: "Time-box temporary compensation and escalate expiry — temporary controls that persist become orphaned risk."
  rationale: "Time-boxing forces remediation closure or deliberate reclassification."
  evidence_level: high

## Recommendations
- recommendation: "Document the risk-reduction evidence for every compensating control — the alternative must demonstrate outcome equivalence."
  context: control_governance
  certainty: strong
  rationale: "Effectiveness evidence is what distinguishes valid compensation from cosmetic substitution."
- recommendation: "Pair compensation with enhanced monitoring of the compensated risk — monitoring is both the control and the early warning."
  context: security_operations
  certainty: strong
  rationale: "Enhanced monitoring bounds the damage window of the compensated risk."
- recommendation: "Reclassify claimed compensations without evidence as risk acceptance — honest classification improves governance."
  context: risk_management
  certainty: strong
  rationale: "Misclassified compensation hides the true risk posture from governance."

# Residual Risk

## Identity
- id: residual-risk
- type: concept
- title: Residual Risk
- tags: [security, residual risk, risk management, risk treatment, risk analysis]
- entities: [residual risk, remaining risk, risk after mitigation, inherent risk, residual exposure]
- concepts: [risk-acceptance, likelihood, confidence, compensating-controls, defense-in-depth, vulnerability-management]

## Claims
- claim: "Residual risk is the risk that remains after risk treatment — mitigation reduces risk but rarely eliminates it."
  certainty: high
  evidence: Risk management standards (ISO 31000, NIST SP 800-30)
  scope: cross-domain
- claim: "Residual risk is the only risk that materially exists — inherent risk is a theoretical pre-mitigation quantity that no organisation actually operates under."
  certainty: high
  evidence: Risk management literature
  scope: cross-domain
- claim: "Residual risk is frequently unmeasured — organisations track mitigated risks and accepted risks but rarely the difference between them."
  certainty: high
  evidence: Risk governance audits, security assessment practice
  scope: cross-domain
- claim: "Residual risk is the true input to risk acceptance — acceptance decisions address residual risk, not inherent risk."
  certainty: high
  evidence: Risk management standards, governance literature
  scope: cross-domain
- claim: "Residual risk is time-variant — controls degrade, threats evolve, and the residual risk profile changes between assessments."
  certainty: high
  evidence: Risk management practice, audit findings
  scope: cross-domain

## Relationships
- concept: risk-acceptance
  relationship: addresses
  description: "Risk acceptance governs residual risk — acceptance is the decision to tolerate what remains after mitigation."
- concept: compensating-controls
  relationship: reduces
  description: "Compensating controls reduce residual risk further when primary controls are incomplete."
- concept: defense-in-depth
  relationship: reduces
  description: "Layered controls reduce residual risk by bounding the damage of any single control failure."
- concept: likelihood
  relationship: quantified_by
  description: "Residual risk is quantified from residual likelihood and impact — after-treatment estimates."
- concept: confidence
  relationship: required
  description: "Residual risk estimates carry confidence — the estimate quality determines acceptance defensibility."

## Tradeoffs
- dimension: residual_tracking_depth_vs_effort
  options:
    quantified_residual:
      value: decision_quality
      rationale: "Explicit residual risk estimates enable sound acceptance decisions but require assessment effort."
    residual_by_inference:
      value: efficiency
      rationale: "Inferring residual from mitigation records is cheaper but produces invisible assumptions."
  importance: high
- dimension: residual_reduction_vs_mitigation_cost
  options:
    push_lower:
      value: risk_reduction
      rationale: "Continue mitigation until residual is minimal — lower risk, higher cost."
    stabilise_at_tolerance:
      value: cost_balance
      rationale: "Mitigate to the tolerance boundary and accept the remainder — efficient but requires accurate estimation."
  importance: high

## Failure Modes
- name: residual_invisibility
  description: "Residual risk is never quantified — mitigation records exist but the remaining risk is unknown."
  likelihood: high
  observable_evidence: "Mitigation completed with no post-mitigation risk estimate; risk registers show pre-mitigation numbers only"
  detection: "Risk register audit — verify every mitigated finding has a residual estimate"
  recovery: "Require residual estimates after every mitigation; retrofit where missing"
  retryable: false
- name: residual_static_assumption
  description: "Residual risk treated as static between reviews — control degradation and threat evolution go unmeasured."
  likelihood: high
  observable_evidence: "Residual estimates unchanged for years; control effectiveness declining without register updates"
  detection: "Residual estimate age tracking; control effectiveness monitoring correlation"
  recovery: "Time-bound residual estimates; link residual updates to control health data"
  retryable: true
- name: inherent_residual_conflation
  description: "Inherent risk is treated as residual — organisations report pre-mitigation risk as their exposure, overstating what actually exists."
  likelihood: medium
  observable_evidence: "Risk reports using inherent (pre-mitigation) numbers; mitigation effects absent from risk presentations"
  detection: "Risk reporting audit; trace reported risk numbers to mitigation records"
  recovery: "Report residual as the operational figure; document inherent separately for context"
  retryable: false

## Observations
- observation: "Residual risk is the least well-measured quantity in most risk programmes — mitigation tracking exists, residual quantification rarely."
  confidence: high
  source: Risk governance audits, security assessment practice
- observation: "Organisations that quantify residual risk make better acceptance decisions — estimates replace guesswork in governance."
  confidence: high
  source: Risk management research, governance practice
- observation: "Residual risk estimation is most unreliable exactly where it matters most — high-impact, low-likelihood risks are hardest to estimate."
  confidence: high
  source: Risk estimation research

## Constraints
- constraint: "Residual risk cannot be zero for any system of interest to an adversary — some exposure always remains."
  type: invariant
  scope: cross-domain
- constraint: "Residual risk is bounded below by assessment error — the true residual cannot be known more precisely than the assessment allows."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Report residual risk as the operational figure — inherent risk is context, not exposure."
  rationale: "Operating decisions rest on what remains after mitigation, not on pre-mitigation theory."
  evidence_level: high
- heuristic: "Time-bound every residual estimate — control degradation and threat evolution invalidate old numbers."
  rationale: "Time-bounded estimates force re-evaluation and prevent static-assumption failure."
  evidence_level: high
- heuristic: "Track residual risk trend, not just level — rising residual trends signal control degradation before materialisation."
  rationale: "Trends are leading indicators; levels are lagging snapshots."
  evidence_level: medium

## Recommendations
- recommendation: "Require a residual risk estimate with confidence for every mitigated finding."
  context: risk_management
  certainty: strong
  rationale: "Residual with confidence is the input that makes acceptance decisions defensible."
- recommendation: "Link residual risk updates to control health and threat intelligence — residual changes when controls or threats change."
  context: risk_operations
  certainty: strong
  rationale: "Automated linkage keeps residual estimates current without heavy manual reassessment."
- recommendation: "Distinguish inherent and residual in all risk reporting — conflation misleads governance."
  context: risk_reporting
  certainty: strong
  rationale: "Clear separation lets executives govern the risk that actually exists."

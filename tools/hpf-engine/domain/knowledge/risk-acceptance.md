# Risk Acceptance

## Identity
- id: risk-acceptance
- type: decision
- title: Risk Acceptance
- tags: [security, risk, risk acceptance, risk management, governance, tolerance]
- entities: [risk acceptance, risk tolerance, risk appetite, residual risk, accept risk, risk decision]
- concepts: [likelihood, confidence, residual-risk, incomplete-evidence, compensating-controls, vulnerability-management]

## Claims
- claim: "Risk acceptance is the formal decision to tolerate a known risk rather than mitigate or avoid it — it is an explicit governance act, not an implicit condition."
  certainty: high
  evidence: Risk management standards (ISO 31000, NIST SP 800-30)
  scope: cross-domain
- claim: "Risk acceptance has no objectively correct answer — the right decision depends on business context, evidence quality, priorities, and constraints."
  certainty: high
  evidence: Risk management literature, organisational decision research
  scope: cross-domain
- claim: "Risk acceptance requires both likelihood and impact assessment — accepting a risk without estimating its dimensions is not a decision, it is an omission."
  certainty: high
  evidence: Risk management standards
  scope: cross-domain
- claim: "Risk acceptance must be time-bound and revisitable — the conditions that justified acceptance (threat landscape, evidence, business context) change."
  certainty: high
  evidence: Risk management practice, audit findings
  scope: cross-domain
- claim: "Formal risk acceptance reduces organisational surprise — an accepted risk that materialises is an expected outcome, not an undiscovered failure."
  certainty: high
  evidence: Risk governance literature, post-incident reviews
  scope: cross-domain

## Relationships
- concept: likelihood
  relationship: requires
  description: "Risk acceptance requires a likelihood estimate — accepting without estimating likelihood is not a decision."
- concept: confidence
  relationship: requires
  description: "Acceptance requires confidence in the assessment — low-confidence assessments should not support acceptance."
- concept: residual-risk
  relationship: addresses
  description: "Risk acceptance is the formal governance of residual risk — the risk remaining after mitigation is either accepted or further treated."
- concept: incomplete-evidence
  relationship: complicates
  description: "Incomplete evidence makes acceptance a gamble — the true risk profile is unknown, not accepted."
- concept: compensating-controls
  relationship: may_support
  description: "Acceptance is often paired with compensating controls — controls that partially offset the accepted risk."
- concept: vulnerability-management
  relationship: triggers
  description: "Vulnerabilities that cannot be remediated within SLA become candidates for risk acceptance."

## Tradeoffs
- dimension: acceptance_threshold_vs_mitigation_cost
  options:
    low_threshold:
      value: conservatism
      rationale: "Accept few risks — safer but higher mitigation spend and slower feature delivery."
    high_threshold:
      value: velocity
      rationale: "Accept more risks — faster delivery but higher exposure and dependence on detection."
  importance: high
- dimension: formality_vs_agility
  options:
    formal_process:
      value: accountability
      rationale: "Documented acceptance with named owners — auditable and defensible but slower."
    informal_acceptance:
      value: speed
      rationale: "Implicit acceptance in engineering decisions — fast but invisible and unowned."
  importance: high

## Failure Modes
- name: implicit_acceptance
  description: "Risk is accepted by omission — decisions are made without explicit acceptance, so risk is unowned and unrecorded."
  likelihood: high
  observable_evidence: "Incident reviews find risks that were effectively accepted without governance; no acceptance record for materialised risks"
  detection: "Risk register audit against decisions; review of unmitigated findings without acceptance records"
  recovery: "Require explicit acceptance for any unmitigated finding; retroactively formalise standing acceptances"
  retryable: false
- name: stale_acceptance
  description: "Acceptance remains valid after its conditions have changed — threat landscape or business context moved but the acceptance did not."
  likelihood: high
  observable_evidence: "Accepted risks remain accepted for years; acceptance reviews overdue; materialised risks accepted under obsolete conditions"
  detection: "Acceptance expiry tracking; periodic acceptance review reports"
  recovery: "Set acceptance validity windows; trigger re-review on threat landscape changes"
  retryable: true
- name: uninformed_acceptance
  description: "Acceptance granted without adequate likelihood/impact/confidence assessment — the decision is not evidence-based."
  likelihood: medium
  observable_evidence: "Acceptances with no supporting assessment; decisions made without confidence statements; management signs off on unknowns"
  detection: "Acceptance quality audit — verify every acceptance has likelihood, impact, and confidence"
  recovery: "Reject uninformed acceptances; require minimum assessment quality before acceptance"
  retryable: false

## Observations
- observation: "Most 'accepted' risk in organisations is implicit — acceptance happens by silence rather than by decision."
  confidence: high
  source: Risk governance audits, incident reviews
- observation: "Risk acceptance decisions are made faster than risk assessments justify — executives accept or reject without reviewing likelihood or confidence."
  confidence: high
  source: Organisational decision research, governance practice
- observation: "Formal acceptance with named owners materially reduces incident surprise — organisations know which risks were accepted."
  confidence: high
  source: Risk governance literature, post-incident analysis

## Constraints
- constraint: "Acceptance without likelihood, impact, and confidence assessment is not a decision — it is an omission that transfers risk to whoever discovers it later."
  type: invariant
  scope: cross-domain
- constraint: "Acceptance validity is bounded by the stability of its conditions — conditions change, and acceptance must be re-evaluated."
  type: invariant
  scope: cross-domain

## Decision Factors
- factor: materiality
  question: "What is the potential business impact if the risk materialises?"
  supporting: "Low-impact risks (cosmetic issues, internal tooling) are appropriate acceptance candidates."
  contradictory: "High-impact risks (customer data, regulatory obligations, availability) demand mitigation regardless of likelihood."
  weight: high
- factor: assessment_confidence
  question: "How confident is the team in the likelihood and impact assessment?"
  supporting: "High-confidence low-likelihood assessments justify acceptance."
  contradictory: "Low-confidence assessments cannot support acceptance — the unknown dominates the estimate."
  weight: high
- factor: mitigation_cost
  question: "What does mitigation cost relative to the risk?"
  supporting: "Mitigation costing more than the expected loss justifies acceptance."
  contradictory: "Cheap mitigations should always be applied — acceptance is only defensible when mitigation is disproportionate."
  weight: high
- factor: detection_compensation
  question: "If the risk materialises, can it be detected and contained?"
  supporting: "Strong detection and response capability makes acceptance defensible — the risk is observable if it materialises."
  contradictory: "Undetectable materialisation is unacceptably dangerous — the organisation would not learn of the compromise."
  weight: high

## Heuristics
- heuristic: "Require explicit, documented acceptance with a named owner for every unmitigated risk finding."
  rationale: "Explicit acceptance creates accountability and prevents surprise; implicit acceptance transfers risk to the discoverer."
  evidence_level: high
- heuristic: "Time-box every acceptance — acceptances expire with their conditions."
  rationale: "Time-bounded acceptance forces re-evaluation when conditions change."
  evidence_level: high
- heuristic: "Never accept a risk whose materialisation would not be detectable."
  rationale: "Undetectable materialisation is worse than the risk itself — the organisation would not learn of compromise."
  evidence_level: high

## Recommendations
- recommendation: "Formalise risk acceptance as a governance act with named owner, time window, and documented assessment."
  context: risk_governance
  certainty: strong
  rationale: "Formal acceptance converts hidden risk into accountable, bounded decisions."
- recommendation: "Re-review every acceptance when threat intelligence indicates a material change in likelihood."
  context: risk_management
  certainty: strong
  rationale: "Acceptance conditions are moving targets — re-review aligns acceptance with the current threat landscape."
- recommendation: "Pair acceptance with compensating controls whenever partial mitigation is possible."
  context: risk_treatment
  certainty: strong
  rationale: "Compensating controls reduce the realised impact of accepted risks without full mitigation cost."

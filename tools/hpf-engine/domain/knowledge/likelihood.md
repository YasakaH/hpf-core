# Likelihood

## Identity
- id: likelihood
- type: concept
- title: Likelihood of Security Events
- tags: [security, probability, likelihood, risk, threat, estimation]
- entities: [likelihood, probability, frequency, threat occurrence, risk estimation, chance]
- concepts: [confidence, incomplete-evidence, risk-acceptance, threat-detection, vulnerability-management]

## Claims
- claim: "Likelihood is the estimated probability or frequency of a security event occurring, typically expressed as a category (rare, unlikely, possible, likely, almost certain) or a probability range."
  certainty: high
  evidence: Risk management standards (ISO 31000, NIST SP 800-30)
  scope: cross-domain
- claim: "Likelihood estimation in security is fundamentally different from probability in engineered systems — it involves an intelligent adversary actively attempting to influence outcomes."
  certainty: high
  evidence: Security risk literature, threat intelligence practice
  scope: cross-domain
- claim: "Adversarial likelihood estimates are conditional — the likelihood of an attack depends on attacker motivation, capability, and opportunity, not just system vulnerability."
  certainty: high
  evidence: Threat modelling literature (STRIDE, MITRE ATT&CK)
  scope: cross-domain
- claim: "Likelihood estimates degrade with uncertainty about attacker behaviour — incomplete threat intelligence widens the confidence interval on any estimate."
  certainty: high
  evidence: Threat intelligence literature
  scope: cross-domain
- claim: "Likelihood and impact are independent dimensions of risk — a low-likelihood event can have catastrophic impact and still warrant mitigation."
  certainty: high
  evidence: Risk management standards
  scope: cross-domain

## Relationships
- concept: confidence
  relationship: qualified_by
  description: "Every likelihood estimate carries a confidence level — without it, the estimate is an assertion without epistemic grounding."
- concept: incomplete-evidence
  relationship: degraded_by
  description: "Incomplete threat intelligence widens likelihood confidence intervals and reduces estimate reliability."
- concept: risk-acceptance
  relationship: informs
  description: "Likelihood × impact = risk — likelihood estimates are the primary input to risk acceptance decisions."
- concept: threat-detection
  relationship: informs
  description: "Likelihood estimates drive detection priorities — higher-likelihood threats justify more detection investment."
- concept: vulnerability-management
  relationship: informs
  description: "Exploit likelihood determines vulnerability prioritisation — not all vulnerabilities are equally likely to be exploited."

## Tradeoffs
- dimension: precision_vs_usability
  options:
    numeric_range:
      value: precision
      rationale: "Probability ranges (e.g. 20-40%) support quantitative analysis but create false precision."
    qualitative_categories:
      value: usability
      rationale: "Categories (rare → almost certain) are usable across teams but lose granularity."
  importance: high
- dimension: historical_basis_vs_adversarial_analysis
  options:
    historical_frequency:
      value: measurable
      rationale: "Basing likelihood on observed frequency is defensible but fails for novel attacks."
    adversarial_analysis:
      value: forward_looking
      rationale: "Analysing attacker capability and intent covers novel attacks but is less empirically grounded."
  importance: high

## Failure Modes
- name: false_precision
  description: "Likelihood expressed with more precision than the evidence supports — '73% likely' on qualitative evidence creates false confidence."
  likelihood: high
  observable_evidence: "Numeric likelihoods without statistical basis; overconfident probability claims in risk registers"
  detection: "Review likelihood justifications; audit estimates against actual outcomes"
  recovery: "Convert to ranges or categories; require evidence basis for numeric estimates"
  retryable: false
- name: likelihood_misattribution
  description: "System-level probability is treated as attack likelihood — the probability of a random failure is conflated with the probability of adversarial exploitation."
  likelihood: high
  observable_evidence: "Security risk registers using availability statistics as attack likelihood; underestimating targeted attack risk"
  detection: "Risk register audit; compare likelihood sources against attack models"
  recovery: "Separate accidental-failure likelihood from adversarial likelihood; develop attacker-centric estimates"
  retryable: false
- name: anchoring_on_history
  description: "Likelihood anchored to past events fails to anticipate novel attack methods — 'has never happened' is treated as 'will never happen'."
  likelihood: medium
  observable_evidence: "Novel attack methods repeatedly surprise organisations; likelihood estimates don't update for new TTPs"
  detection: "Compare estimate updates against threat intelligence feeds; review novel attack post-mortems"
  recovery: "Incorporate intelligence-led likelihood (capability-based); periodically challenge historical anchors"
  retryable: true

## Observations
- observation: "Qualitative likelihood categories are interpreted differently across teams — 'likely' means different things to engineers, executives, and threat analysts."
  confidence: high
  source: Risk management research, organisational studies
- observation: "Adversarial likelihood is systematically underestimated relative to accidental failure likelihood in most risk registers."
  confidence: high
  source: Security risk audits, incident analysis
- observation: "The best likelihood estimates combine historical frequency with attacker capability analysis — neither alone is sufficient."
  confidence: high
  source: Threat intelligence practice, risk management literature

## Constraints
- constraint: "Adversarial likelihood is conditional on attacker variables (motivation, capability, opportunity) — unconditional likelihood statements are not well-defined."
  type: invariant
  scope: cross-domain
- constraint: "Likelihood cannot be zero for any plausible attack path — zero likelihood statements contradict adversarial reasoning."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Express likelihood as a category with a defined range and attach a confidence level."
  rationale: "Categories with ranges communicate uncertainty honestly; confidence exposes estimate reliability."
  evidence_level: high
- heuristic: "Estimate likelihood from the attacker's perspective, not the system's — ask 'would an attacker attempt this and could they succeed?'"
  rationale: "Attacker-centric estimation captures targeted risk that system-centric probability misses."
  evidence_level: high
- heuristic: "Update likelihood estimates when threat intelligence changes, not on a fixed review cycle."
  rationale: "Threat landscape shifts faster than review cycles — stale likelihoods drive wrong priorities."
  evidence_level: medium

## Recommendations
- recommendation: "Never present likelihood without both a basis (historical, analytical, or adversarial) and a confidence level."
  context: risk_management
  certainty: strong
  rationale: "Likelihood without basis or confidence is an opinion that cannot be audited or calibrated."
- recommendation: "Treat novel attack likelihood as non-zero — maintain mitigations proportional to impact regardless of historical frequency."
  context: security_strategy
  certainty: strong
  rationale: "Historical anchoring underestimates novel attacks; impact-proportional mitigation is robust to likelihood error."
- recommendation: "Separate accidental-failure likelihood from adversarial likelihood in risk registers — they require different estimation methods."
  context: risk_assessment
  certainty: strong
  rationale: "Conflating them misallocates mitigation effort and misrepresents the risk profile."

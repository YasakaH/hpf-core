# Incomplete Evidence

## Identity
- id: incomplete-evidence
- type: concept
- title: Incomplete Evidence in Security Analysis
- tags: [security, evidence, uncertainty, intelligence, analysis, gaps]
- entities: [incomplete evidence, evidence gaps, intelligence gaps, unknown unknowns, partial information, missing telemetry]
- concepts: [confidence, likelihood, threat-detection, vulnerability-management, risk-acceptance]

## Claims
- claim: "Security analysis almost always operates on incomplete evidence — full observability of an attacker's behaviour is the exception, not the rule."
  certainty: high
  evidence: Intelligence analysis literature, security operations experience
  scope: cross-domain
- claim: "The distinction between known unknowns (identified gaps) and unknown unknowns (unimagined gaps) determines how evidence gaps should be managed."
  certainty: high
  evidence: Intelligence analysis literature (known-unknown matrix)
  scope: cross-domain
- claim: "Evidence gaps are asymmetric in impact — missing evidence of attack is not evidence of no attack."
  certainty: high
  evidence: Security operations literature, intelligence analysis
  scope: cross-domain
- claim: "Incomplete evidence biases analysis toward visible threats — what is measured is weighted higher than what is not measured."
  certainty: high
  evidence: Behavioural decision research, security telemetry analysis
  scope: cross-domain
- claim: "The cost of closing an evidence gap must be weighed against the cost of acting on incomplete evidence — evidence perfection is rarely affordable."
  certainty: high
  evidence: Security operations practice, cost-benefit analysis
  scope: cross-domain

## Relationships
- concept: confidence
  relationship: reduces
  description: "Incomplete evidence reduces confidence — the less evidence, the less confident a judgement can legitimately be."
- concept: likelihood
  relationship: widens
  description: "Incomplete evidence widens likelihood confidence intervals and degrades estimate reliability."
- concept: threat-detection
  relationship: blinds
  description: "Telemetry gaps create detection blind spots — attacks that evade monitored surfaces are invisible."
- concept: vulnerability-management
  relationship: distorts
  description: "Evidence gaps in asset inventory distort vulnerability prioritisation — unassessed systems are assumed safe."
- concept: risk-acceptance
  relationship: complicates
  description: "Risk acceptance on incomplete evidence is a gamble — the true risk profile is unknown, not accepted."

## Tradeoffs
- dimension: evidence_gathering_vs_action_speed
  options:
    gather_more:
      value: better_grounded
      rationale: "More evidence produces better-grounded decisions but delays action — attacks don't wait."
    act_early:
      value: speed
      rationale: "Acting on partial evidence responds faster but risks acting on wrong conclusions."
  importance: high
- dimension: telemetry_coverage_vs_operational_cost
  options:
    broad_coverage:
      value: visibility
      rationale: "Wide telemetry coverage reduces blind spots but adds cost, noise, and storage burden."
    targeted_coverage:
      value: efficiency
      rationale: "Focused coverage is cheaper and quieter but misses attacks outside the covered surface."
  importance: high

## Failure Modes
- name: evidence_gap_false_assurance
  description: "Absence of attack evidence is treated as evidence of absence — 'we saw nothing, therefore nothing happened'."
  likelihood: high
  observable_evidence: "Breaches undetected for long periods; post-incident discovery that telemetry never covered the attack path"
  detection: "Periodic assumption reviews; red team exercises that verify what telemetry actually captures"
  recovery: "Instrument uncovered surfaces; treat monitoring gaps as findings, not as clean bill of health"
  retryable: false
- name: unknown_unknown_paralysis
  description: "Awareness of unimagined gaps leads to analysis paralysis — the team waits for evidence that cannot be collected."
  likelihood: medium
  observable_evidence: "Decision delays; analysts repeatedly request more data; 'we can't know' used as a reason for inaction"
  detection: "Decision latency metrics; analysis review for circular evidence requests"
  recovery: "Time-box evidence gathering; decide with explicit residual uncertainty; document what would change the decision"
  retryable: true
- name: telemetry_bias
  description: "Analysts weight conclusions toward what is measured, systematically under-weighting unmeasured attack paths."
  likelihood: high
  observable_evidence: "Threat models dominated by monitored surfaces; attacks on unmonitored assets dismissed as 'not in scope'"
  detection: "Threat model review for coverage bias; compare detection coverage against attack surface"
  recovery: "Explicitly map monitored vs unmonitored surfaces; weight unmeasured risks by reasoned priors"
  retryable: false

## Observations
- observation: "The median time-to-detection for breaches remains measured in weeks or months — evidence gaps are the norm, not the exception."
  confidence: high
  source: Breach report statistics, incident research
- observation: "Teams that document evidence gaps as findings (rather than hidden assumptions) make better decisions — visibility of gaps improves judgement."
  confidence: high
  source: Intelligence analysis literature, security operations practice
- observation: "Red teaming is the most effective tool for discovering unknown unknowns — it reveals gaps that analysis alone cannot."
  confidence: high
  source: Security operations experience, red team practice

## Constraints
- constraint: "Evidence absence cannot be used as evidence of security — 'no evidence of compromise' is a finding about coverage, not about compromise."
  type: invariant
  scope: cross-domain
- constraint: "Every analysis carries an unquantified component of unknown unknowns — claims of complete evidence are necessarily false."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Maintain an explicit evidence-gap register alongside the risk register."
  rationale: "Documented gaps keep uncertainty visible and prevent it from being silently assumed away."
  evidence_level: high
- heuristic: "Treat unmonitored attack surface as high-risk by default, not unassessed."
  rationale: "Defaulting unmeasured surfaces to 'unknown risk' prevents false assurance from coverage gaps."
  evidence_level: high
- heuristic: "Ask 'what evidence would change this decision?' before gathering more — most evidence requests don't change decisions."
  rationale: "Focused evidence gathering avoids both paralysis and wasted collection effort."
  evidence_level: high

## Recommendations
- recommendation: "Record confidence degradation explicitly when evidence is incomplete — a finding without confidence is an assumption."
  context: security_analysis
  certainty: strong
  rationale: "Explicit confidence on incomplete evidence keeps uncertainty visible to decision makers."
- recommendation: "Conduct periodic red team exercises specifically to discover unknown unknowns — not just to test known defences."
  context: security_operations
  certainty: strong
  rationale: "Red teaming is the primary tool for converting unknown unknowns into known unknowns."
- recommendation: "When accepting risk on incomplete evidence, document what additional evidence would change the acceptance decision."
  context: risk_management
  certainty: strong
  rationale: "Documented decision-reversal criteria make risk acceptance on partial evidence revisable rather than permanent."

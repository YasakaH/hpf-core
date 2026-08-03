# Attacker Capability

## Identity
- id: attacker-capability
- type: concept
- title: Attacker Capability
- tags: [security, attacker, threat, capability, adversarial, threat-modelling]
- entities: [attacker capability, attacker skill, exploit capability, TTP, adversarial capability, threat actor capability]
- concepts: [threat-actor, attack-surface, kill-chain, likelihood, risk-acceptance]

## Claims
- claim: "Attacker capability describes what an adversary is able to do — their skills, tools, resources, and access — independently of whether they choose to attack."
  certainty: high
  evidence: Threat modelling literature, MITRE ATT&CK framework
  scope: cross-domain
- claim: "Capability is distinct from intent — a highly capable actor with no intent poses no immediate threat, while intent without capability produces no successful attacks."
  certainty: high
  evidence: Threat assessment literature (capability-intent matrix)
  scope: cross-domain
- claim: "Capability levels span a wide spectrum — from untargeted commodity attacks using automated tooling to sophisticated state-sponsored operations with custom exploits."
  certainty: high
  evidence: Threat intelligence literature, ATT&CK data
  scope: cross-domain
- claim: "Capability is observable through behaviour, not just claims — capabilities manifest in TTPs (tactics, techniques, procedures) that can be detected and attributed."
  certainty: high
  evidence: Threat intelligence practice, ATT&CK framework
  scope: cross-domain
- claim: "Capability is not static — it increases through tooling commoditisation, knowledge sharing, and the reuse of previously exploited vulnerabilities."
  certainty: high
  evidence: Security research, exploit market analysis
  scope: cross-domain

## Relationships
- concept: threat-actor
  relationship: characterises
  description: "Attacker capability characterises what a threat actor can do — the capability profile is a core attribute of the actor."
- concept: attack-surface
  relationship: interacts_with
  description: "Capability × attack surface = exploitability — a large attack surface magnifies any given capability level."
- concept: kill-chain
  relationship: enables
  description: "Capability determines which kill-chain stages an attacker can complete — low capability often stops at early stages."
- concept: likelihood
  relationship: drives
  description: "Capability is a primary driver of adversarial likelihood — the 'can they?' component of the threat estimate."
- concept: risk-acceptance
  relationship: informs
  description: "Capability assessment informs which risks are acceptable — an adversary capable of exploiting a gap changes the acceptance calculus."

## Tradeoffs
- dimension: capability_detail_vs_assessment_cost
  options:
    granular_models:
      value: precision
      rationale: "Detailed capability profiles (per actor, per TTP) enable precise threat modelling but cost significant analyst time."
    coarse_models:
      value: efficiency
      rationale: "Broad capability bands (low/medium/high) are cheap and usable but lose discriminating power."
  importance: high
- dimension: capability_vs_intent_weighting
  options:
    capability_heavy:
      value: defensive_pragmatism
      rationale: "Focus on what an adversary could do — prudent for defence because intent is harder to observe."
    intent_heavy:
      value: resource_allocation
      rationale: "Focus on who is actually targeting you — efficient but risks missing capable-but-quiet adversaries."
  importance: high

## Failure Modes
- name: capability_overestimation
  description: "Assumed capability exceeds actual capability, leading to over-investment in defences against threats that cannot materialise."
  likelihood: medium
  observable_evidence: "Defence spending misaligned with realised threats; threat models dominated by sophisticated actors that never appear"
  detection: "Compare threat model assumptions against actual attack observations; review detection-and-response history"
  recovery: "Re-baseline capability assessments against observed behaviour; focus on demonstrable TTPs"
  retryable: false
- name: capability_underestimation
  description: "Assumed capability falls below actual capability, creating blind spots — typically from assuming attackers are unsophisticated."
  likelihood: high
  observable_evidence: "Organisations surprised by attacks using techniques assumed 'too advanced'; detection gaps for sophisticated TTPs"
  detection: "Red team exercises; review assumptions in threat models; track novel TTPs in intelligence feeds"
  recovery: "Upgrade capability baselines; add detection for previously assumed-out-of-scope TTPs"
  retryable: false
- name: static_capability_assumption
  description: "Capability treated as fixed when it is evolving — commodity tooling and public exploit research continuously raise the baseline."
  likelihood: high
  observable_evidence: "Threat models unchanged for years; organisations repeatedly surprised by 'new' techniques that were foreseeable"
  detection: "Review cadence of threat model updates; track exploit commoditisation timelines"
  recovery: "Schedule capability reassessment; incorporate exploit market and CVE exploitation trends"
  retryable: true

## Observations
- observation: "The capability baseline for commodity attackers rises continuously — techniques once exclusive to nation-states appear in commodity tooling within years."
  confidence: high
  source: Security research, exploit market analysis, ATT&CK data
- observation: "Most organisations face commodity capability most of the time — sophisticated capability is rarer than threat models suggest."
  confidence: high
  source: Threat intelligence practice, breach data analysis
- observation: "Capability assessment is most valuable when tied to specific TTPs — abstract capability levels drive few concrete defence decisions."
  confidence: high
  source: Threat modelling practice, ATT&CK adoption

## Constraints
- constraint: "Capability without a path to the attack surface produces no exploit — capability assessment must be paired with attack-surface analysis."
  type: invariant
  scope: cross-domain
- constraint: "Capability assessments are time-bound — an assessment is valid only until tooling or knowledge advances change the baseline."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Model capability at the TTP level (what specific techniques can they execute?) rather than the abstract level."
  rationale: "TTP-level capability maps directly to detection and mitigation decisions; abstract levels do not."
  evidence_level: high
- heuristic: "Reassess capability assumptions every time a tool or technique is commoditised."
  rationale: "Commoditisation changes the baseline — yesterday's sophisticated attack is tomorrow's scripted exploit."
  evidence_level: high
- heuristic: "Assume the capability floor rises — use current commodity tooling as the minimum baseline, not last year's."
  rationale: "Basing minimum baseline on current commodity capability prevents systematic underestimation."
  evidence_level: high

## Recommendations
- recommendation: "Base capability assessments on observed TTPs and intelligence, not on assumed actor sophistication."
  context: threat_assessment
  certainty: strong
  rationale: "Observable TTPs ground capability in evidence; actor-sophistication labels are unreliable and frequently wrong."
- recommendation: "Pair every capability assessment with attack-surface analysis — capability alone does not constitute a threat."
  context: threat_modelling
  certainty: strong
  rationale: "Capability × surface × intent = threat; omitting any factor distorts the conclusion."
- recommendation: "Review capability baselines quarterly against exploit commoditisation and CVE exploitation trends."
  context: security_operations
  certainty: strong
  rationale: "The capability baseline rises continuously — quarterly review keeps threat models aligned with reality."

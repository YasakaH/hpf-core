# Zero Trust

## Identity
- id: zero-trust
- type: principle
- title: Zero Trust Architecture
- tags: [security, zero trust, architecture, identity, least privilege, segmentation]
- entities: [zero trust, zero trust architecture, least privilege, microsegmentation, identity-based access, never trust always verify]
- concepts: [attack-surface, defense-in-depth, threat-detection, incident-response, threat-actor, risk-acceptance]

## Claims
- claim: "Zero trust is an architecture principle: no entity is trusted by virtue of network position — every access request is verified regardless of origin."
  certainty: high
  evidence: NIST SP 800-207, zero trust literature
  scope: cross-domain
- claim: "Zero trust replaces perimeter trust with identity-based, per-request verification — the network no longer implies trust."
  certainty: high
  evidence: NIST SP 800-207, industry adoption research
  scope: cross-domain
- claim: "Zero trust is a journey of architecture changes, not a product — it reorients identity, device, network, workload, and data security."
  certainty: high
  evidence: NIST SP 800-207, adoption guidance
  scope: cross-domain
- claim: "Zero trust assumes breach — the architecture is designed for the reality that attackers are already inside."
  certainty: high
  evidence: Zero trust literature, NIST SP 800-207
  scope: cross-domain
- claim: "Zero trust reduces lateral movement — segmented access limits how far a compromised identity can travel."
  certainty: high
  evidence: Security research, breach analysis, zero trust adoption studies
  scope: cross-domain

## Relationships
- concept: attack-surface
  relationship: reduces
  description: "Zero trust reduces the effective attack surface by removing implicit trust between components — internal exposure stops being accessible."
- concept: defense-in-depth
  relationship: extends
  description: "Zero trust is a modern articulation of depth — per-request verification adds a layer at every access."
- concept: threat-detection
  relationship: depends_on
  description: "Zero trust depends on strong identity and behaviour detection — verification requires continuous signal."
- concept: incident-response
  relationship: supports
  description: "Segmented architecture bounds incidents — zero trust containment limits blast radius."
- concept: threat-actor
  relationship: resists
  description: "Zero trust resists actors who gain a foothold — compromised identities face verification at every move."
- concept: risk-acceptance
  relationship: changes
  description: "Zero trust changes what must be accepted — identity risk replaces perimeter risk in the acceptance portfolio."

## Tradeoffs
- dimension: verification_strictness_vs_experience
  options:
    strict_verification:
      value: security
      rationale: "Verify every request continuously — strongest posture but friction for legitimate users."
    adaptive_verification:
      value: balance
      rationale: "Risk-based verification — strong for risky access, lighter for trusted patterns — better experience, more policy complexity."
  importance: high
- dimension: implementation_speed_vs_transformation_depth
  options:
    incremental:
      value: managed_risk
      rationale: "Gradual migration to zero trust — lower disruption but long period of mixed trust models."
    big_bang:
      value: unified_model
      rationale: "Rapid full transformation — consistent model but high disruption and migration risk."
  importance: high

## Failure Modes
- name: zero_trust_theatre
  description: "Zero trust branding without zero trust substance — architecture unchanged, only the name is new."
  likelihood: high
  observable_evidence: "Zero trust claims with no architecture change; access still implicit; internal trust persists"
  detection: "Architecture review against NIST SP 800-207 pillars; verify actual access decisions"
  recovery: "Re-baseline architecture against zero trust pillars; prioritise identity and segmentation changes"
  retryable: false
- name: identity_single_point
  description: "Identity provider becomes the single point of failure — identity compromise defeats the entire model."
  likelihood: medium
  observable_evidence: "Identity provider breach disables trust decisions; attacker with stolen identity moves freely"
  detection: "Identity provider hardening assessment; compromise simulation"
  recovery: "Harden identity infrastructure; add phishing-resistant MFA; segment identity administration"
  retryable: true
- name: alert_verification_avalanche
  description: "Continuous verification generates alert volume that exhausts the team — verification noise drowns genuine signals."
  likelihood: medium
  observable_evidence: "Alert fatigue; backlog growth; delayed verification reviews; missed genuine anomalies"
  detection: "Alert volume and triage metrics; time-to-review statistics"
  recovery: "Implement risk-based adaptive verification; tune policy granularity; automate routine verification decisions"
  retryable: true

## Observations
- observation: "Most zero trust initiatives are identity and access modernisation in disguise — valuable but not the full architecture."
  confidence: high
  source: Zero trust adoption research, architecture reviews
- observation: "Zero trust adoption correlates with reduced breach impact — segmented organisations contain incidents faster."
  confidence: high
  source: Breach analysis, adoption studies
- observation: "The identity provider is the new perimeter — zero trust concentrates attack value on identity infrastructure."
  confidence: high
  source: Security research, incident analysis

## Constraints
- constraint: "Zero trust cannot eliminate trust — it relocates and bounds it — identity, device, and policy trust remain."
  type: invariant
  scope: cross-domain
- constraint: "Zero trust effectiveness is bounded by identity quality — weak identity undermines every verification."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Start zero trust with identity — phishing-resistant MFA and privileged access control deliver the highest early value."
  rationale: "Identity is the foundation of verification; identity hardening compounds across all other pillars."
  evidence_level: high
- heuristic: "Segment by identity and workload first, network segments later — identity-based segmentation survives modern architecture."
  rationale: "Identity and workload segmentation maps to how modern workloads communicate; network segmentation frequently breaks."
  evidence_level: high
- heuristic: "Adopt adaptive, risk-based verification rather than binary allow/deny — it balances security with usability."
  rationale: "Adaptive verification sustains adoption; binary verification triggers bypass workarounds."
  evidence_level: high

## Recommendations
- recommendation: "Implement zero trust incrementally, identity-first — transformation is architectural, not a product purchase."
  context: security_strategy
  certainty: strong
  rationale: "Incremental identity-first adoption delivers value early and builds the foundation for later pillars."
- recommendation: "Harden the identity provider as the highest-value target — phishing-resistant MFA, privileged access isolation, and monitoring."
  context: security_operations
  certainty: strong
  rationale: "Zero trust concentrates attack value on identity; hardening it protects the entire model."
- recommendation: "Measure zero trust by architecture change and containment outcomes, not by vendor adoption labels."
  context: security_governance
  certainty: strong
  rationale: "Outcome measurement prevents zero-trust theatre and aligns investment with actual risk reduction."

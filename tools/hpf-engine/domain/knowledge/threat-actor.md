# Threat Actor

## Identity
- id: threat-actor
- type: concept
- title: Threat Actor
- tags: [security, threat actor, threat intelligence, adversary, attribution, APT]
- entities: [threat actor, adversary, APT, attacker group, insider, hacktivist, cybercriminal, state-sponsored]
- concepts: [attacker-capability, kill-chain, attack-surface, likelihood, risk-acceptance]

## Claims
- claim: "A threat actor is an entity that poses a security threat — ranging from individual criminals and insiders to organised groups and state-sponsored units."
  certainty: high
  evidence: Threat intelligence literature, MITRE ATT&CK
  scope: cross-domain
- claim: "Threat actors are classified by motivation (financial, espionage, ideology, disruption), capability, and access — these determine their threat profile."
  certainty: high
  evidence: Threat intelligence literature, actor taxonomy research
  scope: cross-domain
- claim: "Actor attribution is probabilistic, not certain — most attributions carry confidence levels and are frequently contested."
  certainty: high
  evidence: Threat intelligence literature, public attribution disputes
  scope: cross-domain
- claim: "Actor behaviour evolves — groups disband, rebrand, share tooling, and change targets, making actor identity less stable than tooling signatures."
  certainty: high
  evidence: Threat intelligence practice, APT tracking research
  scope: cross-domain
- claim: "Insider threats form a distinct actor category — their access advantage compensates for typically lower technical capability."
  certainty: high
  evidence: Insider threat research, breach statistics
  scope: cross-domain

## Relationships
- concept: attacker-capability
  relationship: has
  description: "Every threat actor has a capability profile — capability is the defining attribute that determines what the actor can achieve."
- concept: kill-chain
  relationship: executes
  description: "Threat actors execute kill-chain stages — actor behaviour is observable as kill-chain progression."
- concept: attack-surface
  relationship: targets
  description: "Actors target the attack surface — surface analysis must consider which actors would be motivated to attack."
- concept: likelihood
  relationship: determines
  description: "Actor motivation × capability determines likelihood — the actor model is the foundation of likelihood estimation."
- concept: risk-acceptance
  relationship: informs
  description: "Understanding who might attack informs risk acceptance — a motivated capable actor changes acceptable risk levels."

## Tradeoffs
- dimension: actor_specific_vs_generic_threat_models
  options:
    actor_specific:
      value: tailored_defence
      rationale: "Detailed per-actor models enable tailored defence but cost significant analyst effort and age quickly."
    generic_models:
      value: broad_coverage
      rationale: "General threat categories (commodity, targeted, insider) are robust and cheap but less precise."
  importance: high
- dimension: attribution_effort_vs_defence_value
  options:
    deep_attribution:
      value: strategic_insight
      rationale: "Attribution reveals intent and likely next moves but is expensive and often contested."
    behaviour_only:
      value: operational_value
      rationale: "Modelling behaviour without attribution provides detection value directly and avoids attribution disputes."
  importance: high

## Failure Modes
- name: attribution_fallacy
  description: "Attribution treated as fact when it is probabilistic — teams act on contested attribution as if it were established."
  likelihood: medium
  observable_evidence: "Defence priorities set by attribution conclusions; contested attributions treated as settled; public disputes ignored"
  detection: "Review attribution confidence levels; audit how attribution feeds into defence decisions"
  recovery: "Separate behaviour-based defence from attribution-based strategy; document attribution confidence"
  retryable: false
- name: actor_model_rot
  description: "Threat actor models become stale — disbanded groups, renamed actors, and changed tooling keep models misaligned with current threats."
  likelihood: high
  observable_evidence: "Threat models referencing inactive groups; detection rules keyed to obsolete actor signatures; intelligence feeds showing rebranded actors"
  detection: "Model review cadence; correlation of model references with current intelligence"
  recovery: "Refresh actor models on intelligence cycles; decouple detection from actor identity where possible"
  retryable: true
- name: insider_actor_blindspot
  description: "Insider threats excluded from actor models because they are trusted — the access advantage is systematically ignored."
  likelihood: high
  observable_evidence: "Insider incidents handled as HR matters rather than security incidents; privileged access unmonitored"
  detection: "Privileged access reviews; insider threat programme assessment; anomaly detection on privileged accounts"
  recovery: "Include insider actor in threat model; monitor privileged access; implement least-privilege baselines"
  retryable: false

## Observations
- observation: "Actor classification is converging — distinct groups increasingly share tooling and infrastructure, blurring attribution boundaries."
  confidence: high
  source: Threat intelligence research, tooling reuse analysis
- observation: "Behaviour-based detection outperforms actor-based detection in practice — actor identity adds little to detection effectiveness."
  confidence: high
  source: Security operations practice, detection engineering research
- observation: "Most organisations over-model sophisticated actors and under-model insider and commodity threats."
  confidence: high
  source: Threat assessment audits, breach statistics

## Constraints
- constraint: "Attribution is always probabilistic — no actor identity is ever established with certainty."
  type: invariant
  scope: cross-domain
- constraint: "Actor capability cannot exceed what tooling and knowledge currently enable — actor models are bounded by the capability floor."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Model threats behaviour-first (what TTPs could be executed?) and actor-second (who might execute them?)."
  rationale: "Behaviour-first modelling delivers detection value regardless of attribution disputes."
  evidence_level: high
- heuristic: "Include insider actors in every threat model — access advantage makes them a distinct threat class."
  rationale: "Insider threats are systematically excluded from models despite being responsible for a significant share of incidents."
  evidence_level: high
- heuristic: "Refresh actor models on every major intelligence publication cycle, not on an annual review."
  rationale: "Actor landscapes shift faster than annual reviews — stale models misallocate defence."
  evidence_level: medium

## Recommendations
- recommendation: "Never base critical defence decisions on attribution alone — pair attribution with behaviour-based detection."
  context: security_strategy
  certainty: strong
  rationale: "Attribution is probabilistic and contested; behaviour-based defence remains valid regardless of who is attacking."
- recommendation: "Maintain an explicit insider-threat actor model with privileged access monitoring."
  context: security_operations
  certainty: strong
  rationale: "Insider actors are systematically underestimated; explicit modelling and monitoring close the gap."
- recommendation: "Document confidence levels on every actor attribution and revisit them when counter-evidence appears."
  context: threat_intelligence
  certainty: strong
  rationale: "Explicit confidence keeps probabilistic attribution honest and revisable."

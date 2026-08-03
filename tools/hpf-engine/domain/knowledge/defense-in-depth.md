# Defense in Depth

## Identity
- id: defense-in-depth
- type: principle
- title: Defense in Depth
- tags: [security, defense in depth, layered defence, security architecture, resilience]
- entities: [defense in depth, layered security, layered defence, multiple controls, depth of defence]
- concepts: [attack-surface, kill-chain, threat-detection, incident-response, zero-trust, risk-acceptance]

## Claims
- claim: "Defense in depth is the strategy of layering independent security controls so that the failure of any single control does not compromise the system."
  certainty: high
  evidence: Security literature, NSA defense-in-depth doctrine
  scope: cross-domain
- claim: "Layered controls assume each layer will fail eventually — the design question is what remains secure when any given layer fails."
  certainty: high
  evidence: Security architecture literature
  scope: cross-domain
- claim: "Effective layering requires independence — layers that share a common failure mode provide the appearance of depth without its resilience."
  certainty: high
  evidence: Security architecture research, failure analysis
  scope: cross-domain
- claim: "Depth is measured by the number of independent control failures required for compromise, not by the number of controls present."
  certainty: high
  evidence: Security literature, attack path analysis
  scope: cross-domain
- claim: "Defense in depth extends beyond prevention — detection, response, and recovery layers are as important as access-control layers."
  certainty: high
  evidence: Security operations literature, incident response practice
  scope: cross-domain

## Relationships
- concept: attack-surface
  relationship: complements
  description: "Defense in depth compensates for surfaces that cannot be eliminated — layers protect what remains exposed."
- concept: kill-chain
  relationship: resists
  description: "Layered controls resist kill-chain progression — each stage faces independent controls."
- concept: threat-detection
  relationship: includes
  description: "Detection is one of the layers — detection layers catch what prevention layers miss."
- concept: incident-response
  relationship: includes
  description: "Response is the final layer — containing and recovering from failures of all preceding layers."
- concept: zero-trust
  relationship: extends
  description: "Zero trust is a modern articulation of defense in depth — per-request verification layers trust."
- concept: risk-acceptance
  relationship: reduces_need
  description: "Effective depth reduces residual risk, shrinking what must be formally accepted."

## Tradeoffs
- dimension: layer_count_vs_operational_complexity
  options:
    minimal_layers:
      value: simplicity
      rationale: "Fewer layers are easier to operate and debug but compromise with a single control failure."
    deep_layers:
      value: resilience
      rationale: "More layers survive control failures but add operational complexity, cost, and failure surface of their own."
  importance: high
- dimension: independent_vs_integrated_controls
  options:
    independent:
      value: failure_isolation
      rationale: "Independently operated controls fail independently — true depth but higher management cost."
    integrated:
      value: efficiency
      rationale: "Integrated platforms are cheaper to operate but share failure modes — false depth."
  importance: high

## Failure Modes
- name: false_depth
  description: "Layers appear independent but share a common failure mode — one failure takes down the whole stack."
  likelihood: high
  observable_evidence: "Single-point failures compromise multiple 'layers'; layers share identity providers, networks, or platforms"
  detection: "Layer dependency analysis; failure injection tests that reveal shared failure modes"
  recovery: "Diversify control dependencies; document layer independence assumptions; test single-failure scenarios"
  retryable: false
- name: layer_rot
  description: "Layers degrade over time — rules drift, signatures age, coverage shrinks, and the effective depth falls."
  likelihood: high
  observable_evidence: "Control coverage metrics declining; aged rule sets; layer reviews overdue"
  detection: "Layer health metrics; periodic control effectiveness audits"
  recovery: "Refresh rules and signatures; re-validate layer coverage; retire dead layers"
  retryable: true
- name: depth_through_obscurity
  description: "Depth achieved through obscurity (hidden paths, undocumented behaviour) — controls rely on secrecy rather than independence."
  likelihood: medium
  observable_evidence: "Security relying on undocumented configurations; controls that fail when secrets leak"
  detection: "Architecture review for obscurity reliance; assume-secret-leakage testing"
  recovery: "Replace obscurity with explicit controls; document hidden assumptions"
  retryable: false

## Observations
- observation: "Most organisations believe they have more depth than they do — layer independence is rarely tested."
  confidence: high
  source: Security assessments, architecture reviews
- observation: "Cloud-native environments are shifting depth from network segmentation to identity and policy layers."
  confidence: high
  source: Cloud security research, architecture evolution
- observation: "Detection layers are the most commonly missing layer — most depth designs stop at prevention."
  confidence: high
  source: Security assessments, incident data

## Constraints
- constraint: "Layers sharing a dependency are a single layer — depth is defined by independent failure paths, not control count."
  type: invariant
  scope: cross-domain
- constraint: "No layer count provides absolute security — depth bounds the probability of compromise; it does not eliminate it."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Design for layer failure — ask 'what still protects us if this layer fails?' for every control."
  rationale: "Failure-oriented design reveals false depth and guides investment toward genuine independence."
  evidence_level: high
- heuristic: "Include detection and response as explicit layers — prevention-only depth is incomplete."
  rationale: "Prevention layers eventually fail; detection and response determine the damage when they do."
  evidence_level: high
- heuristic: "Test layer independence with failure injection — validate that one failure does not cascade."
  rationale: "Untested independence is assumed independence; failure injection verifies the depth claim."
  evidence_level: high

## Recommendations
- recommendation: "Document layer independence assumptions and test them with failure injection exercises."
  context: security_architecture
  certainty: strong
  rationale: "Independent layers are the definition of depth — untested independence is a claim, not a property."
- recommendation: "Include prevention, detection, and response layers in every depth design — depth that stops at prevention fails silently."
  context: security_design
  certainty: strong
  rationale: "Detection and response layers determine realised damage when prevention fails."
- recommendation: "Audit effective depth annually — count independent failure paths, not controls."
  context: security_governance
  certainty: strong
  rationale: "Measuring independent failure paths reveals false depth and aligns investment with resilience."

# Design Under Concealment

## Identity
- id: design-under-concealment
- type: concept
- title: Design Under Concealment
- tags: [concealment, design, artifact analysis, adversarial engineering, anti-analysis, concealment design]
- entities: [design under concealment, concealment design, concealed engineering, secrecy-shaped design, anti-analysis design]
- concepts: [artifact, surface-ambiguity, concealed-intent, attacker-capability, incomplete-evidence]

## Claims
- claim: "Concealment is an engineering parameter of the artifact's design — every design decision under concealment serves the artefact's secrecy as well as its function."
  certainty: high
  evidence: Adversarial engineering practice
  scope: cross-domain
- claim: "The design anticipates being read — concealment design treats the analyst as an adversary and shapes the artifact accordingly."
  certainty: high
  evidence: Obfuscation and concealment practice
  scope: cross-domain
- claim: "Concealment is visible only as its effects — the design state of the creator is never presented, only the shape the concealment produced."
  certainty: high
  evidence: Adversarial artifact analysis practice
  scope: cross-domain
- claim: "Concealment shapes the observable surface — the ambiguity the analyst sees is often a designed property, not an accident of capture."
  certainty: high
  evidence: Concealment practice, surface analysis
  scope: cross-domain
- claim: "Concealment has a cost — secrecy trades against function, performance, and robustness, and the trade is visible in the artifact's shape."
  certainty: high
  evidence: Adversarial engineering tradeoff analysis
  scope: cross-domain

## Relationships
- concept: artifact
  relationship: shapes
  description: "Design under concealment shapes the artifact — the secrecy parameter is visible in the object's form."
- concept: surface-ambiguity
  relationship: amplifies
  description: "Design under concealment amplifies surface ambiguity — the designed surface supports more readings."
- concept: concealed-intent
  relationship: explains
  description: "Design under concealment explains concealed intent — the design state is the shape of the purpose."
- concept: attacker-capability
  relationship: expresses
  description: "Design under concealment expresses attacker capability — the secrecy trade shows what the designer could build."
- concept: incomplete-evidence
  relationship: subject_to
  description: "Design under concealment is subject to incomplete evidence — the design state is inferred, never shown."

## Tradeoffs
- dimension: concealment_strength_vs_artifact_cost
  options:
    strong_concealment:
      value: secrecy
      rationale: "Strong concealment protects the artifact's purpose but costs function, size, and performance."
    weak_concealment:
      value: economy
      rationale: "Light concealment is cheap and functional but leaves the artifact legible."
  importance: high
- dimension: secrecy_vs_robustness
  options:
    secrecy_first:
      value: stealth
      rationale: "Secrecy-first design maximises evasion but trades away robustness and reliability."
    robustness_first:
      value: resilience
      rationale: "Robust designs survive interference but are easier to observe and read."
  importance: high

## Failure Modes
- name: concealment_over_attribution
  description: "Concealment is seen everywhere — ordinary artifact properties are read as designed secrecy."
  likelihood: medium
  observable_evidence: "Designs read as deliberate concealment where economy explains them; 'everything is anti-analysis' analyses"
  detection: "Alternative-explanation review; simplicity checks"
  recovery: "Require concealment evidence; prefer the cheaper explanation"
  retryable: true
- name: design_read_error
  description: "The concealment trade is misread — the secrecy parameter is confused with function, or function with concealment."
  likelihood: medium
  observable_evidence: "Trade features attributed to the wrong purpose; concealment cost read as function; function read as concealment"
  detection: "Tradeoff-mapping review; per-feature purpose audit"
  recovery: "Map each feature to its purpose candidates; keep both readings qualified"
  retryable: true
- name: concealment_blindness
  description: "The designed surface is taken at face value — concealment is not considered and the reading inherits the designed innocence."
  likelihood: high
  observable_evidence: "Surfaces read exactly as presented; 'too clean' artifacts accepted; concealment trade never analysed"
  detection: "Design-state review; the surface/semantics distinction applied to the artifact's shape"
  recovery: "Analyse the concealment trade explicitly; treat convenient surfaces as suspect"
  retryable: true

## Observations
- observation: "The concealment trade is the analyst's second window — what the artifact sacrificed to secrecy reveals what it protects."
  confidence: high
  source: Adversarial engineering tradeoff analysis
- observation: "The design anticipating the analyst is the analyst's permanent context — every reading competes with a designer who predicted readings."
  confidence: high
  source: Concealment practice, epistemic symmetry observation
- observation: "The surface is the concealment's residue — the designed ambiguity is the most reliable trace of the design state."
  confidence: high
  source: Surface analysis

## Constraints
- constraint: "Concealment is a design property of the artifact, visible only as its effects — the design state is never presented."
  type: invariant
  scope: cross-domain
- constraint: "Every surface convenience is a design decision — the convenient reading competes with the concealment hypothesis."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Read the concealment trade — ask what the artifact sacrificed for secrecy."
  rationale: "The sacrifice is the design state made visible."
  evidence_level: high
- heuristic: "Treat convenient surfaces as designed, then verify."
  rationale: "The designer's cheapest tool is a plausible innocent surface."
  evidence_level: high

## Recommendations
- recommendation: "Analyse the secrecy trade for every artifact feature, not just the artifact as a whole."
  context: analysis
  certainty: strong
  rationale: "The per-feature trade is the design state made visible."
- recommendation: "Analyse the secrecy trade explicitly for every artifact."
  context: analysis
  certainty: strong
  rationale: "The trade is the second window onto the design state."
- recommendation: "Keep the concealment hypothesis in every reading set."
  context: analysis
  certainty: strong
  rationale: "Concealment blindness is the designed reading's doorway."

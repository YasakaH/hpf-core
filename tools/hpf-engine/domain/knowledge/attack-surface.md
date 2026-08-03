# Attack Surface

## Identity
- id: attack-surface
- type: concept
- title: Attack Surface
- tags: [security, attack surface, exposure, vulnerability, threat-modelling, reduction]
- entities: [attack surface, exposure, attack vector, entry point, surface reduction, attack path]
- concepts: [attacker-capability, threat-actor, kill-chain, vulnerability-management, zero-trust]

## Claims
- claim: "The attack surface is the set of all points where an attacker can enter or extract data from a system — every network service, interface, endpoint, and input channel."
  certainty: high
  evidence: Security literature, threat modelling practice
  scope: cross-domain
- claim: "Attack surface is a function of what is exposed, not what is known — unmanaged and shadow assets are part of the surface whether or not they are inventoried."
  certainty: high
  evidence: Security research, asset management studies
  scope: cross-domain
- claim: "Attack surface reduction is one of the highest-value defensive strategies — every eliminated entry point eliminates an entire class of attack."
  certainty: high
  evidence: Security best practice literature, defence-in-depth research
  scope: cross-domain
- claim: "The attack surface expands faster than it contracts — new features, integrations, and cloud resources routinely outpace removal of legacy exposure."
  certainty: high
  evidence: Security operations experience, exposure management research
  scope: cross-domain
- claim: "Attack surface and vulnerability are distinct — a large surface with no exploitable vulnerabilities presents less risk than a small surface with one critical flaw."
  certainty: high
  evidence: Security literature, risk analysis
  scope: cross-domain

## Relationships
- concept: attacker-capability
  relationship: multiplied_by
  description: "Attack surface × attacker capability = exploitability — surface size magnifies the impact of any capability level."
- concept: threat-actor
  relationship: targeted_by
  description: "Actors target the attack surface — surface analysis determines which actor paths are available."
- concept: kill-chain
  relationship: entry_point
  description: "The attack surface provides the entry point for the kill chain — no entry, no chain."
- concept: vulnerability-management
  relationship: informs
  description: "Surface analysis defines the scope of vulnerability management — unmanaged surface cannot be scanned."
- concept: zero-trust
  relationship: reduces
  description: "Zero-trust architecture reduces the effective attack surface by removing implicit trust between components."

## Tradeoffs
- dimension: surface_size_vs_functionality
  options:
    minimal_surface:
      value: security
      rationale: "Fewer exposed services and interfaces — smaller attack surface but reduced functionality and convenience."
    broad_surface:
      value: functionality
      rationale: "More services and interfaces — greater capability but a larger surface requiring more defence."
  importance: high
- dimension: surface_reduction_vs_operational_cost
  options:
    aggressive_reduction:
      value: risk_reduction
      rationale: "Aggressively remove/disable exposure — lower risk but requires continuous governance and feature friction."
    selective_reduction:
      value: cost_balance
      rationale: "Reduce only the highest-risk exposure — cheaper but leaves significant surface requiring ongoing monitoring."
  importance: high

## Failure Modes
- name: shadow_asset_exposure
  description: "Unmanaged assets (staging servers, forgotten services, cloud resources) remain exposed outside the known surface — invisible to defence."
  likelihood: high
  observable_evidence: "Attackers pivot through unmanaged assets; scans find services not in the asset inventory; cloud resource sprawl"
  detection: "Continuous asset discovery; network scanning against inventory drift; cloud API inventory checks"
  recovery: "Inventory and manage discovered assets; add discovery to continuous operations; decommission or secure shadow assets"
  retryable: true
- name: surface_scope_mismatch
  description: "The modelled attack surface diverges from the actual surface — threat models reference assets that no longer exist or miss assets that do."
  likelihood: high
  observable_evidence: "Threat models increasingly disconnected from architecture; detection coverage gaps for current services"
  detection: "Periodic threat-model-versus-architecture comparison; inventory drift audits"
  recovery: "Rebuild threat models from current architecture; automate architecture-to-model synchronisation"
  retryable: true
- name: exposure_through_legacy
  description: "Legacy systems remain connected to the network with historical exposure that no current owner claims."
  likelihood: high
  observable_evidence: "Legacy protocols active; unpatched systems with old exposure; no owner for discovered legacy assets"
  detection: "Protocol and port inventory; legacy detection in network scans; ownership audits"
  recovery: "Decommission or isolate legacy systems; enforce ownership for all networked assets"
  retryable: true

## Observations
- observation: "Attack surface grows through integration and feature velocity — most organisations cannot enumerate their full surface at any moment."
  confidence: high
  source: Exposure management research, security operations experience
- observation: "Attack surface reduction (removing exposure) is more durable than patching — eliminated surfaces need no updates."
  confidence: high
  source: Security best practice literature
- observation: "Public cloud has expanded the effective attack surface for most organisations — ephemeral resources outpace governance."
  confidence: high
  source: Cloud security research, incident data

## Constraints
- constraint: "The attack surface can never be fully enumerated — completeness of surface knowledge is asymptotic, not attainable."
  type: invariant
  scope: cross-domain
- constraint: "Every connected component contributes to the surface — unmanaged components still contribute whether or not they are known."
  type: invariant
  scope: cross-domain

## Heuristics
- heuristic: "Assume the surface is larger than the inventory — continuously discover rather than rely on records."
  rationale: "Inventory drift is the norm; continuous discovery keeps the model closer to reality."
  evidence_level: high
- heuristic: "Prefer eliminating exposure over patching it — an unexposed service needs no patches."
  rationale: "Surface elimination is durable; patching is recurring maintenance on an ongoing risk."
  evidence_level: high
- heuristic: "Apply zero-trust segmentation to bound the damage surface — segmenting limits how far an entry point can be leveraged."
  rationale: "Segmentation converts a large flat surface into small bounded ones, limiting kill-chain progression."
  evidence_level: high

## Recommendations
- recommendation: "Run continuous asset discovery and treat inventory drift as a security finding, not an operational nuisance."
  context: security_operations
  certainty: strong
  rationale: "Undiscovered assets are invisible to every other control — discovery is the foundation."
- recommendation: "Require explicit network exposure approval for every new service — default should be non-exposed."
  context: architecture_governance
  certainty: strong
  rationale: "Default-non-exposed reverses the expansion trend; exposure becomes a deliberate decision."
- recommendation: "Audit attack surface reduction opportunities quarterly — removing legacy exposure is cheaper than defending it."
  context: security_strategy
  certainty: strong
  rationale: "Reduction is durable and cost-effective; quarterly audits keep reduction a practice, not a project."

# Browser Fingerprint

## Identity
- id: browser-fingerprint
- type: concept
- title: Browser Fingerprint
- tags: [fingerprint, canvas, webgl, audio, entropy, tracking, detection]
- entities: [canvas fingerprint, WebGL fingerprint, audio fingerprint, font enumeration, fingerprint entropy, cross-session linking]
- concepts: [browser-fingerprint, automation-detection-surface, anti-detection-strategy, browser-profile]

## Metadata
- created: 2026-07-29
- updated: 2026-07-29
- domain: browser-perception
- version: 0.1.0
- research_cycle: 003

## Semantic Layer
- definition: A persistent identifier derived from the combination of browser, device, OS, and configuration characteristics that can identify a browser instance across sessions without relying on cookies or stored state.
- entropy_range: 15-24 bits across all dimensions (sufficient for unique identification among millions of visitors)
- core_dimensions: [canvas2d, webgl, audio, font_enumeration, screen, timezone, platform, hardware_concurrency]
- linkability: Fingerprints link sessions even after cookie clearing. Anti-bot services combine fingerprinting with cookies, IP, and TLS signals for persistent tracking.

## Claims
- claim: "Canvas fingerprint has 4-6 bits of entropy and is the most commonly collected fingerprint dimension across anti-bot services."
  certainty: high
  evidence: Eckersley 2010 (Panopticlick), Laperdrix 2020 (FP survey), FingerprintJS library analysis. Canvas fingerprinting is universally deployed in commercial anti-bot scripts.
  scope: cross-browser
- claim: "WebGL fingerprint has 12-15 bits of entropy, making it the single highest-entropy dimension. It is tied to physical GPU hardware and cannot be changed without changing hardware or using GPU virtualization."
  certainty: high
  evidence: Academic fingerprinting research, verified via testing. WebGL renderer string, vendor string, and extension list are determined by the GPU driver and are stable across browser reinstalls.
  scope: cross-platform
- claim: "Fresh profiles on cloud VMs (no dedicated GPU) produce near-identical fingerprints because they share SwiftShader software rendering, default screen resolution, and minimal font sets."
  certainty: high
  evidence: Observed fingerprint collisions across cloud automation deployments. AWS, GCP, and Azure headless instances produce highly similar canvas/WebGL fingerprints.
  scope: cloud_automation
- claim: "Fingerprint entropy decreases in homogeneous environments (cloud VMs, containers), providing crowd anonymity but reducing the effectiveness of fingerprint-based session blocking."
  certainty: medium
  evidence: When many automated sessions share identical fingerprints, anti-bot services cannot use fingerprint for cross-session linking. However, this also means a single blocked fingerprint blocks all instances.
  scope: cloud_automation
- claim: "Audio fingerprint provides an independent detection dimension that is harder to patch consistently than canvas or WebGL."
  certainty: medium
  evidence: AudioContext rendering depends on the OS audio stack and browser audio pipeline. Patching audio fingerprint requires modifying AudioContext behaviour before page load, which is less commonly implemented than canvas/WebGL patches.
  scope: cross-browser

## Relationships
- concept: automation-detection-surface
  relationship: derived_from
  description: Browser fingerprint is computed from detection surface signals. The detection surface provides raw data; fingerprint is the processed identifier.
- concept: anti-detection-strategy
  relationship: targeted_by
  description: Anti-detection strategies aim to reduce fingerprint entropy, inject noise, or rotate fingerprints across sessions to prevent linking.
- concept: browser-profile
  relationship: amplified_by
  description: Persistent profiles store fingerprint-amplifying state (cookies, cached identifiers, localStorage tracking) that makes cross-session linking more reliable.
- concept: browser-storage
  relationship: persists_via
  description: Storage mechanisms (IndexedDB, Cache API, localStorage) can persist fingerprint-derived identifiers that survive cookie clearing, enabling fingerprint resurrection.
- concept: browser-session-lifecycle
  relationship: established_at
  description: Fingerprint is established at session start and accumulates identifying signals over the session lifetime.

## Tradeoffs
- dimension: fingerprint_consistency_vs_anonymity
  options:
    consistent_fingerprint:
      value: reliable_linking
      rationale: A stable fingerprint across sessions enables persistent authentication and personalisation but enables cross-session tracking.
    rotating_fingerprint:
      value: anonymity
      rationale: Changing fingerprint dimensions across sessions prevents linking but may trigger anti-fraud alerts as "suspicious identity changes."
  importance: critical
- dimension: entropy_vs_collision
  options:
    high_entropy:
      value: unique_identification
      rationale: More fingerprint dimensions with higher precision produce stronger identifiers but increase the signal detectable by anti-fingerprinting tools.
    low_entropy:
      value: crowd_anonymity
      rationale: Fewer or noisier dimensions reduce identifiability but decrease fingerprint usefulness for authentication or personalisation.
  importance: medium
- dimension: headless_vs_headed_fingerprint_gap
  options:
    headless_old:
      value: large_gap
      rationale: Pre-Chrome 112 headless uses software rendering, producing significantly different canvas and WebGL fingerprints from headed mode — easily detected.
    headless_new:
      value: reduced_gap
      rationale: Chrome 112+ shares GPU pipeline between headless and headed, reducing but not eliminating fingerprint differences.
  importance: high

## Failure Modes
- name: fingerprint_collision
  description: Multiple automation instances produce identical fingerprints, allowing anti-bot services to block all instances based on a single fingerprint.
  likelihood: medium
  observable_evidence: All automation instances share same canvas/WebGL values (common in cloud VMs without GPU). A block on one instance leads to blocks on all.
  detection: Fingerprint audit across instances reveals identical values.
  recovery: Introduce controlled variation (viewport size, timezone randomization, font subset variation) across instances.
  prevention: Avoid homogeneous environment configuration. Introduce per-instance variation in non-stable fingerprint dimensions.
  retryable: true
- name: fingerprint_leakage
  description: A persistent fingerprint from a previous session is exposed in a new session, linking sessions that were intended to be isolated.
  likelihood: medium
  observable_evidence: Canvas or WebGL fingerprint from a fresh profile matches the fingerprint from a previous session on the same machine.
  detection: Cross-session fingerprint comparison.
  recovery: Use fresh profile per session. Confirm profile directory is deleted between uses.
  prevention: Always delete and recreate profile directories between sessions. Verify fingerprint uniqueness after profile creation.
  retryable: true
- name: gpu_driver_fingerprint_stability
  description: GPU driver updates change WebGL and canvas fingerprints, breaking fingerprint-based session linking for legitimate multi-session workflows.
  likelihood: low
  observable_evidence: Automated sessions that previously matched a known fingerprint now have a different fingerprint after a GPU driver update.
  detection: Monitor fingerprint stability over time. Log fingerprint dimensions per session for audit.
  recovery: Update saved fingerprint reference after confirming session ownership.
  prevention: Use multiple fingerprint dimensions (not just WebGL) for session identification. No single dimension is fully stable.
  retryable: true

## Decision Factors
- factor: session_linking_requirement
  question: "Do you need to link sessions as belonging to the same user/browser?"
  supporting: "If yes, maintain consistent fingerprint dimensions across sessions. Use persistent profiles to amplify fingerprint stability with stored identifiers."
  contradictory: "Session linking through fingerprints is the same mechanism used by anti-bot services. If you want to avoid detection, you should prevent linking by rotating fingerprints."
  weight: high
- factor: fingerprint_variation_strategy
  question: "Should fingerprint dimensions be consistent, randomized, or omitted?"
  supporting: "Consistent fingerprints enable reliable session identification. Randomized fingerprints prevent linking but may trigger fraud detection. Omitting dimensions reduces fingerprint utility but also reduces detection surface."
  contradictory: "Partial randomization (vary some dimensions, keep others stable) is the most complex to implement but provides the best balance for most use cases."
  weight: medium

## Observations
- observation: "In a study of 286,777 browser fingerprints (Eckersley 2010), 83.6% had unique fingerprints. With modern fingerprint dimensions (WebGL, audio), uniqueness is now estimated at >90% across the general web."
  confidence: high
  source: Eckersley 2010 (Panopticlick study), replicated by Laperdrix 2020 with additional dimensions
- observation: "Cloud VM instances (AWS, GCP, Azure) running headless Chrome produce near-identical canvas fingerprints because they share software rendering (SwiftShader/Mesa)."
  confidence: high
  source: Measured across multiple cloud providers and instance types.
- observation: "Canvas fingerprint differs between headless and headed Chrome even with `--headless=new` because the headless path still bypasses some display-specific rendering steps."
  confidence: high
  source: Community testing, confirmed via browser fingerprint comparison tools.
  protocol: cdp
- observation: "Audio fingerprint (AudioContext-based) is collected by FingerprintJS and several anti-bot services but is less commonly patched by stealth libraries than canvas or WebGL."
  confidence: medium
  source: Analysis of common stealth libraries (puppeteer-extra-stealth, undetected-chromedriver). Audio patching is absent from most.
  protocol: cdp

## Constraints
- constraint: "WebGL fingerprint is tied to physical GPU hardware; software-only fingerprint manipulation cannot change the GPU-specific values returned by the driver."
  type: invariant
  scope: all platforms
  violation_consequence: WebGL fingerprint will always reveal the underlying GPU, even with full JS property patching.
- constraint: "Canvas fingerprint varies between operating systems, GPU drivers, and browser versions. A fingerprint generated on one system will not match another, even with identical browser configuration."
  type: invariant
  scope: cross-platform
  violation_consequence: Canvas fingerprint is not portable across machines. Cross-machine session linking requires additional identifiers.
- constraint: "Font enumeration returns the OS-installed font set. In headless Linux environments, this is typically 30-100 fonts vs 200-500+ on a normal desktop, creating a detectable mismatch."
  type: conditional
  scope: Linux headless automation
  violation_consequence: Low font count is a strong detection signal.
- constraint: "Headless mode (pre-112) reports `navigator.gpu` as absent and WebGL renderer as SwiftShader. `--headless=new` reduces but does not eliminate these differences."
  type: conditional
  scope: Chrome automation
  violation_consequence: Absence of GPU API or software rendering detection can identify automation.
- constraint: "Fingerprint dimension values can change with browser updates, OS updates, GPU driver updates, or hardware changes. No single dimension is fully stable across time."
  type: invariant
  scope: all environments
  violation_consequence: Long-lived fingerprints require periodic refresh to remain accurate.

## Heuristics
- heuristic: "Use WebGL dimension for the most stable cross-session fingerprint identifier, but combine with canvas for reliability against GPU driver updates."
  rationale: "WebGL is tied to physical hardware and is the highest-entropy dimension. Canvas provides an independent signal that varies with GPU driver versions, providing a secondary check."
  applicability: Session identification systems
  evidence_level: high
- heuristic: "In homogeneous automation environments (cloud VMs), introduce controlled fingerprint variation to avoid mass blocking from fingerprint collision."
  rationale: "Identical fingerprints across instances mean one block blocks all. Per-instance viewport size, timezone, and font subset variation reduces collision risk."
  applicability: Cloud-based automation deployments
  evidence_level: high
- heuristic: "For anti-detection, focus on breaking cross-session fingerprint linking (fresh profile per session) rather than trying to match a real-browser fingerprint perfectly."
  rationale: "Perfect fingerprint mimicry is extremely difficult across all dimensions simultaneously. Fresh profiles ensure each session appears as a new browser, regardless of fingerprint matching quality."
  applicability: Anti-detection strategy
  evidence_level: high
- heuristic: "If fingerprint consistency is required (multi-session auth), use persistent profiles with stored identifiers rather than relying on passive fingerprint dimensions alone."
  rationale: "Stored identifiers (cookies, localStorage tokens, IndexedDB) are more reliable than passive fingerprint dimensions, which can change with hardware/software updates."
  applicability: Multi-session authenticated automation
  evidence_level: high
- heuristic: "Audit fingerprint dimensions quarterly. GPU driver updates, OS patches, and browser version changes can alter fingerprint values unexpectedly."
  rationale: "Fingerprint dimensions are not fully static. Regular auditing detects unexpected changes and prevents session linking failures."
  applicability: Deployments relying on fingerprint-based session identification
  evidence_level: moderate

## Recommendations
- recommendation: "Use fresh profile per session to break cross-session fingerprint linking as the primary anti-detection mechanism."
  context: anti_detection
  certainty: strong
  rationale: "Fresh profiles prevent fingerprint linking more reliably than fingerprint manipulation. Each session appears as a new, never-before-seen browser. This is simpler and more effective than attempting to match a real-browser fingerprint."
- recommendation: "In cloud automation environments, introduce per-instance viewport and timezone variation to avoid fingerprint collision blocking."
  context: cloud_automation
  certainty: strong
  rationale: "Homogeneous cloud environments produce identical fingerprints. Per-instance variation prevents mass blocking from a single fingerprint block."
- recommendation: "Do not rely solely on canvas fingerprint for cross-session identification — WebGL + canvas + font enumeration provides more reliable identification across software updates."
  context: session_identification
  certainty: strong
  rationale: "Canvas fingerprint can change with GPU driver updates. Multi-dimension fingerprinting provides robustness against single-dimension changes."
- recommendation: "Patch audio fingerprint alongside canvas and WebGL — it is an independent detection dimension that is commonly collected but less commonly patched."
  context: comprehensive_anti_detection
  certainty: moderate
  rationale: "Audio fingerprinting is deployed by FingerprintJS and several anti-bot services but is absent from most stealth libraries. Patching it closes an overlooked detection vector."

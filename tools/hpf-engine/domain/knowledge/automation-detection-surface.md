# Automation Detection Surface

## Identity
- id: automation-detection-surface
- type: concept
- title: Automation Detection Surface
- tags: [detection, signals, fingerprint, anti-bot, evasion]
- entities: [navigator.webdriver, CDP WebSocket, TLS fingerprint, behavioral detection, anti-bot service]
- concepts: [automation-detection-surface, browser-fingerprint, anti-detection-strategy]

## Metadata
- created: 2026-07-29
- updated: 2026-07-29
- domain: browser-perception
- version: 0.1.0
- research_cycle: 003

## Semantic Layer
- definition: The complete set of observable signals that websites use to distinguish automated browser sessions from human-driven sessions, spanning JavaScript properties, protocol-level indicators, process environment characteristics, network fingerprints, and behavioural patterns.
- detection_principle: Anti-bot services correlate multiple independent signals because any single signal can be patched, but maintaining consistency across all signals simultaneously is exponentially harder.
- signal_categories: [javascript_properties, protocol_signals, process_environment, network_fingerprint, behavioural_patterns]
- arms_cycle: Detection signal introduction -> stealth patch -> detection service adaptation -> new signal introduction (3-9 month half-life per signal)

## Claims
- claim: "The most reliable detection signals are not single properties but inconsistencies between multiple properties."
  certainty: high
  evidence: Analysis of major anti-bot service detection scripts; a patched `navigator.webdriver` without matching `navigator.plugins` and `chrome.app` shape is still detectable. Multi-signal correlation is standard practice.
  scope: cross-browser
- claim: "TLS fingerprint (JA3/JA3S) manipulation is the highest-friction anti-detection technique because it requires controlling the TCP/TLS stack, which most automation frameworks delegate to the operating system."
  certainty: high
  evidence: CDP and WebDriver operate at the application layer; they do not expose TLS stack configuration. Proxy-level TLS mimicry (ja3proxy, tls-client) is the only viable approach for most deployments.
  scope: cross-platform
- claim: "Detection surface signals have a half-life of 3-9 months before anti-bot services adapt to new stealth patches."
  certainty: medium
  evidence: Community-maintained stealth libraries (puppeteer-extra-stealth, undetected-chromedriver) show periodic patch updates every 3-9 months. Anti-bot service changelogs (Cloudflare, Datadome) reference new detection signals at similar intervals.
  scope: general
- claim: "Behavioural detection (mouse movement, scrolling, typing patterns) is not widely deployed in production anti-bot services; its effectiveness is unconfirmed."
  certainty: medium
  evidence: No major anti-bot service publishes behavioural detection specifications. Community reports are contradictory. Academic research shows feasibility but no confirmed production deployment.
  scope: general

## Relationships
- concept: browser-fingerprint
  relationship: composes
  description: Detection surface signals are the raw inputs to browser fingerprint computation. Fingerprint is derived from surface signals.
- concept: anti-detection-strategy
  relationship: modifies
  description: Anti-detection strategies are defined by which detection surface signals they patch. Strategy effectiveness is measured by remaining detectable signal count.
- concept: automation-protocol
  relationship: determines
  description: Protocol choice (CDP vs WebDriver vs BiDi) determines which protocol-level signals are exposed on the detection surface.
- concept: browser-profile
  relationship: amplifies
  description: Persistent profiles extend the detection surface across sessions by carrying stored identifiers that link sessions.
- concept: browser-session-lifecycle
  relationship: varies_with
  description: Detection surface signals differ across lifecycle states — a fresh session has fewer accumulated signals than an aged session.

## Tradeoffs
- dimension: detection_risk_vs_patching_depth
  options:
    shallow_patching:
      value: higher_detection_risk
      rationale: Patching only `navigator.webdriver` leaves other signals (chrome.app, plugins, TLS fingerprint) exposed, making detection likely against sophisticated services.
    deep_patching:
      value: lower_detection_risk
      rationale: Coordinated patching across JS properties, protocol signals, and environment characteristics significantly reduces detection probability but increases maintenance burden and complexity.
  importance: critical
- dimension: maintenance_vs_effectiveness
  options:
    low_maintenance:
      value: decreases_over_time
      rationale: A static set of patches that worked 6 months ago will be less effective as anti-bot services discover new signals and update detection models.
    high_maintenance:
      value: sustained
      rationale: Regular updates to match current detection landscape maintain effectiveness but require ongoing engineering investment.
  importance: operational
- dimension: detection_accuracy_vs_false_positives
  options:
    high_sensitivity:
      value: catches_more_automation
      rationale: Aggressive detection (Cloudflare Turnstile, Datadome) catches most automation but also flags some legitimate users (VPN users, headless browsers, users with unusual configurations).
    low_sensitivity:
      value: misses_some_automation
      rationale: Conservative detection catches only obvious automation signals but may miss sophisticated automation deployments.
  importance: medium

## Failure Modes
- name: patch_inconsistency
  description: Patching one signal without coordinating related signals creates detectable inconsistencies that reveal automation.
  likelihood: high
  observable_evidence: Detection scripts find `navigator.webdriver` patched but `chrome.app.isInstalled` returning unexpected values, or `navigator.plugins` shape contradicts `navigator.platform`.
  detection: Cross-signal correlation by anti-bot services.
  recovery: Audit all patched signals for consistency with the target browser profile. Use comprehensive stealth libraries rather than ad-hoc patches.
  prevention: Test patches against known detection scripts. Maintain a signal consistency matrix.
  retryable: true
- name: patch_detection
  description: The patching mechanism itself is detectable — patching scripts have observable signatures (function toString output, property descriptor inspection, timing analysis).
  likelihood: medium
  observable_evidence: Anti-bot JS checks detect `Function.prototype.toString` on patched getters, find property descriptors with `configurable: false` on normally configurable properties, or observe timing anomalies from init script execution.
  detection: Property descriptor inspection, function toString comparison against known browser implementation.
  recovery: Use native-code-level property overrides where available. Minimize init script footprint.
  prevention: Reduce init script complexity. Use browser-native mechanisms (CDP `setWebdriverEnabled`) where available.
  retryable: true
- name: signal_decay
  description: A patching strategy that was effective 6 months ago is no longer effective because anti-bot services have added new detection signals or adapted to known patches.
  likelihood: high
  observable_evidence: Previously working automation deployment begins receiving challenges, CAPTCHAs, or blocks.
  detection: Monitor block rate over time. A gradual increase in detection rate without infrastructure changes suggests signal decay.
  recovery: Update stealth patches to latest versions. Audit current detection surface for new signals.
  prevention: Subscribe to community intelligence (GitHub issues, automation forums). Schedule regular patch review.
  retryable: true

## Decision Factors
- factor: detection_sensitivity_required
  question: "What detection probability is acceptable for this workload?"
  supporting: "Low-value scraping may tolerate 10-20% detection rate. High-value production pipelines may require <1%. Acceptable detection probability determines patching depth investment."
  contradictory: "Lower acceptable detection probability requires exponentially more patching effort. The relationship is not linear — moving from 5% to 1% detection rate may require significantly more investment than moving from 20% to 5%."
  weight: high
- factor: maintenance_capacity
  question: "Can the automation deployment support ongoing stealth patch maintenance?"
  supporting: "Dedicated anti-detection teams can sustain deep patching strategies. Small teams or individual developers should prefer simpler, lower-maintenance approaches and accept higher detection rates."
  contradictory: "Some stealth library maintainers provide regular updates (puppeteer-extra-stealth). Using well-maintained community libraries reduces individual maintenance burden."
  weight: high
- factor: target_diversity
  question: "How many different target sites does the automation interact with?"
  supporting: "Automating against a single target allows targeted anti-detection optimization for that site's specific detection service. Automating against many targets requires a general-purpose strategy that works across detection services."
  contradictory: "Targeted optimization creates dependency on a single target's detection profile. If the target changes detection services, the optimized strategy may fail."
  weight: medium

## Observations
- observation: "Cloudflare Turnstile challenges appeared in late 2022 and have become the most widely deployed anti-bot challenge, present on an estimated 20%+ of the web."
  confidence: high
  source: Cloudflare blog, web census data, community reports
- observation: "The `chrome.app.isInstalled` property returns `false` in normal Chrome and throws a TypeError in headless Chrome, but returns `undefined` in some patched configurations — a detectable inconsistency."
  confidence: high
  source: puppeteer-extra-stealth source analysis, confirmed via testing across Chrome versions 90-126
- observation: "Headless Chrome (pre-112) renders Canvas2D differently from headed Chrome because it uses Mesa/llvmpipe software rendering, producing measurably different canvas fingerprints."
  confidence: high
  source: Academic fingerprinting research, confirmed via browser testing.
  protocol: cdp
- observation: "The `--headless=new` mode (Chrome 112+) shares the GPU rendering pipeline with headed mode, reducing the canvas and WebGL fingerprint gap but not eliminating it."
  confidence: high
  source: Chrome platform status, community testing.
  protocol: cdp

## Constraints
- constraint: "JavaScript property patches must execute before any page script runs; CDP `Page.addScriptToEvaluateOnNewDocument` provides this guarantee but adds measurable latency before pages can begin loading."
  type: invariant
  scope: CDP-based automation
  violation_consequence: If patching script executes after page scripts, detection scripts can observe unpatched properties.
- constraint: "TLS and HTTP/2 fingerprints cannot be modified from JavaScript; they require external proxy or custom browser build."
  type: invariant
  scope: all automation
  violation_consequence: TLS fingerprint will reflect the automation host's TLS stack, not a real browser's.
- constraint: "Behavioural simulation cannot fully replicate human behaviour; fractal complexity of natural movement exceeds current simulation capabilities."
  type: conditional
  scope: all automation
  violation_consequence: Sophisticated behavioural detection may identify simulated behaviour through statistical analysis of movement and timing distributions.
- constraint: "Anti-bot services continuously discover new detection signals; no patching strategy provides permanent effectiveness."
  type: invariant
  scope: all anti-detection
  violation_consequence: Detection rate will increase over time without ongoing patch maintenance.

## Heuristics
- heuristic: "Patch signals in groups, not isolation. If patching `navigator.webdriver`, also patch `navigator.plugins`, `navigator.languages`, `chrome.runtime`, and `chrome.app`."
  rationale: "Anti-bot services check multiple signals and flag inconsistencies. Isolated patches are easily detected."
  applicability: All anti-detection deployments
  evidence_level: high
- heuristic: "Use `--headless=new` (Chrome 112+) over `--headless=old` — it shares more of the GPU stack with headed mode, reducing canvas/WebGL fingerprint differences."
  rationale: "The new headless mode uses the same GPU rendering pipeline as headed mode, producing more realistic canvas and WebGL fingerprints."
  applicability: Chrome automation
  evidence_level: high
- heuristic: "Test stealth patches against known detection scripts (FingerprintJS, Cloudflare challenge page, sannysoft.com) before production deployment."
  rationale: "Detection scripts evolve faster than documentation. Practical testing against current detection tools is more reliable than theoretical patch analysis."
  applicability: All anti-detection deployments
  evidence_level: high
- heuristic: "Prefer well-maintained community stealth libraries over custom patches for general-purpose anti-detection."
  rationale: "Libraries like puppeteer-extra-stealth track detection service updates across multiple signals and browser versions, providing broader coverage than most custom implementations."
  applicability: Teams without dedicated anti-detection expertise
  evidence_level: moderate
- heuristic: "Monitor block/CAPTCHA rate as a continuous metric, not a one-time check — detection effectiveness decays over time."
  rationale: "Signal decay means a strategy that works today may fail in 3-9 months. Monitoring detection rate trends enables proactive maintenance."
  applicability: Production automation deployments
  evidence_level: high

## Recommendations
- recommendation: "Implement layered anti-detection: patch at least JS properties (layer 1), protocol flags (layer 2), and environment consistency (layer 3) for any production deployment."
  context: production_automation
  certainty: strong
  rationale: "Single-layer patching is insufficient against sophisticated anti-bot services. Three layers provide defence in depth with reasonable maintenance burden."
- recommendation: "Use residential proxies for high-value automation targets. IP reputation is the highest-weight single signal for most anti-bot services."
  context: high_value_target
  certainty: strong
  rationale: "IP reputation bypass is operationally simpler than perfecting JS/TLS/behavioural patches. A clean IP with reasonable patching is more effective than perfect patches on a flagged IP."
- recommendation: "Do not rely on behavioural simulation (mouse movement, typing patterns) as a primary anti-detection strategy — its effectiveness in production anti-bot services is unconfirmed."
  context: anti_detection_investment
  certainty: moderate
  rationale: "Engineering time spent on behavioural simulation may be better invested in IP quality, TLS fingerprint management, and comprehensive JS property patching, which have confirmed effectiveness."
- recommendation: "Schedule quarterly stealth patch reviews. Detection signal half-life is 3-9 months; quarterly reviews catch decay before it impacts production."
  context: production_maintenance
  certainty: strong
  rationale: "Signal decay is gradual. Quarterly review cadence allows proactive updating before detection rate increases impact operations."

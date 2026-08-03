# Anti-Detection Strategy

## Identity
- id: anti-detection-strategy
- type: concept
- title: Anti-Detection Strategy
- tags: [anti-detection, stealth, patching, bypass, evasion, fingerprint, proxy]
- entities: [stealth patch, property override, TLS fingerprint, behavioural simulation, proxy rotation, detection avoidance]
- concepts: [anti-detection-strategy, automation-detection-surface, browser-fingerprint, automation-protocol, browser-profile]

## Metadata
- created: 2026-07-29
- updated: 2026-07-29
- domain: browser-perception
- version: 0.1.0
- research_cycle: 003

## Semantic Layer
- definition: A systematic approach to modifying the browser automation detection surface to reduce the probability that a website identifies an automated session as automated. Strategies are layered — each layer patches different detection signals — and effectiveness is probabilistic, not binary.
- principle: Layered defence — failure of one layer should not expose the session. Multi-signal correlation by anti-bot services means patching must be comprehensive across independent signal categories.
- decay_rate: Detection signal half-life is 3-9 months; anti-detection strategies require ongoing maintenance.
- strategy_layers: [javascript_property_patching, protocol_flag_manipulation, environment_consistency, tls_network_fingerprint, infrastructure, behavioural_simulation]

## Claims
- claim: "IP reputation is the single highest-weight signal for most commercial anti-bot services (Cloudflare, Datadome, Akamai). A clean residential proxy with minimal JS patching outperforms perfect JS/TLS patches on a flagged IP."
  certainty: high
  evidence: Community reports across automation forums, Cloudflare documentation referencing IP-based threat scoring. Observed behaviour: changing IP resolves detection without changing any browser configuration in many cases.
  scope: general
- claim: "Patching `navigator.webdriver` alone provides negligible protection against sophisticated anti-bot services — they check multiple signals and detect patching inconsistencies."
  certainty: high
  evidence: Analysis of detection scripts from major anti-bot services. All check multiple navigator properties, chrome object shape, timing signals, and property descriptor integrity.
  scope: cross-browser
- claim: "Behavioural simulation (mouse movement, typing patterns, scrolling) is not confirmed to be deployed in production anti-bot services. Its effectiveness for anti-detection is theoretical."
  certainty: medium
  evidence: No major anti-bot service publishes behavioural detection capability. Academic research demonstrates feasibility. Community evidence on actual deployment is contradictory and anecdotal.
  scope: general
- claim: "No anti-detection strategy provides permanent protection. The arms race between automation and detection services requires continuous maintenance — a fixed strategy will degrade in effectiveness within 3-9 months."
  certainty: high
  evidence: Historical pattern of stealth library updates, changelog analysis of anti-bot services, observed decay in strategy effectiveness over time.
  scope: general

## Relationships
- concept: automation-detection-surface
  relationship: modifies
  description: Anti-detection strategy is defined by which detection surface signals it patches. The strategy's effectiveness is measured by the count and significance of remaining detectable signals.
- concept: browser-fingerprint
  relationship: manipulates
  description: Anti-detection strategies either reduce fingerprint entropy (fewer distinguishable dimensions), inject noise (varying dimensions per session), or rotate fingerprints (fresh profile per session).
- concept: automation-protocol
  relationship: constrained_by
  description: Protocol choice determines which anti-detection techniques are available. CDP allows `Page.addScriptToEvaluateOnNewDocument` for pre-load JS patching. WebDriver has more limited injection capabilities. BiDi is still evolving.
- concept: browser-profile
  relationship: profile_strategy
  description: Profile strategy (fresh vs persistent) is a fundamental anti-detection decision. Fresh profiles prevent cross-session linking. Persistent profiles carry fingerprintable state across sessions.
- concept: browser-session-lifecycle
  relationship: timing_dependent
  description: Anti-detection patches must be applied at specific lifecycle points (before page load, on navigation, after session creation). Late patches may not prevent initial detection.

## Tradeoffs
- dimension: patching_depth_vs_maintenance
  options:
    shallow_strategy:
      value: low_maintenance_higher_detection
      rationale: Patch only obvious signals (navigator.webdriver, user agent). Quick to implement but easily detected by sophisticated services.
    deep_strategy:
      value: high_maintenance_lower_detection
      rationale: Comprehensive patching across all signal categories (JS properties, protocol, environment, TLS, infrastructure). Lower detection risk but significant maintenance burden.
  importance: critical
- dimension: infrastructure_vs_patching_investment
  options:
    invest_in_proxies:
      value: high_impact_simple_setup
      rationale: Residential proxies bypass IP reputation checks, which is the highest-weight single detection signal. Simple to implement but recurring cost.
    invest_in_patches:
      value: lower_cost_complex_setup
      rationale: JS/TLS/behavioural patching avoids proxy costs but requires significant engineering investment and ongoing maintenance.
  importance: operational
- dimension: profile_freshness_vs_session_continuity
  options:
    fresh_profile_per_session:
      value: best_isolation
      rationale: Eliminates cross-session linking entirely. Each session is a clean slate. But loses auth state, cached resources, and session continuity.
    persistent_profile:
      value: operational_convenience
      rationale: Maintains auth state and cached resources across sessions. But accumulates tracking state and enables cross-session fingerprint linking.
  importance: high

## Failure Modes
- name: inconsistent_patching
  description: Patching some signals while leaving related signals unpatched creates detectable inconsistencies. Example: patching `navigator.webdriver` to false but `chrome.runtime` remains present when it should not be.
  likelihood: high
  observable_evidence: Anti-bot service detects automation despite individual signal patches. Cross-signal correlation reveals inconsistencies.
  detection: Run known detection scripts (FingerprintJS, sannysoft) against patched browser and inspect all signals.
  recovery: Audit all patched signals for consistency. Use comprehensive stealth library rather than ad-hoc patches.
  prevention: Maintain a signal consistency matrix. Patch signals in related groups, not individually.
  retryable: true
- name: patch_signature_detection
  description: The patching mechanism itself is detectable through property descriptor inspection, Function.prototype.toString comparison, or timing analysis.
  likelihood: medium
  observable_evidence: Anti-bot JS checks detect Overridden property descriptors. Detected. Timing analysis reveals patching script execution latency.
  detection: Compare patched property descriptors against known browser implementations. Measure init script execution timing.
  recovery: Use native property overrides where available. Minimize patching script complexity.
  prevention: Use CDP-native mechanisms (setWebdriverEnabled, addInitScript with minimal payload) instead of extensive custom overrides.
  retryable: true
- name: strategy_decay
  description: A strategy that was effective 6 months ago no longer prevents detection because anti-bot services have added new signals or adapted to known patches.
  likelihood: high
  observable_evidence: Gradually increasing block rate or CAPTCHA frequency without any infrastructure or workload changes.
  detection: Monitor detection rate over time. Compare current block rate against historical baseline.
  recovery: Update stealth patches to latest versions. Audit current detection tools for new signals.
  prevention: Schedule regular (quarterly) strategy review. Subscribe to community intelligence feeds.
  retryable: true
- name: overpatching
  description: Excessive or aggressive patching creates a browser environment that behaves detectably differently from a normal browser, paradoxically increasing detection risk.
  likelihood: low
  observable_evidence: Overriding properties that anti-bot services do not check creates detectable behaviour (JS errors from missing expected properties, missing functionality).
  detection: A/B test patched vs unpatched configuration against target sites.
  recovery: Remove unnecessary patches. Test each patch individually for side effects.
  prevention: Only patch signals that are actively checked by target anti-bot services. Prefer targeted patching over blanket property overrides.
  retryable: true

## Decision Factors
- factor: target_detection_sophistication
  question: "What anti-bot services protect the target website?"
  supporting: "A target using Cloudflare Turnstile requires different patching than a target using Datadome. Strategy should be tailored to the specific detection service's known signals."
  contradictory: "Tailoring to a specific detection service creates dependency. If the target changes services, the strategy may fail. General-purpose strategies are more resilient."
  weight: high
- factor: acceptable_detection_rate
  question: "What detection probability is operationally acceptable?"
  supporting: "Low-value scraping at scale can tolerate 10-20% detection rate with retry logic. High-value production pipelines may require <1%. Each order of magnitude reduction requires exponentially more investment."
  contradictory: "The cost of reducing detection rate from 2% to 1% may equal the cost of reducing from 20% to 2%. Diminishing returns are significant."
  weight: high
- factor: maintenance_capacity
  question: "Can the engineering team sustain ongoing anti-detection maintenance?"
  supporting: "Dedicated anti-detection engineering enables deep, custom strategies. Small teams should prefer simpler strategies that leverage well-maintained community libraries."
  contradictory: "Community libraries provide broad coverage but update on their schedule, not yours. If a critical target changes detection services, you may need to wait for library updates."
  weight: high
- factor: cost_constraint
  question: "What is the budget for proxy infrastructure?"
  supporting: "Sufficient proxy budget simplifies anti-detection significantly — IP quality is the highest-weight signal. Residential proxies are expensive but effective."
  contradictory: "Proxy costs scale linearly with traffic volume. High-volume automation may find JS/TLS patching more cost-effective than purchasing sufficient proxy bandwidth."
  weight: medium

## Observations
- observation: "puppeteer-extra-stealth patches 20+ JavaScript properties including navigator.webdriver, navigator.plugins, navigator.languages, chrome.runtime, chrome.app, chrome.csi, and WebGL vendor/renderer strings."
  confidence: high
  source: puppeteer-extra-stealth source code, confirmed via testing.
  protocol: cdp
- observation: "undetected-chromedriver uses a multi-pronged approach: patches navigator.webdriver via CDP, removes --automation flag from Chrome command line, masks CDP WebSocket connection, and applies JS property patches."
  confidence: high
  source: undetected-chromedriver source code, confirmed via testing.
  protocol: cdp
- observation: "Cloudflare Turnstile checks multiple browser signals including navigator.webdriver, chrome.runtime existence, chrome.app.isInstalled, plugins array length, and WebGL renderer string."
  confidence: high
  source: Reverse engineering of Turnstile challenge page, community documentation.
- observation: "Changing from a flagged datacenter IP to a residential IP resolves CAPTCHA/block challenges in approximately 70% of cases without any browser configuration change."
  confidence: medium
  source: Community reports, anecdotal evidence from automation forums. Exact percentage varies by target and anti-bot service.
- observation: "The `--headless=new` flag (Chrome 112+) removes the `HeadlessChrome` substring from the user agent, eliminating the most obvious headless UA signal."
  confidence: high
  source: Chrome platform status documentation, confirmed via testing.
  protocol: cdp

## Constraints
- constraint: "JS property patches must execute before any page script; `Page.addScriptToEvaluateOnNewDocument` provides this but only for CDP — WebDriver has no equivalent pre-load injection mechanism."
  type: invariant
  scope: CDP automation
  violation_consequence: Without pre-load injection, detection scripts can observe unpatched properties during page load.
- constraint: "TLS fingerprint cannot be modified from within the browser JavaScript context; requires external proxy or custom browser build."
  type: invariant
  scope: all automation
  violation_consequence: Browser-originated TLS connections will use the host OS TLS stack, producing a potentially detectable JA3/JA3S fingerprint.
- constraint: "Headless mode (even `--headless=new`) exposes some detectable differences from headed Chrome — no single Chrome flag eliminates all detection signals."
  type: conditional
  scope: Chrome automation
  violation_consequence: Even with all flags set to mimic headed mode, some internal differences remain and can be detected by instrumented Chrome builds.
- constraint: "Community stealth libraries update on their maintainer's schedule, not yours. Version pinning prevents unexpected changes but also prevents receiving security/detection updates."
  type: invariant
  scope: community library usage
  violation_consequence: Pinned stealth libraries may become ineffective over time as detection services adapt.
- constraint: "Anti-bot services A/B test detection thresholds. A strategy that works for 90% of sessions may fail for 10% if your session falls into a test group with stricter detection."
  type: conditional
  scope: all automation
  violation_consequence: Non-deterministic detection means a strategy's effectiveness cannot be fully verified before deployment.

## Heuristics
- heuristic: "Start with IP quality (residential proxy) as the foundation, then add JS patching for defence in depth. IP alone defeats many detection services."
  rationale: "IP reputation is the highest-weight single signal. Clean IPs bypass the majority of detection checks. JS patching covers the remaining signals. This ordering prioritises highest-impact investment."
  applicability: Production automation deployments
  evidence_level: high
- heuristic: "Test anti-detection strategy against the actual anti-bot service on the target site, not against generic detection checkers."
  rationale: "Generic detection checkers (FingerprintJS, sannysoft) test general browser consistency. Target-specific anti-bot services may check different signals. Test against the actual challenge page for accurate results."
  applicability: Target-specific automation
  evidence_level: high
- heuristic: "Version-pin stealth libraries and test before updating. Community updates may introduce regressions or change browser behaviour in unexpected ways."
  rationale: "Stealth patches modify core browser APIs. Updates may break automation flows or introduce new detectable patterns. Controlled testing prevents production incidents."
  applicability: Production deployments using community stealth libraries
  evidence_level: high
- heuristic: "For multi-session automation against the same target, rotate both IP and fingerprint on a schedule that exceeds the target's session timeout."
  rationale: "Static IP + static fingerprint across sessions enables reliable tracking by anti-bot services. Rotating both simultaneously breaks the cross-session link."
  applicability: High-volume multi-session automation
  evidence_level: moderate
- heuristic: "Prioritise patching signals that are commonly checked and easy to verify (navigator.webdriver, user agent, screen resolution, plugins) before investing in complex patches (TLS, behavioural)."
  rationale: "The frequently-checked signals are well-documented and easy to patch. Exotic signals (TLS, behavioural) are harder to patch and may not even be checked by your target's anti-bot service."
  applicability: New anti-detection deployments
  evidence_level: high

## Recommendations
- recommendation: "Implement layered anti-detection with at least JS property patching (layer 1), protocol flag manipulation (layer 2), and infrastructure (layer 5) for any production deployment."
  context: production_automation
  certainty: strong
  rationale: "Single-layer patching is insufficient. Three layers provide defence in depth: JS patches cover property checks, flag manipulation covers environment signals, and IP quality covers reputation checks."
- recommendation: "Use residential proxies (not datacenter) for high-value targets. The cost is justified by the significantly lower detection rate."
  context: high_value_target
  certainty: strong
  rationale: "IP reputation is the single highest-weight detection signal. Residential proxies bypass this check entirely, reducing detection rate more than any browser-level patch."
- recommendation: "Do not implement custom behavioural simulation (mouse movement, typing) for production anti-detection without first confirming it is actually deployed on your target site."
  context: anti_detection_investment
  certainty: strong
  rationale: "Behavioural detection deployment in production anti-bot services is unconfirmed. Engineering time spent on behavioural simulation may have zero return."
- recommendation: "Schedule quarterly anti-detection strategy reviews. Detection signal half-life is 3-9 months; quarterly reviews enable proactive maintenance before degradation impacts operations."
  context: production_maintenance
  certainty: strong
  rationale: "Anti-detection effectiveness decays predictably. Regular review and update cadence prevents sudden detection rate increases."
- recommendation: "Test anti-detection strategy weekly against the actual target site. Detection service changes can happen at any time and may not be announced."
  context: continuous_monitoring
  certainty: strong
  rationale: "Weekly testing provides early warning of detection strategy degradation, enabling proactive response before production impact."

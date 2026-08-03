# Automation Protocol

## Identity
- id: automation-protocol
- type: concept
- title: Automation Protocol
- tags: [cdp, webdriver, bidi, protocol, architecture, transport]
- entities: [cdp, chrome devtools protocol, webdriver, webdriver bidi, json-rpc, websocket, http]
- concepts: [automation-protocol, browser-session-lifecycle, automation-detection-surface]

## Claims
- claim: "CDP is a JSON-RPC protocol over WebSocket that exposes every internal Chromium debugging primitive."
  certainty: high
  evidence: Chromium source code, CDP documentation
  scope: Chromium-specific
- claim: "WebDriver Classic is a W3C-standardised HTTP API that abstracts browser internals behind a session model."
  certainty: high
  evidence: W3C WebDriver specification
  scope: cross-browser
- claim: "WebDriver BiDi combines the standardisation of WebDriver with the streaming capability of CDP using JSON-RPC over WebSocket."
  certainty: high
  evidence: W3C BiDi specification (working draft)
  scope: cross-browser
- claim: "BiDi's script module provides execution world isolation — automation scripts and page scripts run in separate JavaScript contexts."
  certainty: medium
  evidence: W3C BiDi specification (script module), community analysis
  scope: BiDi-specific
- claim: "Protocol migration is trending toward standardised protocols (BiDi) but CDP will remain relevant for legacy systems and Chromium-specific features."
  certainty: medium
  evidence: Framework adoption patterns, BiDi module coverage status
  scope: industry-wide

## Relationships
- concept: browser-session-lifecycle
  relationship: defines
  description: Each protocol defines what lifecycle states are visible, controllable, and detectable.
- concept: automation-detection-surface
  relationship: determines
  description: Protocol choice determines the set of observable detection signals exposure.
- concept: browser-readiness-model
  relationship: influences
  description: Protocol command semantics affect how readiness is determined and exposed.
- concept: cdp-mechanics
  relationship: specialises
  description: CDP is one instantiation of the automation protocol concept.
- concept: webdriver-classic
  relationship: specialises
  description: WebDriver Classic is a standardised HTTP-based instantiation.
- concept: webdriver-bidi
  relationship: specialises
  description: WebDriver BiDi is an emerging standardised WebSocket-based instantiation.

## Tradeoffs
- dimension: capability_vs_standardisation
  options:
    cdp:
      value: maximum_capability
      rationale: Full access to every Chromium debugging primitive; tightly coupled to browser version
    webdriver_classic:
      value: maximum_standardisation
      rationale: W3C-defined; works across browsers; limited to session-level commands
    webdriver_bidi:
      value: balanced
      rationale: Standardised protocol with CDP-level streaming; module coverage still in draft
  importance: critical
- dimension: detectability
  options:
    cdp:
      value: high
      rationale: Well-profiled by anti-bot services; multiple unique signals (WS header, navigator.webdriver, chrome.app)
    webdriver_classic:
      value: high
      rationale: navigator.webdriver is W3C-specified; HTTP model adds timing signals
    webdriver_bidi:
      value: medium
      rationale: Less profiled; execution isolation reduces signal surface; advantage is temporary
  importance: high
- dimension: performance
  options:
    cdp:
      value: high
      rationale: Single persistent WebSocket; no HTTP overhead; push events
    webdriver_classic:
      value: lower
      rationale: Each command is an HTTP round-trip; poll-based event model
    webdriver_bidi:
      value: high
      rationale: Single persistent WebSocket; push events; module-level commands
  importance: operational

## Failure Modes
- name: protocol_version_mismatch
  description: Browser version and protocol version are incompatible, causing commands to fail or behave unexpectedly.
  likelihood: medium
  observable_evidence: Command returns unknown method error, browser ignores incoming commands, or returns malformed responses
  detection: Log error messages on command execution; compare protocol versions on connect
  recovery: Update automation tool to match browser version, or pin browser to tool-compatible version
  retryable: false
- name: connection_loss
  description: WebSocket or HTTP connection to browser process drops mid-session.
  likelihood: medium
  observable_evidence: Command timeout errors, WebSocket close event, HTTP connection refused
  detection: Heartbeat/ping mechanism; connection state monitoring
  recovery: Reconnect to browser process; restore session state if possible
  retryable: true

## Decision Factors
- factor: cross_browser_requirement
  question: "Does the automation need to run on multiple browser engines?"
  supporting: "Use WebDriver (Classic or BiDi) — CDP is Chromium-only"
  contradictory: "If Chromium-only is acceptable, CDP provides maximum capability"
  weight: high
- factor: detection_sensitivity
  question: "Is the automation operating in a high-detection-risk environment?"
  supporting: "BiDi offers execution isolation and smaller current detection surface"
  contradictory: "Detection advantage is temporary; CDP detection surface is well-understood with established mitigations"
  weight: high

## Observations
- observation: "Most automation tools use 6-8 CDP domains; remaining domains are relevant only to debugging and profiling."
  confidence: high
  source: Automation framework source analysis (Playwright, Puppeteer, nodriver)
- observation: "No anti-bot service is known to profile BiDi connections as of mid-2026."
  confidence: low
  source: Community reports, absence of documented detection
- observation: "BiDi module coverage is approximately 60% complete — network, storage, and input modules remain in draft."
  confidence: high
  source: W3C BiDi specification status

## Constraints
- constraint: "One protocol connection per browser process."
  type: invariant
  scope: cross-protocol
- constraint: "Protocol version must match browser version within compatibility window."
  type: invariant
  scope: cross-protocol
- constraint: "Network-level protocol metadata (WebSocket upgrade headers) is observable by the page."
  type: invariant
  scope: cdp, bidi

## Heuristics
- heuristic: "Use CDP when maximum capability or Chromium-specific features are required."
  rationale: "CDP provides the finest-grained control; BiDi module coverage is incomplete for advanced use cases."
  evidence_level: high
- heuristic: "Use WebDriver when cross-browser compatibility is the primary requirement."
  rationale: "W3C standard; supported by Chrome, Firefox, Safari, Edge."
  evidence_level: high
- heuristic: "Monitor BiDi adoption for detection-sensitive automation."
  rationale: "BiDi's execution isolation and lower profiling make it attractive for high-detection-risk environments."
  evidence_level: moderate

## Recommendations
- recommendation: "Select protocol based on capability requirements first, then detection sensitivity."
  context: protocol_selection
  certainty: strong
  rationale: "Capability determines whether the task is feasible; detection sensitivity determines how reliably it can run."
- recommendation: "Build protocol-agnostic automation where possible to enable future migration."
  context: production_pipeline
  certainty: moderate
  rationale: "Protocol landscape is evolving; abstraction at the framework layer reduces migration cost."

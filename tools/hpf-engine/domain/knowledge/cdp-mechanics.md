# CDP Mechanics

## Identity
- id: cdp-mechanics
- type: concept
- title: Chrome DevTools Protocol Mechanics
- tags: [cdp, protocol, domains, commands, events, websocket, json-rpc]
- entities: [cdp, chrome devtools protocol, target, json-rpc, websocket, domain, command, event]
- concepts: [automation-protocol, cdp-mechanics, browser-session-lifecycle]

## Claims
- claim: "CDP uses JSON-RPC 2.0 over WebSocket with a command model of method/params/id and an event model of server-push method/params."
  certainty: high
  evidence: Chromium CDP source code, DevTools Protocol documentation
  scope: Chromium-specific
- claim: "CDP exposes approximately 30 domains covering debugging, rendering, network, input, storage, and profiling."
  certainty: high
  evidence: CDP domain list from Chromium source
  scope: Chromium-specific
- claim: "CDP target model enables multi-tab control over a single WebSocket connection via Target.attachToTarget and Target.createTarget."
  certainty: high
  evidence: CDP documentation, automation framework source
  scope: Chromium-specific
- claim: "CDP session model uses targetId routing — each command targets a specific tab or worker within the browser."
  certainty: high
  evidence: CDP documentation
  scope: Chromium-specific
- claim: "CDP detection signals include navigator.webdriver, chrome.app.isInstalled, WebSocket upgrade header, and /json endpoint presence."
  certainty: high
  evidence: Community detection research, anti-bot service analysis
  scope: Chromium-specific

## Relationships
- concept: automation-protocol
  relationship: specialises
  description: CDP is one instantiation of the automation protocol concept — the most capable and least standardised.
- concept: automation-detection-surface
  relationship: exposes
  description: CDP exposes the widest detection surface of any automation protocol due to its Chromium-specific signals.
- concept: browser-session-lifecycle
  relationship: controls
  description: CDP provides the most granular control over session lifecycle via Page, Target, and Runtime domains.
- concept: webdriver-classic
  relationship: contrasts_with
  description: CDP offers WebSocket streaming vs WebDriver's HTTP request-response model.

## Tradeoffs
- dimension: capability_vs_standardisation
  options:
    cdp:
      value: maximum_capability
      rationale: 30 domains, fine-grained control, Chromium-specific
    webdriver_classic:
      value: standardised_but_limited
      rationale: Cross-browser, but limited to coarse session-level commands
  importance: critical
- dimension: tool_ecosystem
  options:
    cdp:
      value: rich
      rationale: Playwright, Puppeteer, nodriver all use CDP natively
    webdriver_classic:
      value: mature
      rationale: Selenium ecosystem, language bindings, grid infrastructure
  importance: high

## Failure Modes
- name: cdp_websocket_handshake_failure
  description: CDP WebSocket connection fails to establish because of port inaccessibility, mismatched protocol version, or browser not in debugging mode.
  likelihood: medium
  observable_evidence: WebSocket connection refused, timeout, or 404
  detection: Connection error on CDP client initialisation
  recovery: Verify browser launched with --remote-debugging-port; check port accessibility; verify browser version compatibility
  retryable: true
- name: domain_not_available
  description: A CDP domain or command is not available in the current browser version.
  likelihood: medium
  observable_evidence: Command returns method not found error
  detection: Error response from CDP command
  recovery: Check Chromium version; use feature detection before calling domain-specific commands
  retryable: false

## Decision Factors
- factor: protocol_capability_requirement
  question: "Does the task require CDP-specific features unavailable in WebDriver?"
  supporting: "Network interception, fine-grained runtime control, multi-tab sessions"
  contradictory: "Most automation tasks use 6-8 CDP domains and can use WebDriver BiDi"
  weight: high

## Observations
- observation: "CDP domain usage is highly skewed — Page, Runtime, Network, DOM, Input, and Target account for >90% of automation tool commands."
  confidence: high
  source: Automation framework source analysis
- observation: "CDP WebSocket upgrade header contains the string 'chrome.devtools' which is a unique detection signal."
  confidence: high
  source: CDP client source code, community detection research

## Constraints
- constraint: "CDP is Chromium-only; no other browser engine implements it."
  type: invariant
  scope: cdp
- constraint: "CDP version is tied to Chromium release version; breaking changes occur per release."
  type: invariant
  scope: cdp

## Heuristics
- heuristic: "Minimise CDP domain usage to the subset required for the automation task."
  rationale: "Each domain call is a detection signal opportunity; fewer domains = smaller surface."
  evidence_level: moderate
- heuristic: "Use target isolation for multi-tab automation — one CDP session per logical context."
  rationale: "Target separation prevents cross-tab interference and simplifies error recovery."
  evidence_level: high

## Recommendations
- recommendation: "Use CDP directly only when WebDriver BiDi does not provide required capability."
  context: protocol_selection
  certainty: strong
  rationale: "CDP is the highest-detectability protocol; BiDi provides equivalent capability for most automation tasks with less detection surface."
- recommendation: "Pin Chromium version in production CDP automation to prevent protocol version mismatch."
  context: production_pipeline
  certainty: strong
  rationale: "CDP version coupling means browser updates can break automation without warning."

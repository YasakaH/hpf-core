# TCP-TLS Foundation

## Identity
- id: tcp-tls-foundation
- type: concept
- title: TCP and TLS Connection Foundation
- tags: [tcp, tls, transport, connection, handshake, fingerprint, port]
- entities: [tcp, tls, connection, handshake, port, ephemeral port, time_wait, ja3, tls fingerprint]
- concepts: [automation-protocol, network-failure-propagation]

## Claims
- claim: "TCP provides reliable, ordered, error-checked delivery of a byte stream — every browser automation connection depends on it."
  certainty: high
  evidence: TCP specification (RFC 793), systems literature
  scope: cross-platform
- claim: "Ephemeral port exhaustion occurs when rapid connections cycling exceeds the available port range (~28K-64K on Linux)."
  certainty: high
  evidence: Systems literature, production networking experience
  scope: cross-platform
- claim: "TIME_WAIT accumulation blocks port reuse for 60 seconds (2*MSL) after client-initiated close, contributing to port exhaustion."
  certainty: high
  evidence: TCP specification (RFC 793), systems literature
  scope: cross-platform
- claim: "The TLS ClientHello produces an observable fingerprint (JA3) that differs between browser TLS stacks and automation TLS libraries."
  certainty: high
  evidence: TLS specification (RFC 8446), community TLS fingerprint research
  scope: cross-platform
- claim: "Nagle's algorithm adds latency to small messages by buffering them — CDP commands are small JSON messages and are affected."
  certainty: high
  evidence: TCP specification (RFC 896), CDP performance analysis
  scope: cross-platform
- claim: "TLS 1.3 reduces handshake latency to 1-RTT (or 0-RTT with session resumption) compared to TLS 1.2's 2-RTT."
  certainty: high
  evidence: TLS 1.3 specification (RFC 8446)
  scope: cross-platform

## Relationships
- concept: http-protocol
  relationship: underlies
  description: TCP carries HTTP data; TLS encrypts HTTP traffic. HTTP cannot function without a transport-layer connection.
- concept: proxy-infrastructure
  relationship: interacts_with
  description: Proxies terminate and re-establish TCP and TLS connections, altering connection properties (fingerprint, latency).
- concept: network-failure-propagation
  relationship: source_of
  description: TCP failures (timeout, reset, port exhaustion) propagate upward to TLS, HTTP, and application layers.
- concept: automation-protocol
  relationship: transports
  description: CDP and BiDi WebSocket connections run over TCP; WebDriver HTTP runs over TCP.
- concept: automation-detection-surface
  relationship: contributes_to
  description: TLS fingerprint (JA3) is a passive detection signal observable before any HTTP request.

## Tradeoffs
- dimension: connection_reuse_vs_freshness
  options:
    persistent:
      value: lower_overhead
      rationale: Avoids handshake latency, conserves ports, maintains state
    per_request:
      value: isolation
      rationale: Each request gets a clean connection; no cross-request state leakage
  importance: operational
- dimension: tls_version
  options:
    tls_1_2:
      value: compatibility
      rationale: Widely supported; 2-RTT handshake; well-understood
    tls_1_3:
      value: performance
      rationale: 1-RTT handshake; improved security; emerging standard
  importance: high

## Failure Modes
- name: ephemeral_port_exhaustion
  description: Automation exhausts available ephemeral ports by opening connections faster than TIME_WAIT releases them.
  likelihood: medium
  observable_evidence: EADDRNOTAVAIL (bind) errors, connection refused on new outbound connections
  detection: Monitor connection counts, TIME_WAIT socket count, port range utilisation
  recovery: SO_REUSEADDR, reduce TIME_WAIT via sysctl (tcp_tw_reuse), connection pooling
  retryable: false
- name: tls_fingerprint_mismatch
  description: Automation TLS stack produces a different ClientHello fingerprint than a real browser, enabling passive detection.
  likelihood: high
  observable_evidence: JA3 fingerprint differs from browser baseline; anti-bot service may challenge or block
  detection: Compare automation TLS fingerprint against browser TLS fingerprint for same target
  recovery: Use browser's TLS library (BoringSSL via CDP), or proxy with matching TLS fingerprint
  retryable: false
- name: tls_certificate_validation_failure
  description: Target server uses a certificate not trusted by the automation's TLS stack.
  likelihood: low
  observable_evidence: TLS handshake failure, certificate verification error
  detection: SSL error on connection attempt
  recovery: Add certificate to trust store, disable verification in dev, ensure proper CA chain
  retryable: true

## Observations
- observation: "Default TCP keep-alive timeout (2 hours on Linux) is too long to detect dead connections in automation context."
  confidence: high
  source: Linux kernel documentation, production automation experience
- observation: "TLS fingerprint databases (JA3) are community-maintained and incomplete — no authoritative browser fingerprint mapping exists."
  confidence: medium
  source: Community TLS fingerprint projects, absence of vendor-maintained databases
- observation: "TCP_NODELAY reduces CDP command latency by up to 40ms per command by disabling Nagle's algorithm."
  confidence: high
  source: CDP performance analysis, networking literature

## Constraints
- constraint: "TCP connection established during SYN-SYN-ACK handshake — no data flows before completion."
  type: invariant
  scope: cross-network
- constraint: "TLS handshake must complete before application data flows over HTTPS."
  type: invariant
  scope: cross-network

## Heuristics
- heuristic: "Enable TCP_NODELAY on all CDP WebSocket sockets to eliminate Nagle-induced latency."
  rationale: "CDP commands are small JSON messages that trigger Nagle's algorithm."
  evidence_level: high
- heuristic: "Use connection pooling for HTTP requests to avoid ephemeral port exhaustion."
  rationale: "Reusing connections reduces churn, conserves ports, and reduces latency."
  evidence_level: high
- heuristic: "Compare automation TLS fingerprint to browser fingerprint before deploying to detection-sensitive targets."
  rationale: "TLS fingerprint is a passive detection signal — know your baseline."
  evidence_level: moderate

## Recommendations
- recommendation: "Set TCP_NODELAY on CDP client sockets to minimise command latency."
  context: cdp_automation
  certainty: strong
  rationale: "Nagle's algorithm adds measurable latency to small CDP messages without benefit."
- recommendation: "Use connection pooling and SO_REUSEADDR to manage TCP connection resources at scale."
  context: production_pipeline
  certainty: strong
  rationale: "Port exhaustion and TIME_WAIT accumulation are common failure modes in high-throughput automation."
- recommendation: "Profile and match browser TLS fingerprint when operating in detection-sensitive environments."
  context: anti_detection
  certainty: moderate
  rationale: "TLS fingerprint is a passive signal detectable before any application-layer interaction."

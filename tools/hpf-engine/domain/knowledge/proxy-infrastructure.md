# Proxy Infrastructure

## Identity
- id: proxy-infrastructure
- type: concept
- title: Proxy Infrastructure
- tags: [proxy, forward proxy, reverse proxy, residential proxy, connection, forwarding, load balancer]
- entities: [proxy, forward proxy, reverse proxy, transparent proxy, socks proxy, residential proxy, load balancer, cdn]
- concepts: [tcp-tls-foundation, http-protocol, network-failure-propagation, automation-detection-surface]

## Claims
- claim: "Forward proxies relay client requests to targets, masking the client's IP address and altering the client's network fingerprint."
  certainty: high
  evidence: Proxy architecture literature, vendor documentation (HAProxy, Squid, nginx)
  scope: cross-platform
- claim: "Residential proxies hosted on ISP connections have better IP reputation than datacenter proxies but are slower and less reliable."
  certainty: high
  evidence: Proxy provider documentation, community performance comparisons
  scope: cross-platform
- claim: "Proxies that terminate TLS and re-encrypt change the TLS fingerprint from the client's to the proxy's."
  certainty: high
  evidence: TLS specification, proxy behaviour documentation
  scope: cross-platform
- claim: "Transparent proxies intercept traffic without explicit client configuration, detectable by the target server via proxy headers or connection properties."
  certainty: medium
  evidence: Proxy literature, community detection research
  scope: cross-platform
- claim: "Connection pool exhaustion at the proxy causes downstream retry storms as clients retry failed requests."
  certainty: high
  evidence: Production operations experience, systems literature
  scope: cross-platform

## Relationships
- concept: tcp-tls-foundation
  relationship: terminates
  description: Proxies terminate incoming TCP connections and establish new outgoing TCP connections, altering connection properties.
- concept: http-protocol
  relationship: forwards
  description: Proxies forward HTTP requests and responses, potentially modifying headers or translating protocol versions.
- concept: network-failure-propagation
  relationship: introduces
  description: Proxies add an intermediate hop that introduces its own failure modes (timeout, pool exhaustion, DNS failure).
- concept: automation-detection-surface
  relationship: affects
  description: Proxy choice affects IP reputation, TLS fingerprint, and protocol fingerprint — all detection signals.
- concept: retry-pattern
  relationship: influenced_by
  description: Proxy failures trigger retry behaviour; proxy rate limiting determines backoff strategy.

## Tradeoffs
- dimension: proxy_type
  options:
    datacenter:
      value: fast_but_detectable
      rationale: Low latency, high bandwidth, but IP ranges are known automation/datacenter ranges
    residential:
      value: stealthy_but_slower
      rationale: IP appears as real user, but slower, less reliable, and more expensive
  importance: critical
- dimension: tls_termination
  options:
    terminate:
      value: inspectable
      rationale: Proxy can inspect/modify traffic; changes TLS fingerprint; enables caching
    passthrough:
      value: transparent
      rationale: Proxy does not alter TLS; preserves original fingerprint; cannot cache or inspect
  importance: high

## Failure Modes
- name: proxy_connection_timeout
  description: Proxy is unreachable or overloaded, causing connection establishment to fail.
  likelihood: medium
  observable_evidence: Socket timeout, connection refused, HTTP 502
  detection: Timeout on proxy connection attempt; monitor proxy health endpoint
  recovery: Rotate to alternative proxy; implement proxy health checking; circuit breaker
  retryable: true
- name: proxy_ip_blacklisting
  description: Proxy IP address is blocked or rate-limited by the target server.
  likelihood: high
  observable_evidence: HTTP 403, 429, CAPTCHA challenge, connection reset
  detection: Response analysis after proxy connection
  recovery: Rotate to different proxy IP; reduce request rate; use residential proxy
  retryable: false
- name: protocol_version_mismatch
  description: Proxy does not support the protocol version (HTTP/2, WebSocket) required by the client or target.
  likelihood: medium
  observable_evidence: Upgrade failure, protocol error, connection drop
  detection: Response analysis; protocol negotiation logs
  recovery: Fall back to HTTP/1.1; use proxy that supports required protocol
  retryable: false

## Observations
- observation: "Residential proxy networks introduce variable latency (100-500ms additional) compared to datacenter proxies (1-10ms additional)."
  confidence: high
  source: Proxy provider documentation, community benchmarks
- observation: "CDN reverse proxies (Cloudflare, Akamai) alter TLS fingerprints at the edge, replacing client fingerprint with CDN's."
  confidence: high
  source: TLS fingerprint databases, community analysis
- observation: "Authentication-based rate limiting at the proxy provider level is more restrictive than per-IP limits."
  confidence: medium
  source: Proxy provider terms of service, user reports

## Constraints
- constraint: "Proxy cannot relay UDP traffic unless it supports SOCKS5 or a tunnelling protocol."
  type: invariant
  scope: proxy_infrastructure
- constraint: "Transparent proxy interception requires the client traffic to pass through the proxy's network path."
  type: invariant
  scope: proxy_infrastructure

## Heuristics
- heuristic: "Use residential proxies for detection-sensitive automation and datacenter proxies for high-throughput non-sensitive tasks."
  rationale: "IP reputation matters proportionally to detection risk."
  evidence_level: high
- heuristic: "Implement proxy health checking and automatic rotation to degrade gracefully when a proxy fails."
  rationale: "Proxy failures are inevitable; automated recovery prevents pipeline stalls."
  evidence_level: high
- heuristic: "Prefer passthrough TLS proxies when fingerprint preservation matters more than content inspection."
  rationale: "TLS passthrough preserves the original client fingerprint; termination replaces it with the proxy's."
  evidence_level: moderate

## Recommendations
- recommendation: "Use residential proxies for any automation where IP reputation is a significant detection risk."
  context: production_pipeline
  certainty: strong
  rationale: "IP reputation is one of the highest-weight detection signals; datacenter IPs are well-known automation sources."
- recommendation: "Implement proxy rotation with health checking and circuit breaker patterns."
  context: production_pipeline
  certainty: strong
  rationale: "Proxy failures are a common source of automation instability; automated recovery is essential at scale."
- recommendation: "Test proxy TLS fingerprint before deploying — residential proxy networks may alter the fingerprint unexpectedly."
  context: anti_detection
  certainty: moderate
  rationale: "TLS fingerprint changes at the proxy can invalidate fingerprint-matching strategies."

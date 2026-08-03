# HTTP Protocol

## Identity
- id: http-protocol
- type: concept
- title: HTTP Protocol
- tags: [http, https, request, response, status, method, header, h2, multiplexing]
- entities: [http, http/1.1, http/2, https, request, response, status code, header, method, connection]
- concepts: [tcp-tls-foundation, proxy-infrastructure, network-failure-propagation]

## Claims
- claim: "HTTP/1.1 uses one TCP connection per request — parallelism requires multiple concurrent connections (typically 6-8 per origin)."
  certainty: high
  evidence: HTTP/1.1 specification (RFC 7230), browser connection behaviour documentation
  scope: cross-platform
- claim: "HTTP/2 multiplexes multiple streams over a single TCP connection, eliminating connection-level head-of-line blocking at the HTTP layer."
  certainty: high
  evidence: HTTP/2 specification (RFC 7540)
  scope: cross-platform
- claim: "HTTP/2 stream multiplexing still experiences head-of-line blocking at the TCP layer — one lost packet affects all streams."
  certainty: high
  evidence: HTTP/2 specification, networking literature (HTTP/3 addresses this via QUIC)
  scope: cross-platform
- claim: "HTTP method idempotency determines retry safety — GET, HEAD, PUT, DELETE are idempotent; POST and PATCH are not."
  certainty: high
  evidence: HTTP/1.1 specification (RFC 7231, Section 4.2.2)
  scope: cross-platform
- claim: "HTTP 429 (Too Many Requests) indicates rate limiting — retry without backoff amplifies the problem."
  certainty: high
  evidence: HTTP specification (RFC 6585)
  scope: cross-platform

## Relationships
- concept: tcp-tls-foundation
  relationship: runs_over
  description: HTTP runs over TCP; HTTPS runs over TLS over TCP. Transport properties (latency, congestion) affect HTTP behaviour.
- concept: proxy-infrastructure
  relationship: traverses
  description: HTTP requests pass through proxies, which may modify headers, terminate TLS, or translate protocol versions.
- concept: network-failure-propagation
  relationship: triggers
  description: HTTP errors (timeout, 502, 504) are common triggers for application-layer retry and failure cascades.
- concept: automation-protocol
  relationship: distinct_from
  description: HTTP is the application protocol for web traffic; CDP/WebDriver are control protocols for browser automation.
- concept: automation-detection-surface
  relationship: contributes_to
  description: HTTP/2 fingerprint (SETTINGS frame parameters) is an observable detection signal.

## Tradeoffs
- dimension: protocol_version
  options:
    http_1_1:
      value: compatible
      rationale: Universal support; simple request-response model; connection-per-request overhead
    http_2:
      value: performant
      rationale: Multiplexed streams; header compression; server push (deprecated); TCP HOL blocking
  importance: high
- dimension: connection_model
  options:
    persistent:
      value: efficient
      rationale: Reuse existing connection; avoid handshake overhead; maintain keep-alive
    per_request:
      value: isolated
      rationale: No cross-request interference; clean state per request; higher overhead
  importance: operational

## Failure Modes
- name: rate_limiting
  description: Server returns 429 Too Many Requests when client exceeds allowed request rate.
  likelihood: high
  observable_evidence: HTTP 429 response, Retry-After header
  detection: Monitor response status codes; track request rate per origin
  recovery: Apply exponential backoff with jitter respecting Retry-After; reduce request rate
  retryable: true
- name: connection_timeout
  description: HTTP request fails because TCP connection cannot be established within timeout.
  likelihood: medium
  observable_evidence: Connection timeout error, socket timeout exception
  detection: Timeout on connection attempt
  recovery: Retry with backoff; check network connectivity; verify target availability
  retryable: true
- name: server_error
  description: Server returns 5xx status indicating temporary or permanent server-side failure.
  likelihood: medium
  observable_evidence: HTTP 500, 502, 503, 504 responses
  detection: Response status code monitoring
  recovery: Retry with backoff (transient) or escalate (persistent); 502/504 may indicate proxy failure
  retryable: true

## Observations
- observation: "HTTP/2 stream priority behaviour differs between browser-driven loads and automation-driven loads, potentially causing observable differences."
  confidence: medium
  source: Community analysis, HTTP/2 implementation studies
- observation: "Most automation frameworks default to HTTP/1.1 and do not advertise HTTP/2 support in their HTTP client configuration."
  confidence: high
  source: Automation framework source code (Python requests, aiohttp, Node fetch)

## Constraints
- constraint: "HTTP request cannot be sent before TCP connection is established and TLS handshake (if HTTPS) is complete."
  type: invariant
  scope: cross-protocol
- constraint: "Idempotent methods (GET, HEAD, PUT, DELETE) produce the same server state regardless of how many times they are executed."
  type: invariant
  scope: cross-platform

## Heuristics
- heuristic: "Prefer HTTP/2 for page-load automation to reduce connection overhead from 6-8 parallel connections to 1-2."
  rationale: "Fewer connections mean fewer ports consumed, lower TLS handshake overhead, and simpler failure management."
  evidence_level: moderate
- heuristic: "Never retry POST requests without an idempotency key or application-level deduplication."
  rationale: "Non-idempotent methods risk duplicate side effects (double charges, duplicate entries)."
  evidence_level: high

## Recommendations
- recommendation: "Implement rate limit detection with automatic backoff at the HTTP client layer."
  context: production_pipeline
  certainty: strong
  rationale: "429 responses are inevitable in high-throughput automation; graceful handling is mandatory."
- recommendation: "Distinguish transient server errors (503, 504) from permanent ones (500, 502 persistent) in retry logic."
  context: production_pipeline
  certainty: strong
  rationale: "Transient errors benefit from retry; permanent errors require escalation, not retry."

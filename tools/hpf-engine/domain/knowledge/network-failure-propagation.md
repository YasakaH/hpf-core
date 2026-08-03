# Network Failure Propagation

## Identity
- id: network-failure-propagation
- type: concept
- title: Network Failure Propagation
- tags: [failure, propagation, cascade, retry, timeout, circuit breaker, backoff, connection pool]
- entities: [failure propagation, cascade, retry storm, circuit breaker, backoff, connection pool, timeout, congestion collapse]
- concepts: [tcp-tls-foundation, http-protocol, proxy-infrastructure, retry-pattern]

## Claims
- claim: "Network failures propagate upward through layers — a TCP timeout becomes an HTTP timeout which becomes an application failure."
  certainty: high
  evidence: Systems literature (SRE, distributed systems), production operations experience
  scope: cross-platform
- claim: "Connection pool exhaustion at any layer (client, proxy, server) causes cascading failures as queued requests accumulate and time out."
  certainty: high
  evidence: Distributed systems literature, production experience
  scope: cross-platform
- claim: "Retry storms — coordinated retry from many clients after a transient failure — can cause sustained overload worse than the original failure."
  certainty: high
  evidence: Systems literature (retry amplification), SRE postmortems
  scope: cross-platform
- claim: "Circuit breakers prevent cascading failures by stopping retries to a failing dependency after a threshold of failures."
  certainty: high
  evidence: Distributed systems literature, circuit breaker pattern documentation
  scope: cross-platform
- claim: "Exponential backoff with jitter is the most effective retry strategy for avoiding retry storms."
  certainty: high
  evidence: Systems literature, AWS / Google SRE recommendations
  scope: cross-platform
- claim: "Congestion collapse occurs when retransmissions consume more bandwidth than data, reducing effective throughput to near zero."
  certainty: high
  evidence: TCP congestion control literature, networking research
  scope: cross-platform

## Relationships
- concept: tcp-tls-foundation
  relationship: originates_from
  description: TCP connection failures (timeout, reset) are the most common source of network failure cascades.
- concept: http-protocol
  relationship: manifests_as
  description: HTTP errors (timeout, 502, 504) are the observable symptoms of lower-layer failures propagating upward.
- concept: proxy-infrastructure
  relationship: amplifies
  description: Proxies add an intermediate hop that introduces additional failure modes (pool exhaustion, DNS delay).
- concept: retry-pattern
  relationship: mitigates
  description: Retry with backoff is the primary mitigation for transient network failures; without it, failures cascade.
- concept: health-check-pattern
  relationship: informs
  description: Health checks detect failure states; circuit breakers use health check results to stop routing traffic to failed dependencies.

## Tradeoffs
- dimension: retry_aggressiveness
  options:
    aggressive:
      value: fast_recovery
      rationale: Retries quickly, minimising latency for transient failures; risks retry storm on systemic failures
    conservative:
      value: safe
      rationale: Backs off aggressively, avoiding retry storms; increases latency for transient failures
  importance: critical
- dimension: connection_pool_size
  options:
    large:
      value: high_throughput
      rationale: More concurrent requests; higher resource usage; slower failure detection
    small:
      value: constrained
      rationale: Fewer concurrent requests; lower resource usage; faster feedback on failures
  importance: high

## Failure Modes
- name: retry_storm
  description: Coordinated retry from multiple automation instances amplifies a transient failure into sustained overload.
  likelihood: medium
  observable_evidence: All instances fail simultaneously at the same retry interval; failure persists longer than original cause
  detection: Correlated failure timing across instances; retry interval pattern matching
  recovery: Introduce jitter in retry timing; circuit breaker; exponential backoff with randomisation
  retryable: false
- name: connection_pool_exhaustion
  description: All connections in the pool are in use or in TIME_WAIT, and new requests cannot acquire a connection.
  likelihood: medium
  observable_evidence: Connection acquisition timeout, connection refused, EADDRNOTAVAIL
  detection: Monitor pool utilisation; track TIME_WAIT socket count; log connection acquisition wait times
  recovery: Increase pool size; reduce connection hold time; implement connection eviction; SO_REUSEADDR
  retryable: true
- name: cascading_timeout
  description: A downstream dependency becomes slow, causing upstream requests to queue, eventually timing out every request.
  likelihood: medium
  observable_evidence: Gradually increasing latency across all requests; timeout errors spreading to unrelated operations
  detection: Latency trend monitoring; dependency-level timing breakdown; timeout distribution analysis
  recovery: Circuit breaker on slow dependency; request timeouts at each layer; shed load at boundaries
  retryable: false

## Observations
- observation: "Retry storms are the most common automation scalability failure mode — a single proxy failure triggers coordinated retry from all browser instances."
  confidence: high
  source: Production automation operations experience
- observation: "Connection pool exhaustion is more common than CPU or memory exhaustion as the bottleneck in high-throughput automation."
  confidence: medium
  source: Production operations experience, community reports
- observation: "Exponential backoff without jitter produces waves of retry traffic that synchronise across instances."
  confidence: high
  source: Systems literature, distributed systems postmortems
- observation: "TCP congestion window collapse after packet loss reduces throughput for 100-500ms before recovery — this is invisible at the HTTP layer."
  confidence: high
  source: TCP specification, networking literature

## Constraints
- constraint: "TCP congestion control reduces send window on packet loss — this is automatic and unavoidable at the transport layer."
  type: invariant
  scope: cross-network
- constraint: "Circuit breaker open state prevents all requests to a failing dependency until the cooldown period expires."
  type: invariant
  scope: application_layer

## Heuristics
- heuristic: "Always add jitter to exponential backoff to prevent retry synchronisation across instances."
  rationale: "Deterministic backoff causes all instances to retry simultaneously, amplifying failures."
  evidence_level: high
- heuristic: "Monitor connection pool utilisation as the leading indicator of capacity-related failures."
  rationale: "Pool exhaustion precedes CPU/memory saturation in networked automation."
  evidence_level: moderate
- heuristic: "Implement circuit breakers at service boundaries to prevent cascading failures."
  rationale: "Circuit breakers give the failing dependency time to recover without amplifying load."
  evidence_level: high

## Recommendations
- recommendation: "Implement exponential backoff with jitter as the default retry strategy for all network operations."
  context: production_pipeline
  certainty: strong
  rationale: "Retry storms are the most preventable automation failure mode; jitter is the critical component."
- recommendation: "Monitor connection pool depth and TIME_WAIT count as capacity metrics — not just CPU and memory."
  context: production_pipeline
  certainty: strong
  rationale: "Network resource exhaustion is the most common bottleneck in browser automation infrastructure."
- recommendation: "Use short request timeouts (5-10s) with retry rather than long timeouts (30-60s) without — fail fast, retry smart."
  context: production_pipeline
  certainty: moderate
  rationale: "Short timeouts prevent cascading queue buildup; smart retry recovers from transient failures."

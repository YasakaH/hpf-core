# Retry Strategy

**Domain**: Browser Reliability

## Definition

A decision framework for re-executing a failed operation, defining when to retry, how long to wait, and when to give up.

## Properties

- **Trigger conditions**: Which error types are retryable (timeout, crash, navigation failure, rate limit)
- **Backoff function**: Fixed delay, exponential backoff, fibonacci, decorrelated jitter
- **Max attempts**: Hard limit or budget-based (total time budget)
- **Circuit breaker**: State tracking (closed/open/half-open) to stop retrying a failing operation
- **Idempotency requirement**: Whether the operation can be safely re-executed

## Relationships

| Concept | Relationship |
|---|---|
| Session Lifecycle | Retry decisions depend on lifecycle phase (retry during navigation? after crash?) |
| Health Check | Health checks determine whether the session is in a retryable state |
| Blocking and Rate Limiting | Rate limiting is a primary trigger for retry strategies |
| Extraction Pattern | Extraction reliability depends on proper retry handling of partial failures |

## Constraints

- Retries during page navigation may cause cascading failures
- Exponential backoff with jitter is standard for rate-limited scenarios
- Circuit breaker is essential for operations with non-recoverable failure modes
- Retry limits must account for total operation time budget, not just attempt count

---

*Canonical concept. Not tool-specific.*

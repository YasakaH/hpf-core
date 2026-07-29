# Memory Pressure

**Domain**: Browser Memory

## Definition

The condition where a browser process approaches or exceeds its available memory budget, leading to performance degradation, tab discarding, process crash, or OS-level termination.

## Pressure Levels

| Level | Symptoms | Typical Triggers | Action Required |
|---|---|---|---|
| Normal | No symptoms | — | None |
| Elevated | JS heap growing, minor GC pauses | Large DOM, many tabs | Monitor, no action |
| High | Tab discarding starts (Chrome), visible slowdown | Memory-intensive page, many tabs | Reduce load, close unused tabs |
| Critical | Renderer OOM, GPU crash, process exit | Leak, extremely large payload | Restart session, investigate root cause |
| Terminal | Browser process kill, OS OOM killer | System-wide memory exhaustion | New process, reduce concurrency |

## Detection Mechanisms

| Method | Granularity | Lead Time | Protocol | Reliability |
|---|---|---|---|---|
| `Performance.getMetrics` (JSHeapUsedSize) | Snapshot | Medium (trend-based) | CDP | High (trend, not threshold) |
| `Memory.getDOMCounters` (node count) | Snapshot | Medium | CDP | Medium (DOM leaks != memory pressure) |
| `performance.memory` (jsHeapSizeLimit) | Snapshot | Medium | JS API | Medium (Chromium-only, estimated) |
| `Inspector.targetCrashed` | Event | None (post-facto) | CDP | High (definitive crash signal) |
| Tab discard event (infer from visibility) | Event | After discard | CDP | Low (indirect, no direct CDP event) |
| OS process metrics (RSS, VSZ) | Continuous | Medium | OS APIs | High (system-level) |
| Command timeout (inferred) | Event | None (post-facto) | CDP/WebDriver | Low (many causes) |

## Relationships

| Concept | Relationship |
|---|---|
| Browser Profile | Large profiles increase memory pressure at startup; profile corruption can cause leaks. |
| Browser Storage | IndexedDB and Cache API can consume significant memory at read/query time. |
| Session Lifecycle | Memory pressure is most dangerous during navigation (allocating new page while old page not GC'd). |
| Retry Strategy | Memory-related failures may not be retryable — retry in same session hits same memory constraint. |
| Health Check | Health checks should include memory metrics to detect elevated pressure before failure. |

## Constraints

- Memory pressure signals are browser-specific: Chromium tab discarding does not exist in Firefox
- Headless Chrome may have different memory behaviour than headed (no GPU process, no display compositor)
- JS heap size is not total memory usage — GPU memory, cache, and DOM storage are not included
- `Inspector.targetCrashed` fires for all crashes, not just OOM — must cross-reference with process exit code
- CDP connection itself consumes memory; multiple attached targets increase per-session overhead
- GC is non-deterministic — `Memory.prepareForLeakDetection` is a hint, not a guarantee

---

*Canonical concept. Not tool-specific.*

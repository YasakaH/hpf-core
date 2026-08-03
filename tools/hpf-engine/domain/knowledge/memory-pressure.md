# Memory Pressure

## Identity
- id: memory-pressure
- type: concept
- title: Browser Memory Pressure
- tags: [memory, OOM, crash, pressure, GC, performance]
- entities: [memory, OOM, crash, pressure, GC, performance, leak]
- concepts: [memory-pressure, browser-profile, browser-storage, browser-session-lifecycle]

## Metadata
- created: 2026-07-29
- domain: browser-automation
- version: 0.1.0
- research_cycle: 002

## Semantic Layer
- definition: Memory pressure is the condition where a browser process approaches or exceeds its available memory budget, causing degradation (tab discarding, slowdown) or failure (renderer OOM, process crash, OS kill).
- detection_gap: There is no single "memory health" event in CDP or WebDriver. Detection requires composing multiple signals: JS heap size trend, DOM node count, process metrics, and crash events.
- key_insight: Memory pressure is often invisible until it causes a crash. The primary challenge is pre-crash detection, not recovery.

## Narrative Layer
Memory pressure is the most under-documented failure mode in browser automation. Unlike navigation failures (which have explicit error events) or session disconnects (which have WebSocket close signals), memory degradation happens gradually with few observable signals. CDP provides `Performance.getMetrics` and `Memory.getDOMCounters` for trend monitoring, but there is no threshold-based alert. WebDriver provides no memory monitoring at all — pressure is only detected when a command times out or the session crashes. For production automation, this makes memory pressure the hardest failure mode to handle proactively.

## Compare Section
- dimension: monitoring_capability
- cdp:
  - signals: Performance.getMetrics, Memory.getDOMCounters, Inspector.targetCrashed
  - granularity: Per-snapshot, per-target
  - lead_time: Medium (trend-based detection possible)
- webdriver:
  - signals: Command timeout, executeScript(performance.memory)
  - granularity: Per-command
  - lead_time: None (post-facto only)

- dimension: pre_crash_detection
- cdp:
  - capability: Can detect rising JS heap, increasing DOM nodes, growing event listener count before crash
  - reliability: Medium (thresholds vary by page)
- webdriver:
  - capability: Cannot detect memory pressure before crash
  - reliability: None

- dimension: crash_recovery
- cdp:
  - capability: Inspector.targetCrashed event provides definitive crash signal; can re-attach to surviving targets
  - reliability: High for crash event; limited for OOM (no OOM-specific event)
- webdriver:
  - capability: Session timeout only; no crash event
  - reliability: Low (must infer crash from timeout)

- tradeoff_table:
  - criterion: memory_monitoring
  - winner: cdp
  - importance: critical_for_production
  - criterion: crash_detection_speed
  - winner: cdp
  - importance: high
  - criterion: cross_browser_consistency
  - winner: neither (both are Chromium-focused)
  - importance: medium

- recommendation:
  - case: production_automation
  - use: cdp
  - reason: Memory monitoring and crash detection are essential for reliability
  - case: simple_scraping
  - use: webdriver
  - reason: Memory pressure is rare for short-lived sessions regardless of protocol

## Troubleshoot Section
- failure_modes:
  - name: renderer_oom
  - observable_evidence: Inspector.targetCrashed fires, tab becomes unresponsive then closes
  - likelihood: medium (depends on page complexity and session duration)
  - detection: Inspector.targetCrashed event (CDP); command timeout (WebDriver)
  - recovery: New session; reduce memory load (fewer tabs, simpler pages, memory limits)
  - retryable: false (same session will hit same memory constraint)
  - prevention: Monitor JS heap trend, set browser memory limits, rotate sessions

  - name: tab_discard
  - observable_evidence: Background tab reloads when focused, CDP events resume after silence
  - likelihood: medium (Chrome only, headed mode)
  - detection: Tab visibility change followed by reload; no direct CDP event
  - recovery: Wait for reload, re-check page state
  - retryable: true (discard is recoverable)
  - prevention: Keep tabs in foreground, set --disable-background-timer-throttling

  - name: gradual_memory_leak
  - observable_evidence: JS heap size increases steadily over time, performance degrades
  - likelihood: high (long-running sessions, SPA-heavy pages)
  - detection: CDP Performance.getMetrics (JSHeapUsedSize increasing, NodeCount rising)
  - recovery: Session rotation, GC hint via Memory.prepareForLeakDetection
  - retryable: true (on fresh session)
  - prevention: Session time-to-live limits, periodic heap monitoring, proactive rotation

  - name: gpu_oom
  - observable_evidence: GPU process crash (Inspector.targetCrashed with GPU-related context), rendering stops
  - likelihood: low (GPU-intensive pages)
  - detection: Inspector.targetCrashed; process type = GPU
  - recovery: New session with --disable-gpu or --use-gl=swiftshader
  - retryable: false (GPU recovery requires process restart)
  - prevention: Use software rendering for headless, limit GPU-intensive operations

  - name: os_kill
  - observable_evidence: Browser process disappears without crash event, process exit code indicates OOM kill
  - likelihood: low (system memory exhaustion)
  - detection: Connection close without Inspector.targetCrashed; process exit code
  - recovery: New process, reduce system-wide memory load, container memory limits
  - retryable: false (OS-level, requires new process)
  - prevention: Container memory limits, process-level resource monitoring, reduce concurrency

## Decide Section
- decision_factors:
  - factor: session_longevity
  - question: "How long does each session run?"
  - supporting: Short sessions (<10 min) rarely encounter memory pressure; long sessions (>1 hour) need monitoring
  - contradictory: Session rotation adds overhead; longer sessions are more efficient for some workloads
  - weight: high

  - factor: page_complexity
  - question: "Are the pages being automated memory-intensive?"
  - supporting: SPAs, dashboards, media-rich pages consume more memory and leak faster
  - contradictory: Simple static pages rarely cause memory issues
  - weight: high

  - factor: reliability_requirement
  - question: "Can the automation tolerate intermittent crashes?"
  - supporting: Memory-monitored systems can pre-emptively rotate sessions before failure
  - contradictory: Overhead of memory monitoring may not justify benefit for tolerant workloads
  - weight: medium

- recommendation:
  - scenario: production_pipeline_long_running
  - use: implement_memory_monitoring + session_rotation
  - certainty: strong
  - scenario: short_lived_scraping
  - use: no_monitoring_needed
  - certainty: strong

## Design Section
- approaches:
  - name: proactive_memory_monitoring
  - description: Poll CDP Performance.getMetrics and Memory.getDOMCounters every 30-60s; rotate session when JS heap exceeds threshold or node count grows abnormally
  - pros: Prevents crashes, clean rotation, measurable thresholds
  - cons: CDP overhead, threshold tuning required, per-page variability
  - best_for: Production automation with high reliability requirements

  - name: reactive_crash_recovery
  - description: Catch Inspector.targetCrashed, restart session, add backoff to prevent crash loops
  - pros: Simple, no monitoring overhead, works for any crash cause
  - cons: Data loss on crash, slower recovery, no prevention
  - best_for: Simple automation, non-critical workloads

  - name: session_ttl_rotation
  - description: Rotate sessions on a fixed schedule (e.g., every 30 min) regardless of observed memory state
  - pros: Simple, prevents gradual leaks from becoming crashes, predictable resource usage
  - cons: May rotate healthy sessions unnecessarily, loses in-memory state
  - best_for: Long-running automation where leak-free sessions are unproven

### Pitfalls
- pitfall: silent_oom_in_headless
- description: Headless Chrome may OOM without Inspector.targetCrashed in some configurations
- mitigation: Monitor connection health and process metrics in addition to CDP events

- pitfall: false_recovery_from_discard
- description: Tab discard reuses the same session, but CDP bindings may be partially invalidated after reload
- mitigation: After tab discard recovery, verify all frame references and CDP event subscriptions

- pitfall: memory_monitoring_overhead
- description: Polling Performance.getMetrics too frequently (every 1-2s) adds measurable overhead
- mitigation: 30-60s interval is sufficient; use trend detection, not threshold-based alerts alone

### Best Practices
- practice: Implement memory monitoring for sessions lasting >10 minutes
- rationale: Most memory leaks manifest within 10-30 minutes; early detection prevents crash

- practice: Use JS heap size trend, not absolute threshold
- rationale: Heap limits vary by page (50MB for simple page vs 500MB for dashboard)

- practice: Rotate sessions proactively when heap grows >2x baseline
- rationale: Consistent doubling pattern indicates leak rather than normal allocation

- practice: Include memory metrics in health check probes
- rationale: A session may be responsive but unhealthy (leaking); health check should catch this

- practice: Never retry memory-intensive operations in the same session after crash
- rationale: The underlying memory constraint (page leak, OOM boundary) still exists

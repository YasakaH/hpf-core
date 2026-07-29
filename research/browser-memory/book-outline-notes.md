# Book Outline Notes — Browser Memory

Notes, not prose.

---

## Perspective A — Browser Automation Engineering

### Where Browser Memory fits
After Browser State (lifecycle) and before Detection (anti-detection principles). Memory explains what state exists and how it persists.

### Key concepts
- Browser profile anatomy (what's in a user-data-dir)
- Storage mechanisms and their lifetimes
- Why clearing cookies doesn't clear everything
- Memory pressure as a failure mode

### Chapter placement
- **Browser profiles** in "How Browsers Work" architectural chapter
- **Storage mechanisms** in "Page Interaction" or "State Management" chapter
- **Memory pressure** in "Reliability" chapter alongside navigation failures

---

## Perspective B — Production Browser Agent Infrastructure

### Where Browser Memory fits
Core operational knowledge. Profile management, session rotation, memory monitoring are production-level concerns.

### Key concepts
- Fresh vs persistent profile trade-offs (decision framework)
- Profile pool architecture
- Memory monitoring integration with health checks
- Session rotation strategies (TTL-based, memory-based, detection-based)
- Storage cleanup automation

### Chapter placement
- **Profile management** in "Session Architecture" chapter
- **Memory monitoring** in "Observability" chapter
- **Profile rotation** in "Operational Patterns" chapter
- Include decision tree: fresh vs persistent for different workloads

---

## Perspective C — Browser UX Engineering / Agent-Ready Web

### Where Browser Memory fits
Storage and memory are invisible to users but critical for agents. Designing for agent-comprehensible storage state is a UX pattern.

### Key concepts
- Storage transparency — agents need to know what state exists
- The case for declarative storage APIs (agent-accessible storage enumeration)
- Memory pressure as a design constraint — agents need graceful degradation signals
- Profile isolation design patterns for multi-agent systems

### Chapter placement
- **Storage transparency** in "What Agents Need That Humans Don't"
- **Graceful degradation** in "Designing for Agent Reliability"
- Propose storage enumeration API pattern (similar to `document.readyState` for storage)

---

*Research Cycle 002 — 2026-07-29*

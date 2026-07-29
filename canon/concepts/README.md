# Canonical Concepts Layer

This is the permanent intellectual property. Concepts are independent of any implementation, tool, or knowledge object.

## Purpose

Research domains produce concepts. Concepts produce knowledge objects. Knowledge objects produce publications.

```
Research Domain
      ↓
Canonical Concept ← YOU ARE HERE
      ↓
HPF Knowledge Object
      ↓
Book chapter / Recipe / Decision guide
```

Concepts survive forever. Knowledge objects may evolve. Books may be rewritten. Concepts should outlast all of them.

## What a Concept Is

A concept is:

- A single, durable idea
- Defined independently of any tool or implementation
- Expressed through its properties, relationships, and constraints
- The atomic unit of the knowledge base

## What a Concept Is Not

- Not a tool profile (Playwright is not a concept — browser automation protocol is)
- Not a knowledge object (HPF objects add structure for the reasoner)
- Not a book chapter (narrative is a publication concern)

## Current Concepts

These are seeded from the HPF knowledge domain and research taxonomy:

| Concept | Domain | Description |
|---|---|---|
| Browser Session Lifecycle | Browser State | The sequence from launch to termination |
| Browser Profile | Browser Memory | Persistent browser identity and state |
| Automation Protocol | Browser Architecture | CDP, WebDriver, BiDi abstractions |
| Anti-Detection | Browser Perception | Techniques to avoid automation detection |
| Blocking and Rate Limiting | Browser Economics | Server-side defense mechanisms |
| Retry Strategy | Browser Reliability | Exponential backoff, jitter, circuit breakers |
| Selector Strategy | Browser Reliability | DOM query mechanisms and their trade-offs |
| Health Check | Browser Reliability | Determining if a browser session is functional |
| Extraction Pattern | Browser State | Pulling data from live browser sessions |
| Download Pipeline | Browser Distributed Systems | Reliable file acquisition from browser sessions |

## Adding a Concept

1. Identify a durable idea from research that is not tool-specific
2. Create a `.md` file in this directory
3. Define: definition, properties, relationships to other concepts, constraints
4. Freeze it (concepts change only when the underlying research understanding changes)

## Relationship to HPF Objects

Each canonical concept may map to one or more HPF knowledge objects. The mapping is documented in the HPF knowledge object metadata.

---

*Frozen: 2026-07-29*

# Open Questions — Browser Memory

Questions discovered during research that are unresolved.

1. **Tab discard in headless** — Does Chrome Memory Saver (tab discarding) operate in headless mode? Current evidence suggests Chrome Saver is headed-only, but OS-level OOM still applies. Undocumented.

2. **CDP Memory domain in incognito** — What is the relationship between CDP `Memory` domain availability and incognito/guest mode? Some domains are restricted in incognito.

3. **Cross-browser profile formats** — Chromium vs Firefox vs WebKit differ significantly in profile structure. Current research is Chromium-dominant. How much of this generalizes?

4. **Supercookie survival** — Can IndexedDB-based supercookies survive a "clear cookies and site data" operation? Or is a new profile required for complete isolation?

5. **CDP memory overhead per target** — Each attached CDP target consumes additional memory on the browser side. What is the overhead per target? Does it scale linearly?

6. **Pre-OOM detection** — Is there a reliable pre-crash warning signal (memory pressure notification, high-water mark event) in any protocol, or is post-crash detection the only option?

7. **Service worker interference** — Can a service worker from a previous session persist and interfere with automation in a new session on the same profile?

8. **Storage quota visibility** — Can automation detect per-origin storage quota usage without JS execution (i.e., via protocol only)?

9. **Profile migration compatibility** — How often do profile format changes between Chromium versions break profile reuse? Current practice is anecdotal.

---

*Research Cycle 002 — 2026-07-29*

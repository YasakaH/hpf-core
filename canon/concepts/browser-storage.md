# Browser Storage

**Domain**: Browser Memory

## Definition

The collection of client-side storage mechanisms available to web pages within a browser origin, including cookies, Web Storage (localStorage, sessionStorage), IndexedDB, Cache API, and the HTTP cache.

## Storage Types

| Mechanism | Scope | Lifetime | Capacity | Sync/Async | Persistence |
|---|---|---|---|---|---|
| Cookie | Domain + path | Session or max-age | 4KB per cookie, ~180 per domain | Sync | Disk (profile Cookies DB) |
| localStorage | Origin | Until cleared | ~5-10MB per origin | Sync | Disk (profile Local Storage) |
| sessionStorage | Tab (origin) | Until tab closes | ~5-10MB per origin | Sync | Memory only |
| IndexedDB | Origin | Until cleared | Unlimited | Async | Disk (profile IndexedDB) |
| Cache API | Origin (SW scope) | Until cleared | Unlimited | Async | Disk (profile Cache Storage) |
| HTTP Cache | Browser-wide | Time/TTL-bound | Disk quota managed | Async (implicit) | Disk (profile Cache) |

## Storage Observability

| Storage Type | CDP Domain | WebDriver Access | Notes |
|---|---|---|---|
| Cookies | `Network.getCookies`, `Network.deleteCookies` | `getCookies`, `addCookie`, `deleteCookie` | Full read/write via both protocols |
| localStorage | `Storage.getDOMStorageItems`, `Storage.setDOMStorageItem` | `executeScript(localStorage.getItem())` | CDP: direct; WebDriver: via JS execution |
| sessionStorage | `Storage.getDOMStorageItems` (same API) | `executeScript(sessionStorage.getItem())` | Only accessible in current tab session |
| IndexedDB | `IndexedDB.requestDatabaseNames`, `IndexedDB.requestData` | `executeScript(JS IDB API)` | CDP: direct enumeration; WebDriver: JS proxy |
| Cache API | `CacheStorage.requestCacheNames`, `CacheStorage.requestEntries` | `executeScript(caches.open())` | CDP: direct; WebDriver: JS proxy |
| HTTP Cache | `Network.clearBrowserCache` | No direct access | Can be cleared, not inspected, via protocols |

## Relationships

| Concept | Relationship |
|---|---|
| Browser Profile | Storage is the content of a profile. Without storage, a profile is an empty directory. |
| Session Lifecycle | Storage writes happen during session lifecycle; reads on navigation. sessionStorage dies with the session. |
| Anti-Detection | Tracking storage (cookies, IndexedDB supercookies, localStorage) enables cross-session identification. |
| Automation Protocol | Protocol choice determines which storage mechanisms are directly controllable. |

## Constraints

- Storage is origin-scoped: `https://a.com` cannot read `https://b.com` storage
- Cross-origin iframes have their own storage (third-party cookie phase-out affects this)
- Clearing cookies does NOT clear localStorage, IndexedDB, or Cache API — independent storage systems
- Service Workers persist across sessions and can re-populate caches after clear
- `sessionStorage` is per-tab, not per-origin — two tabs to the same origin have separate sessionStorage
- Private/incognito mode uses in-memory storage (no disk writes, cleared on close)
- Storage quotas are shared per origin: IndexedDB + localStorage + Cache API share the same pool
- Clearing site data (browser UI) clears all storage types for an origin; clearing cookies (API) clears only cookies

---

*Canonical concept. Not tool-specific.*

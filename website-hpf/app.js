/* HPF Research Workbench — internal knowledge system SPA.
   Consumes ONLY the knowledge-export-core-v1 contract (data/export.json) and
   its derived index (data/index.json). Never reads engine internals. */

"use strict";

const state = {
  export: null,
  index: null,
  authed: false,
};

const $ = (sel) => document.querySelector(sel);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
}[c]));

/* ---------- Auth (in-app layer; Cloudflare Access is the boundary) ---------- */

async function sha256Hex(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function tryLogin(username, password) {
  const users = window.HPF_CONFIG?.auth?.users || {};
  const expected = users[username];
  if (!expected) return false;
  return (await sha256Hex(password)) === expected;
}

function initAuth() {
  const auth = window.HPF_CONFIG?.auth;
  if (!auth || !auth.enabled) {
    state.authed = true;
    return;
  }
  if (sessionStorage.getItem("hpf_session") === "1") {
    state.authed = true;
    return;
  }
  const overlay = $("#login-overlay");
  overlay.classList.remove("hidden");
  $("#login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const ok = await tryLogin($("#login-username").value.trim(), $("#login-password").value);
    if (ok) {
      sessionStorage.setItem("hpf_session", "1");
      state.authed = true;
      overlay.classList.add("hidden");
      boot();
    } else {
      $("#login-error").classList.remove("hidden");
    }
  });
}

/* ---------- Data loading ---------- */

async function loadData() {
  const [exp, idx] = await Promise.all([
    fetch("data/export.json").then((r) => r.json()),
    fetch("data/index.json").then((r) => r.json()),
  ]);
  state.export = exp;
  state.index = idx;
  const gen = exp.generated_at || "";
  $("#topbar-status").textContent =
    `${exp.contract} · schema ${exp.schema_version} · generated ${gen.replace("T", " ").replace("Z", " UTC")}`;
}

/* ---------- Routing ---------- */

function parseHash() {
  const h = location.hash.replace(/^#/, "");
  const [path, query] = h.split("?");
  const parts = path.split("/").filter(Boolean);
  const params = new URLSearchParams(query || "");
  return { parts, params };
}

function navigate(route) {
  location.hash = route;
}

function render() {
  const { parts, params } = parseHash();
  const section = parts[0] || "dashboard";
  document.querySelectorAll(".nav-btn").forEach((b) =>
    b.classList.toggle("active", b.dataset.route === "#/" + section)
  );
  const main = $("#main");
  if (section === "validation") main.innerHTML = viewValidation();
  else if (section === "relationships") main.innerHTML = viewRelationships();
  else if (section === "diagnostics") main.innerHTML = viewDiagnostics();
  else if (section === "object") main.innerHTML = viewObject(parts[1]);
  else main.innerHTML = viewDashboard(params.get("q") || "");
}

/* ---------- Dashboard ---------- */

function viewDashboard(q) {
  const idx = state.index;
  const s = idx.summary;
  const validPct = s.total ? Math.round((s.valid / s.total) * 100) : 0;
  const html = `
    <div class="grid">
      <div class="stat"><div class="num">${s.total}</div><div class="label">Objects</div></div>
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Valid (${validPct}%)</div></div>
      <div class="stat"><div class="num bad">${s.invalid}</div><div class="label">Invalid</div></div>
      <div class="stat"><div class="num warn">${s.error_count}</div><div class="label">Validator errors</div></div>
      <div class="stat"><div class="num">${idx.edges.length}</div><div class="label">Relationship edges</div></div>
      <div class="stat"><div class="num">${idx.cross_domain_edges.length}</div><div class="label">Cross-domain links</div></div>
    </div>
    <div class="grid">
      ${distCard("Origin", s.origins)}
      ${distCard("Authority", s.authorities)}
      ${distCard("Status", s.statuses)}
      ${distCard("Kind", s.kinds)}
    </div>
    <div class="grid">
      ${distCard("Domain", s.domains)}
      <div class="card"><h2>Cycles</h2><p class="muted">${esc(s.cycles.join(", ") || "—")}</p></div>
      <div class="card"><h2>Contract</h2>
        <table>
          <tr><td>Contract</td><td>${esc(idx.source_contract)}</td></tr>
          <tr><td>Schema</td><td>${esc(idx.source_schema_version)}</td></tr>
          <tr><td>Index producer</td><td>${esc(idx.producer)} v${esc(idx.producer_version)}</td></tr>
        </table>
      </div>
    </div>`;
  return html;
}

function distCard(label, dist) {
  const entries = Object.entries(dist || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return `<div class="card"><h2>${esc(label)}</h2><p class="muted">—</p></div>`;
  const rows = entries.map(([k, v]) => `<tr><td>${esc(k)}</td><td>${v}</td></tr>`).join("");
  return `<div class="card"><h2>${esc(label)}</h2><table>${rows}</table></div>`;
}

/* ---------- Validation ---------- */

function viewValidation() {
  const invalid = state.index.invalid;
  const s = state.index.summary;
  return `
    <div class="grid">
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Valid</div></div>
      <div class="stat"><div class="num bad">${s.invalid}</div><div class="label">Invalid</div></div>
      <div class="stat"><div class="num warn">${s.error_count}</div><div class="label">Errors</div></div>
    </div>
    <div class="card"><h2>Invalid objects (metadata only — no content exported)</h2>
      ${invalid.length ? `<table>
        <tr><th>Object</th><th>Source</th><th>Errors</th></tr>
        ${invalid.map((o) => `<tr>
          <td><a href="#/object/${encodeURIComponent(o.id)}">${esc(o.title)}</a></td>
          <td class="muted">${esc(o.source)}</td>
          <td><ul style="margin:0;padding-left:16px">${o.errors.map((e) => `<li>${esc(e)}</li>`).join("")}</ul></td>
        </tr>`).join("")}
      </table>` : `<p class="muted">No invalid objects.</p>`}
    </div>`;
}

/* ---------- Relationships ---------- */

function viewRelationships() {
  const edges = state.index.edges;
  const cross = state.index.cross_domain_edges;
  return `
    <div class="grid">
      <div class="stat"><div class="num">${edges.length}</div><div class="label">All edges (valid objects)</div></div>
      <div class="stat"><div class="num">${cross.length}</div><div class="label">Cross-domain edges</div></div>
    </div>
    <div class="card"><h2>Cross-domain links</h2>
      ${cross.length ? `<table>
        <tr><th>Source</th><th>Relationship</th><th>Target</th></tr>
        ${cross.map((e) => `<tr>
          <td><a href="#/object/${encodeURIComponent(e.source)}">${esc(e.source_title)}</a></td>
          <td>${esc(e.relationship)}</td>
          <td>${esc(e.target)}</td>
        </tr>`).join("")}
      </table>` : `<p class="muted">None.</p>`}
    </div>
    <div class="card"><h2>All relationship edges (${edges.length})</h2>
      <table>
        <tr><th>Source</th><th>Relationship</th><th>Target</th><th>Description</th></tr>
        ${edges.map((e) => `<tr>
          <td><a href="#/object/${encodeURIComponent(e.source)}">${esc(e.source_title)}</a></td>
          <td>${esc(e.relationship)}</td>
          <td><a href="#/object/${encodeURIComponent(e.target)}">${esc(e.target)}</a></td>
          <td class="muted">${esc(e.description || "")}</td>
        </tr>`).join("")}
      </table>
    </div>`;
}

/* ---------- Object detail ---------- */

function viewObject(id) {
  const obj = (state.export.objects || []).find((o) => o.id === id);
  if (!obj) return `<div class="card"><h2>Object not found</h2><p class="muted">${esc(id)}</p></div>`;

  const valid = obj.schema_validation === "valid";
  const badge = `<span class="badge ${valid ? "valid" : "invalid"}">${esc(obj.schema_validation)}</span>`;
  const axes = [
    ["origin", obj.origin], ["authority", obj.authority], ["status", obj.status],
  ].map(([k, v]) => `<span class="badge">${esc(k)}: ${esc(v)}</span>`).join("");

  const blocks = [];
  if (valid) {
    for (const [name, list] of [
      ["Claims", obj.claims], ["Relationships", obj.relationships],
      ["Constraints", obj.constraints], ["Recommendations", obj.recommendations],
    ]) {
      if (!list || !list.length) continue;
      const items = list.map((b) => {
        if (name === "Claims") return `<li>${esc(b.claim)} <span class="muted">(certainty: ${esc(b.certainty)})</span></li>`;
        if (name === "Relationships") return `<li><b>${esc(b.relationship)}</b> → <a href="#/object/${encodeURIComponent(b.concept)}">${esc(b.concept)}</a> — ${esc(b.description || "")}</li>`;
        if (name === "Constraints") return `<li>${esc(b.constraint)} <span class="muted">(${esc(b.type || "")})</span></li>`;
        return `<li>${esc(b.recommendation)} <span class="muted">(${esc(b.context || "")})</span></li>`;
      }).join("");
      blocks.push(`<div class="block"><h3>${name} (${list.length})</h3><ul>${items}</ul></div>`);
    }
  } else {
    blocks.push(`<div class="block"><h3>Validation errors (${obj.errors.length})</h3><ul>${obj.errors.map((e) => `<li>${esc(e)}</li>`).join("")}</ul></div>`);
    blocks.push(`<p class="muted">Invalid objects export metadata and errors only — no semantic content.</p>`);
  }

  return `
    <div class="object-title">${esc(obj.title)}</div>
    <div class="object-sub">${esc(obj.id)} · ${esc(obj.kind || "unknown")}${obj.domain ? " · " + esc(obj.domain) : ""}</div>
    <div class="card" style="margin-bottom:16px">
      <table>
        <tr><th>Schema validation</th><td>${badge}</td></tr>
        ${axes.length ? `<tr><th>Evidence axes</th><td>${axes}</td></tr>` : ""}
        <tr><th>Research cycle</th><td>${esc(obj.research_cycle || "—")}</td></tr>
        <tr><th>Source</th><td class="muted">${esc(obj.source)}</td></tr>
        <tr><th>Blocks</th><td class="muted">${Object.entries(obj.blocks || {}).map(([k, v]) => `${esc(k)}: ${v}`).join(" · ")}</td></tr>
      </table>
    </div>
    <div class="card">${blocks.join("") || `<p class="muted">No content.</p>`}</div>`;
}

/* ---------- Diagnostics ---------- */

function viewDiagnostics() {
  const e = state.export;
  const idx = state.index;
  const s = idx.summary;
  const conformanceOk =
    s.total === e.corpus.total_files &&
    s.valid === e.corpus.valid &&
    s.invalid === e.corpus.invalid &&
    s.error_count === e.corpus.error_count;
  return `
    <div class="grid">
      <div class="stat"><div class="num ${conformanceOk ? "ok" : "bad"}">${conformanceOk ? "PASS" : "FAIL"}</div><div class="label">Index ↔ export conformance</div></div>
      <div class="stat"><div class="num">${esc(e.schema_version)}</div><div class="label">Schema version</div></div>
      <div class="stat"><div class="num">${esc(e.producer)}</div><div class="label">Producer</div></div>
    </div>
    <div class="card"><h2>Contract header</h2>
      <table>
        <tr><td>Contract</td><td>${esc(e.contract)}</td></tr>
        <tr><td>Schema version</td><td>${esc(e.schema_version)}</td></tr>
        <tr><td>Producer</td><td>${esc(e.producer)} v${esc(e.producer_version)}</td></tr>
        <tr><td>Compatibility</td><td>${esc(e.compatibility || "—")}</td></tr>
        <tr><td>Generated at</td><td>${esc(e.generated_at)}</td></tr>
        <tr><td>Axes</td><td>${Object.entries(e.axes || {}).map(([k, v]) => `<b>${esc(k)}</b>: ${esc(v.join(", "))}`).join("<br>")}</td></tr>
      </table>
    </div>
    <div class="card" style="margin-top:16px"><h2>Corpus snapshot</h2>
      <table>
        <tr><td>Files</td><td>${e.corpus.total_files}</td></tr>
        <tr><td>Parsed</td><td>${e.corpus.parsed}</td></tr>
        <tr><td>Valid</td><td>${e.corpus.valid}</td></tr>
        <tr><td>Invalid</td><td>${e.corpus.invalid}</td></tr>
        <tr><td>Errors</td><td>${e.corpus.error_count}</td></tr>
        <tr><td>Cycles</td><td>${esc((e.corpus.cycles || []).join(", ") || "—")}</td></tr>
      </table>
    </div>`;
}

/* ---------- Search ---------- */

function runSearch(q) {
  if (!q) return [];
  const needle = q.toLowerCase();
  return state.index.objects
    .filter((o) =>
      (o.title || "").toLowerCase().includes(needle) ||
      (o.id || "").toLowerCase().includes(needle) ||
      (o.domain || "").toLowerCase().includes(needle) ||
      (o.kind || "").toLowerCase().includes(needle)
    )
    .slice(0, 20);
}

function renderSearchResults(q) {
  const box = $("#search-results");
  if (!q) {
    box.innerHTML = "";
    return;
  }
  const results = runSearch(q);
  box.innerHTML = results.length
    ? results.map((o) =>
        `<div class="search-result" data-id="${esc(o.id)}">
           ${esc(o.title)}
           <div class="muted">${esc(o.id)} · ${o.valid ? "valid" : "invalid"}</div>
         </div>`).join("")
    : `<div class="muted" style="padding:6px 8px">No results.</div>`;
  box.querySelectorAll(".search-result").forEach((el) =>
    el.addEventListener("click", () => {
      $("#search-input").value = "";
      box.innerHTML = "";
      navigate("#/object/" + encodeURIComponent(el.dataset.id));
    })
  );
}

/* ---------- Boot ---------- */

async function boot() {
  await loadData();
  window.addEventListener("hashchange", () => { render(); renderSearchResults($("#search-input").value); });
  document.querySelectorAll(".nav-btn").forEach((b) =>
    b.addEventListener("click", () => { $("#search-input").value = ""; navigate(b.dataset.route); })
  );
  $("#search-input").addEventListener("input", (e) => renderSearchResults(e.target.value));
  render();
}

initAuth();
if (state.authed) boot();

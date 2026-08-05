/* HPF Research Workbench — internal knowledge system SPA.
   Consumes ONLY the knowledge-export-core-v1 contract (data/export.json) and
   its derived index (data/index.json). Never reads engine internals.
   Authentication is handled at the edge by Cloudflare Access — this
   application assumes anyone who reaches it has been authenticated.
   config.json (optional) holds links; the workbench works without it. */

"use strict";

const state = {
  export: null,
  index: null,
  config: {},
};

const $ = (sel) => document.querySelector(sel);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
}[c]));

/* ---------- Data loading ---------- */

async function loadData() {
  const [exp, idx, cfg] = await Promise.all([
    fetch("data/export.json").then((r) => r.json()),
    fetch("data/index.json").then((r) => r.json()),
    fetch("config.json").then((r) => r.json()).catch(() => ({})),
  ]);
  state.export = exp;
  state.index = idx;
  state.config = cfg || {};
  const gen = exp.generated_at || "";
  $("#topbar-status").textContent =
    `Experimental build · ${idx.summary.total} objects · Release ${gen.slice(0, 10)}`;
  const portal = $("#portal-link");
  if (cfg && cfg.site_url) {
    portal.href = cfg.site_url;
    portal.classList.remove("hidden");
  }
}

/* ---------- Research records (local storage) ---------- */

const DRAFTS_KEY = "hpf.research.drafts";

function getDrafts() {
  try { return JSON.parse(localStorage.getItem(DRAFTS_KEY)) || []; } catch { return []; }
}

function saveDrafts(d) {
  localStorage.setItem(DRAFTS_KEY, JSON.stringify(d));
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
  const navKey = "#/" + parts.join("/");
  document.querySelectorAll(".nav-btn").forEach((b) =>
    b.classList.toggle("active", b.dataset.route === navKey)
  );
  const main = $("#main");
  const one = parts[0] || "home";
  if (one === "home") main.innerHTML = viewHome();
  else if (one === "research") main.innerHTML = parts[1] === "new" ? viewResearchNew(params) : viewResearch();
  else if (one === "knowledge") main.innerHTML = parts[1] === "findings" ? viewFindings() : viewKnowledge();
  else if (one === "relationships") main.innerHTML = viewRelationships();
  else if (one === "validation") main.innerHTML = viewValidation();
  else if (one === "corpus") main.innerHTML = viewCorpus();
  else if (one === "publishing") main.innerHTML = viewPublishing();
  else if (one === "diagnostics") main.innerHTML = viewDiagnostics();
  else if (one === "object") main.innerHTML = viewObject(parts[1]);
  else main.innerHTML = viewHome();
  bindPage(parts);
}

/* ---------- Home ---------- */

function viewHome() {
  const i = state.index;
  const s = i.summary;
  const examples = [
    "Compare Microsoft Fara vs nodriver",
    "Latest browser automation tools",
    "Research AI computer-use agents",
    "Review my cookbook",
    "Import an RFC into the corpus",
  ];
  const drafts = getDrafts();
  const researching = drafts.filter((d) => d.status !== "completed").length;
  const chips = examples.map((t) => `<button class="chip" data-example="${esc(t)}">${esc(t)}</button>`).join("");
  return `
    <div class="hero">
      <h1>What would you like to research?</h1>
      <form id="prompt-form" class="prompt">
        <input id="prompt-input" type="text" placeholder="Describe a question, topic, or paper…" autocomplete="off">
        <button type="submit" class="btn">Research</button>
      </form>
      <div class="chips">${chips}</div>
    </div>
    <div class="grid">
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Concepts in the corpus</div><a class="more" href="#/knowledge">Browse</a></div>
      <div class="stat"><div class="num ${s.invalid ? "warn" : "ok"}">${s.invalid}</div><div class="label">Files needing attention</div><a class="more" href="#/validation">Corpus health</a></div>
      <div class="stat"><div class="num">${i.edges.length}</div><div class="label">Relationships mapped</div><a class="more" href="#/relationships">Explore</a></div>
      <div class="stat"><div class="num">${researching}</div><div class="label">Research records</div><a class="more" href="#/research">Open</a></div>
    </div>`;
}

/* ---------- Research ---------- */

function viewResearch() {
  const drafts = getDrafts().sort((a, b) => (b.created > a.created ? 1 : -1));
  const rows = drafts.length ? drafts.map((d) => `
    <div class="research-item">
      <div class="research-head">
        <div class="research-title">${esc(d.topic)}</div>
        <div class="research-meta">${esc(d.created.slice(0, 10))} · ${esc(d.audience)} · ${esc(d.depth)}</div>
      </div>
      ${d.goal ? `<div class="muted">${esc(d.goal)}</div>` : ""}
      <div class="research-actions">
        <span class="badge ${esc(d.status)}">${esc(d.status)}</span>
        ${d.status !== "running" ? `<button class="btn small" data-draft="${esc(d.id)}" data-next="running">Start</button>` : ""}
        ${d.status !== "completed" ? `<button class="btn small" data-draft="${esc(d.id)}" data-next="completed">Complete</button>` : ""}
        <button class="btn small ghost" data-draft="${esc(d.id)}" data-delete="1">Delete</button>
      </div>
    </div>`).join("")
    : `<p class="muted">No research records yet. Records live in this browser until the research orchestrator is built — they will become its intake.</p>`;
  const pipeline = [
    ["Plan investigation", "research question, goals, depth"],
    ["Collect sources", "docs, GitHub, papers, benchmarks, community"],
    ["Extract facts", "normalize into evidence"],
    ["Cross-reference corpus", "match and reconcile with existing objects"],
    ["Generate candidate findings", "proposals, not conclusions"],
    ["Validate and adjudicate", "independent review, confidence, status"],
    ["Admit to corpus", "export for downstream publishing"],
  ].map(([t, d]) => `<li><b>${esc(t)}</b> <span class="muted">— ${esc(d)}</span></li>`).join("");
  return `
    <div class="row-between"><h1>Research</h1><button class="btn" id="new-research">New Research</button></div>
    <div class="card"><h2>Pipeline</h2>
      <p class="muted">HPF performs research; it does not write articles. The orchestrator (agent dispatch, evidence collection, adjudication) is the next subsystem to build. Records started here become its intake.</p>
      <ol class="pipeline">${pipeline}</ol>
    </div>
    <div class="card"><h2>Records (${drafts.length})</h2>${rows}</div>`;
}

function viewResearchNew(params) {
  const topic = params.get("topic") || "";
  return `
    <div class="row-between"><h1>New Research</h1><button class="btn ghost" id="back-research">Back</button></div>
    <div class="card" style="max-width:720px">
      <form id="research-form">
        <div class="form-row"><label>Topic</label><input name="topic" value="${esc(topic)}" required placeholder="e.g. Compare Microsoft Fara vs nodriver"></div>
        <div class="form-row"><label>Goal</label><textarea name="goal" rows="2" placeholder="What question should this answer?"></textarea></div>
        <div class="form-row">
          <label>Audience</label>
          <select name="audience">
            <option>Internal</option><option>Blog</option><option>Whitepaper</option>
          </select>
        </div>
        <div class="form-row">
          <label>Depth</label>
          <select name="depth">
            <option>Quick</option><option selected>Standard</option><option>Deep</option>
          </select>
        </div>
        <button type="submit" class="btn">Record research</button>
        <p class="muted" style="margin-top:8px">Records intent in this browser. The orchestration pipeline executes once built.</p>
      </form>
    </div>`;
}

/* ---------- Knowledge ---------- */

function viewKnowledge() {
  const objs = state.index.objects.filter((o) => o.valid);
  const rows = objs.slice().sort((a, b) => a.title.localeCompare(b.title)).map((o) => `
    <div class="concept"><a href="#/object/${encodeURIComponent(o.id)}">${esc(o.title)}</a>
      <div class="muted">${esc(o.kind)} · ${esc(o.domain)} · cycle ${esc(o.cycle)}</div>
    </div>`).join("");
  return `
    <div class="row-between"><h1>Concepts</h1></div>
    <div class="card"><h2>Corpus (${objs.length} valid)</h2>
      <input type="text" id="concept-q" placeholder="Filter concepts…" autocomplete="off">
      <div class="concept-grid" id="concept-grid">${rows}</div>
    </div>`;
}

function viewFindings() {
  const objs = (state.export.objects || []).filter((o) => o.schema_validation === "valid" && o.claims && o.claims.length);
  const byDomain = {};
  let total = 0;
  for (const o of objs) {
    for (const c of o.claims) {
      total++;
      const d = o.domain || "unassigned";
      (byDomain[d] = byDomain[d] || []).push({ claim: c.claim, certainty: c.certainty, id: o.id, title: o.title });
    }
  }
  const domains = Object.entries(byDomain).sort((a, b) => b[1].length - a[1].length);
  const sections = domains.map(([d, claims]) => `
    <div class="card"><h2>${esc(d)} <span class="muted">(${claims.length})</span></h2>
      <ul class="findings">${claims.map((c) => `<li><span class="badge ${certClass(c.certainty)}">${esc(String(c.certainty))}</span> ${esc(c.claim)} <span class="muted">— <a href="#/object/${encodeURIComponent(c.id)}">${esc(c.title)}</a></span></li>`).join("")}</ul>
    </div>`).join("");
  return `
    <div class="row-between"><h1>Findings</h1></div>
    <div class="card"><h2>Evidence the corpus carries</h2>
      <p class="muted">Previewed from exported claims across ${objs.length} concepts (${total} claims). A first-class findings model is roadmap — it should be produced by research orchestration; this view shows what the corpus already asserts.</p>
    </div>
    ${sections || `<p class="muted">No claims exported.</p>`}`;
}

function certClass(v) {
  const n = String(v || "").toLowerCase();
  return n === "high" ? "valid" : n === "medium" ? "warn" : n === "low" ? "bad" : "";
}

function viewRelationships() {
  const edges = state.index.edges;
  const cross = state.index.cross_domain_edges;
  return `
    <div class="row-between"><h1>Relationships</h1></div>
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

/* ---------- Corpus Health ---------- */

function viewValidation() {
  const invalid = state.index.invalid;
  const s = state.index.summary;
  const tally = {};
  for (const o of invalid) for (const e of o.errors) tally[e] = (tally[e] || 0) + 1;
  const top = Object.entries(tally).sort((a, b) => b[1] - a[1]).slice(0, 3);
  const pct = s.total ? Math.round((s.valid / s.total) * 100) : 0;
  const mostCommon = top.length
    ? `<div class="card"><h2>Most common issue</h2>${top.map(([e, n]) => `<div class="issue"><span class="badge warn">${n}×</span> ${esc(e)}</div>`).join("")}</div>`
    : "";
  return `
    <div class="row-between"><h1>Corpus Health</h1></div>
    <div class="card"><p class="muted">${s.invalid ? `${s.invalid} of ${s.total} knowledge files need attention before a release is clean.` : "All knowledge files pass validation."}</p></div>
    <div class="grid">
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Healthy files (${pct}%)</div></div>
      <div class="stat"><div class="num warn">${s.invalid}</div><div class="label">Files needing attention</div></div>
      <div class="stat"><div class="num bad">${s.error_count}</div><div class="label">Validation issues</div></div>
    </div>
    ${mostCommon}
    <div class="card"><h2>Files needing attention (metadata only — no content exported)</h2>
      ${invalid.length ? `<table>
        <tr><th>Object</th><th>Source</th><th>Issues</th></tr>
        ${invalid.map((o) => `<tr>
          <td><a href="#/object/${encodeURIComponent(o.id)}">${esc(o.title)}</a></td>
          <td class="muted">${esc(o.source)}</td>
          <td><ul style="margin:0;padding-left:16px">${o.errors.map((e) => `<li>${esc(e)}</li>`).join("")}</ul></td>
        </tr>`).join("")}
      </table>` : `<p class="muted">No invalid objects.</p>`}
    </div>`;
}

/* ---------- Release ---------- */

function viewCorpus() {
  const e = state.export;
  const idx = state.index;
  const s = idx.summary;
  return `
    <div class="row-between"><h1>Release</h1></div>
    <div class="card"><h2>This deployment</h2>
      <table>
        <tr><td>Release date</td><td>${esc(e.generated_at.slice(0, 10))}</td></tr>
        <tr><td>Objects</td><td>${s.total} (${s.valid} valid)</td></tr>
        <tr><td>Relationships</td><td>${idx.edges.length} edges (${idx.cross_domain_edges.length} cross-domain)</td></tr>
        <tr><td>Cycles covered</td><td>${esc((s.cycles || []).join(", ") || "—")}</td></tr>
        <tr><td>Exporter</td><td>${esc(e.producer)} v${esc(e.producer_version)}</td></tr>
      </table>
    </div>
    <div class="card"><h2>Corpus snapshot</h2>
      <table>
        <tr><td>Files</td><td>${e.corpus.total_files}</td></tr>
        <tr><td>Parsed</td><td>${e.corpus.parsed}</td></tr>
        <tr><td>Valid</td><td>${e.corpus.valid}</td></tr>
        <tr><td>Invalid</td><td>${e.corpus.invalid}</td></tr>
        <tr><td>Errors</td><td>${e.corpus.error_count}</td></tr>
      </table>
    </div>
    <p class="muted">Data served is the committed, gated release — reproducible from git, never regenerated at deploy time.</p>`;
}

/* ---------- Publishing ---------- */

function viewPublishing() {
  const c = state.config;
  const contractUrl = c.contract_url || "#";
  return `
    <div class="row-between"><h1>Publishing</h1></div>
    <div class="card"><h2>Downstream, never intertwined</h2>
      <p class="muted">Publishing consumes validated findings from the export contract and renders them for an audience. It never researches; research never markets.</p>
      <ul class="pipeline">
        <li><b>Blog posts</b> — technical comparisons and insights</li>
        <li><b>Whitepapers</b> — evidence-backed arguments</li>
        <li><b>Documentation</b> — reference material</li>
        <li><b>Comparison pages</b> — side-by-side findings</li>
        <li><b>FAQ and social</b> — extracts of the same findings</li>
      </ul>
      <p>Readers depend only on the contract: <a href="${esc(contractUrl)}" target="_blank" rel="noopener">${esc(c.contract_label || "knowledge-export-core-v1 (EXPORT_CONTRACT.md)")}</a>. Consumers are read-only — nothing downstream ever mutates the corpus.</p>
    </div>`;
}

/* ---------- Diagnostics ---------- */

function distCard(label, dist) {
  const entries = Object.entries(dist || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return `<div class="card"><h2>${esc(label)}</h2><p class="muted">—</p></div>`;
  const rows = entries.map(([k, v]) => `<tr><td>${esc(k)}</td><td>${v}</td></tr>`).join("");
  return `<div class="card"><h2>${esc(label)}</h2><table>${rows}</table></div>`;
}

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
    <div class="row-between"><h1>Diagnostics</h1></div>
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
    <div class="grid" style="margin-top:16px">
      ${distCard("Kind", s.kinds)}
      ${distCard("Origin", s.origins)}
      ${distCard("Authority", s.authorities)}
      ${distCard("Status", s.statuses)}
      ${distCard("Domain", s.domains)}
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

/* ---------- Page bindings ---------- */

function bindPage(parts) {
  const form = $("#prompt-form");
  if (form) form.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const v = $("#prompt-input").value.trim();
    if (v) location.hash = "#/research/new?topic=" + encodeURIComponent(v);
  });
  document.querySelectorAll(".chip").forEach((c) =>
    c.addEventListener("click", () => { $("#prompt-input").value = c.dataset.example; })
  );
  const nb = $("#new-research");
  if (nb) nb.addEventListener("click", () => { location.hash = "#/research/new"; });
  const bb = $("#back-research");
  if (bb) bb.addEventListener("click", () => { location.hash = "#/research"; });
  const rf = $("#research-form");
  if (rf) rf.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const fd = new FormData(rf);
    const drafts = getDrafts();
    drafts.push({
      id: Date.now() + "-" + Math.random().toString(36).slice(2, 7),
      topic: (fd.get("topic") || "").trim(),
      goal: (fd.get("goal") || "").trim(),
      audience: fd.get("audience"),
      depth: fd.get("depth"),
      status: "planned",
      created: new Date().toISOString(),
    });
    saveDrafts(drafts);
    location.hash = "#/research";
  });
  document.querySelectorAll("[data-draft]").forEach((b) =>
    b.addEventListener("click", () => {
      const id = b.dataset.draft;
      const drafts = getDrafts();
      const i = drafts.findIndex((x) => x.id === id);
      if (i === -1) return;
      if (b.dataset.delete === "1") drafts.splice(i, 1);
      else if (b.dataset.next) drafts[i].status = b.dataset.next;
      saveDrafts(drafts);
      render();
    })
  );
  const cq = $("#concept-q");
  if (cq) cq.addEventListener("input", (ev) => {
    const v = ev.target.value.toLowerCase();
    document.querySelectorAll("#concept-grid .concept").forEach((el) => {
      el.style.display = el.textContent.toLowerCase().includes(v) ? "" : "none";
    });
  });
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

boot();
/* HPF Research Workbench — internal knowledge system SPA.
   Consumes ONLY the knowledge-export-core-v1 contract (data/export.json) and
   its derived index (data/index.json). Never reads engine internals.
   Research sessions are operational evidence records (config.sessions_url),
   not corpus knowledge — they render pipeline + drafts for adjudication.
   Authentication is handled at the edge by Cloudflare Access.
   config.json (optional) holds links; the workbench works without it. */

"use strict";

const state = {
  export: null,
  index: null,
  config: {},
  sessions: [],
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
  if (cfg && cfg.sessions_url) state.sessions = await loadSessions(cfg.sessions_url);
}

async function loadSessions(baseUrl) {
  try {
    const idx = await fetch(baseUrl + "index.json").then((r) => r.json());
    const out = [];
    for (const s of idx.sessions || []) {
      try {
        const sess = await fetch(baseUrl + s.id + "/session.json").then((r) => r.json());
        out.push(sess);
      } catch { /* skip unreadable session */ }
    }
    return out;
  } catch { return []; }
}

/* ---------- Research records (browser) ---------- */

const DRAFTS_KEY = "hpf.research.drafts";

function getDrafts() {
  try { return JSON.parse(localStorage.getItem(DRAFTS_KEY)) || []; } catch { return []; }
}

function saveDrafts(d) {
  localStorage.setItem(DRAFTS_KEY, JSON.stringify(d));
}

function mergedResearch() {
  const drafts = getDrafts().map((d) => ({ ...d, kind: "record" }));
  const sess = state.sessions.map((s) => ({
    id: "session:" + s.id,
    topic: s.topic,
    goal: s.goal || "",
    audience: s.audience,
    depth: s.depth,
    status: s.status,
    created: s.created,
    kind: "session",
  }));
  return drafts.concat(sess).sort((a, b) => (b.created > a.created ? 1 : -1));
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
  else if (one === "research") main.innerHTML = parts[1] === "new" ? viewResearchNew(params) : parts[1] === "session" ? viewSession(parts[2]) : viewResearch();
  else if (one === "library") main.innerHTML = viewLibrary(parts[1]);
  else if (one === "findings") main.innerHTML = viewFindings();
  else if (one === "publish") main.innerHTML = viewPublish();
  else if (one === "validation") main.innerHTML = viewValidation();
  else if (one === "diagnostics") main.innerHTML = viewDiagnostics();
  else if (one === "object") main.innerHTML = viewObject(parts[1]);
  else main.innerHTML = viewHome();
  bindPage(parts);
}

/* ---------- Home ---------- */

function viewHome() {
  const s = state.index.summary;
  const examples = [
    "Compare Microsoft Fara vs nodriver",
    "Latest browser automation tools",
    "Research AI computer-use agents",
    "Review my cookbook",
    "Import an RFC into the corpus",
  ];
  const recent = mergedResearch().slice(0, 4);
  const chips = examples.map((t) => `<button class="chip" data-example="${esc(t)}">${esc(t)}</button>`).join("");
  const recentList = recent.length ? `
    <div class="card"><h2>Recent research</h2>
      ${recent.map((r) => `<div class="recent-item">
        <span class="badge ${badgeFor(r.status)}">${esc(r.status)}</span>
        <a href="${r.kind === "session" ? `#/research/session/${esc(r.id.split("session:")[1])}` : "#/research"}">${esc(r.topic)}</a>
      </div>`).join("")}
    </div>` : "";
  return `
    <div class="hero">
      <div class="hero-kicker">HPF Research</div>
      <h1>What would you like to research?</h1>
      <form id="prompt-form" class="prompt">
        <input id="prompt-input" type="text" placeholder="Describe a question, topic, or paper…" autocomplete="off">
        <button type="submit" class="btn btn-deep">Research</button>
      </form>
      <div class="hero-actions">
        <button class="btn" id="deep-research">Deep Research</button>
        <button class="btn ghost" id="quick-research">Quick Research</button>
        ${getDrafts().length ? `<button class="btn ghost" id="continue-research">Continue Previous Research</button>` : ""}
      </div>
      <div class="chips">${chips}</div>
    </div>
    <div class="grid">
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Concepts in the corpus</div><a class="more" href="#/library">Browse</a></div>
      <div class="stat"><div class="num ${s.invalid ? "warn" : "ok"}">${s.invalid}</div><div class="label">Documents needing attention</div><a class="more" href="#/validation">Corpus quality</a></div>
      <div class="stat"><div class="num">${state.sessions.length}</div><div class="label">Research sessions</div><a class="more" href="#/research">Open</a></div>
      <div class="stat"><div class="num">${state.index.edges.length}</div><div class="label">Relationships mapped</div><a class="more" href="#/library">Library</a></div>
    </div>
    ${recentList}
    <p class="muted" style="margin-top:16px">Release ${esc((state.export.generated_at || "").slice(0, 10))} · ${s.total} objects · ${s.cycles ? s.cycles.join(", ") : ""} cycles</p>`;
}

function badgeFor(status) {
  if (status === "completed" || status === "verified" || status === "valid") return "valid";
  if (status === "running" || status === "needs_adjudication" || status === "in_review") return "warn";
  return "planned";
}

/* ---------- Research ---------- */

function viewResearch() {
  const drafts = getDrafts().sort((a, b) => (b.created > a.created ? 1 : -1));
  const rows = drafts.length ? drafts.map((d) => `
    <div class="research-item">
      <div class="research-head">
        <div class="research-title">${esc(d.topic)}</div>
        <div class="research-meta">${esc(d.created.slice(0, 10))} · ${esc(d.audience)} · ${esc(d.depth)} · browser record</div>
      </div>
      ${d.goal ? `<div class="muted">${esc(d.goal)}</div>` : ""}
      <div class="research-actions">
        <span class="badge ${badgeFor(d.status)}">${esc(d.status)}</span>
        ${d.status !== "running" ? `<button class="btn small" data-draft="${esc(d.id)}" data-next="running">Start</button>` : ""}
        ${d.status !== "completed" ? `<button class="btn small" data-draft="${esc(d.id)}" data-next="completed">Complete</button>` : ""}
        <button class="btn small ghost" data-draft="${esc(d.id)}" data-delete="1">Delete</button>
      </div>
    </div>`).join("")
    : `<p class="muted">No browser records yet.</p>`;
  const sessRows = state.sessions.length ? state.sessions.sort((a, b) => (b.created > a.created ? 1 : -1)).map((s) => `
    <div class="research-item">
      <div class="research-head">
        <div class="research-title"><a href="#/research/session/${encodeURIComponent(s.id)}">${esc(s.topic)}</a></div>
        <div class="research-meta">${esc(s.created.slice(0, 10))} · ${esc(s.audience)} · ${esc(s.depth)} · orchestrator session</div>
      </div>
      ${s.goal ? `<div class="muted">${esc(s.goal)}</div>` : ""}
      <div class="research-actions">
        <span class="badge ${badgeFor(s.status)}">${esc(s.status)}</span>
        <span class="muted">${s.sources.length} sources · ${s.evidence.length} evidence · ${s.findings.length} draft findings</span>
        <a class="more" href="#/research/session/${encodeURIComponent(s.id)}">Open session</a>
      </div>
    </div>`).join("")
    : `<p class="muted">No orchestrator sessions yet.</p>`;
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
      <p class="muted">HPF performs research; it does not write articles. The orchestrator (tools/hpf-research) collects evidence mechanically and emits draft findings for adjudication — it never touches the corpus. Admitted findings flow to export, then to publishing.</p>
      <ol class="pipeline">${pipeline}</ol>
    </div>
    <div class="card"><h2>Sessions (${state.sessions.length})</h2>${sessRows}</div>
    <div class="card"><h2>Browser records (${drafts.length})</h2>${rows}</div>`;
}

function viewResearchNew(params) {
  const topic = params.get("topic") || "";
  const depth = params.get("depth") || "standard";
  const depthSel = (v) => `<option value="${v}" ${depth === v ? "selected" : ""}>${esc(v[0].toUpperCase() + v.slice(1))}</option>`;
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
          <select name="depth">${depthSel("quick")}${depthSel("standard")}${depthSel("deep")}</select>
        </div>
        <button type="submit" class="btn">Record research</button>
        <p class="muted" style="margin-top:8px">Browser records capture intent. To produce a working session, run the orchestrator: <code>python tools/hpf-research/research.py --topic "..."</code> — then sync its output into website-hpf/sessions/.</p>
      </form>
    </div>`;
}

function viewSession(id) {
  const s = state.sessions.find((x) => x.id === id);
  if (!s) return `<div class="card"><h2>Session not found</h2><p class="muted">${esc(id)}</p><p><a href="#/research">Back to research</a></p></div>`;
  const stages = (s.stages || []).map((st, i) => {
    const dot = st.state === "done" ? "done" : st.state === "failed" ? "bad" : "";
    return `<li class="stage-${dot || "planned"}"><span class="stage-dot"></span><b>${esc(st.name)}</b> <span class="muted">— ${esc(st.detail)}</span></li>`;
  }).join("");
  const sources = (s.sources || []).map((src) => `<li><a href="${esc(src.url)}" target="_blank" rel="noopener">${esc(src.title)}</a> <span class="muted">· ${esc(src.status)}${src.chars ? " · " + src.chars + " chars" : ""}</span></li>`).join("");
  const evidence = (s.evidence || []).map((ev) => `<div class="evidence-item"><span class="muted">[${esc(ev.id)}]</span> <span class="ev-src">${esc(ev.source)}</span><div class="ev-text">${esc(ev.excerpt)}</div></div>`).join("");
  const findings = (s.findings || []).map((f) => `
    <div class="finding-card ${badgeFor(f.status)}">
      <div class="finding-head"><span class="badge ${badgeFor(f.status)}">${esc(f.status)}</span> <span class="muted">${esc(f.id)} · method ${esc(f.method)}</span></div>
      <div class="finding-claim">${esc(f.claim)}</div>
      <div class="muted">Sources: ${f.sources.map((u) => esc(u)).join(" · ")}</div>
    </div>`).join("");
  return `
    <div class="row-between"><h1>Research Session</h1><a class="btn ghost" href="#/research">Back</a></div>
    <div class="card session-head">
      <h2>${esc(s.topic)}</h2>
      <div class="research-actions">
        <span class="badge ${badgeFor(s.status)}">${esc(s.status)}</span>
        <span class="muted">${esc(s.created.replace("T", " ").slice(0, 16))} · ${esc(s.audience)} · ${esc(s.depth)} · ${esc(s.id)}</span>
      </div>
      ${s.goal ? `<p class="muted">Goal: ${esc(s.goal)}</p>` : ""}
    </div>
    <div class="card"><h2>Research plan</h2><ol class="pipeline">${stages}</ol></div>
    <div class="card"><h2>Sources (${(s.sources || []).length})</h2><ul>${sources}</ul></div>
    <div class="card"><h2>Findings (${(s.findings || []).length}) — drafts, require adjudication</h2>${findings}</div>
    <div class="card"><h2>Evidence (${(s.evidence || []).length})</h2>${evidence}</div>
    <p class="muted">${esc(s.notes || "")}</p>`;
}

/* ---------- Library ---------- */

function viewLibrary(tab) {
  const active = tab || "concepts";
  const tabBtn = (id, label) => `<button class="tab ${active === id ? "active" : ""}" data-tab="${id}">${label}</button>`;
  const tabs = `<div class="tabs">${tabBtn("concepts", "Concepts")}${tabBtn("relationships", "Relationships")}</div>`;
  if (active === "relationships") return `<div class="row-between"><h1>Library</h1></div>${tabs}${viewRelationshipsBody()}`;
  const objs = state.index.objects.filter((o) => o.valid);
  const rows = objs.slice().sort((a, b) => a.title.localeCompare(b.title)).map((o) => `
    <div class="concept"><a href="#/object/${encodeURIComponent(o.id)}">${esc(o.title)}</a>
      <div class="muted">${esc(o.kind)} · ${esc(o.domain)} · cycle ${esc(o.cycle)}</div>
    </div>`).join("");
  return `<div class="row-between"><h1>Library</h1></div>${tabs}
    <div class="card"><h2>Corpus (${objs.length} valid)</h2>
      <input type="text" id="concept-q" placeholder="Filter concepts…" autocomplete="off">
      <div class="concept-grid" id="concept-grid">${rows}</div>
    </div>`;
}

function viewRelationshipsBody() {
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

/* ---------- Findings ---------- */

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
  const corpusSections = domains.map(([d, claims]) => `
    <div class="card"><h2>${esc(d)} <span class="muted">(${claims.length})</span></h2>
      <ul class="findings">${claims.map((c) => `<li><span class="badge ${certClass(c.certainty)}">${esc(String(c.certainty))}</span> ${esc(c.claim)} <span class="muted">— <a href="#/object/${encodeURIComponent(c.id)}">${esc(c.title)}</a></span></li>`).join("")}</ul>
    </div>`).join("");
  const sessionFindings = state.sessions.flatMap((s) => (s.findings || []).map((f) => ({ ...f, topic: s.topic, sid: s.id })));
  const sessionSection = sessionFindings.length ? `
    <div class="card"><h2>Session findings (drafts) <span class="muted">(${sessionFindings.length})</span></h2>
      ${sessionFindings.map((f) => `<div class="finding-card ${badgeFor(f.status)}">
        <div class="finding-head"><span class="badge ${badgeFor(f.status)}">${esc(f.status)}</span> <a href="#/research/session/${encodeURIComponent(f.sid)}">${esc(f.topic)}</a></div>
        <div class="finding-claim">${esc(f.claim)}</div>
      </div>`).join("")}
    </div>` : "";
  return `
    <div class="row-between"><h1>Findings</h1></div>
    <div class="card"><h2>Evidence the corpus carries</h2>
      <p class="muted">Corpus findings are previewed from exported claims across ${objs.length} concepts (${total} claims). Session findings are mechanical drafts awaiting adjudication — none are corpus knowledge until admitted through the authoring pipeline.</p>
    </div>
    ${sessionSection}
    ${corpusSections || `<p class="muted">No claims exported.</p>`}`;
}

function certClass(v) {
  const n = String(v || "").toLowerCase();
  return n === "high" ? "valid" : n === "medium" ? "warn" : n === "low" ? "bad" : "";
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

/* ---------- Publish ---------- */

function viewPublish() {
  const c = state.config;
  const contractUrl = c.contract_url || "#";
  const drafts = state.sessions.flatMap((s) => (s.findings || []).length ? [{ id: s.id, topic: s.topic, n: s.findings.length }] : []);
  const targets = [
    ["Blog post", "one finding → one narrative, technical"],
    ["Comparison", "side-by-side across two or more findings"],
    ["Whitepaper", "evidence-backed argument, multiple findings"],
    ["Documentation", "reference material from validated concepts"],
    ["Tutorial", "step-by-step from verified recommendations"],
    ["FAQ", "extracts of the same findings"],
    ["Release notes", "validated changes to the corpus"],
  ].map(([t, d]) => `<li><b>${esc(t)}</b> <span class="muted">— ${esc(d)}</span></li>`).join("");
  const sessionRows = drafts.length ? drafts.map((d) => `<li><a href="#/research/session/${encodeURIComponent(d.id)}">${esc(d.topic)}</a> — ${d.n} draft findings</li>`).join("") : `<li class="muted">No sessions with findings yet.</li>`;
  return `
    <div class="row-between"><h1>Publish</h1></div>
    <div class="card"><h2>Downstream, never intertwined</h2>
      <p class="muted">Publishing consumes validated findings from the export contract and renders them for an audience. It never researches; research never markets. Nothing here edits the corpus.</p>
      <ul class="pipeline">${targets}</ul>
      <p>Readers depend only on the contract: <a href="${esc(contractUrl)}" target="_blank" rel="noopener">${esc(c.contract_label || "knowledge-export-core-v1 (EXPORT_CONTRACT.md)")}</a>.</p>
    </div>
    <div class="card"><h2>Ready to work from</h2><ul>${sessionRows}</ul></div>`;
}

/* ---------- Corpus quality ---------- */

function viewValidation() {
  const invalid = state.index.invalid;
  const s = state.index.summary;
  const tally = {};
  for (const o of invalid) for (const e of o.errors) tally[e] = (tally[e] || 0) + 1;
  const top = Object.entries(tally).sort((a, b) => b[1] - a[1]).slice(0, 3);
  const pct = s.total ? Math.round((s.valid / s.total) * 100) : 0;
  const topIssue = top[0];
  const pctBad = invalid.length ? Math.round((invalid.length / s.total) * 100) : 0;
  const fix = topIssue ? {
    "No atomic evidence blocks found. Must have at least one.": "Add at least one atomic evidence block (claims, observations, relationships) to each affected file before the next release.",
  }[topIssue[0]] : "";
  const recommended = fix ? `<li><b>Recommended fix</b> — ${esc(fix)} <span class="muted">(${topIssue[1]}×)</span></li>` : "";
  return `
    <div class="row-between"><h1>Corpus Quality</h1></div>
    <div class="card"><h2>${s.invalid ? `${s.invalid} of ${s.total} documents (${pctBad}%) need attention` : "All documents pass validation"}</h2>
      <p class="muted">${topIssue ? `Most common issue: ${esc(topIssue[0])} (${topIssue[1]}×).` : "No outstanding issues."}</p>
      ${recommended ? `<ul class="pipeline">${recommended}</ul>` : ""}
    </div>
    <div class="grid">
      <div class="stat"><div class="num ok">${s.valid}</div><div class="label">Healthy documents (${pct}%)</div></div>
      <div class="stat"><div class="num warn">${s.invalid}</div><div class="label">Need attention</div></div>
      <div class="stat"><div class="num bad">${s.error_count}</div><div class="label">Validation issues</div></div>
    </div>
    <div class="card"><h2>Open quality tasks (metadata only — no content exported)</h2>
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
  const deep = $("#deep-research");
  if (deep) deep.addEventListener("click", () => location.hash = "#/research/new?depth=deep");
  const quick = $("#quick-research");
  if (quick) quick.addEventListener("click", () => location.hash = "#/research/new?depth=quick");
  const cont = $("#continue-research");
  if (cont) cont.addEventListener("click", () => location.hash = "#/research");
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
  document.querySelectorAll(".tab").forEach((t) =>
    t.addEventListener("click", () => navigate("#/library/" + t.dataset.tab))
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
"""Adjudicate a research session: record the review pass over draft findings.

Sessions are immutable once released; adjudication is a separate REVIEW LAYER
(adjudication.json) written next to session.json. It never mutates the
mechanical record. Like the release layer, it refuses to overwrite.

Usage:
    python tools/hpf-research/adjudicate.py <session-dir> <decisions.json>

decisions.json:
    {
      "adjudicator": "cycle-reviewer",
      "findings": [
        {"id": "f-1", "decision": "reject", "note": "restatement, not a claim"},
        {"id": "f-4", "decision": "revise",
         "revised_claim": "...", "note": "..."},
        {"id": "f-22", "decision": "add",
         "claim": "...", "status": "needs_adjudication",
         "method": "adjudication-synthesis-v0",
         "sources": ["https://..."], "note": "synthesized contradiction"}
      ]
    }

Decisions: approve | revise (revised_claim required) | reject | add.
Nothing graduates automatically: added findings stay drafts with
confidence null, exactly like mechanically drafted ones.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

DECISIONS = {"approve", "revise", "reject", "add"}


def main():
    ap = argparse.ArgumentParser(description="HPF session adjudication layer")
    ap.add_argument("session_dir")
    ap.add_argument("decisions")
    args = ap.parse_args()

    sdir = Path(args.session_dir)
    sf = sdir / "session.json"
    if not sf.exists():
        print(f"! session not found: {sdir}")
        return 2
    session = json.loads(sf.read_text(encoding="utf-8"))
    existing = sdir / "adjudication.json"
    if existing.exists():
        print(f"! refused: {existing.name} already exists (review layer is immutable)")
        return 3

    decisions = json.loads(Path(args.decisions).read_text(encoding="utf-8"))
    findings_by_id = {f["id"]: f for f in session.get("findings", [])}
    review = []
    for d in decisions.get("findings", []):
        fid = d.get("id")
        dec = d.get("decision")
        if dec not in DECISIONS:
            print(f"! invalid decision '{dec}' for {fid}")
            return 4
        if fid not in findings_by_id and dec != "add":
            print(f"! decision references unknown finding {fid}")
            return 4
        if dec == "revise" and not (d.get("revised_claim") or "").strip():
            print(f"! revise for {fid} requires revised_claim")
            return 4
        if dec == "add" and not (d.get("claim") or "").strip():
            print(f"! add requires claim")
            return 4
        entry = {"id": fid, "decision": dec, "note": d.get("note", "")}
        if dec == "revise":
            entry["revised_claim"] = d["revised_claim"].strip()
        if dec == "add":
            entry["claim"] = d["claim"].strip()
            entry["status"] = d.get("status", "needs_adjudication")
            entry["method"] = d.get("method", "adjudication-v0")
            entry["sources"] = d.get("sources", [])
            entry["confidence"] = None
        review.append(entry)

    counts = {"approve": 0, "revise": 0, "reject": 0, "add": 0}
    for e in review:
        counts[e["decision"]] += 1

    adjudication = {
        "schema": "hpf-adjudication-v0",
        "session_id": session["id"],
        "provenance": session.get("provenance", {"events": []}),
        "adjudicated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "adjudicator": decisions.get("adjudicator", "cycle-reviewer"),
        "summary": counts,
        "findings": review,
    }
    existing.write_text(json.dumps(adjudication, indent=2), encoding="utf-8")
    print(f"Adjudicated {session['id']}: {counts}")
    print(f"  {existing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

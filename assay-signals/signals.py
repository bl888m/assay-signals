"""assay-signals: reshape an `assay --json` run into a CSV and a digest.

Reads JSON on stdin (either the `scan --json` list of rows, or the
`paper --json` snapshot object) and writes signals.csv plus a short digest
to the screen. No dependencies, no network, no orders.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import sys


def load_rows(payload):
    """Accept both shapes: scan's list, or paper's snapshot dict."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and "markets" in payload:
        return payload["markets"]
    raise SystemExit("unrecognised input: pipe `assay scan --json` in")


def write_csv(rows, path="signals.csv"):
    cols = ["question", "category", "price", "estimate",
            "edge", "side", "verdict", "stake", "reason"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return path


def digest(rows):
    fired = [r for r in rows if r.get("verdict") == "FIRE"]
    passed = [r for r in rows if r.get("verdict") != "FIRE"]
    fired.sort(key=lambda r: abs(r.get("edge", 0)), reverse=True)

    line = "-" * 60
    print("assay-signals , " + dt.date.today().isoformat())
    print(line)
    print(f"{len(rows)} markets scored , {len(fired)} fired , {len(passed)} passed\n")

    print("TOP EDGES (fired)")
    if fired:
        for r in fired[:5]:
            print("  {:>+5.1%}  {:<3}  ${:<6,.0f} {}".format(
                r.get("edge", 0), r.get("side", ""),
                r.get("stake", 0), r.get("question", "")[:46]))
    else:
        print("  nothing cleared risk this run")

    # tally the reasons risk held trades back
    reasons = {}
    for r in passed:
        why = (r.get("reason") or "").split()
        key = why[0] if why else "other"
        reasons[key] = reasons.get(key, 0) + 1
    if reasons:
        tally = "  ·  ".join(f"{k} {v}" for k, v in sorted(reasons.items()))
        print("\nheld back by risk\n  " + tally)
    print(line)


def main():
    raw = sys.stdin.read().strip()
    if not raw:
        raise SystemExit("no input. try: assay scan --json | python signals.py")
    rows = load_rows(json.loads(raw))
    digest(rows)
    path = write_csv(rows)
    print("csv written , " + path)


if __name__ == "__main__":
    main()

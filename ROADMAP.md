# Roadmap

Where assay-signals goes next. It stays a thin, read-only reshape of the
desk's output, never a model of its own.

## Shipped

- Read assay scan --json or assay paper --json from stdin.
- Write a flat signals.csv, one row per market.
- Print a daily digest: top edges that fired, and a tally of why the rest
  were held back by risk.

## Next

- A --top N flag to trim the digest to the strongest N edges.
- Group the digest by category, so you can see where the edge concentrates.
- An optional Markdown export of the digest, for pasting into a thread.

## Later

- A tiny static HTML report, same numbers, sortable in the browser.
- A rolling file of past digests, so you can watch the desk over days.
- A calibration column once assay tracks how its estimates resolved.

## Non-goals

- No model, no estimate of its own. If a number is not already in the desk's
  output, assay-signals does not invent it.
- No orders, ever. It reshapes numbers; it never places anything.

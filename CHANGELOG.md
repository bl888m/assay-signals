# Changelog

## v0.1.1
- Added USAGE.md with run examples and a column reference.
- Added ROADMAP.md.

## v0.1.0
- Read assay scan --json or assay paper --json from stdin.
- Write signals.csv, one row per market.
- Print a daily digest: top edges that fired, and a tally of why the rest
  were held back by risk.
- Zero dependencies, read-only, no orders.

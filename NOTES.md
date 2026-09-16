# Notes

A working log for assay-signals.

## Why it stays thin

The value of this tool is that it does nothing clever. It reshapes numbers the
desk already printed into a CSV and a digest. The moment it starts estimating
anything on its own, it stops being auditable and starts being a second model
to trust. So it will not do that.

## Decisions

- Read from stdin, not from a hardcoded path. A pipe composes; a path does not.
- Accept both input shapes (scan list and paper snapshot) so the same command
  works whichever way the desk was run.
- Tally the PASS reasons in the digest. Knowing why the desk refused is often
  more useful than the fires themselves.

## Open ideas

- --top N to trim the digest.
- Group edges by category to see where the mispricing concentrates.
- A rolling archive of past digests, to watch the desk over days.

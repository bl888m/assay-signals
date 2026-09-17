# FAQ

**What is this?**
A thin companion to assay. It reads the desk's --json output and reshapes it
into a CSV and a short daily digest. That is all it does.

**Does it decide anything on its own?**
No. It has no model and no estimate. Every number in the output was already
printed by assay; this just re-sorts and files it.

**Does it place trades?**
No. It reshapes numbers. There is no wallet, no key, no order anywhere in it.

**What input does it take?**
Either shape of assay's JSON: the list from scan --json, or the snapshot
object from paper --json. It detects which automatically.

**What comes out?**
signals.csv, one row per market, plus a digest printed to the screen: the
top edges that fired and a tally of why the rest were held back.

**Do I need assay installed?**
Yes, this reads assay's output. See github.com/bl888m/assay.

**Why keep it separate from assay?**
So the desk stays the desk, and the reshaping lives on its own. Easier to
read, easier to trust, easier to fork and change for your own markets.

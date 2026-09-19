# History

Why assay-signals exists, short version.

The desk (assay) prints its decisions as cards and, with --json, as raw data.
The cards are good for reading; the data is good for everything else. What was
missing was the small step in between: take the JSON, drop it into a spreadsheet
you can sort, and get a one-screen digest of the strongest edges.

That step kept getting rewritten by hand after every run. So it became a tool.

The rule from day one: assay-signals reshapes numbers, it never invents them.
No model, no estimate, no orders. If a figure is not already in the desk's
output, this tool does not produce it. That constraint is the whole point, it
keeps the reshaping honest and auditable, and it keeps the desk the single
place where any real thinking happens.

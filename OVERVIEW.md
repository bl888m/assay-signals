# Overview

assay-signals is the last mile after the desk has done its thinking.

assay scores prediction markets and prints its decisions. With --json it prints
them as data. assay-signals takes that data and does two boring, useful things:
writes a flat CSV you can sort in a spreadsheet, and prints a one-screen digest
of the strongest edges that cleared risk.

That is the entire scope. No model, no estimate, no orders. It reshapes numbers
the desk already produced, so the desk stays the single place any real thinking
happens, and this stays easy to read, easy to trust, and easy to fork.

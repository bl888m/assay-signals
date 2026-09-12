# assay-signals

`turn an assay --json run into a CSV and a one-screen daily digest`

A tiny companion to [assay](https://github.com/bl888m/assay), the six-agent
desk for prediction markets. assay scores markets and prints JSON;
assay-signals reads that JSON and lays it out two ways: a flat CSV you can
open in a spreadsheet, and a short digest of the strongest edges the desk
would fire on.

Zero dependencies. It reads JSON on stdin and writes files, nothing else. It
never places an order, because assay never does either. Paper by default,
research not advice.

## Use it

```bash
# pipe a live scan straight in
python -m assay scan --json | python signals.py

# or from a saved run
python -m assay paper --json --n 120 > run.json
python signals.py < run.json
```

Outputs:
- `signals.csv` , one row per market: question, category, price, estimate,
  edge, side, verdict, stake.
- a digest printed to the screen , the top edges that cleared risk.

## What a digest looks like

```
assay-signals , 2026-09-12
------------------------------------------------------------
12 markets scored , 3 fired , 9 passed

TOP EDGES (fired)
  +5.5%  YES  $500   Will Umbra IPO in 2026?
  +4.4%  YES  $500   Government shutdown before Aug?
  +3.1%  NO   $420   Will a named storm hit Juno in Jun?

held back by risk
  liquidity  4   ·  edge floor  3   ·  time  2
------------------------------------------------------------
csv written , signals.csv
```

## Why it exists

The desk is easier to trust when its output is boring data you can re-sort
yourself. This is that: no model, no magic, just a reshape of numbers assay
already printed. Read the desk itself at
[github.com/bl888m/assay](https://github.com/bl888m/assay).

MIT. `@bl888m_eth`

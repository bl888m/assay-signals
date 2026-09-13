# Usage

Every way to feed assay-signals, and what each column means.

## Pipe a live scan

```bash
python -m assay scan --json | python signals.py
```

## From a saved run

```bash
python -m assay paper --json --n 120 > run.json
python signals.py < run.json
```

## Only the fires, wider universe

```bash
python -m assay scan --json --n 200 | python signals.py
```

signals.py accepts both shapes automatically: the `scan --json` list of rows
and the `paper --json` snapshot object.

## The CSV columns

| column     | meaning                                                        |
| ---------- | -------------------------------------------------------------- |
| question   | the market                                                     |
| category   | Politics, Crypto, Sports, Econ, Tech, Weather, Culture         |
| price      | the crowd's implied probability of YES                         |
| estimate   | assay's probability after recalibration and momentum          |
| edge       | estimate minus price, on the chosen side                       |
| side       | YES or NO                                                      |
| verdict    | FIRE (cleared risk) or PASS                                    |
| stake      | hypothetical paper stake in USD                               |
| reason     | for a PASS, the single rule that stopped it                    |

## Notes

- Nothing here places an order. It reshapes numbers the desk already printed.
- Sort the CSV by `edge` to see the strongest signals, or filter `verdict`
  to `FIRE` for only what cleared risk.
- The digest tallies why trades were held back, so you can see whether the
  desk is refusing on liquidity, edge, or time.

Read the desk itself at [github.com/bl888m/assay](https://github.com/bl888m/assay).

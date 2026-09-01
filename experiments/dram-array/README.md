# DRAM array: pins and open rows

## Historical question

Why did DRAM reuse package address pins for a row and then a column, and why can nearby accesses behave differently from accesses that repeatedly change rows?

## Run

```bash
python experiments/dram-array/dram_array.py
```

## Model

The script constructs a synthetic 256 × 256 one-bank array. It compares the number of package address pins needed to present a flat address at once with the number needed when the same pins carry row and column fields at different moments. It then charges invented costs for `ACTIVATE`, column access, and `PRECHARGE` while running three deterministic traces.

## What it demonstrates

- row/column multiplexing can trade extra protocol phases for fewer address pins;
- once a row has been sensed into row-buffer circuitry, accesses within it can reuse that work;
- changing rows repeatedly can cost more even when the number of requested words is identical.

## What it cannot establish

This is not an electrical model, controller simulator, benchmark, or timing table for any historical or modern DRAM. Real devices vary by generation, organization, bank count, page policy, burst protocol, refresh schedule, and controller. The costs are deliberately synthetic. The experiment exposes tradeoff structure; it does not prove why any particular vendor selected a design.

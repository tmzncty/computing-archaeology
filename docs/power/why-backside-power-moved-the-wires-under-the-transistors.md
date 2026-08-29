# Why Backside Power Moved the Wires Under the Transistors

Power delivery used to share the frontside metal stack with signals. As wiring shrank, that sharing became expensive.

## Historical record

Imec describes traditional frontside power as traversing many BEOL layers while competing with signal routing. Its backside-power work separates the power-delivery network from signal wiring using backside metal, buried power rails, extreme wafer thinning, and nano-TSVs.[^imec]

## Engineering reconstruction

At low voltage, a small resistance creates a meaningful IR drop. Narrow frontside rails also consume routing resources that could carry signals.

Backside power changes the geometry:

```text
package power
  -> backside metal
  -> short vertical connection
  -> local rails / transistor

frontside metal
  -> mostly signal routing
```

This can reduce path resistance and routing congestion, but requires wafer thinning, alignment, backside processing, and new design/test flows.

## Speed connection

A transistor cannot switch quickly if its local supply collapses during current transients. Power integrity therefore becomes timing infrastructure.

## Experiment

`experiments/backside-power-ir/backside_power_ir.py` compares synthetic frontside and backside resistance/IR-drop budgets.

[^imec]: Imec, “How to power chips from the backside,” https://www.imec-int.com/en/articles/how-power-chips-backside

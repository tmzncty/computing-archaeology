# Why Gate-All-Around Nanosheets Went Further Than FinFET

FinFET improved gate control by wrapping the gate around multiple sides of a vertical fin. Gate-all-around (GAA) nanosheets push the same logic further: surround the channel more completely.

## Historical record

IBM Research's 2017 VLSI Technology paper demonstrated horizontally stacked gate-all-around nanosheets as a candidate to replace FinFET at the 5 nm node and beyond. The paper emphasized electrostatic control, effective width per active footprint, stacked sheets, work-function integration, and manufacturability problems such as sheet stiction.[^ibm]

## Engineering reconstruction

A nanosheet device is not simply a 'smaller FinFET.' It changes which dimensions designers and process engineers can trade.

```text
FinFET
  vertical fin
  gate around sides/top

GAA nanosheet
  ===== sheet =====
  gate surrounds sheet
  ===== sheet =====
  gate surrounds sheet
  ===== sheet =====
```

Stacking creates effective channel width vertically. Sheet width can become a design variable, while sheet thickness, spacing, release, inner-spacer formation, gate fill, and contact access become manufacturing constraints.

The transistor becomes a released-and-refilled three-dimensional cavity structure.

## New failure modes

Better electrostatics do not eliminate manufacturing difficulty. They relocate it:

- sacrificial layers must be removed without destroying channels;
- nanosheets must not collapse or stick;
- gate dielectric and metal must coat hidden surfaces;
- inner spacers must control source/drain proximity;
- contact resistance competes with smaller geometry;
- variability across multiple sheets can accumulate.

## Experiment

[`experiments/nanosheet-width/nanosheet_width.py`](../../experiments/nanosheet-width/nanosheet_width.py) compares a synthetic fixed-fin width model with stacked sheets whose width can vary. It exposes geometry flexibility versus stack/process burden; it does not model a real node.

## Source caution

IBM's paper is a research demonstration, not proof that every later commercial GAA implementation shares the same stack, dimensions, or process sequence.

[^ibm]: N. Loubet et al., “Stacked nanosheet gate-all-around transistor to enable scaling beyond FinFET,” VLSI Technology 2017, IBM Research, https://research.ibm.com/publications/stacked-nanosheet-gate-all-around-transistor-to-enable-scaling-beyond-finfet

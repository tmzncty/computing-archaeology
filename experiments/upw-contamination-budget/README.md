# UPW contamination budget

Run:

```bash
python experiments/upw-contamination-budget/upw_contamination_budget.py
```

This deliberately simple model treats five contamination classes independently:

- ions;
- particles;
- organics;
- metals;
- microbial contamination.

The point is to show why a water stream can look excellent on one purity metric and still fail another process requirement.

## Historical status

The contaminant values and pass/fail threshold are **synthetic normalized numbers**.

They are not a SEMI specification and do not represent a historical fab.

Historical grounding belongs in [`../../docs/facilities/why-ultrapure-water-became-a-process-material.md`](../../docs/facilities/why-ultrapure-water-became-a-process-material.md).

## What it can show

It can show the structure of a multi-dimensional purity requirement.

It cannot determine what limits a real process needs, what contaminants dominate a particular technology node, or how a real UPW plant should be designed.
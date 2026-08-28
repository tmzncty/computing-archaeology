# Fab traceability

A tiny event-log model showing why lot/tool/process history is valuable when an excursion is discovered after material has already moved on.

Run:

```bash
python experiments/fab-traceability/fab_traceability.py
```

The example reconstructs a possible exposure set from recorded lot/tool events.

It is **not** a MES, SECS/GEM, GEM300, AMHS, or semiconductor traceability implementation. It omits wafer-level identity, rework, recipes, reticles, equipment chambers, genealogy, timing, split/merge lots, and real factory state machines.

Its only purpose is to expose one idea: without persistent identity and event history, containment after an excursion becomes guesswork.
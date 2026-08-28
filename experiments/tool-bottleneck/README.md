# Fab Tool Bottleneck Experiment

Question:

> Why can one specialized process tool limit the throughput of an otherwise fast production line?

This model treats a fab flow as a sequence of stations with synthetic capacities and reports the bottleneck.

Run:

```bash
python experiments/tool-bottleneck/tool_bottleneck.py
```

The station names are generic and capacities are invented. This is not a model of a specific fab.
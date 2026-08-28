# Package Pin-Budget Experiment

Historical question:

> How can the number of package pins force system architecture to multiplex or serialize signals?

The model starts with address, data, power, and control requirements, then compares several package pin budgets. If the full interface does not fit, it shows simple conceptual strategies such as address/data multiplexing.

This is not a model of one historical CPU package. It exposes the physical I/O budget that connects die architecture to PCB architecture.

## Run

```bash
python experiments/package-pin-budget/package_pin_budget.py
```

# Assembly Defects Experiment

Historical question:

> Why can replacing individually wired/soldered connections with a repeatable board-and-batch-solder process dramatically change production economics?

This toy model compares two abstract assembly styles:

1. many individually made connections with a per-connection defect probability;
2. a more repeatable printed-board process with a lower per-joint defect probability but a small chance of a board-wide process defect.

The probabilities are synthetic. The model does not describe one factory, solder process, or era. Its purpose is to show how repeatability and shared process failures create different reliability structures.

## Run

```bash
python experiments/assembly-defects/assembly_defects.py
```

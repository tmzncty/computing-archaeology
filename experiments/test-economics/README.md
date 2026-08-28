# Automatic Test Economics

This toy model asks why more test coverage is not free.

Run:

```bash
python experiments/test-economics/test_economics.py
```

It compares synthetic test times with resulting units/hour and invented defect-detection fractions.

It does **not** model a historical Fairchild, TI, Signetics, or Teradyne tester. It does not estimate real fault coverage or tester cost.

Its purpose is to expose the constraint in [`../../docs/manufacturing/why-automatic-test-became-an-industry.md`](../../docs/manufacturing/why-automatic-test-became-an-industry.md): every extra second of test is multiplied by production volume, so coverage, throughput, and outgoing quality must be engineered together.
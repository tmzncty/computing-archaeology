# Lithography Throughput

This toy model isolates one production constraint of step-and-repeat lithography:

> higher field count and longer exposure time consume tool time.

Run:

```bash
python experiments/lithography-throughput/lithography_throughput.py
```

All numbers are synthetic. The model ignores alignment, focus, reticle changes, resist processing, maintenance, tool availability, field stitching, optical limits, and historical machine specifications.

It exists only to accompany [`../../docs/semiconductor/why-lithography-became-a-capital-equipment-race.md`](../../docs/semiconductor/why-lithography-became-a-capital-equipment-race.md) and show why lithography progress has to balance resolution with throughput.
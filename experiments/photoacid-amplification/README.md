# Photoacid Amplification

This synthetic model treats exposure events as generating catalytic gain, then adds a diffusion/blur penalty that rises with amplification.

Run:

```bash
python experiments/photoacid-amplification/photoacid_amplification.py
```

It is not a chemically calibrated resist model. The narrow lesson is that amplification can improve effective sensitivity while simultaneously creating a spatial-fidelity problem.
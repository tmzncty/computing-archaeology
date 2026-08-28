# Implant Dose

Conceptual question:

> What changes when a dopant target can be expressed as an implant dose plus an activation fraction?

Run:

```bash
python experiments/implant-dose/implant_dose.py
```

The model multiplies a synthetic implant dose by a synthetic activation fraction. It does **not** model implant depth, channeling, straggle, species chemistry, oxide stopping power, crystal damage, or a historical implanter.

Its only purpose is to expose the manufacturing abstraction described in [`../../docs/semiconductor/why-ion-implantation-made-doping-programmable.md`](../../docs/semiconductor/why-ion-implantation-made-doping-programmable.md): a desired electrical population becomes something process equipment can approach through measurable recipe variables.
# PCB material stack

This synthetic experiment compares thermal expansion of several deliberately simplified board/package material categories over the same length and temperature excursion.

Run:

```bash
python experiments/pcb-material-stack/pcb_material_stack.py
```

All values are illustrative. This is **not** a real FR-4, copper, resin, solder, via-reliability, laminate-selection, or thermal-design model.

The lesson is simply that a PCB is a stack of materials with different thermal responses; repeated heating and cooling therefore creates mechanical interactions that a schematic cannot show.

Historical context: [`../../docs/pcb/why-a-pcb-is-a-materials-stack.md`](../../docs/pcb/why-a-pcb-is-a-materials-stack.md).
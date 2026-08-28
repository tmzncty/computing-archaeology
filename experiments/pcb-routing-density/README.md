# PCB Routing-Density Experiment

Historical question:

> Why do extra routing layers and vias make denser systems possible even though they make board fabrication harder?

The model generates synthetic point-to-point connections on a grid and estimates how many same-layer crossings occur when all routes are forced onto one layer versus split across multiple layers.

It is not a PCB autorouter and does not model real design rules, impedance, via cost, or placement. It simply makes the graph-versus-plane problem visible.

## Run

```bash
python experiments/pcb-routing-density/pcb_routing_density.py
```

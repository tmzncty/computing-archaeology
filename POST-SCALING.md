# Post-Scaling Computing Archaeology

This track asks what happened after simple planar shrinking stopped being enough.

The answer was not one replacement technology. Computing continued scaling by changing transistor geometry, lithography, memory placement, package topology, serial-link signaling, power distribution, and cooling at the same time.

## Completed first-pass topics

- [x] FinFET: gate control moves from one surface to multiple sides.
- [x] Gate-all-around nanosheets: the gate wraps the channel more completely and width becomes a design variable.
- [x] EUV: lithography becomes a vacuum-and-mirror machine at 13.5 nm.
- [x] High-NA EUV: numerical aperture rises from 0.33 to 0.55 and field/optics/stage constraints change again.
- [x] HBM/TSV: memory is vertically stacked and moved physically close to the processor.
- [x] Silicon interposers / CoWoS: package wiring becomes system-scale infrastructure.
- [x] Hybrid bonding / SoIC-style integration: the boundary between wafer process and package assembly blurs.
- [x] UCIe: chiplet integration begins acquiring a package-level open interoperability boundary.
- [x] PCIe 6 PAM4/FEC/FLIT: higher bandwidth accepts a noisier raw channel and repairs it with coding/protocol machinery.
- [x] Retimers: a passive PCB trace becomes an actively regenerated digital channel.
- [x] 48 V busbars / high-current rack power: power delivery becomes a geometry and connector problem.
- [x] Cold plates / manifolds / quick disconnects: plumbing enters the server as an ordinary computing interface.

## Dependency chain

```text
planar MOSFET scaling pressure
  -> FinFET
  -> GAA nanosheet

shorter wavelength / harder patterning
  -> EUV vacuum mirrors
  -> High-NA EUV

memory bandwidth pressure
  -> TSV-stacked HBM
  -> interposer / package-scale wiring

reticle and yield pressure
  -> chiplets
  -> hybrid bonding
  -> package-level standards

channel loss pressure
  -> PAM4 + FEC
  -> retimers

compute power density
  -> 48 V busbar / high-current connectors
  -> cold plates / manifolds / quick disconnects
```

## Runnable experiments

- `experiments/finfet-gate-control/finfet_gate_control.py`
- `experiments/nanosheet-width/nanosheet_width.py`
- `experiments/euv-reflection-chain/euv_reflection_chain.py`
- `experiments/highna-field/highna_field.py`
- `experiments/hbm-bandwidth-density/hbm_bandwidth_density.py`
- `experiments/interposer-reach/interposer_reach.py`
- `experiments/hybrid-bond-pitch/hybrid_bond_pitch.py`
- `experiments/chiplet-partition/chiplet_partition.py`
- `experiments/pam4-margin/pam4_margin.py`
- `experiments/retimer-budget/retimer_budget.py`
- `experiments/rack-power/rack_power.py`
- `experiments/coldplate-loop/coldplate_loop.py`

All experiment numbers are synthetic unless explicitly tied to a historical source. They expose constraint structure; they are not process recipes, link-compliance tools, power designs, or cooling-sizing calculators.

## Source map

See [`docs/references/post-scaling-field-set.md`](docs/references/post-scaling-field-set.md).

## Acknowledgements

See [`docs/manufacturing/ACKNOWLEDGEMENTS-POST-SCALING.md`](docs/manufacturing/ACKNOWLEDGEMENTS-POST-SCALING.md).

## What this changes about the story

The usual story says Moore's-law scaling slowed and the industry moved to 'advanced packaging.' That phrase hides too much.

The post-scaling system is a coordinated stack of new interfaces:

```text
channel geometry
mask / EUV optical system
stacked memory
package wiring
bond pitch
chiplet protocol
serial error correction
retimer placement
busbar current
coolant loop
```

A modern accelerator is therefore not merely a bigger chip. It is a machine whose useful computation depends on the coordinated behavior of many manufacturing layers outside the transistor itself.

> **When one dimension stopped scaling cleanly, computing continued by turning previously external infrastructure into architecture.**

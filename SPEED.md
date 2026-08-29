# Speed Infrastructure Archaeology

This track asks a simple question: what did the industry have to turn into architecture in order to keep making computation faster?

The answer is broader than clocks. Speed pressure migrated into lithography stochastic yield, power delivery, transistor packing, stacked memory, bonding/test, optics, electrical channels, rack voltage, coolant chemistry, and even in-network collective computation.

## Completed first-pass topics

- [x] EUV stochastic defectivity and pellicle throughput tax.
- [x] Backside power delivery and frontside routing relief.
- [x] Forksheet / CFET as density mechanisms beyond ordinary GAA.
- [x] HBM4-class wider memory interfaces and base-die complexity.
- [x] Hybrid-bond known-good-die / inspection economics.
- [x] Co-packaged optics and external laser infrastructure.
- [x] 224G -> 448G electrical-channel scaling.
- [x] 800 VDC / megawatt-class rack power distribution.
- [x] CDU / coolant chemistry as a fleet reliability interface.
- [x] In-network collective offload for AI scale-up/scale-out.

## Dependency chain

```text
lower EUV dose
  -> more throughput
  -> more stochastic risk

narrower wiring
  -> worse IR drop / congestion
  -> backside power

smaller cells
  -> GAA
  -> forksheet / CFET

more accelerator FLOPS
  -> more memory bandwidth
  -> HBM4 / wider base die

finer die-to-die pitch
  -> hybrid bonding
  -> KGD / inspection pressure

faster switch ASICs
  -> shorter electrical reach
  -> co-packaged optics

faster electrical SerDes
  -> 224G / 448G channel engineering

higher rack power
  -> 48 V
  -> 800 VDC
  -> lower distribution current

higher heat flux
  -> cold plates
  -> CDU / coolant chemistry

larger GPU collectives
  -> network movement dominates
  -> in-network reduction / SHARP
```

## Runnable experiments

- `experiments/euv-stochastic-window/euv_stochastic_window.py`
- `experiments/backside-power-ir/backside_power_ir.py`
- `experiments/cfet-density/cfet_density.py`
- `experiments/hbm4-interface/hbm4_interface.py`
- `experiments/hybrid-bond-kgd/hybrid_bond_kgd.py`
- `experiments/cpo-reach/cpo_reach.py`
- `experiments/cei-rate-budget/cei_rate_budget.py`
- `experiments/hvdc-rack-current/hvdc_rack_current.py`
- `experiments/coolant-chemistry-window/coolant_chemistry_window.py`
- `experiments/collective-offload/collective_offload.py`

All numerical assumptions in these scripts are synthetic unless explicitly identified otherwise. They are constraint demonstrations, not process recipes, compliance tools, power-system designs, or cooling specifications.

## Sources and labor

See [`docs/references/speed-infrastructure-field-set.md`](docs/references/speed-infrastructure-field-set.md) and [`docs/manufacturing/ACKNOWLEDGEMENTS-SPEED-INFRASTRUCTURE.md`](docs/manufacturing/ACKNOWLEDGEMENTS-SPEED-INFRASTRUCTURE.md).

> **Every time computing got faster, some previously invisible delay became important enough to acquire its own materials, machines, standards, maintenance crews, and failure modes.**

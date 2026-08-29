# Why Hybrid Bonding Blurred Wafer and Package

Traditional package interconnects rely on bumps or solder structures that are enormous compared with on-die wiring. As chiplet and 3D integration pitch shrank, the gap between 'wafer fabrication' and 'packaging' became harder to maintain.

Hybrid bonding moves toward direct fine-pitch dielectric and copper-to-copper interfaces.

## Historical record

TSMC describes SoIC as a front-end 3D inter-chip stacking technology for reintegrating chiplets, with CoW and WoW schemes and sub-10-micrometer-class bond-pitch scaling in its current platform description.[^soic]

Intel has similarly described Foveros Direct as direct copper-to-copper bonding intended to move below conventional bump pitches.[^intel]

## Engineering reconstruction

```text
microbump stack:
 die -- bump -- solder/interface -- bump -- die

hybrid bond:
 die -- dielectric/Cu interface -- die
```

Reducing pitch increases connection density and can reduce interconnect energy and latency. But it makes surfaces much less forgiving.

Hybrid bonding depends on:

- planarization;
- surface cleanliness;
- particle control;
- copper recess/protrusion control;
- alignment;
- wafer/die warpage;
- known-good-die strategy;
- post-bond inspection and test.

A single particle that was irrelevant at coarse package pitch can become a local bonding catastrophe.

## Experiment

[`experiments/hybrid-bond-pitch/hybrid_bond_pitch.py`](../../experiments/hybrid-bond-pitch/hybrid_bond_pitch.py) scales a synthetic interconnect-density benefit against particle/alignment sensitivity as pitch shrinks.

## Source caution

SoIC and Foveros Direct are vendor platforms, not generic synonyms for all hybrid-bonding processes.

[^soic]: TSMC, “The Whats, Whys, and Hows of TSMC-SoIC,” https://www.tsmc.com/english/dedicatedFoundry/technology/SoIC_inDepth
[^intel]: Intel, “Intel Accelerates Process and Packaging Innovations,” https://www.intc.com/news-events/press-releases/detail/1486/intel-accelerates-process-and-packaging-innovations

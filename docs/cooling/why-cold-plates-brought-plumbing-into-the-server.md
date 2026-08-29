# Why Cold Plates Brought Plumbing Into the Server

Air cooling makes the server boundary feel electrically clean: power and data go in, hot air comes out.

Direct liquid cooling breaks that illusion. The compute node now contains wetted materials, cold plates, hoses, manifolds, quick disconnects, coolant chemistry, leak risk, pressure drop, flow monitoring, and service procedures.

## Historical record

The Open Compute Project cold-plate workstream defines rack-manifold cooling loops and explicitly includes coolant, CDU, manifold, quick-disconnect couplings, cold plates, wetted-material compatibility, safety, monitoring, and maintenance concerns.[^ocp]

OCP product examples now routinely combine high-TDP CPUs/GPUs, 48 V busbar rack power, and cold-plate liquid cooling.[^server]

## Engineering reconstruction

```text
chip
 -> TIM
 -> cold plate
 -> quick disconnect
 -> node hose
 -> rack manifold
 -> CDU
 -> facility water / heat rejection
```

This is a thermal network and a fluid network at the same time.

## New failure modes

Liquid cooling introduces computing-specific plumbing constraints:

- cold-plate thermal resistance;
- flow distribution among parallel nodes;
- pressure drop;
- pump/CDU capacity;
- corrosion and galvanic compatibility;
- particulate contamination;
- seal aging;
- dripless connector behavior;
- service spill control;
- leak detection;
- coolant quality over years.

The best quick disconnect is one a technician can operate repeatedly without turning maintenance into a fluid incident.

## Experiment

[`experiments/coldplate-loop/coldplate_loop.py`](../../experiments/coldplate-loop/coldplate_loop.py) models a synthetic parallel rack loop where flow imbalance raises local temperature while total rack flow can still look acceptable.

## Source caution

OCP documents open-system requirements and examples; proprietary datacenter implementations can differ substantially.

[^ocp]: Open Compute Project, Cold Plate workstream, https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate
[^server]: Open Compute Project, liquid-cooled ORv3 GPU server example, https://www.opencompute.org/products/723/pegatron-ms303-2a1g-2ou-2-node-orv3-ai-gpu-server

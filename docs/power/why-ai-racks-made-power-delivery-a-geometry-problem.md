# Why AI Racks Made Power Delivery a Geometry Problem

Once accelerators reached hundreds of watts each and racks accumulated many accelerators, power delivery stopped being an invisible cable problem.

Current, conductor cross-section, connector temperature, conversion stages, serviceability, and rack topology became computing architecture.

## Historical record

NVIDIA lists up to 700 W configurable TDP for H100 SXM modules.[^h100]

Open Compute Project ORv3 material uses 48 V DC busbar architectures, and OCP-published MGX rack material describes busbars supporting very high rack currents. OCP marketplace material also shows direct busbar contacts and liquid-cooling-ready rack designs.[^ocp-rack][^mgx]

## Engineering reconstruction

For a given power:

```text
current = power / voltage
resistive loss ~ current^2 * resistance
```

Raising distribution voltage reduces current for the same power, which can reduce conductor loss before local conversion near the load.

But high-power racks still confront:

- busbar cross-section;
- connector contact resistance;
- hot-swap protection;
- PSU/power-shelf redundancy;
- VRM proximity to GPU/CPU rails;
- transient load response;
- copper area and package power delivery;
- thermal interaction with power components.

## Why geometry matters

At high current, one milliohm is not 'almost zero.' Contact resistance multiplied by hundreds of amps becomes heat and voltage drop.

The physical shape of copper, clips, busbars, planes, vias, and connectors becomes part of the compute power envelope.

## Experiment

[`experiments/rack-power/rack_power.py`](../../experiments/rack-power/rack_power.py) compares synthetic 12 V and 48 V distribution for equal rack power, then adds connector-resistance heating. It is not a rack electrical design.

## Source caution

OCP contributions and marketplace examples represent open rack/platform practice, not every datacenter architecture.

[^h100]: NVIDIA, H100 GPU specifications, https://www.nvidia.com/en-us/data-center/h100/
[^ocp-rack]: Open Compute Project, ORv3 rack examples, https://www.opencompute.org/ai-marketplace/products/440/rittal-open-rack-v3-orv3
[^mgx]: Open Compute Project, MGX Accelerated Computing Rack specification, https://www.opencompute.org/documents/mgx-accelerated-computing-rack-and-trays-specification-1-1-pdf-1

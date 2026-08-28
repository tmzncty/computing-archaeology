# Why Probe and Burn-In Screened a Population

A finished wafer is not a collection of guaranteed chips.

It is a population of candidate devices that still has to be measured, classified, and screened.

Two practices made that fact operationally visible:

- **wafer probing** — contacting die before packaging;
- **burn-in** — deliberately stressing devices so some early failures happen in the factory rather than in the customer's system.

The historical question is:

> **How did semiconductor manufacturing learn to avoid spending package and system cost on bad die, while also filtering devices likely to fail early?**

## Probe before package

Packaging adds cost.

If a die is already electrically bad, attaching it to a lead frame or substrate, bonding it, encapsulating it, marking it, and testing it again wastes downstream capacity.

Automatic wafer probers therefore became an important manufacturing layer.

SEMI oral history from Peter Wolken describes Electroglas building an early automatic high-speed wafer prober in the late 1960s and competing internationally in wafer-prober equipment.[^wolken]

The prober is not itself the tester. It solves the mechanical contact and positioning problem:

```text
move wafer
-> align die
-> place probe needles/pins
-> make electrical contact
-> tester applies patterns/measurements
-> record result / bin
-> move to next die
```

This is a manufacturing robot whose output is information about the wafer.

## Probe cards are consumable interfaces

The electrical interface between tester and die sounds abstract until one remembers that microscopic pads must be touched repeatedly and reproducibly.

A probe interface has to negotiate:

- pad pitch;
- planarity;
- contact force;
- oxide or contamination on pads;
- current capacity;
- high-frequency behavior;
- needle wear;
- cleaning;
- alignment;
- damage limits.

As pad counts and frequencies rise, the probe interface becomes a specialized product rather than a bundle of wires.

### Reconstruction

This is another recurring history pattern:

> stable automation requires a replaceable physical interface.

Without repeatable contact mechanics, automatic test cannot scale simply by making the tester faster.

## Burn-in attacks infant mortality

Some semiconductor defects fail quickly under use rather than being perfectly dead at final test.

High-reliability programs therefore used burn-in: operate devices at elevated stress, often temperature and voltage, so susceptible parts fail during screening.

A 1972 NASA technical memorandum discusses qualification, power burn-in, testing, screening, and a 100-percent burn-in policy for the flight programs considered in that report.[^nasa-1972]

JPL guidance later describes burn-in explicitly as a way to identify devices that would otherwise fail during the infant-mortality period.[^jpl-burn]

The idea is conceptually simple:

```text
latent manufacturing weakness
+ accelerated stress
-> failure happens now
-> reject part before mission/customer use
```

But the engineering is not simple.

## Screening can also consume life

More stress is not automatically better.

NASA reliability work from the 1980s warned that conventional burn-in could become problematic for increasingly complex devices and could shorten the lifetime of otherwise good parts if applied badly.[^nasa-1987]

So burn-in creates an optimization problem:

> stress enough to expose weak devices, but not so much that screening becomes a new damage mechanism.

This is why burn-in belongs with reliability physics and process control, not superstition.

## Test economics changes product economics

Probe and burn-in both consume capital equipment and time.

A high-volume product may encounter costs from:

```text
probe seconds per die
x candidate die

burn-in hours
x sockets / boards / chambers

retest / handling
x screened population
```

Even when the silicon fabrication cost is fixed, test strategy can change cost per shipped good device.

This is why the manufacturing history of a processor includes testers, probe cards, handlers, burn-in boards, chambers, sockets, and test-program engineers.

## Experiment

[`../../experiments/screening-tradeoff/`](../../experiments/screening-tradeoff/) compares a synthetic population under no screening, moderate screening, and aggressive screening.

The model deliberately includes both removal of weak units and a configurable stress penalty on survivors.

It is not a reliability model for any real device family.

## What this teaches us

A chip is not born as a product the moment fabrication ends.

It becomes a product through measurement and classification.

> **Wafer probe saves downstream work by learning earlier; burn-in trades factory stress and time for a lower probability of early field failure.**

Both are examples of the semiconductor industry turning uncertainty about a population into controlled manufacturing decisions.

## References

[^wolken]: SEMI Oral History Interview, Peter Wolken, discussion of Electroglas and automatic wafer probers in the late 1960s, https://www.semi.org/en/Oral-History-Interview-Peter-Wolken
[^nasa-1972]: R. V. Allen, *Reliability of Hybrid Microcircuit Discrete Components*, NASA-TM-X-64686, 1972, https://ntrs.nasa.gov/citations/19730007481
[^jpl-burn]: NASA/JPL Parts Engineering, ASIC reliability guidance, “Infant Mortality” and “Burn-In,” https://parts.jpl.nasa.gov/asic/Sect.4.3.html
[^nasa-1987]: NASA reliability study discussing limits of conventional screening/burn-in as VLSI complexity increases, https://ntrs.nasa.gov/api/citations/19870017771/downloads/19870017771.pdf

## Source note

NASA/JPL sources emphasize aerospace and high-reliability screening and should not be generalized into universal commercial practice. Wolken's SEMI interview is participant oral history. Future deepening should add probe-card manufacturer records, tester/prober manuals, commercial production flows, and period cost data.
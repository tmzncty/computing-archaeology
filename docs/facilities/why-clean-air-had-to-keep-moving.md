# Why Clean Air Had to Keep Moving

The first intuitive cleanroom strategy was defensive:

- seal the room;
- clean it carefully;
- put workers in protective clothing;
- try not to introduce dust.

That approach fails for a simple reason:

> **a working room continuously generates contamination.**

People move. Machines move. Materials shed. Doors open. Air circulates. Particles do not politely remain where they were created.

The historical breakthrough was therefore not merely “filter the air better.” It was to make airflow itself into a manufacturing mechanism.

## Whitfield's problem was close-tolerance manufacturing

Sandia's historical account says Willis Whitfield was asked in 1959 to solve contamination problems affecting increasingly small precision components.[^sandia2012]

Existing cleanrooms relied on sealing, protective clothing, housekeeping, and conventional turbulent airflow. Particles could still remain suspended or recirculate through the work area.[^sandia2012]

Whitfield's solution was to continuously sweep the room with highly filtered air.

By the end of 1960 he had drawn an early design, and the prototype used a bank of filters rated at 99.97 percent removal for particles larger than 0.3 micrometers.[^sandia2012]

Sandia's period-derived figures report that the laminar-flow room achieved particle counts dramatically below conventional cleanrooms of the time.[^sandia2012]

The essential shift was conceptual:

> contamination control became a **flow problem**, not only a cleaning problem.

## A cleanroom is a particle-transport machine

The room is not clean because no particles are ever generated.

It is clean because the airflow is designed to remove them before they settle where they matter.

```text
particle source
-> controlled airflow
-> transport away from work
-> filtration
-> recirculation
```

Later vertical configurations used downward flow through the work area and a perforated/grated floor, allowing gravity and directional airflow to cooperate.[^sandia2012]

This makes the cleanroom part of the process tool.

The wafer is being manufactured not only by the aligner, furnace, etcher, or implant system in front of it, but also by the invisible air field surrounding those tools.

## The filter is not the entire cleanroom

A common simplification is:

> cleanroom = HEPA filter.

But filter efficiency does not determine what the wafer actually experiences by itself.

The result also depends on:

- airflow direction;
- airflow velocity;
- recirculation rate;
- pressure relationships between rooms;
- turbulence around equipment;
- leakage;
- personnel movement;
- gowning;
- particle-generating maintenance;
- where process exhaust removes air;
- how replacement air enters.

### Reconstruction

A perfect filter attached to badly designed airflow can still permit contamination to move from a dirty source toward a critical surface.

So cleanroom design becomes a spatial control problem:

```text
how clean is the air?
+
where is it going?
+
how long does contamination remain near the wafer?
```

## Purity became more than particles

As semiconductor processes became more sensitive, another class of contamination became important: substances too small or too chemically active to be described only as dust.

Modern clean-space engineering recognizes airborne molecular contamination such as:

- acids;
- bases;
- condensable organics;
- dopant-related species.

These can alter photoresist chemistry, corrosion, deposition, or surface condition without appearing as a visible particle.

This later development matters historically because it shows the same pattern seen in ultrapure water:

> one successful purity metric creates the conditions for the next, subtler contamination class to become visible.

Particle control did not end contamination history. It changed which contaminants became limiting.

## Temperature and humidity are part of “clean”

Clean air is not only low-particle air.

Temperature and humidity affect:

- resist behavior;
- dimensional stability;
- static charge;
- condensation;
- operator comfort and gowning;
- equipment repeatability.

ASHRAE's clean-space engineering guidance notes that semiconductor process requirements have historically driven temperature/humidity control, with temperature stability needed where dimensional expansion or contraction matters.[^ashrae]

This means the HVAC system has two simultaneous jobs:

1. move contamination away;
2. maintain a stable thermodynamic environment.

A fab therefore spends enormous energy moving and conditioning air not because workers like air conditioning, but because the process itself occupies the room.

## People became a controlled source term

A human body is incompatible with microscopic manufacturing in many ordinary ways:

- skin flakes;
- hair;
- fibers;
- breath;
- motion-driven turbulence;
- oils;
- chemical residues.

Gowns do not make people “clean.”

They reduce the rate at which people inject uncontrolled material into a controlled airflow system.

This is why cleanroom labor history matters.

The famous photographs of workers in suits can make the clothing look ceremonial or futuristic. In engineering terms, it is a source-control technology.

## Maintenance can be dirtier than production

Normal production often occurs inside closed, conditioned systems.

Maintenance opens those systems.

Filters are changed. Chambers are opened. Ducts are exposed. Pumps are serviced. Residues are disturbed.

So a facility can have excellent nominal cleanroom classification and still face acute contamination risk during interventions.

The cleanroom therefore depends on procedures, staging, cleaning, tool recovery, and qualification after maintenance.

Again, the abstraction “the room is Class X” hides operational labor.

## Experiment

See [`../../experiments/airflow-removal/`](../../experiments/airflow-removal/).

The model compares a room that only dilutes contamination slowly with one that continuously removes particles through a directed recirculation/filter loop.

It is not a CFD model and does not reproduce Whitfield's prototype.

## What this teaches us

The important historical shift is:

> **cleanliness stopped meaning “a room that had been cleaned” and became “a continuously controlled environmental state.”**

That is a profound manufacturing idea.

A semiconductor fab is never simply clean.

It is always **being kept clean**.

## References

[^sandia2012]: Sandia National Laboratories, “Willis Whitfield, inventor of modern-day laminar-flow clean room, passes away,” 2012, with historical material from Sandia archives and interviews, https://www.sandia.gov/labnews/2012/11/16/12-16-11-2/
[^ashrae]: ASHRAE Handbook, “Clean Spaces,” section on semiconductor fab conditions, https://handbook.ashrae.org/Handbooks/A23/SI/a23_ch19/a23_ch19_si.aspx

## Source note

Sandia is an institutional retrospective about its own laboratory and inventor; the article preserves useful period measurements and design history but should still be treated as retrospective institutional evidence. ASHRAE is later engineering guidance used to explain mature facility requirements, not to project modern tolerances onto 1960s fabs.
# Why Separable Contacts Need Plating, Force, and Wipe

A solder joint gets to become permanent.

A connector contact has a harder job: it must remain electrically good while being separable, repeatedly mated, vibrated, thermally cycled, contaminated, and stored for years.

That is why connector metallurgy became its own engineering world.

## Historical record

Electrical-contact researchers had long recognized **fretting corrosion**: tiny repeated relative motions at a contact interface can wear protective films, expose reactive base metal, create oxide debris, and increase contact resistance.

A 1981 study of gold-plated connector contacts showed that even gold systems could fail when wear penetrated the finish, while lubrication and plating structure influenced how long low resistance was maintained.[^antler81]

By 1985 the subject had become important enough for broad reviews. One historical driver was economic: rising gold cost encouraged substitution with less noble finishes, which made fretting problems more visible.[^antler85]

## Contact resistance is made at microscopic spots

Two apparently flat metal surfaces really touch at small asperities.

The electrical interface therefore depends on:

```text
normal force
+ real contact area
+ surface films
+ plating
+ roughness
+ wiping motion
+ contamination
```

A connector designer wants enough force and wiping action to break through films and maintain stable contact, but not so much that insertion force, wear, or mechanical damage becomes unacceptable.

## Gold is not magic

Gold is useful because it is chemically noble, but a practical contact is usually a stack:

```text
spring base alloy
-> nickel or other underplate
-> gold / palladium alloy / tin system
-> mating interface
```

Thickness and porosity matter. If motion wears through the noble finish, base-metal oxides can dominate the interface.

NASA's modern workmanship standard also warns specifically against mating gold-coated and tin-coated separable contacts because transferred tin can oxidize and produce fretting-related resistance growth.[^nasa]

The important point is not “always use gold.”

It is:

> **a connector is a tribological system carrying current.**

## Wipe is deliberate damage

Many connectors include a small wiping motion during mating.

That sounds undesirable until one realizes the purpose:

```text
wipe
-> disrupt oxide / contamination film
-> expose fresh conductive asperities
-> establish lower-resistance interface
```

But every wipe also spends wear life.

So the connector is designed around controlled sacrificial motion.

## Engineering reconstruction

The experiment in [`../../experiments/contact-fretting/`](../../experiments/contact-fretting/) uses a synthetic contact-resistance model with:

- plating thickness;
- normal force;
- micromotion amplitude;
- wear cycles;
- oxide accumulation.

It demonstrates why noble plating can delay failure without making the interface immortal.

It is not a connector qualification model.

## What became invisible

A consumer inserts:

- RAM;
- PCIe cards;
- USB cables;
- power connectors;
- CPU sockets;
- display cables.

Each ordinary action depends on invisible contact engineering:

```text
spring temper
contact geometry
plating thickness
underplate
wipe length
normal force
lubrication
mating-cycle rating
fretting qualification
mixed-flow-gas testing
```

A connector succeeds when two pieces of metal are allowed to move but the electrical boundary behaves as if they were one conductor.

[^antler81]: M. Antler, “Fretting corrosion of gold-plated connector contacts,” *Wear* 74, no. 1 (1981), 27–50, https://doi.org/10.1016/0043-1648(81)90192-7 .
[^antler85]: M. Antler, “Electrical effects of fretting connector contact materials: A review,” *Wear* 106 (1985), 5–33, https://doi.org/10.1016/0043-1648(85)90101-2 .
[^nasa]: NASA-STD-6016C, workmanship/material requirements for spaceflight hardware, section discussing gold/tin separable contact interfaces and fretting corrosion, https://standards.nasa.gov/sites/default/files/standards/NASA/C/2021-09-30-NASA-STD-6016C-Approved.pdf . This is mature aerospace guidance, not evidence for early commercial connector practice.

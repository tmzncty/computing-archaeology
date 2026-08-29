# Why CAF Made Laminate a Reliability Path

A printed-circuit-board laminate is supposed to keep conductors apart.

Under the wrong combination of moisture, voltage, material interfaces, and process damage, it can instead help grow a conductive path between them.

That failure is known as **conductive anodic filamentation** (CAF).

## Historical record

CAF was identified in the late 1970s as a catastrophic printed-wiring-board failure mode. Later IPC historical reviews describe it as an electrochemically formed, copper-containing conductive filament that can propagate inside glass-reinforced epoxy laminate along glass/epoxy interfaces.[^history]

IPC now maintains dedicated CAF resistance test methods and coupons, evidence that what began as a failure-analysis problem became a standardized material/process qualification problem.[^test]

## The board interior is not inert

A simple PCB drawing shows:

```text
copper via | insulating laminate | copper via
```

CAF introduces hidden state:

```text
humidity
+ electric field
+ copper source
+ glass/resin interface
+ drilling / thermal history
-> electrochemical path growth
```

The filament can grow where no designer placed copper.

That makes the laminate itself part of the electrical reliability model.

## Why density made CAF more important

The risk becomes harder to ignore as products push toward:

- smaller conductor spacing;
- smaller drilled-hole spacing;
- more layers;
- higher voltage gradients across small distances;
- repeated thermal excursions;
- harsher environmental exposure.

IPC's CAF test method explicitly varies drilled-hole-wall spacing and treats laminate, design, and manufacturing-process changes as relevant variables.[^test]

So “make the board denser” is not free.

Every reduction in physical separation spends some of the electrochemical reliability margin.

## Drilling can create future electrical geography

CAF is also a beautiful example of manufacturing damage becoming latent architecture.

A drilled hole changes:

- glass bundles;
- resin interfaces;
- copper wicking opportunity;
- local mechanical damage;
- moisture pathways.

Years later, the filament may follow those old process-created interfaces.

The board therefore remembers how it was drilled and laminated.

## Engineering reconstruction

The experiment in [`../../experiments/caf-path/`](../../experiments/caf-path/) uses a synthetic path-risk score based on:

- conductor spacing;
- humidity;
- voltage gradient;
- interface damage.

It is not IPC-TM-650 and does not predict CAF lifetime. It only demonstrates why reducing spacing while increasing humidity or process damage can multiply risk rather than add it linearly.

## What became invisible

A finished motherboard looks like copper on green material.

The hidden reliability stack includes:

```text
glass style
resin chemistry
lamination quality
drill damage
hole-wall spacing
moisture uptake
ionic species
voltage gradient
CAF coupon testing
cross-section failure analysis
```

Once again, successful standardization makes the problem disappear from ordinary computer history.

[^history]: Laura J. Turbini, “Conductive Anodic Filament (CAF) Formation: An Historic Perspective,” IPC APEX EXPO 2005. IPC technical-resource summaries note discovery in the 1970s and describe CAF as a copper-containing electrochemical filament growing within epoxy/glass interfaces; see https://www.ipc.org/technical-resources and archived conference material such as https://www.ipc.org/system/files/technical_resource/E17%26S02-3.pdf .
[^test]: IPC-TM-650 Method 2.6.25B, *Conductive Anodic Filament (CAF) Resistance Test: X-Y Axis*, https://www.ipc.org/sites/default/files/test_methods_docs/2.6.25b.pdf .

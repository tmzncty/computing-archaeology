# Why Wet Chemistry Had to Become Electronic Grade

A semiconductor fab can spend billions of dollars controlling nanometer-scale geometry and then ruin the wafer with a trace contaminant dissolved in a bottle of otherwise familiar acid.

This is why a list such as

```text
HF
HCl
H2SO4
H2O2
NH4OH
HNO3
H3PO4
```

is historically misleading if it is read as an ordinary chemistry-shopping list.

The relevant industrial achievement was not merely learning that these chemicals etch, oxidize, strip, or clean silicon and metals. It was learning to manufacture, package, transport, dispense, monitor, and dispose of them at purity levels compatible with semiconductor surfaces.

The historical question is:

> **When did familiar industrial chemicals become precision process materials?**

## The same molecule can belong to a different industry

Hydrofluoric acid is hydrofluoric acid whether it is sold for bulk industrial use or semiconductor processing.

But the process result can depend on what else is present.

Unwanted species may include:

- sodium, potassium, iron, copper, nickel, and other metals;
- particles;
- organics;
- dissolved gases;
- residues from containers or plumbing;
- water of inadequate purity;
- cross-contamination from previous chemicals.

The point is not that every trace species always matters equally. It is that semiconductor fabrication creates surfaces and films whose electrical behavior can be sensitive to contamination invisible to ordinary industrial specifications.

## Wet processing was already chemically dense by the early 1980s

The U.S. Environmental Protection Agency's 1983 development document for the electrical and electronic components industry describes hydrofluoric acid as a semiconductor etchant and cleaner and identifies organic solvents from photoresist development, stripping, drying, and cleaning as major process streams.[^epa-1983]

Contemporary occupational-health investigations likewise document semiconductor workers handling mixtures including HF, HCl, HNO3, H3PO4, H2SO4, H2O2, NH4OH, acetic acid, acetone, methanol, and chlorinated solvents.[^niosh-1983]

These records are valuable because they recover the factory as a chemical system rather than a diagram of transistors.

## Wafer cleaning became a chemistry of contaminant classes

Werner Kern's RCA cleaning work, developed in the 1960s and published with David Puotinen in 1970, is an important milestone because it framed wafer cleaning as a sequence aimed at different contamination mechanisms rather than one generic rinse.

The later literature conventionally distinguishes:

- organic / particle removal;
- oxide removal where required;
- ionic / metallic contamination removal.

That structure matters more historically than memorizing one recipe.

The logic is:

```text
contaminant type
-> choose chemistry that removes or complexes it
-> avoid redeposition
-> avoid unacceptable attack on the desired surface
-> rinse without adding new contamination
```

Cleaning therefore becomes process integration.

## Purity extends into the container and delivery path

Electronic-grade chemistry is not finished when a chemical producer certifies the bulk liquid.

The material must still pass through:

```text
container
-> shipping
-> storage
-> valve / fitting
-> distribution
-> filter
-> dispense point
-> process vessel
```

Every wetted surface is a possible contamination source.

This is why the history of semiconductor chemicals connects directly to the history of fluoropolymer plumbing, high-purity fittings, point-of-use filtration, ultrapure water, and contamination metrology.

## HF reveals the materials problem

Hydrofluoric acid is especially revealing because it attacks silicon dioxide and also attacks many materials that would be ordinary choices for chemical equipment.

A fab therefore cannot choose pipe, valve, tank, or filter materials only by pressure rating and price.

The material must also survive the chemistry while contributing sufficiently little contamination.

This is one reason fluoropolymers later become so important in wet-process infrastructure.

## The chemical supplier becomes part of device yield

Once contamination limits become tight, the chemical manufacturer is no longer an upstream commodity vendor in the ordinary sense.

Its operations can affect:

- lot-to-lot metal content;
- particle load;
- moisture;
- container cleanliness;
- analytical certification;
- traceability;
- shelf and transport behavior.

A fab's process capability therefore depends partly on another company's purification and analytical capability.

That is the same organizational pattern seen elsewhere in this repository:

```text
design rules
-> foundry interface

mass-flow controller
-> gas-recipe interface

electronic-grade chemical specification
-> wet-process material interface
```

## Reconstruction: why one number is never enough

Suppose a chemical is described only by `99.999% purity`.

That sounds excellent, but it hides distribution.

The remaining fraction could be dominated by a harmless species or by a contaminant strongly coupled to the process.

So useful qualification is usually multi-dimensional:

```text
bulk assay
+ metals
+ particles
+ organics
+ water
+ specific ionic contaminants
+ container / handling qualification
```

The experiment in [`../../experiments/wet-chem-purity/`](../../experiments/wet-chem-purity/) models this as separate contamination channels rather than one scalar purity number.

It is not a historical fab specification.

## Why this belongs in computer history

A CPU history that begins with photolithography silently assumes that the fab can repeatedly obtain chemicals whose uncontrolled impurities are low enough not to dominate the intended process.

That capability rests on:

- bulk chemical production;
- purification;
- analytical chemistry;
- packaging;
- clean transport;
- compatible materials;
- filtration;
- waste handling;
- operator discipline.

The acid bottle is therefore not a background prop.

It is part of the manufacturing civilization beneath computation.

## What this teaches us

The key transition is:

> **A familiar chemical becomes a semiconductor process material when its unwanted contents, container, delivery path, and analytical history matter as much as its nominal formula.**

The fab does not merely consume `HF` or `H2SO4`.

It consumes a tightly controlled material state.

## References

[^epa-1983]: U.S. Environmental Protection Agency, *Development Document for Effluent Limitations Guidelines and Standards for the Electrical and Electronic Components Point Source Category, Phase I*, 1983, https://www.epa.gov/sites/default/files/2016-05/documents/eec_phase_1_dd_apr_1983.pdf
[^niosh-1983]: C. L. Moseley, *Health Hazard Evaluation Report HETA-83-164-1377: Siemens Components, Inc.*, NIOSH, 1983, https://stacks.cdc.gov/view/cdc/172024

## Source note

The EPA and NIOSH documents are period regulatory/industrial-health evidence for chemical use and factory streams, not semiconductor purity specifications. Later cleaning literature is useful for process mechanism but should not be back-projected as the exact recipe used by every fab in the 1960s or 1970s.
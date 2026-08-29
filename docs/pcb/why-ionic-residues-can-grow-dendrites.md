# Why Ionic Residues Can Grow Dendrites

A circuit board can be electrically correct, visually clean, and still contain the ingredients for a future short circuit.

The missing ingredients are often:

```text
ionic residue
+ absorbed moisture
+ DC bias
+ time
```

Together they can produce **electrochemical migration** (ECM).

## Historical record

Electrochemical migration on printed-circuit assemblies is the growth of conductive metal structures through a thin electrolyte layer under electrical bias. IPC technical literature describes the sequence as metal dissolution at the anode, ion transport, and metal deposition at the cathode, eventually producing dendritic growth that can lower surface insulation resistance or bridge adjacent conductors.[^ecm]

Later assembly-cleanliness work connected surface contamination, flux residues, humidity, and SIR testing directly to ECM risk.[^sir]

## “No-clean” does not mean “no chemistry”

A modern board may retain residues from:

- flux activators;
- solder paste;
- handling;
- cleaning chemistry;
- masks and temporary materials;
- environmental contamination.

Many residues are harmless under dry, unbiased conditions.

The electrical meaning changes when humidity creates a mobile ionic medium.

```text
residue
+ water film
-> electrolyte

metal + bias
-> ions migrate
-> metal deposits elsewhere
```

The board has begun electroplating itself in the wrong place.

## Dendrites can create intermittent ghosts

ECM failures are especially unpleasant because a thin dendrite may:

1. bridge two conductors;
2. carry current;
3. heat and fuse open;
4. regrow later.

That can produce intermittent faults that disappear during inspection.

The failure therefore belongs to both chemistry and debugging history.

An engineer may observe:

```text
system fails in humidity
board dries
failure disappears
lab cannot reproduce
```

without realizing that the electrical path physically existed and then burned away.

## Cleanliness became an electrical specification

Once this mechanism was understood, cleanliness could no longer be judged only by appearance.

Industry used methods such as:

- surface insulation resistance (SIR);
- resistivity of solvent extract;
- ion chromatography;
- temperature-humidity-bias testing;
- optical and microscopic failure analysis.

IPC studies explicitly compare contamination measurements with insulation resistance and metal-migration behavior.[^sir]

This is another recurring repository theme:

> **measurement infrastructure appears when the dangerous state is invisible to ordinary inspection.**

## CAF is related but not identical

This repository keeps two mechanisms separate:

- **surface ECM** commonly grows through a moisture/electrolyte film across assembly surfaces;
- **CAF** grows internally through laminate interfaces.

Both involve electrochemistry and bias, but their physical paths and qualification methods differ.

## Engineering reconstruction

The experiment in [`../../experiments/ecm-dendrite/`](../../experiments/ecm-dendrite/) uses a synthetic growth accumulator driven by humidity, ionic contamination, bias, and conductor spacing.

It also includes a simple fuse/regrow behavior to demonstrate why ECM can create intermittent faults.

It is not an SIR or ECM qualification model.

## What became invisible

A user sees a clean motherboard.

The manufacturing stack remembers:

```text
flux chemistry
reflow completeness
wash chemistry
rinse quality
standoff height
trapped residues
surface energy
humidity exposure
bias spacing
SIR qualification
```

The extraordinary part is not that wet contaminated metal can corrode.

It is that industry learned to build extremely dense electronics while keeping enough of this invisible chemistry under control for billions of boards to survive ordinary life.

[^ecm]: X. He, M. H. Azarian, and M. G. Pecht, “Comparative Assessment of Electrochemical Migration on Printed Circuit Boards with Lead-Free and Tin-Lead Solders,” IPC technical paper, https://www.ipc.org/system/files/technical_resource/E8%26S14_02.pdf .
[^sir]: X. He, M. H. Azarian, M. Kostinovsky, and M. G. Pecht, “An Evaluation of the Insulation Resistance and Surface Contamination of Printed Circuit Board Assemblies,” IPC APEX EXPO 2012 summary, https://www.ipc.org/node?page=279 .

# Why Read-Only Memory Kept Becoming Less Read-Only

“ROM” sounds like one device class. Historically it names a sequence of answers to a production question:

> **At what point should information become fixed, who should be allowed to change it, and what machinery should a change require?**

Mask ROM, PROM, EPROM, EEPROM and Flash did not simply add features in a straight line. Each moved the boundary between factory, equipment maker, system manufacturer, technician and end user.

## Mask ROM: put stable information into production

A mask-programmed ROM encodes contents during semiconductor fabrication through a pattern of connections or devices. Once the design is established and volume is high, per-unit memory can be dense and need no field-programming mechanism.

But the information is committed on the manufacturing side of the boundary:

```text
firmware change
-> new pattern / mask information
-> new wafer processing
-> package and test again
```

This is attractive when many identical copies are needed and expensive when code is still changing or volumes are uncertain. “Read only” is therefore partly a supply-chain statement: the user receives a fixed lookup structure because production has already made the choices.

## PROM: program after manufacture, once

A programmable ROM ships blank and lets a customer or system maker set bits with a programmer. Classic bipolar PROMs used fusible links or related one-time structures: programming permanently changed selected elements.

PROM solved the inventory problem of ordering a unique mask ROM before contents or demand were stable. The same blank device could be stocked, then specialized late. The cost was that an error consumed the part; there was no ordinary erase cycle.

```text
mask ROM: specialize in wafer fabrication
PROM:      specialize after fabrication, once
```

## EPROM: make iteration recoverable

Dov Frohman's floating-gate work placed charge on an electrically isolated gate so a transistor's conduction represented stored information. His patent describes programming by charge injection, long retention without continuous power, and removing charge with ultraviolet or X-ray exposure.[^frohman-patent]

Commercial EPROM put a quartz window over the die so ultraviolet light could erase the array. Intel's corporate history says the device reduced prototype iteration from days or weeks to hours and initially appeared especially useful for development before microprocessor systems expanded its role.[^intel-eprom]

EPROM did not make rewriting casual:

- the package window cost money;
- the chip usually had to leave the target system;
- erasure exposed the whole die for minutes rather than changing one byte;
- programming required special voltage and equipment;
- windowless one-time-programmable packages intentionally gave up erasure for lower product cost.

The iconic window was not decoration. Packaging was part of the erase interface. The repository already treats this development-side consequence in [`../semiconductor/why-eprom-made-hardware-development-iterative.md`](../semiconductor/why-eprom-made-hardware-development-iterative.md); this page places it in the larger production lineage rather than repeating that article.

## EEPROM: move erasure into the electrical interface

Electrically erasable programmable ROM removed the ultraviolet and package-removal step. A system could alter retained information electrically, often at byte or small-unit granularity depending on the device.

That solved operational problems EPROM handled poorly:

- calibration and configuration state could change after assembly;
- firmware or parameters could be updated without removing the package;
- service equipment no longer needed a UV erase cycle.

The extra select, tunneling and high-voltage circuitry cost area and made writes slower and more limited than reads. EEPROM was not “RAM that happens to remember.” It exposed asymmetric operations and finite program/erase endurance.

## Flash: erase many cells together to recover density

Flash memory retained electrical programming and erasure but organized erase around larger groups of cells. Fujio Masuoka and Toshiba colleagues described a “flash E2PROM” cell and array in 1984; the name emphasized erasing the memory rapidly as a group rather than providing a separate erase path for every byte.[^masuoka]

This grouping matters physically and economically. Sharing erase structures lets the array become denser, but software can no longer assume that the smallest readable or programmable unit is also independently erasable.

A simplified NOR/NAND distinction is useful but should not be made absolute:

- **NOR Flash** emphasizes random read access suitable for code and memory-mapped use, with cells connected more directly to bitlines;
- **NAND Flash** strings cells in series to improve density and favors page transfer plus block erase, with controller-managed storage use.

Specific geometries and command sets vary. The durable constraint is the asymmetry:

```text
read:    small unit, relatively easy
program: page or subpage rules, changes constrained state
reuse:   erase a much larger block first
```

## Why programming is not ordinary overwriting

Floating-gate and charge-trap devices represent state by changing a transistor threshold. High electric fields move charge through an insulating barrier. Reading senses the resulting conduction; programming and erasing stress the tunnel dielectric and change trapped charge populations.

Consequences appear at the interface:

1. programming usually moves cell state in only one direction from the erased state;
2. reversing that direction requires erase;
3. erase acts on a shared block, not one arbitrary byte;
4. program/erase cycles gradually widen distributions and damage the insulating system;
5. retention, read disturb and program disturb become statistical rather than perfectly binary limits.

A filesystem or SSD cannot expose these raw rules directly without making ordinary updates awkward. Controllers therefore use out-of-place writes, logical-to-physical mapping, garbage collection, bad-block management, ECC and wear leveling.

Run [`experiments/flash-erase/`](../../experiments/flash-erase/) to see why one logical page updated repeatedly can either concentrate erase wear or be remapped across free physical pages. Its numbers are synthetic; it is not an FTL or endurance predictor.

## Wear is a population-management problem

“Flash wears out after N writes” is misleading. Endurance depends on device type, geometry, temperature, voltage algorithms, data patterns, retention requirement and error-correction margin. Failures and threshold shifts form distributions across a population.

The system response is layered:

```text
cell/process margin
+ verify-and-retry algorithms
+ ECC
+ spare blocks
+ bad-block retirement
+ wear leveling
+ telemetry
```

This is a close relative of ECC DRAM: apparently clean storage is maintained by statistical infrastructure below the interface.

## Production boundaries left modern fossils

Each ROM generation changed who could revise information:

| Technology | Contents fixed by | Ordinary revision cost |
|---|---|---|
| mask ROM | semiconductor production | new production pattern/run |
| PROM | customer/system maker | replace a programmed part |
| EPROM | programmer + UV eraser | remove/expose/reprogram device |
| EEPROM | in-system electrical commands | slow bounded writes, endurance |
| Flash | in-system controller over blocks/pages | mapping, erase, reclamation, wear |

Modern interfaces still expose these bargains:

- firmware “flashing” is an operation, not a normal store instruction;
- erase-block alignment affects update cost;
- storage devices need discard/TRIM and garbage collection;
- write amplification measures hidden physical work;
- controller firmware and mapping tables are part of data durability;
- power loss during remapping can be more dangerous than a failed read.

The word “read-only” kept changing because the economically useful question was never simply whether electrons could move. It was **where revision belonged in the product lifecycle and how much array area, package machinery and controller complexity the ability to revise was worth.**

## Cautions

- ROM-family names describe broad product classes; exact cells and erase/program mechanisms vary.
- EPROM's iteration story is supported here partly by Intel corporate history and should be read as an interested institutional source.
- Flash was not the first electrically erasable nonvolatile memory; its density bargain depended on coarser shared erase.
- A controller's block interface does not reveal raw NAND geometry faithfully.

[^frohman-patent]: Dov Frohman-Bentchkowsky, “Floating gate transistor and method for charging and discharging same,” US Patent 3,660,819, filed 15 June 1970, issued 2 May 1972, https://patents.google.com/patent/US3660819A/en
[^intel-eprom]: Intel, “A Success…Out of Quality Control Issues,” corporate history of EPROM, https://www.intel.com/content/www/us/en/history/virtual-vault/articles/eprom.html
[^masuoka]: Fujio Masuoka et al., “A new flash E2PROM cell using triple polysilicon technology,” *1984 International Electron Devices Meeting*, pp. 464–467, DOI 10.1109/IEDM.1984.190752, https://doi.org/10.1109/IEDM.1984.190752

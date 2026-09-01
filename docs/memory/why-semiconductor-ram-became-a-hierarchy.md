# Why Semiconductor RAM Split into SRAM and DRAM

Magnetic core made a bit into a selected magnetic object. Semiconductor memory made a different bargain: put storage and selection on one substrate, then choose whether each bit should contain an actively stable circuit or a very small, temporary packet of charge.

That choice produced **SRAM** and **DRAM**, then a hierarchy in which their different cell economics became cache and main memory.

## Historical record: density was the opening

The Computer History Museum records John Schmidt's 64-bit p-channel MOS static RAM at Fairchild in 1964 and later static and dynamic projects. Intel's 1,024-bit 1103 DRAM became a significant commercial challenger to core beginning in 1970, although it used a three-transistor dynamic cell rather than the later one-transistor cell.[^chm-dram]

Robert Dennard's 1967 filing described a cell with one field-effect transistor and one capacitor. The patent makes its intended trade explicit: use the transistor both to charge and interrogate the capacitor, minimizing components and cell area so many cells can fit on one substrate.[^dennard]

The familiar `1T1C` cell must not be silently projected onto every early commercial DRAM. It was a density direction that later became dominant; the 1103 bridge from core was not itself a production example of that final cell form.[^chm-dram]

## SRAM pays transistors for a stable local decision

A conventional SRAM cell uses a bistable circuit—commonly two cross-coupled inverters—plus access transistors. In the familiar six-transistor CMOS cell, the cross-coupled pair continually reinforces one of two states while power is present.

The cell must meet three competing requirements:

1. **hold:** leakage and noise must not flip the state;
2. **read:** connecting an internal node to a precharged bitline must not disturb it;
3. **write:** the external driver must overpower the cell long enough to change it.

Strong pull-down devices improve read stability; weaker pull-ups make writing easier; access devices must be strong enough to write but not so strong that a read destroys state. Process, voltage and temperature variation shrink these margins.

“SRAM is fast because it uses six transistors” is incomplete. SRAM is fast because the cell presents an actively regenerated state that can be selected without first recovering a tiny capacitor charge or scheduling refresh. The cost is cell area and leakage: much lower density than a 1T1C array.

## DRAM pays controller work to make the cell small

A 1T1C cell reduces local circuitry to:

```text
bitline -- access transistor -- storage capacitor
                    |
                 word line
```

Charge leaks away; Dennard's patent says periodic regeneration is necessary.[^dennard] But leakage is only one part of the cycle.

The tiny storage capacitor shares charge with a long, higher-capacitance bitline. Before reading, circuitry precharges the bitline near a reference. Raising a word line connects a cell, producing only a small voltage difference. A **sense amplifier** resolves that imbalance and drives a full logic level.

Connecting the cell to the precharged bitline also changes the cell's charge. While the word line remains active, the sense amplifier's result restores the selected cell. Thus sensing and restoration are consequences of a small capacitor on a shared bitline:

```text
precharge
-> activate row
-> charge sharing
-> sense a small difference
-> drive a full level
-> restore the cell
```

Cells also need restoration when software does not read them. A controller periodically activates rows before leakage removes too much signal. Refresh consumes time and power and must be scheduled by the interface or device.

This differs physically from core destructive read, but the architectural pattern is familiar: support electronics hide a medium whose behavior does not match a clean load/store abstraction. Compare [`why-core-memory-was-worth-weaving.md`](why-core-memory-was-worth-weaving.md).

## Why row and column addresses reused package pins

Package pins and board traces are not free. Mostek's MK4096 compressed 4,096 bits into a conventional 16-pin package; the later MK4116 used multiplexed address inputs with row-address-strobe (`RAS`) and column-address-strobe (`CAS`) timing.[^chm-dram][^mk4116]

```text
put row bits on address pins
-> assert RAS
-> put column bits on the same pins
-> assert CAS
```

For `r` row bits and `c` column bits, a flat address needs about `r + c` signal pins. Time-multiplexing needs about `max(r, c)` address pins plus controls. It converts **package scarcity into time**.

Activating a word line also connects an entire physical row to sense amplifiers. Those amplifiers hold the resolved row, so another column from it can reuse activation work. This left a behavioral fossil: accesses within an open row can differ from those that close one row and activate another.

Run [`experiments/dram-array/`](../../experiments/dram-array/) to expose both tradeoffs. It is a synthetic model, not a device timing simulator.

## Asynchronous DRAM to DDR: what changed

These names describe how repeated transfers are coordinated after a row is opened.

- **Asynchronous DRAM:** the controller drove addresses, `RAS`, `CAS` and enable signals against specified delays; no continuous command clock organized operations.
- **Fast Page Mode (FPM):** keep a row active while changing columns and cycling `CAS`, reusing the sensed page.
- **Extended Data Out (EDO):** hold output valid longer while the next column operation begins, enabling more overlap. It did not eliminate activation or refresh.
- **SDRAM:** register commands and addresses against a clock; use banks and programmable bursts. Period datasheets describe `ACTIVE`, `READ`, `WRITE`, `PRECHARGE` and refresh commands.[^micron-sdram]
- **DDR SDRAM:** transfer burst data on both edges of a data strobe. The name describes the interface; it does not mean every access has half the latency.

The direction was:

```text
asynchronous strobes
-> keep a sensed page open
-> overlap output and next column work
-> clocked commands, banks and bursts
-> higher-rate edge-based burst transfer
```

Each step extracted more bandwidth and coordination from an array still constrained by activation, sensing, restoration, precharge and refresh.

## Why cache is usually SRAM and main memory is usually DRAM

A cache needs low latency and high access frequency beside logic. Paying several transistors per bit is rational when the store is small and every cycle matters. Main memory needs much more capacity at acceptable cost; DRAM's smaller cell wins density while controllers amortize its maintenance.

This is engineering reconstruction, not a claim that one calculation decided every product:

```text
small, latency-sensitive store -> spend area on SRAM
large, capacity-sensitive store -> spend controller work on DRAM
```

The hierarchy is a negotiated boundary between two physical cell bargains, not merely a software diagram labeled “fast” and “slow.”

## What survives in modern memory

Modern DDR and HBM are far removed from 1970s products, but commands still activate and precharge rows; refresh remains mandatory; banks expose parallelism while preserving row-local behavior; bursts move multiple words per command; controllers schedule constraints hidden from ordinary loads.

HBM changes package geometry by moving a very wide DRAM interface beside the processor, not by abolishing DRAM's core-array behavior. Continue with [`why-hbm-moved-memory-beside-the-processor.md`](why-hbm-moved-memory-beside-the-processor.md).

## Cautions

- The 1103 was not a 1T1C DRAM.
- FPM, EDO, SDRAM and DDR did not replace one another on one clean global date.
- Open-row behavior depends on generation, organization, controller and policy.
- SRAM/DRAM is dominant, not universal.

The defensible continuity is narrower: **cell area, weak stored signal, shared sensing, package pins and coordination shaped both the devices and behavior systems still expose.**

[^chm-dram]: Computer History Museum, “1970: MOS Dynamic RAM Competes with Magnetic Core Memory on Price,” *The Silicon Engine*, https://www.computerhistory.org/siliconengine/mos-dynamic-ram-competes-with-magnetic-core-memory-on-price/
[^dennard]: Robert H. Dennard, “Field-effect transistor memory,” US Patent 3,387,286, filed 14 July 1967, issued 4 June 1968, https://patents.google.com/patent/US3387286A/en
[^mk4116]: Mostek, *MK 4116(N/P)-3 16,384-Bit Dynamic Random Access Memory*, in *Mostek Memory Products* (1977), Bitsavers, https://bitsavers.org/components/mostek/_dataBooks/1977_Mostek_Memory_Products.pdf
[^micron-sdram]: Micron Technology, *MT48LC16M16A2 256Mb: x4, x8, x16 SDRAM* data sheet, command, burst and refresh descriptions, https://media-www.micron.com/-/media/client/global/documents/products/data-sheet/dram/sdram/256mb_sdram.pdf

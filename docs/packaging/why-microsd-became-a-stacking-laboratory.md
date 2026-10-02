# Why a microSD Card Became a Stacking Laboratory

A memory card smaller than a postage stamp reached 2 TB with the same 15 × 11 × 1 mm outline it has had since the mid-2000s. The card did not grow. The stacking did.

## Historical record

SanDisk introduced the microSD (then TransFlash) form factor in 2004–2005; the SD Association standardized the outline, and capacities climbed from 128 MB-class cards to retail 1 TB (2019) and retail 2 TB products (Kioxia announced volume production of 2 TB microSD at end-2023 with sales from January 2024; SanDisk followed with 2 TB retail products in 2024), all inside the same mechanical envelope.[^sdassoc][^kioxia2tb]

3D NAND — reorienting the charge-trap cell string vertically — entered volume production around 2013–2014 and passed 200 stacked word-line layers per die in the 2020s.[^bd3dnand]

SDXC defines the 2 TB ceiling; SDUC extends the standard's address space to 128 TB.

## Engineering reconstruction

The card is three stackings happening at once:

```text
package level:   thinned NAND die stacked and wire-bonded, molded in resin
die level:       200+ deposited word-line layers, deep-etched vertical channels
cell level:      QLC thresholds: 16 charge states = 4 bits per cell
```

The terabyte-class card exists only because package-level die stacking, 3D NAND deposition/etch, and multi-level cell encoding compound. (A documented instance: Kioxia's 2 TB microSD uses sixteen 1 Tbit NAND die in the package — one vendor's stacking showcase, not a universal requirement of every TB-class card.) Two die of planar SLC inside this outline would hold a small fraction of a terabyte.

The controller's job list is a direct consequence: ECC strong enough for 16-state threshold sensing, bad-block management, address mapping, garbage collection, wear leveling, and read-voltage calibration all live inside the same resin.

The interface tells the complementary story. UHS-I cards run 8 contacts at ~104 MB/s; UHS-II/III add a second row of contacts; SD Express borrows PCIe/NVMe. Capacity grew by four orders of magnitude while the pin count barely moved — when the connector could not scale, the standard's answer was more rows, not more area.

## Constraints that do not scale

- Thermal: a 1 mm-thick stack has essentially no heat-spreading budget; sustained controller+NAND power is milliwatt-class by necessity.
- Random performance: marketing speeds are sequential; small-file random I/O exposes the small controller and NAND latency directly.
- Data egress: writing is convenient, reading back a full card at ~80 MB/s takes hours — the capacity grew faster than the pipe.

## Why it matters

The microSD is a consumer-visible endpoint of advanced packaging: wafer thinning, die stacking, wire bonding over mold, and a controller co-packaged with its media. When cinema cameras outgrew it (Blackmagic URSA Cine 17K records to internal multi-TB Media Modules at roughly hundreds of MB/s to ~2 GB/s per the official tech specs), the constraint that broke was not capacity density but bandwidth and thermals — the same two axes the stacking had been optimizing against all along.

## Sources

[^sdassoc]: SD Association, SD specifications and capacity standards (SDHC/SDXC/SDUC). https://www.sdcard.com/
[^kioxia2tb]: Kioxia, 2 TB microSD volume production announcement (2023-12), https://www.kioxia.com/ja-jp/personal/news/2023/20231220-1.html
[^bd3dnand]: 3D NAND adoption timeline as documented by memory vendors (Samsung V-NAND 2013; industry 200+ layer nodes in the 2020s).

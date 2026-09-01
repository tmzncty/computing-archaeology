# Semiconductor Memory Field-Set Source Map

This source map supports the first treatment connecting magnetic core to ordinary semiconductor memory, ROM families, Flash, cache hierarchy and ECC. It distinguishes period documents from later institutional interpretation.

## 1. Dynamic and static RAM

### Robert H. Dennard, 1T1C patent

- Robert H. Dennard, “Field-effect transistor memory,” US Patent 3,387,286, filed 14 July 1967, issued 4 June 1968: https://patents.google.com/patent/US3387286A/en

Primary patent evidence for the one-transistor/one-capacitor cell, charge storage, read path, regeneration requirement and the explicit cell-area objective. A patent establishes disclosed design and claimed invention, not commercial adoption by itself.

### Contemporary DRAM products

- Mostek, *Mostek Memory Products* (1977): https://bitsavers.org/components/mostek/_dataBooks/1977_Mostek_Memory_Products.pdf
- Intel, *Intel Memory Design Handbook* (1977): http://bitsavers.org/components/intel/_dataBooks/1977_Intel_Memory_Design_Handbook.pdf

Use the Mostek book for MK4116 multiplexed address pins, `RAS`/`CAS`, refresh and timing. Use the Intel handbook for period system-design context. Datasheets establish interfaces and limits, not a vendor's private motives.

### Later historical synthesis

- Computer History Museum, “1970: MOS Dynamic RAM Competes with Magnetic Core Memory on Price”: https://www.computerhistory.org/siliconengine/mos-dynamic-ram-competes-with-magnetic-core-memory-on-price/
- Robert H. Dennard, “Evolution of the MOSFET dynamic RAM—A personal view,” *IEEE Transactions on Electron Devices* 31, no. 11 (1984), 1549–1555, DOI 10.1109/T-ED.1984.21744.

The CHM entry is a curated retrospective useful for the 1103/MK4096/MK4116 sequence and bibliography. Dennard's later personal view is valuable retrospective testimony, but should not replace the 1967 filing when discussing the original disclosed trade.

### Synchronous interface evidence

- Micron Technology, *MT48LC16M16A2 256Mb SDRAM* datasheet: https://media-www.micron.com/-/media/client/global/documents/products/data-sheet/dram/sdram/256mb_sdram.pdf
- JEDEC, DDR SDRAM standards landing/catalog: https://www.jedec.org/standards-documents/focus/memory-ssd-jc-42

Use period/vendor datasheets to establish `ACTIVE`, `READ`, `WRITE`, `PRECHARGE`, refresh, bank and burst behavior. Do not describe SDRAM as eliminating row-cycle latency; it coordinates commands with a clock.

## 2. ROM, EPROM and EEPROM

### Floating-gate EPROM

- Dov Frohman-Bentchkowsky, “Floating gate transistor and method for charging and discharging same,” US Patent 3,660,819, filed 15 June 1970, issued 2 May 1972: https://patents.google.com/patent/US3660819A/en
- Intel, “A Success…Out of Quality Control Issues”: https://www.intel.com/content/www/us/en/history/virtual-vault/articles/eprom.html
- Intel, *1702A 2048-bit Electrically Programmable Read Only Memory* datasheet, in contemporary Intel data books preserved at Bitsavers: http://bitsavers.org/components/intel/_dataBooks/

The patent supports isolated-gate charge, injection, nonvolatile retention and UV/X-ray erasure. Intel's article supports the company's account of development iteration and microprocessor complementarity; label it corporate history.

### ROM/PROM production distinction

- Intel, *Memory Design Handbook* (1977), ROM/PROM/EPROM product and application material: http://bitsavers.org/components/intel/_dataBooks/1977_Intel_Memory_Design_Handbook.pdf

Use period catalog/handbook language to establish who programs a part, one-time versus erasable behavior and required programming equipment. The broader supply-chain interpretation remains engineering reconstruction.

## 3. Flash

### Original Flash E2PROM publication

- Fujio Masuoka et al., “A new flash E2PROM cell using triple polysilicon technology,” *1984 International Electron Devices Meeting*, 464–467, DOI 10.1109/IEDM.1984.190752: https://doi.org/10.1109/IEDM.1984.190752

Primary conference evidence for Toshiba's 1984 flash E2PROM cell/array proposal and group-erase framing. Do not use it alone to narrate later NOR/NAND market history or modern SSD controllers.

### Device behavior and endurance

- Micron, NAND Flash technical documentation and datasheets: https://www.micron.com/products/storage/nand-flash
- JEDEC, JESD47 and solid-state memory standards catalog: https://www.jedec.org/standards-documents

Vendor datasheets establish page program, block erase, bad-block and endurance conditions for the named generation only. Do not turn one product's block size or cycle rating into a timeless property of all Flash.

## 4. Error correction and soft errors

### Coding theory

- R. W. Hamming, “Error Detecting and Error Correcting Codes,” *Bell System Technical Journal* 29, no. 2 (1950), 147–160, DOI 10.1002/j.1538-7305.1950.tb00463.x: https://doi.org/10.1002/j.1538-7305.1950.tb00463.x

Primary paper for parity-check structure, syndrome-based correction and the operational problem that motivated Hamming. It is not a DRAM-specific ECC deployment history.

### Semiconductor soft errors

- T. C. May and M. H. Woods, “Alpha-particle-induced soft errors in dynamic memories,” *IEEE Transactions on Electron Devices* 26 (1979), 2–9, DOI 10.1109/T-ED.1979.19370: https://doi.org/10.1109/T-ED.1979.19370

Near-primary period evidence connecting trace uranium/thorium in package material to charge deposition and dynamic-memory upset. It supports the need for layered material/device/system responses, not a universal modern soft-error rate.

## Claims deliberately kept as reconstruction

The articles mark or phrase these as engineering reconstruction rather than documented intent:

- package-pin scarcity made address multiplexing economically attractive in general;
- cache/main-memory placement follows latency-versus-density pressure;
- out-of-place Flash updates trade mapping/reclamation work for fewer immediate erases;
- scrub cadence controls the accumulation window for correctable errors;
- modern interface behaviors are “fossils” of cell/array constraints.

## Known source limits

- Publicly recoverable early SRAM cell-design papers and period FPM/EDO transition manuals deserve a narrower follow-up.
- Intel and other corporate histories are interested sources and should not carry priority claims alone.
- Paywalled IEEE papers are cited by DOI and bibliographic metadata; no inaccessible quotation or page-specific claim is invented.
- Datasheet URLs can move. Titles, vendors, dates and archive paths are recorded so sources remain recoverable.

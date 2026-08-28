# Source Map — Media and Compatibility Fossils Field Set

This source map supports the excavation set covering:

- Williams–Kilburn CRT memory;
- 80-column punched-card path dependence;
- sequential magnetic tape;
- front-panel bootstrapping;
- ASCII / EBCDIC / CR-LF device fossils;
- byte order and network serialization.

Article footnotes remain the claim-level citation layer. This file records **source type, provenance, and caution points**.

## Williams–Kilburn CRT storage

### Tom Kilburn, 1947 report

- Tom Kilburn, “A Storage System for Use with Binary Digital Computing Machines,” report to the Telecommunications Research Establishment, 1 December 1947.
- University of Manchester Digital60 transcription: https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/report1947.html
- Document index/context: https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/manchestercomputers/mark1/documents/index.html

**Source type:** contemporary technical report by a principal engineer.

**High-value claims:**

- charge-pattern storage on commercial CRTs;
- short-term retention and regeneration;
- pickup plate and raster organization;
- 1,024/2,048-digit experiments;
- focus, screen quality, spot size, and signal-to-noise as capacity constraints;
- hypothetical machine integration.

**Caution:** surviving web text is a later institutional transcription. Cite Kilburn as author/source and Manchester as preservation host.

### Manchester preservation history

- “The Williams Tube”: https://curation.cs.manchester.ac.uk/computer50/www.computer50.org/kgill/williams/williams.html
- “How it all began”: https://curation.cs.manchester.ac.uk/digital60/www.digital60.org/birth/how/index.html

**Source type:** later institutional preservation/history.

Use for chronology, integration with the Baby, and context around the 1947 work. Do not let the later “first stored-program computer” framing substitute for precise priority criteria.

## Eighty-column punched cards

### IBM punched-card institutional history

- IBM, “The punched card”: https://www.ibm.com/history/punched-card

**Source type:** corporate retrospective.

Use for:

- IBM's 1928 80-column format chronology;
- rectangular-hole/card dimensions;
- broad business and installed-base context.

**Caution:** IBM is narrating its own history. Use original manuals or independent scholarship for disputed priority/impact claims.

### IBM 29 Card Punch

- IBM, *IBM 29 Card Punch Reference Manual*, Form A24-3332: https://www.bitsavers.org/pdf/ibm/punchedCard/Keypunch/029/A24-3332-3_29_Reference_Man.pdf

**Source type:** manufacturer primary manual; Bitsavers is preservation host.

Use for field-oriented punching workflows, automatic skip/duplicate behavior, physical column positions, and operator interaction with 80-column records.

### IBM 711 / 72-column programming practice

- Columbia University Computing History, “IBM Card Sorters”: https://www.columbia.edu/cu/computinghistory/sorter.html

**Source type:** later university preservation/research page using IBM documentation and surviving practice.

Use for the relationship between IBM 711 row-binary input, the common 72-column program field, and columns 73–80 as sequence/identification space.

### Continuing card-image convention

- IBM, “Example 2: Punch Sequential Data Sets”: https://www.ibm.com/docs/en/zos/3.2.0?topic=examples-example-2-punch-sequential-data-sets

**Source type:** modern IBM product documentation illustrating a durable convention.

Use only to demonstrate persistence of 80-byte records / 73–80 sequence fields in descendant software practice, not as evidence of how the convention originated.

## Magnetic tape

### Computer History Museum

- “Tape unit developed for data storage”: https://www.computerhistory.org/storageengine/tape-unit-developed-for-data-storage/
- Memory & Storage timeline: https://www.computerhistory.org/timeline/memory-storage/

**Source type:** museum synthesis.

Use for UNISERVO/IBM 726 chronology, broad physical descriptions, and navigation into primary material.

### IBM magnetic-tape history

- IBM, “Magnetic tape”: https://www.ibm.com/history/magnetic-tape

**Source type:** corporate retrospective.

Use for vacuum-column engineering narrative, commercial chronology, and IBM product context.

**Caution:** colorful invention anecdotes should not substitute for engineering reports where exact priority or causality matters.

### IBM Data File Handbook

- IBM, *Data File Handbook*, Form C20-1638-1, March 1966: https://www.bitsavers.org/pdf/ibm/generalInfo/C20-1638-1_Data_File_Handbook_Mar66.pdf

**Source type:** period manufacturer technical documentation.

Use for tape speeds, densities, nominal interrecord gaps, and device-family characteristics.

### Logical records and physical blocks

- IBM, “Blocks and records”: https://www.ibm.com/docs/en/epfz/6.1.0?topic=characteristics-blocks-records

**Source type:** modern IBM documentation.

Use to explain the durable logical-record / physical-block abstraction and why blocking reduces interblock-gap and I/O overhead.

Do not project modern PL/I/JCL interfaces backward onto 1950s systems.

## Front-panel bootstrapping / PDP-8

### DEC Small Computer Handbook

- Digital Equipment Corporation, *digital Small Computer Handbook*, 1970: https://bitsavers.org/pdf/dec/pdp8/handbooks/SmallComputerHandbook_1970.pdf

**Source type:** manufacturer primary handbook.

Use for:

- manual memory entry from the operator console;
- RIM loader as a principal use of manual storage;
- loading paper tape after the seed loader exists.

### DEC Introduction to Programming

- DEC, *Introduction to Programming*, 1969: https://bitsavers.org/pdf/dec/pdp8/handbooks/IntroToProgramming1969.pdf

**Source type:** manufacturer primary instructional material.

Use for staged loader taxonomy: RIM, BIN, HELP, DECtape bootstrap.

### PDP-8 FORTRAN manual / exact RIM sequence

- DEC, *PDP-8 FORTRAN Programming Manual*: https://bitsavers.trailing-edge.com/www.computer.museum.uq.edu.au/pdf/DEC-08-AFAC-D%20PDP-8%20FORTRAN%20Programming%20Manual.pdf

**Source type:** manufacturer primary manual preserved by a Bitsavers mirror.

Use for the octal RIM listing and literal LOAD ADDRESS / DEPOSIT console procedure.

### Surviving PDP-8 hardware

- University of Iowa PDP-8 tour: https://homepage.cs.uiowa.edu/~dwjones/pdp8/UI-8/guide.shtml
- PDP-8/I front panel preservation page: https://www.pdp8online.com/pdp8i/pics/pdp8i_frontpanel.shtml

**Source type:** later preservation documentation.

Use for physical panel construction, lights/switches, and surviving printed RIM-loader references. Primary DEC manuals remain the technical authority.

## ASCII, CR/LF, and device controls

### RFC 20 / USASCII

- Vint Cerf, RFC 20, “ASCII format for Network Interchange,” 16 October 1969: https://www.rfc-editor.org/rfc/rfc20.html

**Source type:** contemporary network standard document reproducing the then-current USASCII table/definitions.

Use for:

- 7-bit ASCII in an 8-bit network byte;
- control-character names and semantics;
- CR, LF, BEL, BS, FF, DC1–DC4, ESC, DEL;
- DEL's perforated-tape rationale.

### RFC 318 / TELNET NVT

- Jon Postel, RFC 318, “Telnet Protocols,” April 1972: https://www.rfc-editor.org/rfc/rfc318.html

**Source type:** contemporary protocol specification.

Use for:

- Network Virtual Terminal;
- CR-LF network end-of-line convention;
- mapping between hosts with different local newline behavior;
- CR NUL distinction.

This is the key source for explaining why network newline semantics are a compatibility layer over heterogeneous terminal systems.

## EBCDIC / IBM byte-oriented compatibility

### Original System/360 architecture

- IBM, *System/360 Principles of Operation*, Form A22-6821-0: https://www.bitsavers.org/pdf/ibm/360/princOps/A22-6821-0_360PrincOps.pdf

**Source type:** original manufacturer architecture manual.

Use for 8-bit byte organization and System/360 architecture. Trace exact character-code statements to the relevant edition/page before making detailed claims about early EBCDIC revisions.

### Durable EBCDIC installed base

- IBM, “The EBCDIC character set”: https://www.ibm.com/docs/en/zos-basic-skills?topic=mainframe-ebcdic-character-set

**Source type:** modern IBM technical education/documentation.

Use for present-day byte values, collating-order differences, and IBM's explicit description of the installed-base cost of conversion.

Do not use a modern code page as a universal representation of every historical EBCDIC variant.

## Endianness

### Danny Cohen, 1980

- Danny Cohen, IEN 137, “On Holy Wars and a Plea for Peace,” 1 April 1980: https://www.ietf.org/ietf-ftp/rfc/ien/ien137.html

**Source type:** contemporary networking/architecture essay.

Use for Big-Endian/Little-Endian terminology and the interoperability framing.

### PDP-11

- DEC, *PDP-11 Conventions*, DEC-11-HR6A-D, September 1970: https://www.bitsavers.org/pdf/dec/pdp11/handbooks/DEC-11-HR6A-D_PDP-11_Conventions_197009.pdf
- DEC, *PDP-11/40 Processor Handbook*, 1972: https://bitsavers.org/pdf/dec/pdp11/handbooks/PDP-11_40_Processor_Handbook_1972.pdf

**Source type:** manufacturer primary documentation.

Use for low-order byte at the even/lower address and byte/word addressing behavior.

### IBM big-endian lineage

- IBM, *z/Architecture Principles of Operation*: https://www.ibm.com/docs/en/module_1678991624569/pdf/SA22-7832-14.pdf?cp=HW11W

**Source type:** modern descendant architecture manual.

It explicitly states that System/360, System/370, ESA/390, and z/Architecture use big-endian byte order.

Use original System/360 manuals/design papers when explaining *why* the 1964 architecture chose its layout; the descendant manual establishes persistence, not original intent.

### Internet canonical order

- Jon Postel, RFC 791, *Internet Protocol*, September 1981: https://www.rfc-editor.org/rfc/rfc791.html

**Source type:** Internet standard/specification.

Use for Appendix B's explicit rule that multi-octet numeric quantities transmit the most-significant octet first.

## Cross-source caution rules for this field set

1. **Do not infer a causal chain merely because two conventions share a number.** The 80-column card created a powerful installed base; it did not single-handedly determine every later terminal width.
2. **Do not call Williams storage passive RAM.** Regeneration is part of the mechanism.
3. **Do not equate streaming bandwidth with random-access latency.** Tape is a central counterexample.
4. **Do not say early machines lacked firmware in general.** The PDP-8 front-panel story is a concrete system/example, not a universal claim about all computers of the era.
5. **Do not collapse ASCII, an 8-bit byte, and EBCDIC into one standards story.** They interact historically but are distinct design/standardization threads.
6. **Do not treat EBCDIC as one timeless code table.** It has code-page/variant history.
7. **Do not describe endianness as a purely aesthetic preference.** The compatibility cost appears at byte-addressed memory and interchange boundaries.
8. **Do not infer historical intent from the experiments.** All six experiments isolate constraints with synthetic parameters unless explicitly sourced otherwise.
# Source Map — Strange Constraints Field Set

This research map records the main primary, archival, museum, and preservation sources used for the repository's second field set: mechanical carry, relay contact bounce, acoustic delay-line memory, magnetic-core memory, teleprinters, and CTSS.

It supplements [`source-ledger.md`](source-ledger.md). Article-level footnotes remain the authoritative map from claims to sources.

## Mechanical carry and the Pascaline

### Blaise Pascal, 1645 — primary inventor texts

- *Lettre Dédicatoire de la Machine Arithmétique*:
  https://fr.wikisource.org/wiki/%C5%92uvres_de_Blaise_Pascal/Lettre_D%C3%A9dicatoire_de_la_Machine_Arithm%C3%A9tique_et_Avis_n%C3%A9cessaire/Lettre
- *Avis nécessaire à ceux qui auront curiosité de voir la Machine Arithmétique, et de s'en servir*:
  https://fr.wikisource.org/wiki/%C5%92uvres_de_Blaise_Pascal/Lettre_D%C3%A9dicatoire_de_la_Machine_Arithm%C3%A9tique_et_Avis_n%C3%A9cessaire/Avis

Use for Pascal's own stated goals: relieving the operator of remembering carries and borrows, durability, transportability, ease of operation, and his defense of practical mechanical complexity against abstractly simpler proposals.

Source type: primary inventor description and promotion. Excellent for stated intent; not an independent performance evaluation.

### ACONIT / Inria Pascaline exhibit

https://aconit.inria.fr/omeka/exhibits/show/histoire-machines/prehistoire/pascaline.html

Use for surviving-machine explanation of the gravity-operated `sautoir`, staged carry transfer, wheel independence, and complement-based subtraction.

Source type: museum / institutional technical synthesis.

### Computer History Museum Babbage Engine exhibit

- Engines: https://www.computerhistory.org/babbage/engines/
- How it Works: https://www.computerhistory.org/babbage/howitworks/

Use for Babbage's consideration of multiple number bases, decimal choice, and the finite-difference transformation that reduces tabulation to repeated addition.

Source type: museum synthesis grounded in drawings, artifacts, and reconstruction work.

## Relay switching and contact bounce

### *Telephony III*, 1951 reissue

https://www.coxhill.com/trlhistory/media/Technical%20Training%20Publications/Telephony%203.%20%28reissued%29.%201951.pdf

Section 9.4 explicitly discusses contact bounce, difficult-to-trace circuit failures, shortened contact life, and mechanical damping strategies.

Source type: period technical-training material. Strong evidence that contact bounce was treated as an ordinary practical telephone-engineering problem.

### “Relays in the Bell System,” 1924

Bell Labs publication archive:
https://www.nokia.com/bell-labs/publications-and-media/publications/relays-in-the-bell-system/

Use for the industrial scale of relay switching in the Bell System and the engineering importance of relay speed and accuracy.

Source type: contemporary institutional technical publication.

### Later relay terminology and testing

- U.S. FDA, “Electronic Relays”:
  https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/electronic-relays
- U.S. Department of Defense, MIL-PRF-83536A, relay specification, NASA NEPP mirror:
  https://nepp.nasa.gov/docuploads/53ECF6EE-9BF8-40B5-A61D5C51B5A8FB3E/MIL-PRF-83536.pdf

Use only for stable later terminology and evidence that bounce remains a formal measured property. Do not project modern bounce thresholds or timing limits backward onto 1930s–1950s computing relays.

## Acoustic delay-line memory

### Computer History Museum

- Delay Lines, *Revolution*:
  https://www.computerhistory.org/revolution/memory-storage/8/309
- EDSAC delay-line storage, *The Storage Engine*:
  https://www.computerhistory.org/storageengine/edsac-computer-employs-delay-line-storage/
- 1949 EDSAC timeline entry:
  https://www.computerhistory.org/timeline/1949/

Use for radar lineage, acoustic pulse conversion/regeneration, serial access, EDSAC context, and the fact that information is available only when it reaches the access point.

Source type: museum synthesis.

### Smithsonian SEAC mercury delay-line object

https://americanhistory.si.edu/collections/search/object/nmah_334663

Use for physical construction: mercury-filled tubes, quartz transmitter/receiver crystals, and sound-wave information storage.

Source type: national museum object record.

### Museums Victoria — CSIRAC hot box

https://collections.museumsvictoria.com.au/items/385194

Use for evidence that CSIRAC's mercury delay lines were installed in a temperature-controlled enclosure.

Source type: museum object record.

### National Museum of Computing — EDSAC Replica Project

https://www.tnmoc.org/edsac

Use for reconstruction methodology: incomplete/as-evolved historical records and the replica project's substitution of magnetostrictive delay lines for original mercury tanks.

Source type: modern reconstruction project. Useful for reconstruction uncertainty and practical substitution, not a primary 1949 machine record.

## Magnetic-core memory

### Jay W. Forrester, 1951

- “Digital Information Storage in Three Dimensions Using Magnetic Cores,” *Journal of Applied Physics* 22(1), January 1951, pp. 44–48, DOI 10.1063/1.1699817.
- U.S. Patent 2,736,880, “Multicoordinate Digital Information Storage Device,” filed 11 May 1951:
  https://patents.google.com/patent/US2736880A/en

Use for the selection problem, nonlinear magnetic switching, coordinate wires, and coincident-current organization.

Source type: primary designer paper and patent. The patent documents claimed/intended architecture; it is not by itself a complete priority history.

### MIT Museum — Whirlwind core memory

https://mitmuseum.mit.edu/collections/object/2000.006.001

Use for Whirlwind object history and institutional context.

Source type: museum object record.

### Computer History Museum

- Magnetic Core Memory:
  https://www.computerhistory.org/revolution/memory-storage/8/253
- Whirlwind core-memory milestone:
  https://www.computerhistory.org/storageengine/whirlwind-computer-debuts-core-memory/

Use for broad core-memory chronology and manufacturing context.

Source type: museum synthesis.

### Smithsonian Whirlwind core plane

https://www.si.edu/object/mainframe-computer-component-whirlwind-magnetic-core-memory-plane%3Anmah_334413

Especially important for labor history. The object record describes early MIT laboratory assistants, largely women, threading cores and wires by hand, and records that a larger 64 × 64 plane could take up to two weeks to manufacture.

Source type: national museum object record tied to a preserved artifact.

### NASA-hosted memory technology survey

McDonnell Douglas Astronautics Company, *Memory Technology Survey*, Report MDC E2365, 13 February 1981:
https://ntrs.nasa.gov/api/citations/19830006682/downloads/19830006682.pdf

Use for later technical explanation of destructive core readout and restoration.

Source type: technical retrospective. Not a substitute for machine-specific 1950s core-memory circuit documentation.

## Teletypes, ASCII, paper tape, and low-speed terminals

### Teletype Corporation documentation

- 1965 Model 32/33/35 line brochure, Bitsavers preservation:
  https://bitsavers.org/communications/teletype/brochures/LINE35M10565_Teletype_Line_Brochure_1965.pdf
- 1969 equipment features/pricing documentation:
  https://www.navy-radio.com/manuals/tty/tty-equip-price-1969-04.pdf

Use for manufacturer-stated market positioning, 100-wpm operation, code family, equipment options, and 110-baud Model 33 configurations.

Source type: manufacturer primary material. Advertising claims should not be treated as neutral evaluations.

### DEC PDP-12 maintenance manual

Digital Equipment Corporation, *PDP-12 Maintenance Manual, Volume I*, November 1972:
https://deramp.com/downloads/mfe_archive/011-Digital%20Equipment%20Corporation/09%20PDP-12/01%20PDP-12%20Documentation/DEC-12-HR1B-D%20Maintenance%20Manual%20Vol%20I%20Nov72.pdf

Use for one documented computer integration of the Model 33 ASR, including ten-character-per-second maximum transfer and paper-tape reader/punch functions.

Source type: manufacturer technical manual.

### Bob Bemer / ASCII

R. W. Bemer, “The American Standard Code for Information Interchange,” preserved in the Computer History Museum Bemer papers:
https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-02-acc.pdf

Use for a contemporary participant account of ASCII as an interchange standard and its 1963 approval context.

Source type: participant technical account; valuable but not a neutral committee transcript.

### NIST ASCII history

NIST Special Publication 958, *A Century of Excellence in Measurements, Standards, and Technology*:
https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication958.pdf

Use for later institutional standards history and interoperability context.

Source type: institutional retrospective.

### Bell 103A data set

Bell System Practices, Section 591-014-100, *Data Set 103A Type: Identification and Operation*:
https://www.manualslib.com/manual/1847989/Bell-103a.html

Use for low-speed serial data over switched voice telephone infrastructure.

Source type: preserved manufacturer/service documentation; the current host is a secondary manual mirror.

## CTSS and interactive time-sharing

### 1962 experimental system paper

Fernando J. Corbató, Marjorie Merwin-Daggett, Robert C. Daley, et al., “An Experimental Time-Sharing System,” *Proceedings of the 1962 Spring Joint Computer Conference*, pp. 335–344, DOI 10.1145/1460833.1460871.

Use for the project's contemporary framing, implementation problems, and scheduling discussion.

Source type: project-authored contemporary conference paper.

### 1966 CTSS Programmer's Guide

MIT Computation Center, *The Compatible Time-Sharing System: A Programmer's Guide*, 1966 edition:
https://people.csail.mit.edu/saltzer/Multics/CTSS-Documents/CTSS_ProgrammersGuide_1966.pdf

Use for the distinction between hardware-utilization multiprogramming and concurrent effective use by several users, system goals, user environment, and background compatibility.

Source type: primary project manual.

### CTSS Technical Notes

Jerome H. Saltzer et al., MIT Project MAC Technical Report MAC-TR-16, March 1965:
https://web.mit.edu/saltzer/www/publications/TRs%2BTMs/Multics/TR-016.pdf

Use for timer interrupts, memory protection/relocation, disk/drum channels, 7750 communications, terminal character flow, supervisor buffers, and system organization.

Source type: primary/near-primary project technical documentation.

### CTSS text editing

Jerome H. Saltzer, “Manuscript Typing and Editing,” CTSS guide section AH.9.01:
https://web.mit.edu/saltzer/www/publications/ctss/AH.9.01.pdf

Use for line-oriented editing practice in a printing-terminal environment.

Source type: primary user documentation.

### MIT CSAIL CTSS preservation collection

https://www.csail.mit.edu/ctss-documents

The collection documents the preservation work behind many online CTSS scans. It credits the Multics History Project and in particular Roger Roach and Olin Sibert for major scanning work, with source material including Jerome Saltzer's files and Bitsavers.

Source type: institutional preservation history.

## Cross-field cautions

This field set repeatedly uses a modern engineering analogy to illuminate an old mechanism. Those analogies must remain explicitly labeled.

Examples:

- mechanical carry compared with ripple-carry dependency;
- core half-selection shown with normalized `0.5 + 0.5 = 1.0` values;
- delay-line average wait described with an ideal circular serial-store model;
- relay bounce handled with synthetic software-style qualification models;
- 110-baud output translated into modern wall-clock examples;
- time-sharing think-time modeled with a toy round-robin queue.

None of these models proves that historical designers used the same equations, thresholds, algorithms, or terminology.

Their role is narrower:

> make a documented constraint tangible without inventing historical intent.

# Acknowledgements

This project depends on generations of historians, archivists, curators, engineers, collectors, conservators, oral-history interviewers, librarians, volunteers, operators, programmers, technicians, production workers, standards participants, and people who kept apparently obsolete documents from being thrown away.

`computing-archaeology` is not an attempt to replace their work. It is possible only because that work exists.

## Institutions and collections currently used

### Computer History Museum (CHM)

CHM is a major foundation for the excavation set. The repository currently cites its material on:

- Charles Babbage's Difference and Analytical Engines;
- George Stibitz and Bell Labs computing;
- ENIAC and early electronic computers;
- EDSAC and acoustic delay-line memory;
- Williams–Kilburn tube memory;
- magnetic drums, magnetic tape, magnetic disks, and magnetic-core memory;
- Jay Forrester;
- IBM Project Stretch archival documents;
- PDP-1 documentation;
- CDC 6600 design material;
- Bob Bemer / ASCII archival material;
- MOS Technology / 6502 oral histories;
- KIM-1 object history;
- oral histories and early operating-system preservation.

Particular thanks are due to the people who preserve and make accessible the museum's **Timeline of Computer History**, **Revolution** exhibit, **The Storage Engine**, Babbage materials, oral-history program, Software Preservation Group, scanned manuals, photographs, and archival engineering documents.

https://computerhistory.org/

### Bitsavers and independent document preservation

https://bitsavers.org/

A large fraction of serious computing history remains recoverable because people scanned and organized manuals, schematics, program-library documents, listings, field-engineering material, brochures, standards-adjacent documentation, and training books long after their original manufacturers stopped distributing them.

This repository now relies on Bitsavers-preserved material including:

- IBM 650 and SOAP documentation;
- IBM 704 manuals;
- IBM System/360 Principles of Operation;
- IBM Data File Handbook;
- IBM 29 Card Punch documentation;
- PDP-8 handbooks and programming manuals;
- PDP-11 conventions, system manuals, UNIBUS handbooks, and peripheral handbooks;
- VT100 user and technical manuals;
- Teletype literature.

Special thanks are due to **Al Kossow** and the many contributors, collectors, donors, scanners, mirror maintainers, and document identifiers whose work made such material searchable rather than disposable.

Independent mirrors and enthusiast archives also matter. A manual preserved on a university, hobbyist, or specialist site may be the only public copy of a manufacturer document that once existed in thousands of service binders.

### Digital Equipment Corporation documentation and PDP preservation communities

DEC's surviving documentation is central to the repository's histories of:

- PDP-1 word architecture;
- PDP-8 front-panel operation and bootstrap loaders;
- paper-tape loading practice;
- PDP-11 byte addressing and little-endian organization;
- UNIBUS arbitration, DMA, interrupt practice, and peripheral integration;
- VT100 ANSI-mode terminal behavior and maintenance;
- minicomputer operator interfaces.

Later preservation communities make the manuals materially useful rather than merely bibliographic citations.

Particular thanks are due to the maintainers of **pdp8online.com**, the University of Iowa PDP-8 preservation project, PDP-11 documentation mirrors, terminal collectors, and people who preserved machines, front panels, paper tapes, diagnostic programs, bus cards, VT100 hardware, and DEC software documents.

The historical fact that a loader once had to be toggled in by hand — or that a disk controller could become bus master — is far easier to understand when the octal listing, console manual, bus handbook, and surviving hardware can still be compared.

### IBM History and surviving IBM documentation

IBM's historical pages and preserved primary manuals are currently used for:

- Hollerith and punched-card data processing;
- the 1928 80-column IBM card;
- keypunch and card-oriented workflows;
- punched-card sort, merge, compare, and collate operations;
- the IBM 650 and magnetic-drum computing;
- SOAP / optimal drum placement;
- the IBM 704's 36-bit organization;
- IBM 726/729-era magnetic-tape systems;
- vacuum-column tape engineering;
- the IBM 305 RAMAC and IBM 350 direct-access disk;
- IBM Project Stretch;
- EBCDIC and System/360 compatibility;
- the continuing cost of preserving long-lived data and code conventions.

Corporate histories are cited as institutional sources rather than treated as neutral final authorities. Surviving period manuals and engineering memos are preferred for technical claims.

https://www.ibm.com/history

### RAMAC restoration and disk-drive preservation

The history of early magnetic disk storage depends heavily on people who kept not just brochures but mechanisms, service manuals, access-arm diagrams, maintenance records, and restoration notes.

The **RAMAC Restoration** archive maintained by **Ed Thelen** and contributors provides a valuable map to IBM 305/350 manuals, customer-engineering documentation, access-mechanism reports, parts catalogs, photographs, and restoration experience.

https://www.ed-thelen.org/RAMAC/

Particular credit is due to restorers and document donors such as **Joe Feng**, **Tim Coslet**, and others identified in the archive. Their work makes it possible to move beyond “the first hard disk was huge” toward the real engineering problems of coating disks, holding head spacing, moving the actuator, diagnosing faults, and keeping a multi-refrigerator-sized storage system operational.

### RFC Editor / IETF archival infrastructure

The history of network text and byte order is unusually well served by a public paper trail.

The repository currently uses:

- RFC 20 for ASCII network interchange and control-character definitions;
- RFC 318 for TELNET's Network Virtual Terminal and CR-LF convention;
- RFC 791 for Internet Protocol byte-transmission order;
- IEN 137 for Danny Cohen's “On Holy Wars and a Plea for Peace.”

https://www.rfc-editor.org/

https://www.ietf.org/

Thanks are due not only to the original authors and working groups but also to the people who kept early RFCs and Internet Experiment Notes readable, searchable, and stably linked decades after the network that produced them changed beyond recognition.

### MIT, Project MAC, CTSS, and Multics preservation

MIT documentation supports the repository's Whirlwind/core-memory, CTSS/time-sharing, and Multics/computer-utility excavations.

The surviving CTSS manuals and technical notes make it possible to reconstruct details that disappear in broad summaries: timer interrupts, memory protection and relocation, terminal character buffering, IBM 7750 communication paths, secondary storage, and line-oriented editing.

Multics material extends the trail into segmentation, paging, dynamic linking, protection rings, persistent files, controlled sharing, and the explicit idea of computing as a utility available like telephone or power service.

The **Multics History Project** is especially important because it preserves both the project's early design aspirations and later implementation evidence — and repeatedly warns readers not to confuse the two.

https://multicians.org/

The MIT CSAIL CTSS preservation page records how much modern access depends on the Multics History Project, especially scanning by **Roger Roach** and **Olin Sibert**, with important material from **Jerome Saltzer's** files and Bitsavers.

https://www.csail.mit.edu/ctss-documents

That preservation chain deserves citation alongside the original authors. A PDF does not simply appear on the internet fifty years later.

### Smithsonian Institution / National Museum of American History

Smithsonian object records are used for physical evidence that textual histories can make too abstract:

- Whirlwind magnetic-core planes;
- hand-threaded core-memory construction;
- SEAC mercury delay-line hardware;
- archival technical documents such as the EDVAC *First Draft* through Smithsonian Libraries.

https://americanhistory.si.edu/

https://library.si.edu/digital-library

The Whirlwind core-plane record is especially important because it preserves manufacturing labor inside the object history: early core planes were threaded by laboratory assistants, largely women, and a dense plane could require sustained manual precision work.

### ACONIT / Inria

The ACONIT virtual computing museum hosted by Inria provides an unusually concrete technical explanation of the Pascaline, especially the `sautoir` carry mechanism and complement-based subtraction.

https://aconit.inria.fr/

This is a reminder that very early computing history survives not only through famous books but through object study, reconstruction, and museum interpretation.

### Museums Victoria

Museums Victoria's CSIRAC collection preserves the physical infrastructure around an early computer, including the temperature-controlled **hot box** used with mercury delay lines.

https://collections.museumsvictoria.com.au/

A memory technology becomes much easier to understand when the heater box is preserved alongside the logical diagram.

### University of Manchester / Digital60

The University of Manchester's preservation of the Manchester Baby, Mark I, Williams–Kilburn storage, original papers, technical recollections, and digitized documents makes it possible to discuss CRT memory from contemporary engineering evidence rather than folklore.

Tom Kilburn's 1947 report is especially valuable because the preserved transcription exposes the real design constraints: charge decay, regeneration, focus, screen quality, pickup signals, spot size, and capacity.

https://curation.cs.manchester.ac.uk/digital60/

Thanks are due both to the original Manchester computing teams and to the later historians, editors, computer-conservation volunteers, archivists, and university staff who kept their documentation accessible.

### University of Pennsylvania

Penn's ENIAC anniversary histories and institutional records help recover not only the machine's hardware but also its reliability engineering, programming practice, and the work of its programmers.

https://almanac.upenn.edu/

### The National Museum of Computing

TNMOC's Colossus collection and reconstruction work preserve a machine whose wartime secrecy could easily have left it as a thin legend rather than an inspectable engineering system.

The EDSAC Replica Project also documents reconstruction uncertainty and the practical substitutions required when a historical technology such as mercury delay-line storage cannot simply be copied without qualification.

https://www.tnmoc.org/

### Bell Labs / telephone-engineering archives

Computing repeatedly borrowed from telephone engineering: relays, switching practice, transmission infrastructure, modems, and maintenance knowledge.

Bell Labs' publication archive and surviving telephone training material make it possible to see that inheritance before it was renamed “computer technology.”

https://www.nokia.com/bell-labs/publications-and-media/

The repository also relies on preservation work by telecommunications historians who kept training publications such as *Telephony III* available, including its period discussion of contact bounce.

### Teletype, VT100, and communications-document preservation

Model 33 and VT100 history depends on surviving Teletype Corporation brochures, DEC user and maintenance manuals, Bell System data-set documentation, ANSI-era references, and the people who scanned and mirrored them.

Those records preserve the computer terminal as a machine rather than a retrospective icon: motors, paper, paper tape, serial rate, CRT electronics, keyboard scanning, setup state, cursor protocols, and service procedures all remain visible.

### Semiconductor oral-history preservation

The low-cost microprocessor story is difficult to reconstruct from datasheets alone.

The Computer History Museum's oral histories with **Chuck Peddle**, **Bill Mensch**, Motorola 6800 participants, and other semiconductor engineers preserve discussions of die-size targets, process development, yield, pricing, documentation, team movement between companies, and disagreements over credit.

These recollections are not neutral transcripts of the past. They are participant evidence recorded decades later. Their value increases when compared against contemporary advertisements, manuals, die photographs, company records, and other participants' testimony.

## People whose work appears in the excavation set

The current material builds on the work of historical engineers, programmers, operators, researchers, standards participants, and historians including, among many others:

- **Blaise Pascal** — arithmetic-machine design and a remarkably explicit 1645 defense of practical mechanical constraints;
- **Charles Babbage** — Difference and Analytical Engine designs;
- **Joseph Clement** — precision engineering and construction work for Difference Engine No. 1;
- **Ada Lovelace** — published notes on the Analytical Engine and its possible symbolic reach;
- **Herman Hollerith** — punched-card statistical data processing;
- IBM card designers, keypunch engineers, card-plant workers, sorters, verifiers, collator operators, and clerical workers who turned cardboard into information infrastructure;
- **George Stibitz** — relay calculation and remote computing demonstration;
- the generations of telephone relay engineers and maintainers whose switching knowledge made reliable electromechanical logic practical;
- **Tommy Flowers** and the Colossus teams — large-scale electronic switching informed by telecommunications engineering;
- **J. Presper Eckert**, **John Mauchly**, and the wider ENIAC/EDVAC teams — electronic computing, memory, and programming-system development;
- **John von Neumann** — the influential 1945 EDVAC report, understood in the context of the larger ENIAC/EDVAC design community;
- **Kathleen McNulty**, **Frances Bilas**, **Betty Jean Jennings**, **Ruth Lichterman**, **Marlyn Wescoff**, and **Betty Snyder** — ENIAC programming work joining mathematics, machine configuration, timing, debugging, and diagnosis;
- **Maurice Wilkes** and the EDSAC team — practical stored-program computing service and acoustic delay-line systems;
- **Frederic Williams**, **Tom Kilburn**, **Geoff Tootill**, and colleagues at Manchester — electrostatic CRT storage and the Manchester Baby;
- **Jay W. Forrester** and the Whirlwind team — coincident-current magnetic-core memory and real-time computing;
- the MIT laboratory assistants and production workers who physically threaded, wired, inspected, tested, and repaired magnetic-core arrays;
- IBM and Remington Rand tape engineers who turned magnetic recording into high-speed computer storage, including the mechanical work required to buffer reel inertia and protect fragile media;
- tape librarians, operators, mount crews, and data-processing workers whose work made “read the tape” a functioning institutional operation;
- **Reynold B. Johnson**, **Louis D. Stevens Jr.**, **William A. Goddard**, **R. Manning Hermes**, **Arthur J. Critchlow**, **John W. Haanstra**, and the wider IBM San Jose team — turning moving-head magnetic disk storage from laboratory possibility into the RAMAC product;
- disk manufacturing, coating, assembly, customer-engineering, field-service, and restoration workers whose labor made “random access” physically dependable;
- **Werner Buchholz** and the IBM Project Stretch team — word-length, byte, and architecture design work;
- **James E. Thornton**, **Seymour Cray**, and the CDC 6600 team — architecture shaped around scientific throughput, instruction packing, and floating-point precision;
- **Robert L. Patrick**, **Owen Mock**, the GM Research / North American Aviation teams, and later SHARE participants — early batch and operating-system practice;
- the programmers who developed **SOAP** and related IBM 650 tools, turning drum geometry into an assembler problem rather than permanent manual drudgery;
- **Fernando Corbató**, **Marjorie Merwin-Daggett**, **Robert Daley**, **Jerome Saltzer**, **Victor Vyssotsky**, **Robert Graham**, **Michael Schroeder**, and the wider MIT / Bell Labs / GE / Honeywell Multics community — time-sharing, computer-utility goals, segmentation, paging, protection, and shared persistent computing;
- DEC processor, UNIBUS, peripheral, and documentation teams who made a small computer into a platform that laboratories and third parties could physically extend;
- **Chuck Peddle**, **Bill Mensch**, **John Paivinen**, **Terry Holdt**, and the wider MOS Technology team — designing a microprocessor and manufacturing process around a deliberately low cost target;
- engineers, technicians, test workers, packaging workers, application engineers, and technical writers whose work turned a cheap die into a usable product;
- DEC VT100 engineers, firmware/software authors, service technicians, and manual writers who helped turn ANSI terminal control into an installed compatibility target;
- **Bob Bemer** and the larger standards community behind ASCII — character interchange as a compatibility problem rather than merely a code table;
- **Vint Cerf**, **Jon Postel**, and the early Network Working Group participants whose documents made terminal and byte interchange conventions explicit;
- **Danny Cohen** — for framing byte-order conflict as an interoperability problem and giving the Big-/Little-Endian dispute its enduring vocabulary;
- DEC engineers and technical writers whose handbooks documented front-panel loading, RIM/BIN loaders, PDP-11 byte addressing, and practical details later histories often compress into one sentence.

This list is not a claim that these systems were created by isolated individuals. Large computing projects and standards were collective engineering efforts involving many people whose names are less visible in popular histories.

## The people hidden behind “the machine ran”

Computing history is especially vulnerable to narratives that celebrate designers while erasing the labor that made systems work.

A phrase such as “the computer executed the job” can conceal an entire production system:

```text
keypunching
card checking and verification
card manufacturing and sorting
collator setup and exception handling
messenger work
media preparation
console operation
front-panel loading
tape mounting and labeling
tape-library work
disk alignment and maintenance
printer operation
fault diagnosis
preventive maintenance
component replacement
relay adjustment
core threading and inspection
bus configuration and termination
terminal service
output sorting
documentation
standards work
archive preservation
```

The same is true of hardware abstractions.

A box labeled `CORE MEMORY` can hide ferrite production, wire preparation, threading, termination, testing, repair, sense electronics, and the dexterity of the people assembling the planes.

A command labeled `READ TAPE` can hide a reel library, physical mounts, media labeling, vacuum-column transport, cleaning, error handling, and scheduled data-processing work.

A request labeled `GET RECORD` can hide rotating platters, an air-bearing head, actuator positioning, magnetic coating quality, customer-engineering adjustment, and software placement decisions.

A file labeled `SOURCE` can inherit assumptions from a physical card that someone had to keypunch, verify, transport, sort, merge, and recover if its deck order failed.

A box labeled `TERMINAL` can hide paper handling or CRT electronics, keyboard scanning, telephone/serial circuits, maintenance, code standards, and protocol state.

A line labeled `DMA` can hide arbitration, bus grant chains, electrical loading, termination, and a device temporarily taking control of the machine's shared interconnect.

Future additions should actively recover, where sources permit:

- operators;
- programmers;
- wiring and assembly workers;
- keypunch and verifier operators;
- sorter and collator operators;
- card-production workers;
- tape librarians and mount operators;
- disk technicians and field engineers;
- terminal technicians;
- bus/peripheral integrators;
- semiconductor fabrication, test, and packaging workers;
- technicians;
- maintenance staff;
- production workers;
- magnetic-core weavers and inspectors;
- relay adjusters;
- telephone and communications workers;
- clerical workers;
- documentation writers;
- standards participants;
- preservation scanners and cataloguers;
- users whose workflows shaped the machines.

Acknowledgement should not be ceremonial. Labor, maintenance, standards work, manufacturing, and institutional practice are part of the causal history of computing.

## Historians and preservation researchers

This project increasingly depends on historians who have challenged deceptively simple stories about “firsts” and isolated inventors.

The ENIAC/stored-program section in particular benefits from work by **Thomas Haigh, Mark Priestley, and Crispin Rope**, whose reconstruction of ENIAC programming and later modification demonstrates why machine logs, operating practices, and exact definitions matter.

The project should continue to deepen its use of scholarship from **IEEE Annals of the History of Computing**, the **Charles Babbage Institute**, museum research programs, university archives, standards archives, and scholarly monographs.

Preservation researchers deserve equal visibility. The work of scanning, cataloguing, identifying revisions, maintaining mirrors, transcribing old reports, restoring machines, recording oral histories, and documenting provenance is often what makes later historical argument possible.

## Validation-tool dependencies

Repository validation uses these pinned, MIT-licensed Python packages:

- [`markdown-it-py` 4.2.0](https://github.com/executablebooks/markdown-it-py) parses CommonMark and GFM tables for the internal-link checker;
- [`mdit-py-plugins` 0.6.1](https://github.com/executablebooks/mdit-py-plugins) supplies GFM-compatible footnote parsing;
- [`mdurl` 0.1.2](https://github.com/executablebooks/mdurl) is the URL-normalization dependency of `markdown-it-py`.

Their exact distribution hashes are recorded in [`tools/requirements.txt`](tools/requirements.txt). They are tooling dependencies, not historical sources.

## AI assistance

Initial repository architecture, research framing, source triage, experiments, and draft prose were produced with assistance from **ChatGPT (GPT-5.6 Sol), OpenAI**, at the direction of the repository owner.

AI assistance is acknowledged here for transparency, not treated as historical authority. Historical claims remain answerable to the cited evidence, and engineering models remain labeled as reconstructions rather than proof of historical intent.

## Thank you

If you digitized an old manual, catalogued a machine, recorded an oral history, preserved a box of engineering memos, restored an obsolete computer, scanned a punched card, threaded a core plane, mounted a tape reel, aligned an early disk mechanism, toggled a loader into a front panel, adjusted a relay, terminated a bus, repaired a terminal, maintained a mirror after the original site disappeared, transcribed a fading technical report, interviewed an operator, or wrote careful scholarship about a system nobody thought anyone would care about fifty years later:

**this project is able to ask better questions because you kept the evidence alive.**

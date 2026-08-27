# Acknowledgements

This project depends on generations of historians, archivists, curators, engineers, collectors, conservators, oral-history interviewers, librarians, volunteers, operators, programmers, technicians, and production workers who preserved machines and the paper trails around them.

`computing-archaeology` is not an attempt to replace their work. It is possible only because that work exists.

## Institutions and collections currently used

### Computer History Museum (CHM)

CHM is a major foundation for the excavation set. The repository currently cites its material on:

- Charles Babbage's Difference and Analytical Engines;
- George Stibitz and Bell Labs computing;
- ENIAC and early electronic computers;
- EDSAC and delay-line memory;
- Williams–Kilburn tube memory;
- magnetic drums and magnetic-core memory;
- Jay Forrester;
- IBM Project Stretch archival documents;
- PDP-1 documentation;
- CDC 6600 design material;
- oral histories and early operating-system preservation.

Particular thanks are due to the people who preserve and make accessible the museum's **Timeline of Computer History**, **Revolution** exhibit, **The Storage Engine**, Babbage materials, oral-history program, Software Preservation Group, scanned manuals, photographs, and archival engineering documents.

https://computerhistory.org/

### Bitsavers and independent document preservation

https://bitsavers.org/

A large fraction of serious computing history remains recoverable because people scanned and organized manuals, schematics, program-library documents, listings, field-engineering material, brochures, and training books long after their original manufacturers stopped distributing them.

This repository currently relies on Bitsavers-preserved IBM 650 and IBM 704 documentation and uses the collection as a map toward many future primary sources.

Special thanks are due to **Al Kossow** and the many contributors, collectors, donors, and scanners whose work made such material searchable rather than disposable.

### IBM History and surviving IBM documentation

IBM's historical pages and preserved primary manuals are currently used for:

- Hollerith and punched-card data processing;
- the IBM punched-card ecosystem;
- the IBM 650 and magnetic-drum computing;
- SOAP / optimal drum placement;
- the IBM 704's 36-bit organization;
- IBM Project Stretch;
- System/360 and the consolidation of byte-oriented compatibility.

Corporate histories are cited as institutional sources rather than treated as neutral final authorities. Surviving period manuals and engineering memos are preferred for technical claims.

https://www.ibm.com/history

### University of Manchester / Digital60

The University of Manchester's preservation of Manchester Baby, Mark I, Williams–Kilburn storage, original papers, technical recollections, and digitized documents makes it possible to discuss the stored-program transition without reducing it to a slogan.

https://curation.cs.manchester.ac.uk/digital60/

Thanks are due both to the original Manchester computing teams and to the later historians, computer-conservation volunteers, archivists, and university staff who kept their documentation accessible.

### University of Pennsylvania

Penn's ENIAC anniversary histories and institutional records help recover not only the machine's hardware but also its reliability engineering, programming practice, and the work of its programmers.

https://almanac.upenn.edu/

### The National Museum of Computing

TNMOC's Colossus collection and reconstruction work preserve a machine whose wartime secrecy could easily have left it as a thin legend rather than an inspectable engineering system.

https://www.tnmoc.org/

The repository is especially grateful for material connecting Colossus to British telecommunications engineering and practical valve experience.

### Smithsonian Libraries

The Smithsonian's digitization of historical technical works, including John von Neumann's *First Draft of a Report on the EDVAC*, provides stable public access to documents too often encountered only through quotations in later textbooks.

https://library.si.edu/digital-library

## People whose work appears in the excavation set

The current material builds on the work of historical engineers, programmers, operators, researchers, and historians including, among many others:

- **Charles Babbage** — Difference and Analytical Engine designs;
- **Joseph Clement** — precision engineering and construction work for Difference Engine No. 1;
- **Ada Lovelace** — published notes on the Analytical Engine and its possible symbolic reach;
- **Herman Hollerith** — punched-card statistical data processing;
- **George Stibitz** — relay calculation and remote computing demonstration;
- **Tommy Flowers** and the Colossus teams — large-scale electronic switching informed by telecommunications engineering;
- **J. Presper Eckert**, **John Mauchly**, and the wider ENIAC/EDVAC teams — electronic computing, memory, and programming-system development;
- **John von Neumann** — the influential 1945 EDVAC report, understood in the context of the larger ENIAC/EDVAC design community;
- **Kathleen McNulty**, **Frances Bilas**, **Betty Jean Jennings**, **Ruth Lichterman**, **Marlyn Wescoff**, and **Betty Snyder** — ENIAC programming work that joined mathematics, machine configuration, timing, debugging, and diagnosis;
- **Maurice Wilkes** and the EDSAC team — practical stored-program computing service and delay-line systems;
- **Frederic Williams**, **Tom Kilburn**, and colleagues at Manchester — Williams–Kilburn storage and the Manchester Baby;
- **Jay W. Forrester** and the Whirlwind team — practical magnetic-core memory and real-time computing;
- **Werner Buchholz** and the IBM Project Stretch team — word-length, byte, and architecture design work;
- **James E. Thornton**, **Seymour Cray**, and the CDC 6600 team — architecture shaped around scientific throughput, instruction packing, and floating-point precision;
- **Robert L. Patrick**, **Owen Mock**, the GM Research / North American Aviation teams, and later SHARE participants — early batch and operating-system practice;
- the programmers who developed **SOAP** and related IBM 650 tools, turning drum geometry into an assembler problem rather than permanent manual drudgery.

This list is not a claim that these systems were created by isolated individuals. Large computing projects were collective engineering efforts involving many people whose names are less visible in popular histories.

## The people hidden behind “the machine ran”

Computing history is especially vulnerable to narratives that celebrate designers while erasing the labor that made systems work.

A phrase such as “the computer executed the job” can conceal an entire production system:

```text
keypunching
card checking
messenger work
media preparation
console operation
tape mounting
printer operation
fault diagnosis
preventive maintenance
component replacement
output sorting
documentation
```

The batch-processing material in this repository makes that particularly obvious. Keeping a mainframe busy could require card-to-tape operators, mainframe operators, tape-to-print operators, messengers, programmers, and standardized procedures working as one pipeline.

Future additions should actively recover, where sources permit:

- operators;
- programmers;
- wiring and assembly workers;
- keypunch operators;
- technicians;
- maintenance staff;
- production workers;
- magnetic-core weavers and inspectors;
- clerical workers;
- documentation writers;
- standards participants;
- users whose workflows shaped the machines.

Acknowledgement should not be ceremonial. Labor, maintenance, and institutional practice are part of the causal history of computing.

## Historians and preservation researchers

This project increasingly depends on historians who have challenged deceptively simple stories about “firsts” and isolated inventors.

The ENIAC/stored-program section in particular benefits from work by **Thomas Haigh, Mark Priestley, and Crispin Rope**, whose reconstruction of ENIAC programming and later modification demonstrates why machine logs, operating practices, and exact definitions matter.

The project should continue to deepen its use of scholarship from **IEEE Annals of the History of Computing**, the **Charles Babbage Institute**, museum research programs, university archives, and scholarly monographs.

## AI assistance

Initial repository architecture, research framing, source triage, experiments, and draft prose were produced with assistance from **ChatGPT (GPT-5.6 Sol), OpenAI**, at the direction of the repository owner.

AI assistance is acknowledged here for transparency, not treated as historical authority. Historical claims remain answerable to the cited evidence, and engineering models remain labeled as reconstructions rather than proof of historical intent.

## Thank you

If you digitized an old manual, catalogued a machine, recorded an oral history, preserved a box of engineering memos, restored an obsolete computer, scanned a punched card, maintained a mirror after the original site disappeared, interviewed an operator, or wrote careful scholarship about a system nobody thought anyone would care about fifty years later:

**this project is able to ask better questions because you kept the evidence alive.**

# GosFAP: why a software fund was not yet a software ecosystem

**Scope:** Soviet State Fund of Algorithms and Programs (Государственный фонд алгоритмов и программ, ГосФАП), institutional design in 1975–1980, subsequent assessments, and the engineering economics of reuse. First-pass case study, 2026-11-25.

## Historical question

When many computing organizations independently solve similar problems, why is it not sufficient to collect their programs and distribute them to other organizations? Which additional services make a program reusable outside its originating installation?

The contemporary problem was improving the use of computers and avoiding duplicated software development, not inventing GitHub. Asianometry's November 2026 video prompted this excavation; its title is a modern analogy, not a historical classification.[^video]

## 1. Historical record

### A federated fund with central discovery

A 1979 decision of the USSR State Committee for Science and Technology (GKNT), No. 581, dated 10 December, explicitly refers back to decisions No. 28 (21 February 1966), No. 443 (10 October 1969), and No. 258 (5 June 1975). The last established the network of specialized, departmental and territorial funds. The 1979 decision introduced revised regulations effective 1 March 1980. It reported funds operating in a number of union republics and more than 80 ministries and agencies; this is an official claim of institutional coverage, not a count of successfully reused programs.[^regulation]

The architecture was not one central executable-code store. A central information fund at VNTITsentr coordinated discovery; specialized, ministerial and republican collections held program materials. The latter were subdivided into program and information holdings. A central entry could therefore describe a program without providing an executable copy directly. See regulation §§7–17.[^regulation]

### The rules already recognized software maintenance

The 1979 rules went beyond cataloguing. The following is an analytical map of the obligations in the regulation, not an assertion that all were fulfilled:

| Layer | Intended mechanism |
| --- | --- |
| Discovery | Central records and the *Algorithms and Programs* bulletin (§19) |
| Acceptance | Expert appraisal and classification (§20) |
| Distribution | Copies on machine-readable media; accompanying documents (§21) |
| Adoption | Training, installation and control examples (§21) |
| Resource allocation | Service tariffs and planned fund-maintenance activity (§§22, 30–33) |
| Maintenance | Original holder responsible for corrections and notification (§28) |

The rules also differentiated compulsory submissions under specified plans and assignments from other work (§23), and deposit from service charges (§§22, 25). §27 treated qualifying registered algorithms as published work for the specified academic qualification rules. §21 restricted onward duplication by recipients. These features caution against describing GosFAP as either a voluntary open-source community or an indiscriminate national source-code dump.[^regulation]

### Evidence of problems, and limits of that evidence

Kratov and Sokolova's SoRuCom-2017 conference paper retrospectively describes low circulation and quality problems alongside organizational and economic shortcomings. It dates cessation to the early 1990s and discusses the Siberian Branch of the Russian Academy of Sciences' renewed fund initiative in 2008, including a web catalogue and corporate software repository.[^sorucom]

S. E. Goodman's near-contemporary 1978 study of Soviet software identifies hardware availability, resource priorities, institutions and foreign technology transfer as relevant analytical dimensions; it is a useful corrective to single-cause narratives. The publisher's public abstract and bibliographic entry were consulted here, not the complete chapter.[^goodman]

The historical record in this first treatment establishes the institutional design and a retrospective diagnosis. It does not establish a national reuse rate, the relative causal weights of hardware and institutional constraints, or uniform failure across all funds. A surviving registered program is evidence of registration, not of adoption; conversely, an aggregate criticism does not disprove useful local libraries.

## 2. Engineering reconstruction

The following is a modern analytical reconstruction rather than attributed Soviet testimony.

### Software is a dependency-bearing artifact

A program's transfer crosses several interfaces: instruction set, numerical representation, operating environment, language implementation, file format, input/output conventions, and application-domain assumptions. A source listing may preserve an algorithm while omitting the exact implementation environment. A binary may preserve an implementation while preventing useful modification. Even installations using the same machine family may differ in peripherals, operating-system revisions or data conventions.

The economically relevant unit is not a deposited program but a **successful installation that replaces otherwise necessary work**.

For a receiving installation, reuse is attractive when:

`C_search + C_acquire + C_port + C_validate + C_integrate + C_support < C_reimplement`

All terms refer to the receiving organization's expected effort for equivalent functionality over a comparable service horizon. For a producing organization, documenting, packaging and maintaining transferable software may impose additional effort whose benefit appears elsewhere. A fund can lower these costs through documentation, specialist assistance and standardization, but its existence does not guarantee that those services are delivered or that costs are credited to the actors who bear them.

### Three different objects of preservation

- **Catalogue:** identity, description, location and access conditions.
- **Transferable artifact:** executable or source, dependencies, media, installation instructions, test inputs and expected outputs.
- **Living service:** responsibility, defect feedback, version identification, correction distribution and actual users.

A catalogue can be useful without being a complete artifact repository. A complete deposit can still be unusable in another environment. A working installation can still become unsupported.

The failure mechanism to investigate is the gap between those layers, not a presumption that state coordination or centralization by itself necessarily fails.

### Comparison without anachronism

| Question | GosFAP regulations | Modern collaborative development (idealized) |
| --- | --- | --- |
| What is indexed? | Programs, documents and descriptions across funds | Repositories, releases and related metadata |
| How is a copy obtained? | Institutional request and media transfer | Network retrieval |
| How are changes conveyed? | Original-holder corrections and notifications | Version histories, releases, issues and pull requests |
| How is usability assessed? | Expert appraisal and installation support prescribed | Tests, reproducible builds, CI and user reports where maintained |
| What permissions apply? | Specified institutional distribution rights | Project-specific licenses and access controls |

GitHub is not itself a guarantee of any of the modern practices in the right-hand column. Nor was GosFAP a predecessor in a demonstrated technical genealogy of Git. The comparison isolates comparable engineering functions under different material and institutional conditions.

## 3. Synthetic paper experiment

No empirical parameters or executable reconstruction are claimed. Consider three hypothetical receiving sites, all offered one catalogued numerical program. Let local reimplementation cost 100 labor units at each site, with all units invented for illustration.

| Site | Find/acquire | Port | Validate/integrate | Support | Reuse total | Local decision |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Compatible | 10 | 10 | 20 | 10 | 50 | Reuse |
| Different runtime | 10 | 45 | 30 | 20 | 105 | Reimplement |
| Missing environment | 10 | 70 | 35 | 20 | 135 | Reimplement |

One deposited artifact, three potential recipients, only one economical reuse in this toy model. If a shared compatibility and test service cuts porting and validation costs by 40 units at the latter two sites, all three become economical reuse candidates (50, 65, 95). The model deliberately excludes the fixed cost of providing that service: a system-level investment decision must account for it, and for future maintenance. This is not a historical GosFAP estimate or proof of its failure.

## 4. Research backlog

- Retrieve the full 1966, 1969 and 1975 decisions; identify exactly how organization, eligibility and reporting changed.
- Locate original *Алгоритмы и программы* bulletins, registration cards and machine-readable deposits; follow at least one entry into a recipient installation.
- Find original adoption records, reported savings, rejection logs, maintenance budgets and update correspondence. Separate copies distributed from verified operational installations.
- Trace the video’s anecdote about multiple Minsk-22 implementations of a structural-calculation algorithm to an identifiable period report before quoting its numbers. It remains unverified in this study.
- Compare a specific machine family and toolchain with a successful period program library; test whether compatibility, documentation, staffing or access explains differences in adoption.
- Read the complete Goodman chapter and locate the late-Soviet assessment quoted in the 2017 conference paper. Do not infer the exact national scale of failure from the retrospective alone.

## Sources and evidence boundaries

[^regulation]: USSR State Committee for Science and Technology, Resolution No. 581, 10 December 1979, *О повышении эффективности функционирования и использования Государственного фонда алгоритмов и программ*, including attached regulations effective 1 March 1980. [Digital legal-text reproduction](https://meganorm.ru/mega_doc/dop_norm/41/gost_r_51189-98_gosudarstvennyy_standart_rossiyskoy/0/postanovlenie_gknt_sssr_ot_10_12_1979_N_581_o_povyshenii.html). Primary normative text via a secondary host, not an archival scan; establishes prescriptions rather than compliance. Earlier resolutions are cited within this document but not independently inspected.
[^sorucom]: S. V. Kratov and O. D. Sokolova, *Фонды алгоритмов и программ: история и перспективы*, SoRuCom-2017 conference proceedings, [Virtual Computer Museum reproduction](https://computer-museum.ru/articles/materialy-mezhdunarodnoy-konferentsii-sorucom-2017/1853/). Retrospective institutional account; particularly useful for the 2008 initiative, but not independent measurement of the Soviet system's outcomes.
[^goodman]: S. E. Goodman, *Software in the Soviet Union: Progress and Problems*, Advances in Computers, vol. 18 (1978), [publisher entry](https://www.sciencedirect.com/science/article/abs/pii/S0065245808605859). Abstract-level contextual evidence only in this pass.
[^video]: Asianometry, *Why the Soviet GitHub Failed*, November 2026, [original video](https://www.youtube.com/watch?v=CIFWlxQrl88). Research lead, not primary historical evidence; no full transcript independently verified in this pass.

Related repository themes: [architecture and compatibility](../../docs/architecture/), [standards](../../docs/standards/), and [the constraint-first method](../../docs/methodology/constraint-first-history.md).

AI-assisted research and drafting: ChatGPT (OpenAI), 2026-11-25.

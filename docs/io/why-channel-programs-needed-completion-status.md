# Why a channel program needed two kinds of completion

**Scope:** IBM System/360 channel-command chaining, channel end versus device end, and recovery status. This is a bounded first treatment, not a history of all mainframe I/O or HASP.

## Research question

How could a CPU launch several device operations with one `START I/O` without confusing the completion of data transfer, the completion of physical device work, and a failed or partially transferred operation?

## Historical record

The IBM *System/360 Principles of Operation*, GA22-6821-8 (November 1970), describes `START I/O`, channel address words (CAWs), channel command words (CCWs), command chaining and data chaining, and the channel status word (CSW). See the **Input/Output Operations** chapter, especially the CCW, chaining, status and CSW sections (printed pp. 99–121). [Archived primary manual](https://vtda.org/docs/computing/IBM/Mainframe/Hardware/System/GA22-6821-8_System360PrinciplesOperation_Nov70.pdf).

A CCW contains a command code, data address, flags and count. **Data chaining** continues a single device operation with another storage area; **command chaining** starts a further device command, conditional on completion/status. The channel may fetch the next CCW without asking the CPU to issue a new `START I/O`. The manual distinguishes **channel end** (the channel-facing transfer phase is complete) from **device end** (the device's operation is complete). These can be reported separately; they must not be collapsed into a single generic 'done'. Unusual conditions can suppress chaining. The CSW reports channel/unit status, a command address and residual count.

An independent period operations source, IBM *Disk Operating System Operating Guide*, C24-5022-8 (November 1969), instructs operators/programmers to inspect the CAW at hex 48 and the CSW at hex 40 when analyzing I/O commands. Its diagnostic procedure explicitly uses the CSW's command address, status bits and residual byte count to distinguish wrong-length records, rejected commands and transfer/data-check failures. [Archived primary guide](https://bitsavers.trailing-edge.com/pdf/ibm/360/dos/C24-5022-8_Disk_Operating_System_Operating_Guide_Release_21_Nov1969.pdf), section **How to Analyze Input/Output Commands**.

These are **two period documents**, not interchangeable versions of a single implementation: the 1970 architecture manual defines the interface; the 1969 DOS operating guide documents a practical diagnostic workflow.

## Engineering reconstruction (not a claim of recorded design intent)

A disk or tape mechanism may continue a mechanical action after the channel no longer needs the data path. A channel program must also know whether a data buffer was fully consumed, whether the device rejected a command, and whether a subsequent command is safe to issue. If every transition returned to the CPU, interrupt and dispatch overhead would accumulate; if the channel blindly proceeded, errors and physical completion boundaries would be lost.

The architecture therefore separates: (1) **the CPU's initiation**; (2) **channel execution of descriptors**; (3) **device/control-unit completion**; and (4) **status returned for software recovery**. The CCW chain is not merely a list of DMA buffers: data chaining and command chaining have different meanings, and exceptional status changes control flow.

This design was reasonable when peripherals had different timing, physical motion and failure modes, while expensive CPU cycles should remain available for computation.

## Operations and maintenance labor

The DOS guide is evidence that troubleshooting required reading low-memory control words and interpreting residual counts. 'I/O failed' was not enough: personnel had to distinguish device status, channel status and partial transfer, then decide how to recover or rerun work. This is a concrete diagnostic interface, not an assertion that all sites used the same procedures.

## Modern comparison, not identity

Modern descriptor rings, scatter/gather DMA and completion queues similarly separate CPU submission, device execution and completion status. Their protocol and memory-consistency semantics differ; System/360 CCWs must not be described as an implementation of modern NVMe or PCIe queues.

## What is not established

- These manuals do not establish the first invention of channel programming or the exact microarchitecture of every System/360 model.
- They do not give observed installation-wide throughput or interruption costs.
- A channel-end event alone must not be interpreted as successful physical completion.
- The cited 1969 DOS guide does not establish that every OS/360 or HASP operator used identical recovery procedures.
- A complete command-specific account requires the relevant control-unit/device manual; CCW modifier meanings and sense data can be device-specific.

## Bounded experiment brief (proposed, not implemented)

`experiments/channel-completion-boundaries/`: Python standard library, deterministic event trace only. Input: two synthetic CCWs (one data-chain transition, one command-chain transition), device-transfer end, delayed device end, and one injected unit-check or residual-count mismatch. Output: ordered CPU/channel/device events, whether the next CCW may start, and synthetic status/residual count. Stop after the fixed trace and failure variant; no wall-clock waiting, hardware emulation or unbounded queue. The experiment illustrates why **transfer completion, device completion and error status are distinct**. It cannot prove IBM timing, actual status-bit encodings, historical throughput, or designer intent.

## Related bridge

This is a narrower continuation of the repository's missing **Field Set D — I/O becomes infrastructure**. It can later link to selector/multiplexor subchannel state and HASP checkpoint/restart, but neither is necessary to establish the present claim.

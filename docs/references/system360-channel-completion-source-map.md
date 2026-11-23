# System/360 channel completion and recovery — source map

| Source | Type/date | Precise locator | Supports | Limits |
| --- | --- | --- | --- | --- |
| [IBM *System/360 Principles of Operation*, GA22-6821-8](https://vtda.org/docs/computing/IBM/Mainframe/Hardware/System/GA22-6821-8_System360PrinciplesOperation_Nov70.pdf) | IBM architecture manual, November 1970 | Input/Output Operations, printed pp. 99–121: CAW, CCW, data/command chaining, unit/channel status, CSW | CPU/channel/device boundaries, conditional chaining, separate channel-end/device-end, residual count | Architecture-level contract; not measured performance or a specific model's implementation |
| [IBM *DOS Operating Guide*, C24-5022-8](https://bitsavers.trailing-edge.com/pdf/ibm/360/dos/C24-5022-8_Disk_Operating_System_Operating_Guide_Release_21_Nov1969.pdf) | IBM operations manual, November 1969 | “How to Analyze Input/Output Commands” | CAW hex 48, CSW hex 40, status and residual-count diagnostics | DOS-specific procedures, not all installations or all OS/360 variants |

**Evidence classes:** The table is historical record. CPU-overhead and failure-boundary reasoning in the companion article is engineering reconstruction. The proposed trace is an experiment brief, not a historical replica.

**Verification caution:** Printed-page locators in the architecture manual are chapter/page references; confirm PDF image page offsets when creating exact page anchors. Do not equate the 1969 DOS guide with the November 1970 architecture revision.

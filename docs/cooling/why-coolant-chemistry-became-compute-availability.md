# Why Coolant Chemistry Became Compute Availability

Once liquid enters the rack, cooling performance depends on more than flow and inlet temperature.

## Historical record

OCP's cold-plate requirements describe the CDU as a system of pumps, heat exchangers, reservoirs, valves, controls, and sensors, and explicitly require material compatibility with the cooling liquid. OCP maintains coolant-fluid workstreams for water-based, glycol-based, and two-phase fluids.[^requirements][^workstream]

## Engineering reconstruction

Coolant is an operating material. Its long-term state can affect:

- corrosion;
- galvanic compatibility;
- conductivity;
- biological growth;
- inhibitor depletion;
- deposits;
- filter loading;
- pump/seal life;
- sensor accuracy;
- heat-transfer performance.

A rack can have adequate nominal flow yet lose availability through chemistry drift or contamination.

## Speed connection

Higher sustained compute requires higher sustained heat removal. Thermal throttling converts coolant condition directly into lower useful throughput.

## Experiment

`experiments/coolant-chemistry-window/coolant_chemistry_window.py` combines synthetic corrosion, conductivity, fouling, and heat-transfer proxies into an operating window.

[^requirements]: Open Compute Project, “ACS Liquid Cooling Cold Plate Requirements Document,” https://www.opencompute.org/documents/ocp-acs-liquid-cooling-cold-plate-requirements-pdf
[^workstream]: Open Compute Project, Cold Plate workstream, https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate

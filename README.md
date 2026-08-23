# F117 | Agentic Digital Twin Engineer | L3 Gold Standard | v1.0

A governed five-agent reference architecture for digital-twin engineering across system scoping, physical-to-digital data mapping, model development, calibration, validation, uncertainty analysis, synchronization, cybersecurity, configuration traceability, and qualified human engineering review.

F117 is engineering-support only. It can organize evidence, assumptions, models, validation results, uncertainty, and engineering recommendations, but it cannot autonomously deploy a model into operational control, connect to a live-control loop, change operating limits or control setpoints, certify validation, or override safety interlocks.

## Digital twin lifecycle

```text
Physical System and Use Case
        -> Twin Scope
        -> Data and Signal Mapping
        -> Model Architecture
        -> Calibration
        -> Validation
        -> Uncertainty Assessment
        -> Synchronization and Configuration Review
        -> Cybersecurity Review
        -> Qualified Human Engineering Approval
```

The workflow is fail closed. Data-quality gaps, synchronization failures, calibration deficiencies, incomplete validation, excessive uncertainty, unsafe control coupling, cybersecurity risk, incomplete traceability, or missing qualified approval prevent release.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Scope Agent | Defines physical system, twin purpose, boundaries, fidelity, users, operating envelope, and decision context | What exactly is the twin intended to represent and support? |
| Data Mapping Agent | Maps physical signals, data sources, semantics, timing, quality, transformations, and interfaces | Is the digital representation connected to trustworthy and interpretable physical evidence? |
| Modeling Agent | Develops model structure, assumptions, parameters, calibration logic, and model registry entries | Does the model represent the intended physical behavior within its stated scope? |
| Validation Agent | Tests the twin against independent evidence, acceptance criteria, scenarios, and operating regimes | Has the twin been validated for the intended use rather than merely fitted to data? |
| Uncertainty Agent | Characterizes uncertainty, extrapolation risk, sensitivity, synchronization limits, and decision boundaries | How much confidence should engineers place in the twin's outputs? |

The agents support engineering analysis. They do not replace qualified domain engineers, controls engineers, safety engineers, cybersecurity specialists, operators, validation authorities, equipment owners, or certification bodies.

## Repository structure

```text
AGENTS/
├── scope_agent.py
├── data_mapping_agent.py
├── modeling_agent.py
├── validation_agent.py
└── uncertainty_agent.py

SKILLS/
├── scope_reasoning.py
├── data_reasoning.py
├── model_reasoning.py
├── validation_reasoning.py
└── uncertainty_reasoning.py

TOOLS/
├── assumption_register.py
├── model_registry.py
├── signal_registry.py
├── validation_table.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates model reasoning from deterministic registries, validation records, governance gates, state, observability, and evaluation.

## Twin scope

The safety policy requires `twin_scope_reviewed`.

A digital twin should begin with an explicit purpose and system boundary. Scope can include:

```text
physical_asset_or_process
intended_use
users
decisions_supported
spatial_boundary
temporal_boundary
operating_envelope
fidelity_requirement
update_frequency
latency_requirement
inputs
outputs
excluded_behaviors
safety_significance
control_relationship
```

A model that is adequate for visualization may be inadequate for prediction, optimization, fault diagnosis, or control support. F117 should therefore preserve the intended use rather than treating every model as a universal twin.

## Digital twin versus simulation

A simulation model and a digital twin can share mathematical structure, but a digital twin generally requires a governed relationship to a physical system, including identity, data mapping, configuration, and lifecycle synchronization.

F117 should distinguish among:

```text
offline simulation
digital model
digital shadow
digital twin
control model
```

The label should not imply live synchronization or control authority when those capabilities are absent.

## Physical-to-digital identity

The digital representation should be traceable to the physical asset, process, subsystem, or fleet it represents.

Identity can include:

- asset identifier
- serial number
- model or product revision
- software or firmware version
- configuration
- installed components
- location
- commissioning state
- maintenance state
- calibration state

A twin should not silently inherit data or parameters from a different physical configuration.

## Data mapping

`SKILLS/data_reasoning.py` and `TOOLS/signal_registry.py` support physical-to-digital mapping.

A signal record can include:

```text
signal_id
physical_quantity
source_sensor
asset_id
units
coordinate_frame
sampling_rate
timestamp_source
latency
transformation
quality_state
calibration_reference
model_variable
version
```

The policy requires `data_mapping_reviewed`.

`data_quality_gap` blocks release when source-data quality or mapping remains unresolved.

## Semantic mapping

Correct values with incorrect semantics can still produce an invalid twin.

Mapping review should consider:

- units
- sign conventions
- coordinate frames
- reference points
- scaling
- engineering units
- sensor location
- naming
- timestamps
- aggregation windows
- interpolation
- missing-value treatment

F117 should not infer semantics merely from a variable name when metadata is incomplete.

## Time synchronization

A digital twin can depend on consistent timing across sensors, models, events, and control systems.

Synchronization review can consider:

- clock source
- timestamp accuracy
- time zone
- drift
- network delay
- buffering
- out-of-order data
- sample alignment
- event sequencing
- model update rate

`synchronization_gap` blocks release when physical-to-digital synchronization is materially unreliable.

## Data quality

Source data should be reviewed for fitness for the intended model use.

Relevant dimensions include:

- completeness
- accuracy
- precision
- calibration
- missingness
- noise
- drift
- saturation
- outliers
- stale data
- sampling adequacy
- regime coverage
- provenance

A sophisticated model cannot make invalid evidence trustworthy by itself.

## Sensor and telemetry faults

Unexpected twin behavior may originate from data infrastructure rather than physical-system behavior.

Potential causes include:

- sensor failure
- communication loss
- gateway faults
- unit conversion errors
- duplicated signals
- stale caches
- timestamp errors
- configuration mismatch
- unauthorized data changes

F117 should preserve data-fault hypotheses alongside physical-system hypotheses.

## Model architecture

`SKILLS/model_reasoning.py` and `TOOLS/model_registry.py` support explicit model definition and lifecycle tracking.

Model approaches can include:

- first-principles physics
- reduced-order models
- finite-element models
- computational fluid dynamics
- system identification
- state-space models
- empirical models
- statistical models
- machine learning
- neural surrogates
- hybrid physics and data-driven models
- co-simulation

The architecture should be selected according to intended use, fidelity, computational constraints, available evidence, and required interpretability.

## Model registry

A model registry entry can preserve:

```text
model_id
model_type
purpose
physical_scope
version
code_version
parameter_set
training_or_calibration_data
assumptions
input_schema
output_schema
operating_bounds
validation_reference
owner
review_state
```

A model version should be inseparable from the data, assumptions, configuration, and validation evidence supporting it.

## Assumption register

`TOOLS/assumption_register.py` makes modeling assumptions explicit.

Assumptions can concern:

- linearity
- steady state
- boundary conditions
- material properties
- environmental conditions
- friction
- heat transfer
- loads
- degradation
- sensor behavior
- independence
- distributional form
- control behavior

An assumption should be treated as an assumption, not silently converted into a physical fact.

## Calibration

The safety policy requires `model_calibration_reviewed`.

Calibration can estimate model parameters using observed physical-system evidence.

A governed calibration record should preserve:

- calibration data
- parameter bounds
- objective function
- optimization method
- prior values
- fitted values
- identifiability concerns
- residuals
- convergence status
- sensitivity
- excluded data
- model version

`calibration_gap` blocks release when calibration is incomplete or materially unsupported.

## Calibration versus validation

Calibration and validation are distinct.

```text
calibration -> tune parameters using evidence
validation -> test predictive adequacy against evidence not used to tune the model
```

F117 should not represent excellent fit on calibration data as independent validation.

## Parameter identifiability

Multiple parameter combinations can sometimes reproduce the same observed behavior.

The system should surface non-identifiability and parameter correlation where they materially affect predictions. A numerically optimized parameter is not automatically a physically identified parameter.

## Validation

`SKILLS/validation_reasoning.py` and `TOOLS/validation_table.py` support validation planning and evidence tracking.

The policy requires `validation_reviewed`.

Validation can assess:

- accuracy
- bias
- residual structure
- operating-regime coverage
- transient response
- steady-state response
- extreme conditions
- fault conditions
- cross-validation
- holdout performance
- physical consistency
- conservation laws
- boundary behavior
- scenario performance

`validation_gap` blocks release when validation evidence is incomplete or outside the intended-use scope.

## Validation table

A validation record can include:

```text
validation_case
requirement
physical_condition
reference_evidence
model_prediction
acceptance_criterion
error_metric
result
limitations
reviewer
```

Validation should be tied to intended use and operating envelope rather than summarized by one global score.

## Validation acceptance criteria

Acceptance criteria should be established before interpreting results where practical.

Criteria can be based on:

- engineering tolerance
- measurement uncertainty
- safety margin
- decision sensitivity
- domain standard
- historical performance
- physical law
- project requirement

The system should not move acceptance thresholds after observing results merely to produce a passing validation outcome.

## Verification versus validation

F117 should preserve the distinction:

```text
verification -> was the model implemented correctly?
validation -> is the model sufficiently representative for the intended real-world use?
```

Code correctness alone does not establish physical validity.

## Numerical verification

For numerical models, verification can include:

- solver convergence
- mesh independence
- timestep sensitivity
- numerical stability
- conservation checks
- regression tests
- unit tests
- reference solutions

Numerical error should be separated from physical-model error where possible.

## Uncertainty quantification

`SKILLS/uncertainty_reasoning.py` supports uncertainty analysis.

The policy requires `uncertainty_reviewed`.

Uncertainty sources can include:

- measurement uncertainty
- parameter uncertainty
- model-form uncertainty
- numerical uncertainty
- boundary-condition uncertainty
- operating-condition uncertainty
- data sparsity
- stochastic variability
- configuration uncertainty
- extrapolation

`uncertainty_exceeds_limit` blocks release when uncertainty exceeds reviewed operating bounds.

## Aleatory and epistemic uncertainty

Where useful, F117 can distinguish:

```text
aleatory uncertainty -> inherent variability
epistemic uncertainty -> lack of knowledge
```

This distinction matters because additional evidence may reduce epistemic uncertainty but not inherent variability.

## Sensitivity analysis

Sensitivity analysis can identify which inputs, parameters, assumptions, or boundary conditions most influence outputs.

This can support:

- model simplification
- sensor prioritization
- calibration planning
- uncertainty reduction
- experiment design
- risk analysis

Sensitivity should not be confused with causal importance without appropriate evidence.

## Extrapolation risk

A twin should identify when it is operating outside the conditions represented by calibration and validation evidence.

Examples include:

- higher loads
- new environmental conditions
- new materials
- new product variants
- unusual fault states
- new operating modes
- aging beyond observed history

Out-of-domain use should trigger uncertainty escalation or fail-closed behavior rather than confident prediction.

## Operating envelope

A governed twin should define reviewed operating bounds.

Bounds can include:

- temperature
- pressure
- speed
- load
- flow
- voltage
- environmental conditions
- product type
- configuration
- degradation state

A model validated within one envelope should not silently be treated as validated outside it.

## Synchronization lifecycle

A twin can drift away from the physical system when maintenance, configuration, software, process, or environmental changes are not reflected digitally.

Synchronization should account for:

- component replacement
- maintenance
- calibration
- software update
- firmware update
- parameter changes
- tooling changes
- process changes
- sensor replacement
- topology changes

Material synchronization gaps should trigger re-review.

## Configuration management

The policy requires `version_traceability_reviewed`.

A twin package should preserve traceability across:

```text
physical configuration
data schema
sensor configuration
model code
model parameters
assumptions
calibration data
validation data
software dependencies
runtime configuration
review decision
```

`version_traceability_gap` blocks release when model, data, or configuration versions cannot be reliably reconstructed.

## Model and data lineage

A result should be traceable to the model and evidence that generated it.

Useful lineage includes:

```text
result -> model version -> parameter set -> input data -> transformations -> source signal -> physical asset
```

This supports reproducibility, debugging, auditability, and change-impact analysis.

## Change impact

Changes to the physical system or twin can invalidate previous calibration or validation.

Examples include:

- geometry changes
- component replacement
- supplier changes
- material changes
- software changes
- control logic changes
- sensor relocation
- data preprocessing changes
- model architecture changes
- new operating modes

Material changes should trigger targeted or full revalidation as appropriate.

## Cybersecurity

The policy requires `cybersecurity_reviewed`.

Digital twins can connect engineering models to operational data and therefore create cyber-physical risk.

Cybersecurity review can include:

- authentication
- authorization
- least privilege
- network segmentation
- data integrity
- encryption
- secrets management
- logging
- software supply chain
- dependency risk
- model integrity
- remote access
- API security
- command pathways

`cybersecurity_risk` blocks release when material cybersecurity or access-control risk remains unresolved.

## Read-only versus write-capable integration

A major governance distinction is whether the twin only observes or can influence the physical system.

```text
read-only telemetry -> analytical risk
write-capable integration -> cyber-physical control risk
```

F117 should default toward separation of analytical twins from operational control unless a separately engineered and authorized control architecture exists.

## Live-control coupling

`live_control_coupling_risk` is an explicit blocker.

A model may be informative for operators without being safe for automatic control. Latency, model error, uncertainty, stale data, cybersecurity, failover, and unmodeled dynamics can make direct coupling hazardous.

`connect_live_control` is a protected action.

## Model deployment boundary

`deploy_model` is protected.

F117 can prepare a model package and deployment-readiness evidence, but it cannot autonomously deploy a model into a production, operational, or control environment.

Deployment requires authorized engineering and operational processes.

## Control setpoint boundary

`write_control_setpoint` is protected.

The system may analyze candidate operating points or optimization scenarios, but it cannot write a setpoint to a physical control system.

## Operating-limit boundary

`change_operating_limit` is protected.

A digital twin may provide evidence relevant to operating limits, but changing a limit can affect equipment safety, process safety, quality, regulatory compliance, and warranty conditions. Such decisions remain under qualified authority.

## Safety-interlock boundary

`override_safety_interlock` is permanently protected.

Twin predictions must never autonomously bypass trips, guards, permissives, interlocks, emergency stops, alarms, or other safety protections.

## Validation certification boundary

`certify_validation` is protected.

F117 can assemble validation evidence and identify whether reviewed criteria appear satisfied, but it cannot issue a formal validation certificate or represent that an authorized organization has certified the twin.

## Human-in-the-loop engineering

The intended architecture is:

```text
physical evidence -> twin analysis -> engineering recommendation -> qualified review -> authorized action
```

The twin supports decisions without collapsing analytical support and operational authority into one autonomous system.

## Real-time operation

Real-time twins should account for:

- latency
- jitter
- stale data
- dropped packets
- asynchronous updates
- compute delays
- model execution time
- failover
- degraded modes

A twin that cannot meet timing requirements should degrade safely rather than silently continue presenting stale outputs as current.

## State estimation

Digital twins may estimate unmeasured internal states using observers, filters, estimators, or learned models.

Estimated state should remain distinguishable from directly measured state. Confidence, observability, and estimator assumptions should be preserved.

## Data assimilation

Data assimilation can update model state or parameters from physical observations.

A governed implementation should preserve update method, prior state, evidence, uncertainty, and version history so that the evolution of the twin can be reconstructed.

## Hybrid models

Hybrid twins can combine physical laws and machine learning.

The system should preserve which outputs arise from physical equations, learned components, empirical correlations, or fusion logic. Learned components should not obscure physical constraints or validation limitations.

## Machine-learning components

When ML is used, governance can include:

- training-data provenance
- feature definitions
- leakage controls
- train/validation/test separation
- model version
- drift monitoring
- out-of-distribution detection
- calibration
- explainability appropriate to risk

An ML surrogate should not inherit the validation status of the high-fidelity model it approximates without independent evidence.

## Surrogate models

Reduced-order or surrogate models can accelerate computation but may lose fidelity.

F117 should preserve the domain over which the surrogate has been compared against higher-fidelity models or physical evidence.

## Co-simulation and model coupling

Complex twins may combine mechanical, electrical, thermal, fluid, software, and control models.

Coupling review should consider:

- interface variables
- units
- timestep coordination
- solver compatibility
- convergence
- feedback loops
- algebraic loops
- synchronization

Errors at subsystem interfaces can invalidate an otherwise correct component model.

## Geometry and coordinate systems

For spatial twins, geometry versions and coordinate systems should be explicit.

Misaligned coordinate frames, outdated geometry, or incorrect asset locations can create serious interpretation errors even when sensor values are correct.

## Physics constraints

Where applicable, models should be checked against physical constraints such as:

- conservation of mass
- conservation of energy
- momentum
- kinematic constraints
- material limits
- thermodynamic consistency
- electrical laws

Data fit should not automatically override known physical impossibility.

## Scenario simulation

F117 can support what-if analysis for reviewed scenarios.

Scenario outputs should identify assumptions, boundary conditions, model version, uncertainty, and whether the scenario lies inside the validated envelope.

A simulated outcome is not evidence that the physical system will necessarily behave identically.

## Optimization boundary

A twin can support optimization of throughput, energy, maintenance, quality, or other objectives.

Optimization should preserve constraints, uncertainty, safety margins, and tradeoffs. The mathematically optimal point may be operationally unacceptable.

Optimization output remains advisory unless separately reviewed and authorized.

## Failure and degradation modeling

Twins can model wear, fatigue, thermal degradation, fouling, corrosion, battery aging, or other degradation mechanisms.

F117 should preserve whether degradation parameters are measured, calibrated, assumed, or inferred and should avoid presenting a modeled failure date as certainty.

## Digital twin and predictive maintenance

A digital twin can provide inputs to predictive-maintenance workflows, but the twin does not itself authorize maintenance, deferral, shutdown, or return to service.

Maintenance decisions should remain under the governance of the appropriate maintenance and safety process.

## Manufacturing and process twins

Manufacturing twins can represent machines, cells, lines, factories, logistics, or process operations.

They can support simulation and analysis of:

- cycle time
- throughput
- WIP
- energy
- quality
- scheduling
- bottlenecks
- changeovers

F117 should not autonomously change line balance, staffing, process parameters, or production controls through such analysis.

## Product twins

Product twins can represent configuration, performance, lifecycle state, service history, or field behavior.

Identity and version traceability are essential when many physical products share a common model but differ in configuration or history.

## Fleet twins

Fleet-level models can identify common behavior and population trends, but they should not erase asset-specific differences.

A fleet prior should remain distinguishable from asset-specific measurements and state estimates.

## Evidence discipline

Material conclusions should distinguish among:

```text
measured physical evidence
derived signal
calibrated parameter
assumption
model prediction
estimated state
validation result
engineering interpretation
qualified-human decision
```

F117 must not fabricate sensor data, model performance, calibration results, validation evidence, physical configurations, cybersecurity reviews, or human approvals.

## Unsupported conclusions

Examples of unsupported conclusions include:

- claiming a twin is validated outside tested conditions
- treating calibration fit as validation
- asserting a model represents the current physical configuration without synchronization evidence
- claiming a predicted state is directly measured
- presenting uncertainty-free forecasts from uncertain inputs
- claiming safe control coupling based only on simulation performance

The system should expose limitations instead of manufacturing confidence.

## Required reviews

The implemented safety policy requires all eight conditions:

```text
twin_scope_reviewed
data_mapping_reviewed
model_calibration_reviewed
validation_reviewed
uncertainty_reviewed
cybersecurity_reviewed
version_traceability_reviewed
qualified_engineering_approval
```

Missing any required review fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- source-data quality or mapping remains unresolved
- physical-to-digital synchronization remains unresolved
- model calibration is incomplete
- validation evidence is incomplete or outside scope
- model uncertainty exceeds reviewed operating bounds
- unsafe or unreviewed live-control coupling is detected
- cybersecurity or access-control risk remains unresolved
- model, data, or configuration traceability is incomplete
- any required review is missing
- qualified engineering approval is missing

The system should surface the blocker rather than generate a falsely authoritative twin package.

## Protected actions

The safety policy permanently protects:

```text
deploy_model
connect_live_control
change_operating_limit
certify_validation
write_control_setpoint
override_safety_interlock
```

These actions remain outside autonomous authority even when every review flag is satisfied.

## Human authority boundaries

F117 must not autonomously:

- deploy models into operational environments
- connect a model to live control
- write machine or process setpoints
- change operating limits
- certify validation
- override safety systems
- authorize equipment operation
- declare a twin fit for safety-critical control without qualified approval
- conceal uncertainty or extrapolation
- represent a model as synchronized when configuration evidence is incomplete

Final engineering, control, safety, deployment, and certification authority remains with qualified humans and authorized organizations.

## Qualified engineering approval

The final review should be performed by personnel competent for the modeled system and intended use.

Depending on the application, this may include mechanical, electrical, controls, process, manufacturing, reliability, safety, software, data, cybersecurity, validation, or domain-specific engineering expertise.

## Versioning and change impact

A digital twin should preserve versions of:

- physical configuration
- sensor map
- data schema
- preprocessing
- model code
- parameters
- assumptions
- calibration evidence
- validation evidence
- software dependencies
- runtime configuration
- cybersecurity configuration
- approval state

Material changes should trigger impact analysis and appropriate revalidation.

## Memory and state

The `memory/` layer can preserve structured context across agent stages.

State should distinguish source evidence, deterministic transformations, assumptions, model outputs, validation findings, uncertainty, and human decisions.

Stale state should not silently override current physical configuration or telemetry.

## Observability

The `observability/` layer supports traceability across the workflow.

Useful telemetry includes:

- twin scope state
- signal mapping state
- data-quality flags
- synchronization status
- model version
- calibration status
- validation coverage
- uncertainty bounds
- out-of-domain events
- cybersecurity review
- configuration traceability
- governance blockers
- qualified approval state
- protected-action attempts

Observability supports engineering accountability but does not grant control authority.

## Explicit failure states

Useful explicit states include:

```text
TWIN SCOPE INCOMPLETE
DATA MAPPING GAP
SOURCE DATA INVALID
SYNCHRONIZATION GAP
CALIBRATION INCOMPLETE
VALIDATION INCOMPLETE
VALIDATION OUT OF SCOPE
UNCERTAINTY EXCEEDS LIMIT
OUT OF VALIDATED DOMAIN
LIVE CONTROL COUPLING RISK
CYBERSECURITY RISK
VERSION TRACEABILITY GAP
QUALIFIED ENGINEERING APPROVAL REQUIRED
MODEL DEPLOYMENT PROHIBITED
LIVE CONTROL CONNECTION PROHIBITED
OPERATING LIMIT CHANGE PROHIBITED
VALIDATION CERTIFICATION PROHIBITED
CONTROL SETPOINT WRITE PROHIBITED
SAFETY INTERLOCK OVERRIDE PROHIBITED
```

## End-to-end reference workflow

A typical F117 workflow follows this sequence:

1. Define the physical system, intended use, users, fidelity, and operating envelope.
2. Establish physical asset identity and configuration.
3. Map source signals, units, timing, semantics, transformations, and model variables.
4. Review source-data quality and synchronization.
5. Select and register the model architecture.
6. Record assumptions, parameters, and physical constraints.
7. Calibrate the model with traceable evidence.
8. Verify numerical implementation where applicable.
9. Validate against independent evidence and predefined criteria.
10. Quantify uncertainty and sensitivity.
11. Identify extrapolation and out-of-domain conditions.
12. Review cybersecurity and any live-control coupling.
13. Verify model, data, and configuration version traceability.
14. Perform independent engineering readiness review.
15. Apply fail-closed governance gates.
16. Require explicit qualified-human engineering approval.
17. Keep deployment, live control, operating-limit changes, validation certification, setpoint writes, and safety overrides outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test both engineering usefulness and governance behavior, including:

- scope completeness
- data mapping
- data-quality enforcement
- synchronization-gap detection
- calibration enforcement
- validation independence and coverage
- uncertainty handling
- out-of-domain detection
- cybersecurity escalation
- version traceability
- qualified-human approval enforcement
- protected-action enforcement

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out digital-twin governance suite.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance behavior, held-out digital-twin scenarios, and execution of the governed reference workflow.

## Reproducibility

Install development dependencies:

```bash
python -m pip install -e .
```

Then run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

Reproducibility also depends on preserving model, data, parameter, assumption, dependency, and physical-configuration versions.

## Extension points

Organization-specific implementations can add governed integrations for:

- historians
- read-only SCADA telemetry
- IoT platforms
- PLM systems
- asset registries
- CAD and geometry repositories
- simulation platforms
- model registries
- data lakes
- condition-monitoring systems
- laboratory and test systems
- CMMS or EAM systems
- visualization platforms

Write-capable operational integrations require additional safety, cybersecurity, control, and authorization architecture beyond this reference system.

## Example applications

Potential governed uses include:

- machine and equipment twins
- manufacturing-line twins
- process twins
- energy-system twins
- building-system twins
- product lifecycle twins
- fleet twins
- virtual commissioning support
- condition and degradation modeling
- engineering what-if analysis
- validation and calibration workflow support
- digital-twin training and simulation

F117 is not an autonomous controller, safety system, certification authority, operational command system, or substitute for qualified engineering judgment.

## Design principles

F117 follows these principles:

1. Define intended use and physical scope before building the twin.
2. Preserve physical-to-digital identity, semantics, timing, and provenance.
3. Separate calibration from independent validation.
4. Quantify uncertainty and detect extrapolation beyond validated conditions.
5. Keep the twin synchronized with physical configuration and lifecycle changes.
6. Treat cybersecurity and live-control coupling as engineering safety concerns.
7. Preserve complete model, data, assumption, and configuration lineage.
8. Fail closed when evidence or required review is incomplete.
9. Keep deployment, operational control, certification, setpoint changes, and safety overrides under qualified human authority.

## Scope statement

F117 demonstrates a governed multi-agent architecture for digital-twin engineering support. It combines specialized agents, deterministic model and signal registries, calibration and validation discipline, uncertainty analysis, cybersecurity review, observability, evaluation, and fail-closed governance while preserving strict human authority over operational control and certification.

It is a reference implementation for governed digital-twin engineering, not a substitute for qualified engineering, safety, controls, cybersecurity, or certification judgment.
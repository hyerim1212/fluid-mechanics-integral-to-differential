# Fluid Mechanics: From Integral to Differential Analysis

## Project Overview

This repository documents an independent fluid-mechanics study project that connects physical modeling, integral analysis, differential analysis, analytical solutions, numerical solutions, and verification.

The project begins with control-volume analysis and the Reynolds transport theorem. It will gradually proceed toward the differential analysis of viscous flow, an analytical solution for fully developed laminar internal flow, and a finite-difference numerical solution.

The primary goal is not simply to reproduce known equations or generate graphs. Each stage connects:

* governing conservation laws;
* physical assumptions;
* mathematical derivations;
* computational implementations;
* verification procedures;
* physical interpretations.

The overall project sequence is:

**Physical modeling → Integral analysis → Differential analysis → Analytical solution → Numerical solution → Verification → Dynamic-system modeling → Basic feedback control**

---

## Central Research Question

> How can integral and differential fluid-mechanics models be connected to describe pressure-driven internal flow, and how accurately can a finite-difference method reproduce the analytical velocity profile of fully developed laminar flow?
> Can a verified fluid model be reformulated as a simple dynamic system suitable for basic feedback control?

Supporting questions include:

* What quantities can be predicted using a control-volume model?
* Why can integral analysis determine overall forces and flow rates without determining the complete velocity field?
* How does differential analysis provide local information that integral analysis cannot?
* How do pressure and viscosity interact to produce an internal velocity profile?
* How can a numerical solution be verified using an analytical benchmark?

---

## Current Status

- Project start date: July 19, 2026
- Current phase: Integral analysis of fluid flow
- Latest completed topic: Integral linear-momentum conservation
- Next major topic: Integral energy analysis

## Completed

- Physical-system and repository setup
- Reynolds transport theorem review
- Control-volume mass balance
- Steady and unsteady mass-conservation cases
- Reusable mass-balance functions
- Integral linear-momentum equation
- Momentum-flux calculations
- Pressure-force calculations
- Wall-force and reaction-force calculations
- Multiple-inlet and multiple-outlet systems
- Moving control-volume concepts
- Non-inertial control-volume concepts
- Reusable momentum-analysis functions
- Computational input validation and benchmark testing

## In Progress

Consolidation of the integral linear-momentum documentation
Unit-level README organization
Repository documentation update

## Planned

Integral energy analysis
Comparison between Bernoulli analysis and viscous-flow analysis
Differential continuity equation
Differential momentum equation
Viscous-flow analytical solution
Finite-difference numerical solution
Analytical and numerical comparison
Grid-convergence study
Parameter study
Dynamic-system modeling
Basic feedback-control extension
Final technical report

## Completed Work

### 1. Reynolds Transport Theorem

The Reynolds transport theorem was reviewed as the connection between a system description and a control-volume description.

The study focused on:

* extensive and intensive properties;
* system and control-volume descriptions;
* transport across a control surface;
* conservation of mass;
* physical interpretation of accumulation and flux terms.

The theorem provides the foundation for the integral mass, momentum, and energy equations used in the following stages.

---

### 2. Control-Volume Mass Balance

A computational model was developed to analyze mass accumulation in a control volume.

The governing relation is:

**Rate of mass accumulation in the control volume = Total inlet mass flow rate − Total outlet mass flow rate**

For an incompressible fluid:

**Mass flow rate = Density × Volume flow rate**

and

**Mass flow rate = Density × Cross-sectional area × Average velocity**

The implementation includes:

* mass-flow-rate calculations;
* multiple inlet and outlet handling;
* control-volume accumulation;
* liquid-level change in a tank;
* input validation;
* physically meaningful limiting-case checks.

Reusable functions were separated from the main notebook so that they can be applied in later project stages.

---

#### 3. Integral Linear-Momentum Analysis

The integral linear-momentum equation was studied and implemented for steady and extended control-volume problems.

For one-dimensional inlet and outlet flows:

**Net momentum flux = Sum of outlet momentum flow rates − Sum of inlet momentum flow rates**

The analysis includes:

- straight ducts;
- accelerating nozzles;
- flow-direction changes;
- 90-degree elbows;
- pressure forces;
- wall forces;
- body forces;
- multiple inlet and outlet streams;
- moving control volumes;
- non-inertial reference frames.

The computational implementation treats momentum and force as vector quantities.

Representative benchmark cases were used to verify:

- conservation of mass;
- momentum-flux direction;
- pressure-force signs;
- wall-force calculations;
- action-reaction force pairs;
- velocity-vector validation;
- mass-flow-rate validation.

Detailed derivations, numerical values, and physical interpretations are stored in the unit notebook and its related documentation.

## Integral and Differential Analysis

The completed work establishes an important distinction between integral and differential modeling.

### Integral Analysis Can Determine

- total mass accumulation;
- average inlet and outlet quantities;
- net momentum flux;
- resultant force on a control volume;
- pressure-force and wall-force relationships;
- system-level flow and force balances.
- 
### Integral Analysis Does Not Directly Determine
- the complete internal velocity field;
- local velocity gradients;
- local shear-stress distributions;
- transverse velocity profiles;
- local pressure and stress variation throughout the domain.

These local quantities require differential conservation equations.

The next major stages of the project will therefore move from whole-control-volume balances to local field equations.

---

## Repository Structure

```text
fluid-mechanics-integral-to-differential/
│
├── README.md
├── requirements.txt
│
├── note/
│   ├── 00_Reynolds_Transport_Theorem/
│   │   ├── README.md
│   │   ├── control_volume_mass_balance.ipynb
│   │   └── control_volume_utils.py
│   │
│   └── 01_integral_analysis/
│       ├── README.md
│       ├── 01_linear_momentum_balance.ipynb
│       │
│       └── src/
│           ├── __init__.py
│           ├── control_volume_utils_copy.py
│           └── momentum_tool.py
│
└── progress/
    ├── concept_checklist.md
    └── daily_log.md
```

### Directory Roles

* `note/00_Reynolds_Transport_Theorem/` contains the Reynolds transport theorem review, control-volume mass-balance notebook, and reusable mass-balance functions.
* `note/01_integral_analysis/` contains the integral linear-momentum notebook, unit documentation, and reusable computational modules.
* `note/01_integral_analysis/src/` contains Python functions separated from the explanatory notebook.
* `progress/concept_checklist.md` tracks the concepts studied and verified.
* `progress/daily_log.md` records the chronological development of the project.
* `requirements.txt` lists the Python packages required to reproduce the notebooks.

Generated cache files such as `__pycache__/` and `.pyc` files are not shown because they are not part of the meaningful project structure.


## Documentation Structure

The repository follows three levels of documentation.

### Root README

The root README provides:

* the overall project purpose;
* the current project status;
* major completed results;
* the repository structure;
* the long-term roadmap.

### Unit-Level README Files

Each major study unit will contain a README file or an equivalent explanatory document.

A unit-level README should include:

* objective;
* governing equations;
* assumptions;
* implementation;
* verification;
* physical interpretation;
* conclusion;
* connection to the next stage.

### Daily Learning Log

The file `notes/daily_log.md` preserves the chronological learning process.

Each daily entry records:

* topics studied;
* problems solved;
* implementation progress;
* difficulties;
* corrections;
* verification results;
* next steps.

The root README presents the latest consolidated project state, while the daily log preserves the complete development history.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/hyerim1212/fluid-mechanics-integral-to-differential.git
cd fluid-mechanics-integral-to-differential
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
```

### 3. Install the required packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start Jupyter Notebook

```bash
python -m jupyter notebook
```

Open the desired notebook inside the `simulations` directory.

Run Jupyter from the repository root unless a notebook contains different path instructions. This allows the notebook to locate its corresponding source modules correctly.

---

## Verification Protocol

Each computational result should satisfy both physical and computational checks.

### Physical Checks

* Mass must be conserved under steady incompressible conditions.
* Momentum must be treated as a vector.
* Pressure-force directions must be determined from the control-surface orientation.
* The force exerted by the fluid on a solid must be opposite to the force exerted by the solid on the fluid.
* Units must be dimensionally consistent.
* Limiting cases must produce physically reasonable results.

### Computational Checks

* Invalid inputs must be rejected.
* Velocity vectors must have consistent dimensions.
* Mass flow rates must be nonnegative.
* Multiple inlet and outlet contributions must be summed correctly.
* Reusable functions must be separated from demonstration notebooks.
* Numerical results must be compared with manually calculated benchmark cases.

---

## Project Roadmap

### Phase 1: Integral Analysis

Completed:

* Conservation of mass
* Linear momentum equation
* Momentum-flux calculation
* Pressure and wall-force analysis

In progress:

* Remaining linear-momentum applications
* More complex control-volume problems

Planned:

* Energy equation
* Comparison with Bernoulli analysis

### Phase 2: Differential Analysis

Planned topics:

* material derivative;
* local acceleration;
* convective acceleration;
* differential continuity equation;
* differential momentum equation;
* assumption-based equation reduction.

### Phase 3: Viscous-Flow Analysis

The primary physical system will be steady, incompressible, fully developed laminar flow between two stationary parallel plates.

The flow will be represented by a streamwise velocity that changes only across the channel.

The reduced streamwise momentum equation will balance:

* the pressure gradient driving the flow;
* the viscous diffusion resisting velocity differences.

The analytical stage will determine:

* velocity profile;
* maximum velocity;
* mean velocity;
* volume flow rate;
* wall shear stress.

### Phase 4: Numerical Solution

The governing second-order differential equation will be discretized using a central finite-difference approximation.

This will produce a matrix equation of the form:

**Coefficient matrix × Unknown velocity vector = Source vector**

The numerical stage will include:

* grid generation;
* coefficient-matrix construction;
* boundary-condition implementation;
* linear-system solution;
* numerical integration;
* comparison with the analytical solution.

### Phase 5: Verification

The numerical result will be compared with the analytical solution using:

* maximum absolute error;
* mean absolute error;
* root-mean-square error;
* flow-rate error;
* centerline-velocity error;
* grid-convergence analysis.

## Phase 7: Dynamic-System Modeling 
## Phase 8: Basic Feedback Control — Optional

Suggested grid-point counts are:

* 11
* 21
* 41
* 81
* 161

### Phase 6: Parameter Study

The effects of the following variables will be investigated:

* dynamic viscosity;
* pressure gradient;
* channel half-height.

The study will examine how each parameter affects:

* the velocity profile;
* maximum velocity;
* mean velocity;
* flow rate;
* wall shear stress.

---

## Latest Update

### July 21, 2026

The conceptual study of integral linear-momentum conservation was completed through moving and non-inertial control-volume analysis.

The current project work includes:

- derivation and interpretation of the integral momentum equation;
- momentum-flux calculations;
- pressure-force analysis;
- wall-force and reaction-force analysis;
- straight-duct, nozzle, elbow, and multiple-stream cases;
- moving control-volume concepts;
- non-inertial reference-frame concepts;
- reusable computational functions;
- benchmark and invalid-input tests;
- consolidated notebook documentation.

### Next Step

The next stage is integral energy analysis.

This stage will connect:

- energy transport;
- work and heat-transfer terms;
- mechanical-energy loss;
- Bernoulli’s equation;
- viscous internal-flow analysis.
- The project will then proceed to integral energy analysis.

---

## Final Deliverables

The completed project is expected to include:

* physical-system diagrams;
* integral mass analysis;
* integral momentum analysis;
* integral energy analysis;
* explanation of the limitations of Bernoulli’s equation;
* differential governing-equation derivation;
* analytical laminar-flow solution;
* finite-difference numerical solver;
* analytical and numerical comparison;
* grid-convergence study;
* parameter studies;
* reusable Python modules;
* organized learning logs;
* final technical report.

---

## Project Principles

1. State the physical system before selecting an equation.
2. List the assumptions before simplifying the governing law.
3. Derive the mathematical model before coding.
4. Check units and force directions.
5. Verify each function using a simple benchmark.
6. Distinguish local quantities from cross-sectional averages.
7. Separate reusable functions from demonstration notebooks.
8. Record errors and corrections.
9. Verify the core model before adding extensions.
10. Do not claim more than the assumptions support.

---

## Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

The project primarily uses:

* Python
* NumPy
* Matplotlib
* Jupyter Notebook

The exact package versions and additional dependencies are specified in `requirements.txt`.

---

## Author

**Hyerim Jung**

First-year undergraduate independent study project in fluid mechanics, numerical analysis, and engineering computation.

## Long-Term Vision

This project is intended as the first stage of a longer study in fluid mechanics, numerical methods, dynamic systems, and feedback control.

The immediate objective is to construct and verify a trustworthy fluid-mechanics model.

Only after that foundation is complete will the project expand toward dynamic-system representation and basic control.

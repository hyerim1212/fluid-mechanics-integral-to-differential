# Fluid Mechanics: From Integral to Differential Analysis

## Project Overview

This repository documents an independent fluid-mechanics study project that connects

[
\text{physical system}
\rightarrow
\text{integral analysis}
\rightarrow
\text{differential analysis}
\rightarrow
\text{analytical solution}
\rightarrow
\text{numerical solution}
\rightarrow
\text{verification}.
]

The project begins with control-volume analysis and the Reynolds transport theorem. It will gradually proceed toward the differential analysis of viscous flow, an analytical solution for fully developed laminar internal flow, and a finite-difference numerical solution.

The primary goal is not simply to reproduce known equations or generate graphs. Each stage is designed to connect the governing conservation law, physical assumptions, mathematical derivation, computational implementation, and verification process.

---

## Central Research Question

> How can integral and differential fluid-mechanics models be connected to describe pressure-driven internal flow, and how accurately can a finite-difference method reproduce the analytical velocity profile of fully developed laminar flow?

The project also considers the following supporting questions:

* What quantities can be predicted using a control-volume model?
* Why can integral analysis determine overall forces and flow rates without determining the complete velocity field?
* How does differential analysis provide local information that integral analysis cannot?
* How do pressure and viscosity interact to produce an internal velocity profile?
* How can a numerical solution be verified using an analytical benchmark?

---

## Current Status

**Current phase:** Integral analysis of fluid flow
**Latest completed topic:** Integral linear-momentum analysis
**Project start date:** July 19, 2026

### Progress

* [x] Physical-system and repository setup
* [x] Reynolds transport theorem review
* [x] Control-volume mass balance
* [x] Reusable mass-balance functions
* [x] Integral linear-momentum equation
* [x] Momentum-flux calculation
* [x] Pressure-force and wall-force analysis
* [x] Reusable momentum-analysis functions
* [ ] Completion of integral linear-momentum notes
* [ ] Integral energy analysis
* [ ] Differential continuity equation
* [ ] Differential momentum equation
* [ ] Viscous-flow analytical solution
* [ ] Finite-difference method
* [ ] Analytical–numerical comparison
* [ ] Grid-convergence study
* [ ] Parameter study
* [ ] Final technical report

---

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

The governing relation is

[
\frac{dm_{\mathrm{CV}}}{dt}
===========================

## \sum_{\mathrm{in}}\dot{m}

\sum_{\mathrm{out}}\dot{m}.
]

For an incompressible fluid,

[
\dot{m}=\rho Q=\rho A V.
]

The implementation includes:

* mass-flow-rate calculations;
* multiple inlet and outlet handling;
* control-volume accumulation;
* liquid-level change in a tank;
* input validation;
* physically meaningful limiting-case checks.

Reusable functions were separated from the main notebook so that they can be applied in later project stages.

---

### 3. Integral Linear-Momentum Analysis

The integral linear-momentum equation was studied and implemented for steady control-volume problems.

The general form is

[
\sum \mathbf{F}_{\mathrm{CV}}
=============================

\frac{\partial}{\partial t}
\int_{\mathrm{CV}}
\rho\mathbf{V},dV
+
\int_{\mathrm{CS}}
\rho\mathbf{V}
(\mathbf{V}\cdot\mathbf{n}),dA.
]

For steady, one-dimensional inlet and outlet flows, the momentum-flux term becomes

[
\mathbf{P}_{\mathrm{net}}
=========================

## \sum_{\mathrm{out}}\dot{m}\mathbf{V}

\sum_{\mathrm{in}}\dot{m}\mathbf{V}.
]

The current notebook examines several representative cases.

#### Case 1: Straight duct with unchanged velocity

A steady incompressible flow enters and leaves a constant-area straight duct with the same velocity.

Result:

[
\mathbf{P}_{\mathrm{net}}
=========================

(0,0,0)\ \mathrm{N}.
]

This case demonstrates that a zero net momentum flux does not imply that all individual forces vanish. Pressure and friction forces may still exist while their vector sum is zero.

#### Case 2: Accelerating nozzle flow

A reduction in cross-sectional area increases the outlet speed under steady incompressible flow.

The case connects:

* continuity;
* outlet velocity;
* mass flow rate;
* streamwise momentum-flux change.

The calculated net momentum flux was

[
\mathbf{P}_{\mathrm{net}}
=========================

(60,0,0)\ \mathrm{N}.
]

#### Case 3: Ninety-degree elbow

The elbow case treats momentum as a vector quantity and includes pressure forces at the inlet and outlet.

The calculated net momentum flux was

[
\mathbf{P}_{\mathrm{net}}
=========================

(-80,80,0)\ \mathrm{N}.
]

The calculated wall force on the fluid was

[
\mathbf{F}_{\mathrm{wall\ on\ fluid}}
=====================================

(-680,480,0)\ \mathrm{N}.
]

By Newton’s third law, the force exerted by the fluid on the elbow was

[
\mathbf{F}_{\mathrm{fluid\ on\ elbow}}
======================================

(680,-480,0)\ \mathrm{N}.
]

These results verify that the direction of each velocity, pressure force, and reaction force must be handled explicitly.

---

## Current Physical Interpretation

The completed work establishes the following distinction:

### Integral analysis can determine

* total mass accumulation;
* mean inlet and outlet quantities;
* net momentum flux;
* resultant forces on a control volume;
* relationships among pressure, wall force, and flow rate.

### Integral analysis does not directly determine

* the complete internal velocity field;
* local velocity gradients;
* local shear-stress distributions;
* the transverse velocity profile (u(y)).

Determining these local quantities requires a differential formulation of mass and momentum conservation.

---

## Repository Structure

```text
fluid-mechanics-integral-to-differential/
│
├── README.md
├── requirements.txt
│
├── notes/
│   ├── daily_log.md
│   └── concept_checklist.md
│
└── simulations/
    └── 01_integral_analysis/
        ├── mass-balance notebook
        ├── 01_linear_momentum_balance.ipynb
        │
        └── src/
            ├── reusable mass-balance functions
            └── momentum_tool.py
```

The repository will expand as new stages are completed.

Planned additions include:

```text
simulations/
├── 01_integral_analysis/
├── 02_differential_analysis/
├── 03_viscous_flow/
├── 04_finite_difference/
└── 05_verification/

figures/
report/
```

---

## File Organization Principle

The repository follows three levels of documentation.

### Root `README.md`

Provides the current project overview, overall progress, major results, repository structure, and roadmap.

### Unit-level documentation

Each major study unit will contain a README or equivalent explanatory document describing:

* objectives;
* governing equations;
* assumptions;
* implementation;
* verification;
* conclusions;
* connection to the next stage.

### Daily learning log

`notes/daily_log.md` preserves the chronological learning process, including:

* topics studied;
* problems solved;
* implementation progress;
* difficulties;
* corrections;
* verification results;
* next steps.

The root README presents the latest consolidated state, while the daily log preserves the full development history.

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
.venv\Scripts\Activate.ps1
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

> Run Jupyter from the repository root unless a notebook contains different path instructions. This allows the notebook to locate its corresponding `src` modules correctly.

---

## Verification Protocol

Each computational result should satisfy the following checks.

### Physical checks

* Mass is conserved under steady incompressible conditions.
* Momentum is treated as a vector.
* Pressure-force directions are determined using control-surface normals.
* The force exerted by the fluid on a solid is opposite to the force exerted by the solid on the fluid.
* Units are dimensionally consistent.
* Limiting cases produce physically reasonable results.

### Computational checks

* Invalid inputs are rejected.
* Velocity vectors have consistent dimensions.
* Mass flow rates are nonnegative.
* Multiple inlet and outlet contributions are summed correctly.
* Reusable functions are separated from demonstration notebooks.
* Numerical results are compared with manually calculated benchmark cases.

---

## Project Roadmap

### Phase 1 — Integral Analysis

* [x] Conservation of mass
* [x] Linear momentum equation
* [x] Pressure and wall-force analysis
* [ ] Remaining linear-momentum applications
* [ ] Energy equation
* [ ] Comparison with Bernoulli analysis

### Phase 2 — Differential Analysis

* [ ] Material derivative
* [ ] Local and convective acceleration
* [ ] Differential continuity equation
* [ ] Differential momentum equation
* [ ] Assumption-based equation reduction

### Phase 3 — Viscous-Flow Analysis

The primary physical system will be steady, incompressible, fully developed laminar flow between two stationary parallel plates.

The expected velocity field will be represented as

[
\mathbf{V}=(u(y),0,0).
]

After applying the physical assumptions, the streamwise momentum equation will be reduced to

[
0
=

-\frac{dp}{dx}
+
\mu\frac{d^2u}{dy^2}.
]

The analytical stage will determine:

* velocity profile;
* maximum velocity;
* mean velocity;
* volume flow rate;
* wall shear stress.

### Phase 4 — Numerical Solution

The governing differential equation will be discretized using a central finite-difference approximation:

[
\frac{u_{i+1}-2u_i+u_{i-1}}{\Delta y^2}
=======================================

\frac{1}{\mu}\frac{dp}{dx}.
]

The resulting linear system will be expressed as

[
A\mathbf{u}=\mathbf{b}.
]

### Phase 5 — Verification

The numerical result will be compared with the analytical solution using:

* maximum absolute error;
* mean absolute error;
* root-mean-square error;
* flow-rate error;
* centerline-velocity error;
* grid-convergence analysis.

Suggested grid sizes are

[
N=11,\ 21,\ 41,\ 81,\ 161.
]

### Phase 6 — Parameter Study

The effects of the following variables will be investigated:

* dynamic viscosity (\mu);
* pressure gradient (dp/dx);
* channel half-height (H).

The study will examine how each parameter affects the velocity profile, mean velocity, flow rate, and wall shear stress.

---

## Latest Update

### July 20, 2026

The integral linear-momentum equation was studied through control-volume force analysis and computational examples.

Completed work includes:

* momentum-flux calculations for multiple inlets and outlets;
* straight-duct analysis;
* accelerating-nozzle analysis;
* ninety-degree elbow force analysis;
* pressure-force calculations;
* wall and reaction-force calculations;
* error handling for invalid velocity vectors and mass flow rates;
* separation of reusable momentum functions into `momentum_tool.py`.

### Next step

Complete the remaining integral linear-momentum concepts and documentation, including more complex force contributions and moving or non-inertial control-volume considerations where applicable. The project will then proceed to integral energy analysis.

---

## Final Deliverables

The completed project is expected to include:

* physical-system diagrams;
* integral mass and momentum analyses;
* explanation of the limitations of Bernoulli’s equation;
* differential governing-equation derivation;
* analytical laminar-flow solution;
* finite-difference numerical solver;
* analytical–numerical comparison;
* grid-convergence study;
* parameter studies;
* reusable Python modules;
* organized learning logs;
* final technical report.

---

## Project Principles

1. State the physical system before selecting an equation.
2. List assumptions before simplifying the governing law.
3. Derive the mathematical model before coding.
4. Check units and force directions.
5. Verify each function with a simple benchmark.
6. Distinguish local quantities from cross-sectional averages.
7. Separate reusable functions from demonstration notebooks.
8. Record errors and corrections.
9. Verify the core model before adding extensions.
10. Do not claim more than the assumptions support.

---

## Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

The project primarily uses:

* Python;
* NumPy;
* Matplotlib;
* Jupyter Notebook.

The exact package versions and additional dependencies are specified in `requirements.txt`.

---

## Author

**Hyerim Jung**

First-year undergraduate independent study project in fluid mechanics, numerical analysis, and engineering computation.

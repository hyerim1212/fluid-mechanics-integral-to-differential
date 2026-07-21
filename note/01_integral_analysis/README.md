# Integral Analysis of Fluid Flow

## Overview

This directory documents the integral-analysis stage of the project.

The purpose of this stage is to apply conservation laws to a control volume and determine system-level quantities such as:

* mass flow rate;
* momentum flux;
* resultant external force;
* pressure force;
* wall force;
* reaction force;
* relative velocity for a moving control surface.

The analysis focuses on quantities evaluated over the entire control volume or control surface.

It does not yet attempt to determine the complete internal velocity or stress field. Those local quantities will be addressed later through differential analysis.

---

## Current Scope

The current contents focus primarily on integral linear-momentum conservation.

Topics covered include:

* derivation of the integral linear-momentum equation;
* steady one-dimensional simplification;
* momentum transport through control surfaces;
* vector treatment of momentum flux;
* pressure and wall forces;
* multiple inlet and outlet streams;
* nonuniform velocity distributions;
* momentum-flux correction factors;
* moving control volumes;
* relative velocity;
* non-inertial reference frames.

Integral energy analysis will be added as the next major topic.

---

## Governing Principle

For a fixed control volume in an inertial reference frame, the integral linear-momentum equation states:

**Net external force = Rate of momentum accumulation inside the control volume + Net momentum transport through the control surface**

For steady flow, the accumulation term becomes zero.

For one-dimensional inlet and outlet flows, the equation is simplified to:

**Net external force = Sum of outlet momentum flow rates − Sum of inlet momentum flow rates**

Each momentum contribution depends on:

* mass flow rate;
* velocity magnitude;
* velocity direction.

Because velocity is a vector, momentum flux and force must also be treated as vectors.

---

## Relationship to the Reynolds Transport Theorem

The integral linear-momentum equation is obtained by applying the Reynolds transport theorem to Newton’s second law.

The system form of Newton’s second law relates net external force to the time rate of change of system momentum.

The Reynolds transport theorem converts this system description into a control-volume description consisting of:

* momentum accumulation inside the control volume;
* momentum transported across the control surface.

This connection is the main theoretical foundation of the notebook.

---

## External Forces

The net external force acting on the fluid may include:

* pressure force;
* wall or surface force;
* shear force;
* gravity;
* support or reaction force;
* inertial-force terms in a non-inertial reference frame.

Force directions must be defined consistently with the selected coordinate system.

The pressure force acts inward on a control surface because pressure is compressive.

The force exerted by the fluid on a solid boundary is opposite to the force exerted by the solid boundary on the fluid.

---

## Momentum Flux

For steady flow with multiple inlets and outlets:

**Net momentum flux = Total outlet momentum flow − Total inlet momentum flow**

The computational implementation represents each inlet or outlet using:

* a three-component velocity vector;
* a mass flow rate.

This allows the same function to handle:

* straight flow;
* acceleration or deceleration;
* changes in flow direction;
* multiple inlet and outlet streams.

A zero net momentum flux does not mean that every individual external force is zero.

It means that the vector sum of all external forces is zero under the stated steady-flow assumptions.

---

## Moving Control Volumes

When the control surface moves, the velocity crossing the surface must be evaluated relative to the control surface.

The relative velocity is:

**Relative velocity = Absolute fluid velocity − Control-surface velocity**

Two velocities must therefore be distinguished:

* absolute fluid velocity, which determines the momentum carried by the fluid;
* relative velocity, which determines how rapidly the fluid crosses the moving control surface.

The module includes a reusable function for calculating this relative velocity.

---

## Nonuniform Velocity Distribution

The one-dimensional momentum equation generally uses a cross-sectional average velocity.

When the velocity distribution is nonuniform, a momentum-flux correction factor is required.

The correction factor accounts for the fact that momentum flux depends on the square of the local velocity.

For a uniform velocity profile, the correction factor is equal to one.

This topic provides an important connection between integral analysis and the local velocity profiles that will later be studied through differential analysis.

---

## Computational Applications

The notebook includes representative applications designed to test both the physical model and the computational functions.

### Case 1: Straight Duct

A steady incompressible flow enters and exits a constant-area duct with the same average velocity.

Main purpose:

* verify that equal inlet and outlet momentum contributions produce zero net momentum flux;
* explain how pressure and friction forces may still exist while their resultant is zero.

### Case 2: Accelerating Nozzle

The outlet area is smaller than the inlet area, causing the fluid speed to increase.

Main purpose:

* connect mass conservation with momentum conservation;
* calculate the outlet velocity;
* determine the streamwise momentum-flux change.

### Case 3: 90-Degree Elbow

The fluid changes direction while passing through an elbow.

Main purpose:

* treat velocity and momentum as vectors;
* include pressure forces at multiple control surfaces;
* determine the wall force on the fluid;
* determine the force exerted by the fluid on the elbow.

### Multiple Inlet and Outlet Cases

Several streams are represented using lists of inlet and outlet dictionaries.

Main purpose:

* verify correct vector summation;
* test reusable functions for generalized control-volume configurations.

### Moving Control-Surface Case

The fluid velocity is compared with the control-surface velocity.

Main purpose:

* calculate relative velocity;
* distinguish momentum velocity from crossing velocity.

---

## Implemented Functions

### `mass_flow_rate`

Calculates mass flow rate using:

**Mass flow rate = Density × Area × Normal speed**

Inputs:

* density;
* cross-sectional area;
* velocity component normal to the surface.

Validation:

* density must be positive;
* area must be positive;
* speed magnitude must be nonnegative.

---

### `net_momentum_flux`

Calculates the net momentum flux for a steady control volume with multiple inlets and outlets.

Each stream is represented by a dictionary containing:

```python
{
    "velocity": [vx, vy, vz],
    "mass_flow_rate": value
}
```

The function returns a three-component NumPy array representing the net momentum-flux vector.

Validation:

* each velocity must contain exactly three components;
* mass flow rates must be nonnegative.

---

### `relative_velocity`

Calculates the fluid velocity relative to a moving inspection surface.

Inputs:

* fluid velocity vector;
* inspection-surface velocity vector.

The function returns:

**Fluid velocity − Inspection-surface velocity**

Validation:

* both vectors must contain exactly three components.

---

## Directory Structure

```text
01_integral_analysis/
│
├── README.md
├── 01_linear_momentum_balance.ipynb
│
└── src/
    ├── __init__.py
    ├── control_volume_utils_copy.py
    └── momentum_tool.py
```

### File Roles

* `01_linear_momentum_balance.ipynb` contains the governing theory, physical interpretations, computational cases, and verification results.
* `src/momentum_tool.py` contains reusable functions for mass flow rate, momentum flux, and relative velocity.
* `src/control_volume_utils_copy.py` contains control-volume utility functions reused from the previous mass-conservation stage.
* `src/__init__.py` allows the `src` directory to be imported as a Python package.
* `README.md` summarizes the purpose, methods, contents, and limitations of this unit.

Generated files such as `__pycache__/` and `.pyc` files are not part of the meaningful project structure.

---

## How to Run

Run Jupyter Notebook from the repository root:

```bash
python -m jupyter notebook
```

Then open:

```text
note/01_integral_analysis/01_linear_momentum_balance.ipynb
```

The notebook imports functions from the local `src` directory.

Run the cells in order so that:

* imports are completed first;
* variables are defined before use;
* computational results remain reproducible.

---

## Verification Strategy

The computational implementation is checked using simple cases with independently predictable results.

### Physical Verification

* Mass conservation is checked before momentum calculations.
* Momentum directions are checked using the selected coordinate system.
* Pressure forces are checked using control-surface orientations.
* Wall and reaction forces are compared using Newton’s third law.
* Units are checked for dimensional consistency.
* Limiting cases are interpreted physically.

### Computational Verification

* Incorrect velocity-vector dimensions raise errors.
* Negative mass flow rates raise errors.
* Nonphysical density and area values raise errors.
* Multiple inlet and outlet terms are summed separately.
* Net momentum flux is calculated as outlet contribution minus inlet contribution.
* Reusable functions are tested independently from the notebook cases.

---

## Key Findings

The current analysis demonstrates that:

1. Momentum conservation must be handled as a vector equation.
2. Mass conservation and momentum conservation serve different purposes.
3. A zero momentum-flux change does not require every individual force to vanish.
4. Pressure-force direction depends on the orientation of each control surface.
5. The wall force on the fluid and the fluid force on the wall form an action-reaction pair.
6. Moving control volumes require relative velocity in the flux term.
7. Absolute fluid velocity still determines the momentum carried by the fluid.
8. Nonuniform velocity profiles require a momentum-flux correction factor.
9. Integral analysis predicts resultant quantities but not complete local fields.

---

## Limitations

The present analysis uses simplified control-volume models.

Depending on the case, assumptions may include:

* steady flow;
* incompressible flow;
* one-dimensional inlet and outlet conditions;
* uniform density;
* uniform or cross-sectionally averaged velocity;
* negligible heat transfer;
* negligible deformation of the control volume;
* simplified pressure distributions.

The current implementation does not directly resolve:

* internal velocity profiles;
* local pressure distributions;
* local shear-stress distributions;
* turbulence;
* compressibility effects;
* complete rotational-frame dynamics.

These limitations motivate the transition to differential analysis.

---

## Connection to the Next Stage

Integral analysis determines how mass, momentum, and energy are transported across the boundaries of a control volume.

However, it does not directly determine how velocity, pressure, and stress vary at every point inside the flow.

The next stages of the project will therefore study:

1. integral energy conservation;
2. mechanical-energy loss;
3. Bernoulli’s equation and its limitations;
4. differential continuity;
5. differential momentum conservation;
6. viscous internal-flow modeling.

The long-term objective is to connect the control-volume model to a local differential model and eventually verify a numerical solution against an analytical laminar-flow solution.


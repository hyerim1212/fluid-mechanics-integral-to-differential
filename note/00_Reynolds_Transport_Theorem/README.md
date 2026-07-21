# Reynolds Transport Theorem and Control-Volume Mass Balance

## Overview

This directory documents the first theoretical and computational stage of the project.

The main objective is to connect a system description of fluid motion with a control-volume description using the Reynolds transport theorem.

The notebook then applies this framework to conservation of mass for steady and unsteady control volumes.

The work in this directory establishes the foundation for the later integral momentum, energy, differential, and numerical analyses.

---

## Learning Objectives

This unit is designed to develop the ability to:

* distinguish a system from a control volume;
* distinguish extensive and intensive properties;
* interpret accumulation and transport terms;
* apply the Reynolds transport theorem;
* derive the control-volume mass-balance equation;
* calculate mass flow rate;
* analyze multiple inlet and outlet streams;
* distinguish steady and unsteady flow;
* calculate liquid-level change in a tank;
* verify conservation using residual calculations;
* implement reusable and validated Python functions.

---

## System and Control-Volume Descriptions

A system is a fixed collection of matter.

Its boundary moves and deforms with the selected fluid particles, and no mass crosses the system boundary.

A control volume is a selected region in space.

Fluid may enter or leave through its control surface.

The system viewpoint follows matter, while the control-volume viewpoint observes what happens inside a selected region.

Engineering fluid-flow problems are often easier to analyze using a control volume because inlet and outlet quantities can be measured or prescribed.

---

## Extensive and Intensive Properties

An extensive property depends on the amount of matter in the system.

Examples include:

* mass;
* linear momentum;
* angular momentum;
* total energy.

An intensive property is the corresponding property per unit mass.

The Reynolds transport theorem relates a system extensive property to its control-volume representation.

For conservation of mass:

* the extensive property is total mass;
* the intensive property per unit mass is one.

This produces the control-volume mass-conservation equation.

---

## Reynolds Transport Theorem

The Reynolds transport theorem connects the time rate of change of a system property with:

* accumulation inside the control volume;
* net transport across the control surface.

Its physical structure is:

**Rate of change of a system property
= Accumulation inside the control volume

* Net outward transport across the control surface**

This theorem is not itself a conservation law.

It is a mathematical relationship that converts a system description into a control-volume description.

A conservation law is obtained after selecting the relevant extensive property.

Examples include:

* mass;
* linear momentum;
* angular momentum;
* energy.

---

## Conservation of Mass

Mass cannot be created or destroyed.

For a control volume:

**Mass accumulation rate
= Total inlet mass flow rate − Total outlet mass flow rate**

For steady flow, the mass inside the control volume does not change with time.

Therefore:

**Total inlet mass flow rate = Total outlet mass flow rate**

For an incompressible fluid with uniform density and average normal velocity:

**Mass flow rate = Density × Area × Normal velocity**

The volume flow rate is:

**Volume flow rate = Area × Normal velocity**

Therefore:

**Mass flow rate = Density × Volume flow rate**

---

## Sign Convention

All individual inlet and outlet mass flow rates are entered into the computational functions as nonnegative magnitudes.

The mass-balance function applies the sign convention internally:

* inlet contributions are positive;
* outlet contributions are subtracted.

Therefore:

**Accumulation rate = Total inflow − Total outflow**

The result is interpreted as follows:

* positive accumulation rate: mass inside the control volume increases;
* zero accumulation rate: no net mass accumulation;
* negative accumulation rate: mass inside the control volume decreases.

---

## Computational Applications

The notebook contains representative control-volume problems that connect the governing theory to computational implementation.

### Case 1: Steady Incompressible Nozzle

A fluid passes through a nozzle with different inlet and outlet areas.

The case demonstrates:

* circular cross-sectional area calculation;
* mass flow rate calculation;
* steady mass conservation;
* the relationship between area and velocity;
* verification that inlet and outlet mass flow rates are equal.

For steady incompressible flow through one inlet and one outlet:

**Density × Inlet area × Inlet velocity
= Density × Outlet area × Outlet velocity**

If the outlet area decreases, the outlet velocity must increase to conserve mass.

---

### Case 2: Multiple-Inlet Control Volume

Several streams enter a control volume and one or more streams leave it.

The case demonstrates:

* summation of multiple inlet mass flow rates;
* summation of multiple outlet mass flow rates;
* calculation of net accumulation;
* determination of an unknown outlet velocity;
* handling of streams with different densities or areas.

For steady flow:

**Sum of inlet mass flow rates = Sum of outlet mass flow rates**

The unknown outlet mass flow rate is found from the difference between total inflow and the known outlet flows.

---

### Case 3: Unsteady Tank Filling

A constant-area tank receives an inlet volume flow and may also have an outlet volume flow.

The liquid height changes because the amount of fluid stored inside the control volume changes with time.

Under the assumptions of:

* incompressible fluid;
* constant tank cross-sectional area;
* constant inlet volume flow rate;
* constant outlet volume flow rate;
* horizontal free surface;

the liquid height changes linearly with time.

The net filling rate is:

**Net volume-flow rate = Inlet volume-flow rate − Outlet volume-flow rate**

The height-change rate is:

**Height-change rate = Net volume-flow rate ÷ Tank area**

This case connects the control-volume accumulation term to an observable time-dependent quantity.

---

## Implemented Functions

### `cross_sectional_area`

Calculates the internal cross-sectional area of a circular pipe from its diameter.

Input:

* pipe diameter in meters.

Output:

* cross-sectional area in square meters.

Validation:

* diameter must be positive.

---

### `mass_flow_rate`

Calculates mass flow rate assuming uniform density and uniform normal velocity.

Inputs:

* density;
* cross-sectional area;
* normal velocity magnitude.

Output:

* mass flow rate in kilograms per second.

Validation:

* density must be positive;
* area must be positive;
* speed magnitude must be nonnegative.

---

### `mass_balance`

Calculates the total inlet flow, total outlet flow, and mass accumulation rate.

Inputs:

* list of inlet mass flow rates;
* list of outlet mass flow rates.

Output:

```python
{
    "total_inflow": value,
    "total_outflow": value,
    "accumulation_rate": value
}
```

Validation:

* inlet and outlet arguments must be lists;
* every flow-rate value must be numeric;
* all individual flow-rate magnitudes must be nonnegative.

---

### `outlet_velocity`

Calculates an unknown average outlet velocity using steady mass conservation.

Inputs:

* total inlet mass flow rate;
* known outlet mass flow rate;
* density of the unknown outlet stream;
* area of the unknown outlet.

Output:

* average outlet velocity.

Validation:

* inlet and known outlet flow rates must be nonnegative;
* density and area must be positive;
* known outlet flow cannot exceed total inflow under the assumed flow directions.

---

### `tank_height`

Calculates the liquid height in a constant-area tank at a specified time.

Inputs:

* initial liquid height;
* inlet volume flow rate;
* outlet volume flow rate;
* tank cross-sectional area;
* elapsed time.

Output:

* liquid height at the specified time.

Validation:

* initial height must be nonnegative;
* inlet and outlet volume flow rates must be nonnegative;
* tank area must be positive;
* time must be nonnegative;
* the requested time must not produce a physically negative liquid height.

If the tank becomes empty before the requested time, the function raises an error and reports the estimated emptying time.

---

## Directory Structure

```text
00_Reynolds_Transport_Theorem/
│
├── README.md
├── control_volume_mass_balance.ipynb
└── control_volume_utils.py
```

### File Roles

* `control_volume_mass_balance.ipynb` contains the governing theory, control-volume applications, visualizations, and verification results.
* `control_volume_utils.py` contains reusable calculation and validation functions.
* `README.md` summarizes the objective, theory, implementation, verification strategy, and connection to later project stages.

---

## How to Run

Start Jupyter Notebook from the repository root:

```bash
python -m jupyter notebook
```

Then open:

```text
note/00_Reynolds_Transport_Theorem/control_volume_mass_balance.ipynb
```

Run the notebook cells in order.

The notebook imports functions from:

```text
note/00_Reynolds_Transport_Theorem/control_volume_utils.py
```

The project dependencies can be installed from the repository root using:

```bash
pip install -r requirements.txt
```

---

## Verification Strategy

The notebook uses conservation residuals, limiting cases, and manual calculations to verify the implementation.

### Mass-Balance Residual

For steady flow, a mass-balance residual can be defined as:

**Residual = Total inlet mass flow rate − Total outlet mass flow rate**

A correctly balanced steady control volume should produce a residual of zero, apart from numerical round-off.

For an unsteady control volume, the residual should equal the rate of mass accumulation.

---

### Physical Checks

Each result is checked using the following questions:

* Is mass conserved?
* Are inlet and outlet directions interpreted correctly?
* Are density, area, and velocity units consistent?
* Does a smaller nozzle area produce a larger velocity?
* Does liquid level rise when inflow exceeds outflow?
* Does liquid level remain constant when inflow equals outflow?
* Does liquid level fall when outflow exceeds inflow?
* Does a larger tank area reduce the height-change rate?
* Does the result remain physically meaningful?

---

### Computational Checks

The reusable functions reject:

* nonpositive pipe diameters;
* nonpositive density;
* nonpositive area;
* negative flow-rate magnitudes;
* negative elapsed time;
* invalid list inputs;
* nonnumeric flow-rate entries;
* impossible outlet-flow conditions;
* tank heights that would become negative.

These checks prevent mathematically executable but physically invalid calculations.

---

## Representative Verification Results

The completed notebook includes checks such as:

* equal inlet and outlet mass flow rates for a steady nozzle;
* zero steady mass-balance residual;
* correct summation for multiple inlet streams;
* correct calculation of an unknown outlet velocity;
* linear tank-height change for constant volume-flow rates;
* agreement between the analytical tank-height relation and the computed trend.

The detailed numerical values and plots are contained in the notebook.

---

## Key Findings

This unit demonstrates that:

1. The Reynolds transport theorem connects system and control-volume descriptions.
2. The theorem must be combined with a physical conservation law.
3. Mass conservation applies to both steady and unsteady flows.
4. Steady flow does not necessarily mean that fluid particles are stationary.
5. Incompressibility does not automatically imply steady flow.
6. Multiple inlet and outlet streams must be summed before applying the balance.
7. Mass accumulation is determined by the difference between total inflow and total outflow.
8. A tank-level problem is an unsteady control-volume problem even when the inlet and outlet flow rates are constant.
9. Residual calculations provide a direct method for checking conservation.
10. Input validation is part of producing a physically trustworthy computational model.

---

## Assumptions and Limitations

The computational cases use simplified models.

Depending on the case, assumptions may include:

* one-dimensional flow at each inlet and outlet;
* uniform density over each cross section;
* uniform or cross-sectionally averaged normal velocity;
* incompressible flow;
* fixed control volume;
* constant tank area;
* constant inlet and outlet flow rates;
* horizontal tank free surface;
* no dependence of outlet flow rate on liquid height.

The current unit does not determine:

* detailed internal velocity fields;
* pressure-force distributions;
* momentum transport;
* energy transport;
* local shear stress;
* viscous velocity profiles.

These quantities require later integral and differential analyses.

---

## Connection to the Next Stage

The Reynolds transport theorem provides a general framework for transporting extensive properties across a control surface.

In this unit, the selected property is mass.

In the next unit, the selected property is linear momentum.

This transition introduces:

* vector momentum flux;
* pressure forces;
* wall and reaction forces;
* changes in flow direction;
* moving control volumes;
* non-inertial reference frames.

The mass-balance functions developed here are reused in the integral linear-momentum analysis because momentum calculations must also satisfy conservation of mass.

The long-term project sequence is:

**Mass conservation → Momentum conservation → Energy conservation → Differential analysis → Viscous-flow modeling → Numerical solution → Verification**

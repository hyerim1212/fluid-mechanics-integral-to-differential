# Concept Checklist

This checklist tracks conceptual understanding, mathematical derivation, computational implementation, and verification throughout the project.

An item should be checked only when I can:

1. explain the concept without relying heavily on notes;
2. state the relevant assumptions;
3. apply it to a representative problem;
4. interpret the result physically;
5. identify at least one limitation.

---

## 0. Physical Modeling Fundamentals

* [x] Define the physical system before selecting an equation
* [x] Identify known quantities and unknown quantities
* [x] Choose an appropriate control volume
* [x] Define inlet, outlet, wall, and control-surface boundaries
* [x] Establish a coordinate system and sign convention
* [x] Distinguish physical assumptions from mathematical conclusions
* [x] Check dimensional consistency
* [x] Check limiting cases
* [x] Distinguish local quantities from cross-sectional averages
* [x] Explain why model limitations must be stated explicitly

---

## 1. Reynolds Transport Theorem

### Core Concepts

* [x] Distinguish a system from a control volume
* [x] Distinguish a system boundary from a control surface
* [x] Define extensive and intensive properties
* [x] Explain the relationship between an extensive property and its value per unit mass
* [x] Explain the physical meaning of accumulation
* [x] Explain the physical meaning of transport across a control surface
* [x] State the general purpose of the Reynolds transport theorem
* [x] Explain that the Reynolds transport theorem is not itself a conservation law
* [x] Explain how the theorem converts a system equation into a control-volume equation

### Fixed and Moving Control Volumes

* [x] Apply the theorem to a fixed control volume
* [x] Explain why relative velocity is required for a moving control surface
* [x] Distinguish absolute fluid velocity from relative crossing velocity
* [ ] Derive the Reynolds transport theorem for a deforming control volume
* [ ] Apply the theorem to a control volume whose volume changes with time

---

## 2. Control-Volume Mass Conservation

### Governing Concepts

* [x] Derive mass conservation from the Reynolds transport theorem
* [x] Explain why the specific property for mass is equal to one
* [x] Interpret the accumulation term
* [x] Interpret inlet and outlet mass-flow terms
* [x] Apply the inlet-positive and outlet-negative sign convention
* [x] Distinguish steady flow from unsteady flow
* [x] Distinguish steady flow from incompressible flow
* [x] Explain why steady flow does not mean zero fluid velocity

### Mass and Volume Flow Rates

* [x] Calculate circular cross-sectional area
* [x] Calculate volume flow rate
* [x] Calculate mass flow rate
* [x] Use density, area, and average normal velocity consistently
* [x] Explain the meaning of normal velocity
* [x] Check the units of mass flow rate
* [x] Calculate an unknown outlet velocity from mass conservation

### Control-Volume Applications

* [x] Analyze a steady incompressible nozzle
* [x] Analyze multiple inlet streams
* [x] Analyze multiple outlet streams
* [x] Handle streams with different densities
* [x] Calculate total inflow and total outflow
* [x] Calculate the mass-accumulation rate
* [x] Analyze an unsteady tank-filling problem
* [x] Derive the linear liquid-height relation for constant flow rates
* [x] Determine whether a tank level rises, remains constant, or falls
* [x] Calculate the emptying time under the simplified tank model

### Verification

* [x] Define a mass-balance residual
* [x] Verify zero residual for a steady balanced control volume
* [x] Verify that the residual equals accumulation for an unsteady control volume
* [x] Check that a smaller nozzle area produces a larger velocity
* [x] Check that a larger tank area reduces the height-change rate
* [x] Reject physically invalid density, area, velocity, and time inputs

---

## 3. Integral Linear-Momentum Conservation

### Derivation and Interpretation

* [x] Define linear momentum as a system extensive property
* [x] Connect Newton’s second law to the Reynolds transport theorem
* [x] Derive the integral linear-momentum equation
* [x] Interpret momentum accumulation inside a control volume
* [x] Interpret momentum transport through a control surface
* [x] Derive the steady one-dimensional momentum equation
* [x] Explain why momentum conservation is a vector equation
* [x] Distinguish mass conservation from momentum conservation

### Momentum Flux

* [x] Calculate inlet momentum-flow contributions
* [x] Calculate outlet momentum-flow contributions
* [x] Calculate net momentum flux
* [x] Apply the outlet-minus-inlet convention
* [x] Handle three-dimensional velocity vectors
* [x] Analyze multiple inlet and outlet streams
* [x] Explain why zero net momentum flux does not imply zero individual forces
* [x] Check the units of momentum flux as force units

### External Forces

* [x] Identify pressure forces
* [x] Identify wall or surface forces
* [x] Identify shear-force contributions
* [x] Identify gravity or body-force contributions
* [x] Identify support and reaction forces
* [x] Determine pressure-force direction from the outward normal
* [x] Distinguish wall force on the fluid from fluid force on the wall
* [x] Apply Newton’s third law to a fluid-solid interaction
* [x] Construct a control-volume force balance

### Representative Applications

* [x] Analyze a straight duct with unchanged velocity
* [x] Analyze an accelerating nozzle
* [x] Analyze a flow-direction change
* [x] Analyze a 90-degree elbow
* [x] Include inlet and outlet pressure forces
* [x] Calculate the wall force on the fluid
* [x] Calculate the force exerted by the fluid on a solid
* [x] Analyze multiple-stream momentum flux

### Nonuniform Velocity Distribution

* [x] Explain why momentum flux depends on the square of local velocity
* [x] Define the momentum-flux correction factor
* [x] Explain when the correction factor is equal to one
* [x] Explain why each inlet or outlet may have a different correction factor
* [ ] Calculate the correction factor directly from a specified velocity profile
* [ ] Compare correction factors for uniform, laminar, and other profiles

### Moving Control Volumes

* [x] Define relative velocity
* [x] Calculate fluid velocity relative to a moving control surface
* [x] Explain why relative velocity determines surface crossing
* [x] Explain why absolute velocity determines transported momentum
* [x] Distinguish a moving control volume from a non-inertial reference frame
* [ ] Solve a complete momentum problem using a moving control volume

### Non-Inertial Reference Frames

* [x] Explain why inertial-force terms appear in an accelerating frame
* [x] Identify translational inertial acceleration
* [x] Identify angular-acceleration terms
* [x] Identify Coriolis acceleration
* [x] Identify centripetal acceleration
* [x] Relate the centripetal term to the centrifugal inertial-force term
* [x] Distinguish absolute, relative, and reference-frame motion
* [ ] Solve a complete fluid momentum problem in a rotating reference frame
* [ ] Verify a non-inertial result using an equivalent inertial-frame analysis

### Computational Implementation

* [x] Implement a mass-flow-rate function
* [x] Implement a multiple-stream momentum-flux function
* [x] Implement a relative-velocity function
* [x] Represent stream data using dictionaries
* [x] Represent multiple streams using lists
* [x] Validate three-component velocity vectors
* [x] Reject negative mass-flow-rate magnitudes
* [x] Test reusable functions using simple benchmark cases
* [x] Separate reusable functions from the explanatory notebook

---

## 4. Integral Energy Analysis

### Energy Concepts

* [ ] Distinguish internal, kinetic, and potential energy
* [ ] Identify heat-transfer and work-transfer terms
* [ ] Derive the control-volume energy equation from the Reynolds transport theorem
* [ ] Interpret energy accumulation inside a control volume
* [ ] Interpret energy transport across a control surface
* [ ] Derive the steady-flow energy equation
* [ ] Explain flow work and enthalpy
* [ ] Check energy units consistently

### Mechanical Energy and Bernoulli Analysis

* [ ] Derive Bernoulli’s equation from the mechanical-energy relation
* [ ] State the assumptions required for Bernoulli’s equation
* [ ] Distinguish total energy from mechanical energy
* [ ] Include pump work
* [ ] Include turbine work
* [ ] Include head loss
* [ ] Explain viscous mechanical-energy dissipation
* [ ] Compare Bernoulli analysis with the full energy equation
* [ ] Explain why Bernoulli’s equation cannot determine an internal velocity profile

### Applications

* [ ] Analyze a nozzle using the energy equation
* [ ] Analyze a pipe system with head loss
* [ ] Analyze a pump or turbine control volume
* [ ] Apply an energy correction factor for nonuniform velocity
* [ ] Verify energy conservation using a benchmark case

---

## 5. Differential Analysis of Fluid Flow

### Velocity and Acceleration Fields

* [ ] Define a velocity field
* [ ] Distinguish Eulerian and Lagrangian descriptions
* [ ] Derive the material derivative
* [ ] Interpret local acceleration
* [ ] Interpret convective acceleration
* [ ] Evaluate acceleration from a specified velocity field
* [ ] Explain when convective acceleration can exist in steady flow

### Differential Continuity

* [ ] Derive the differential continuity equation
* [ ] Apply the incompressibility condition
* [ ] Interpret velocity divergence
* [ ] Test whether a velocity field satisfies continuity
* [ ] Connect differential continuity to integral mass conservation

### Differential Momentum

* [ ] Identify normal and shear stresses
* [ ] Write the differential momentum balance
* [ ] Explain the physical meaning of each momentum-equation term
* [ ] State the Newtonian-fluid constitutive relation
* [ ] Write the incompressible Navier–Stokes equations
* [ ] Reduce the equations using physical assumptions
* [ ] Check dimensional consistency term by term
* [ ] Connect differential momentum to integral momentum conservation

---

## 6. Viscous Internal-Flow Analysis

### Physical Assumptions

* [ ] Define steady flow
* [ ] Define incompressible flow
* [ ] Define fully developed flow
* [ ] Define unidirectional flow
* [ ] Apply the no-slip boundary condition
* [ ] Explain why streamwise velocity can depend only on the transverse coordinate
* [ ] Construct an assumptions-to-terms table

### Plane Poiseuille Flow

* [ ] Derive the reduced streamwise momentum equation
* [ ] Apply both wall boundary conditions
* [ ] Derive the analytical velocity profile
* [ ] Verify symmetry of the velocity profile
* [ ] Determine maximum velocity
* [ ] Determine mean velocity
* [ ] Derive the maximum-to-mean velocity relation
* [ ] Calculate volume flow rate
* [ ] Calculate wall shear stress
* [ ] Relate pressure gradient to flow rate
* [ ] Nondimensionalize the velocity profile
* [ ] Check physical parameter trends

### Model Applicability

* [ ] Calculate Reynolds number
* [ ] Check whether the laminar-flow assumption is reasonable
* [ ] Identify the limitations of the parallel-plate model
* [ ] Distinguish analytical verification from experimental validation

---

## 7. Finite-Difference Method

### Discretization

* [ ] Generate a one-dimensional spatial grid
* [ ] Define grid spacing
* [ ] Derive the central-difference approximation using Taylor expansion
* [ ] Identify the truncation-error order
* [ ] Discretize the governing differential equation
* [ ] Apply no-slip boundary conditions
* [ ] Construct the coefficient matrix
* [ ] Construct the source vector
* [ ] Express the system as a matrix equation

### Numerical Solution

* [ ] Solve the linear system using NumPy
* [ ] Plot the numerical velocity profile
* [ ] Calculate numerical maximum velocity
* [ ] Calculate numerical mean velocity
* [ ] Calculate numerical flow rate
* [ ] Compare analytical and numerical solutions
* [ ] Separate grid, matrix, solution, and analysis functions

---

## 8. Numerical Verification

* [ ] Define maximum absolute error
* [ ] Define mean absolute error
* [ ] Define root-mean-square error
* [ ] Calculate centerline-velocity error
* [ ] Calculate flow-rate error
* [ ] Repeat the calculation using multiple grid sizes
* [ ] Plot error against grid spacing
* [ ] Create a log-log convergence plot
* [ ] Estimate the observed order of convergence
* [ ] Compare observed and expected convergence orders
* [ ] Identify a sufficiently fine grid
* [ ] Explain the difference between grid convergence and physical validation

---

## 9. Parameter Study

* [ ] Vary dynamic viscosity while holding other variables constant
* [ ] Vary pressure gradient while holding other variables constant
* [ ] Vary channel half-height while holding other variables constant
* [ ] Interpret changes in maximum velocity
* [ ] Interpret changes in mean velocity
* [ ] Interpret changes in flow rate
* [ ] Interpret changes in wall shear stress
* [ ] Identify linear and nonlinear scaling relationships
* [ ] Verify that dimensionless velocity profiles collapse onto one curve
* [ ] Confirm model applicability for each parameter set

---

## 10. Dynamic-System Modeling

This section is an extension and should begin only after the core fluid model has been verified.

* [ ] Select an appropriate dynamic fluid system
* [ ] Define the plant
* [ ] Identify system inputs
* [ ] Identify system outputs
* [ ] Identify disturbances
* [ ] Derive a time-dependent conservation equation
* [ ] Identify equilibrium conditions
* [ ] Linearize the model if necessary
* [ ] Express the model as a first-order differential equation
* [ ] Construct a transfer-function representation
* [ ] Construct a state-space representation
* [ ] Simulate the open-loop response

---

## 11. Basic Feedback Control

This section is optional.

* [ ] Define a control objective
* [ ] Construct a closed-loop block diagram
* [ ] Implement proportional control
* [ ] Implement PI control
* [ ] Compare open-loop and closed-loop responses
* [ ] Evaluate rise time
* [ ] Evaluate overshoot
* [ ] Evaluate settling time
* [ ] Evaluate steady-state error
* [ ] Test disturbance rejection
* [ ] State the limitations of the simplified control model

---

## 12. Programming and Reproducibility

* [x] Organize notebooks by theoretical unit
* [x] Separate reusable functions from notebook demonstrations
* [x] Use descriptive function and variable names
* [x] Add input validation
* [x] Include physical units in documentation
* [x] Maintain a `requirements.txt` file
* [x] Maintain a root README
* [x] Maintain unit-level README files
* [x] Maintain a chronological daily log
* [x] Maintain this concept checklist
* [ ] Remove generated cache files from version control
* [ ] Add `__pycache__/` to `.gitignore`
* [ ] Add `*.pyc` to `.gitignore`
* [ ] Add `.ipynb_checkpoints/` to `.gitignore`
* [ ] Confirm that all notebooks run from a clean environment
* [ ] Confirm that another user can reproduce the results
* [ ] Export final figures in a consistent format
* [ ] Complete the final technical report

---

## Current Milestone

### Completed

* Reynolds transport theorem
* Control-volume mass conservation
* Steady and unsteady mass-balance applications
* Integral linear-momentum conservation
* Pressure, wall, and reaction-force analysis
* Multiple-stream momentum-flux analysis
* Moving control-volume concepts
* Non-inertial reference-frame concepts
* Reusable mass and momentum functions
* Unit-level repository documentation

### Next

* Integral energy conservation
* Mechanical-energy analysis
* Bernoulli-equation limitations
* Preparation for differential analysis

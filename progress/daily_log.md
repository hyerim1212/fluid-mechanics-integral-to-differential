# Daily Study Log

## 2026-07-19

### Topic

Reynolds Transport Theorem and control-volume mass balance

### Reviewed

- System and control-volume descriptions
- Extensive and intensive properties
- Reynolds Transport Theorem
- Conservation of mass
- Steady and unsteady flow
- Mass flow rate and volume flow rate

### Problems solved

- Steady incompressible nozzle flow
- Multiple-inlet and single-outlet flow
- Unsteady tank-filling problem
- Mass-balance residual verification
  
### Difficulties

- Applying density correctly when multiple streams have different densities
- Managing variables consistently between notebook cells
- Exporting the notebook to HTML

### Result

Completed and uploaded:

`simulations/00_Reynolds_Transport_Theorem/control_volume_mass_balance.ipynb`

### Next step

Study the integral linear-momentum equation and develop a control-volume
simulation involving forces, pressure, and momentum flux.

### Verification

- For Case 1, the calculated outlet velocity was 8.0 m/s.
- The inlet and outlet mass flow rates were both 15.708 kg/s.
- The mass-balance residual was 0.0 kg/s.

### Summary
본격적으로 note 작성 및 개인 project 진행을 위해 방학 동안 공부한 내용을 정리하는 시간을 가졌다. 
제일 최근에 공부한 RTT를 다루었다.

---------------------------------
## 2026-07-20

### Topic

Integral linear-momentum equation and control-volume force analysis

### Studied

- Integral form of the linear-momentum equation
- Momentum flux through control surfaces
- Vector representation of inlet and outlet velocities
- Pressure forces acting on control surfaces
- Wall force and reaction force
- Application of Newton’s third law
- Use of multiple inlets and outlets in computational analysis

### Problems solved

- Straight duct with unchanged inlet and outlet velocities
- Accelerating nozzle flow
- (90^\circ) elbow flow with pressure forces
- Multiple-inlet and multiple-outlet momentum-flux test cases
- Error-handling tests for invalid velocity vectors and negative mass flow rates
  
### Difficulties

- Passing a dictionary instead of a list of dictionaries to the momentum-flux function
- Preventing the mass_flow_rate function name from being overwritten by a numerical variable

### Result

Completed and prepared for upload:

`simulations/01_integral_analysis/01_linear_momentum_balance.ipynb`

Separated the reusable functions into:

`simulations/01_integral_analysis/src/momentum_tool.py`

### Next step 

I'll continue studying the integral linear-momentum equation and extend the analysis to more complex control-volume problems.

### Verification

- For Case 1, the net momentum flux was ((0.0, 0.0, 0.0)\ \mathrm{N}).
- For Case 2, the outlet velocity was (5.0\ \mathrm{m/s}).
- The nozzle net momentum flux was ((60.0, 0.0, 0.0)\ \mathrm{N}).
- For Case 3, the net momentum flux was ((-80.0, 80.0, 0.0)\ \mathrm{N}).
- The wall force on the fluid was ((-680.0, 480.0, 0.0)\ \mathrm{N}).
- The force exerted by the fluid on the elbow was ((680.0, -480.0, 0.0)\ \mathrm{N}).

### Summary
적분형 선형 운동량 방정식의 유도 -> 단순화된 선형 운동량 방정식 -> 선형 운동량 방정식의 적용 -> 유동 방향의 변화 -> 압력 및 속도 변화 -> 무게, 압력, 마찰 및 비균일 속도 -> 비균일 압력 ->움직이는 검사체적 까지 개념에 대한 공부를 진행하였으며, 이에 대한 계산 및 검증 내용을 담은 노트를 작성하였다. 이후 개념 부분에 대한 노트 정리와 비관성계에 관한 남은 개념을 공부하고, 유동의 적분해석: 선형 운동량 보존에 대한 파트 1차 개념 공부를 마무리할 예정이다.

---

## 2026-07-21

### Topic

Completion and verification of the integral linear-momentum analysis

### Studied

* General integral form of the linear-momentum equation
* Derivation of the momentum equation using the Reynolds Transport Theorem
* Physical interpretation of momentum accumulation and momentum flux
* Classification of pressure, wall, shear, gravity, and support forces
* Steady one-dimensional momentum equation
* Momentum-flux correction factor for nonuniform velocity distributions
* Moving control volumes and relative velocity
* Difference between a moving control volume and a non-inertial reference frame
* Velocity and acceleration transformations in translating and rotating reference frames
* Coriolis, Euler, and rotational acceleration terms
* Limitations of integral momentum analysis

### Problems solved

* Multiple-inlet and multiple-outlet momentum-flux calculations
* Symmetric momentum-vector cancellation test
* Moving-control-surface relative-velocity calculations
* Nonuniform velocity-profile momentum-flux comparison
* Nozzle and elbow momentum-residual calculations

### Implementation

Completed and organized:

`simulations/01_integral_analysis/01_linear_momentum_balance.ipynb`

The notebook now includes:

* theoretical derivation of the integral linear-momentum equation;
* representative control-volume applications;
* reusable momentum-analysis functions;
* relative-velocity calculations;
* benchmark tests;
* limiting-case tests;
* invalid-input tests;
* momentum-conservation residual tests;
* discussion of the limitations of integral analysis.

The reusable functions remain separated in:

`simulations/01_integral_analysis/src/momentum_tool.py`

### Verification

A total of 17 tests were conducted.

The tests confirmed that:

* mass flow rate is calculated correctly;
* zero normal velocity produces zero mass flow rate;
* invalid density, area, velocity, and mass-flow-rate inputs are rejected;
* inlet and outlet momentum contributions are combined vectorially;
* the straight-duct benchmark produces zero net momentum flux;
* the accelerating-nozzle benchmark produces a net momentum flux of ((60.0, 0.0, 0.0)\ \mathrm{N});
* the ninety-degree elbow benchmark produces a net momentum flux of ((-80.0, 80.0, 0.0)\ \mathrm{N});
* relative velocity is calculated correctly for a moving control surface;
* a control surface moving with the fluid has zero relative velocity;
* a nonuniform velocity distribution produces a momentum flux different from the value estimated using only the average velocity;
* the nozzle and elbow momentum-balance residuals are approximately zero.

Final test result:

`17/17 tests passed`

### Difficulties

* Distinguishing the absolute velocity that carries momentum from the relative velocity that determines flow across a moving control surface
* Defining the velocity and acceleration terms consistently in a rotating non-inertial frame
* Maintaining consistent vector directions for pressure, wall, and reaction forces

### Corrections

* Corrected the gravity term to use a control-volume integral
* Defined relative velocity as
  (\mathbf{V}*{r}=\mathbf{V}-\mathbf{V}*{\mathrm{CV}})
* Clarified that absolute velocity determines transported momentum, while relative velocity determines control-surface crossing
* Removed the momentum-flux correction factor from the accumulation term
* Clarified the distinction between the force exerted by the wall on the fluid and the force exerted by the fluid on the wall
* Revised the non-inertial-frame notation using absolute, relative, translational, Coriolis, Euler, and rotational acceleration terms
* Improved the theoretical explanations, unit notation, and test descriptions

### Physical interpretation

Integral linear-momentum analysis can determine:

* the net momentum flux through a control surface;
* the resultant external force acting on the fluid;
* pressure-force contributions;
* wall and support reaction forces;
* the effect of changes in flow speed and direction;
* the relative velocity associated with a moving control surface.

However, it does not directly determine:

* the complete internal velocity field;
* local velocity gradients;
* local shear-stress distributions;
* spatial pressure gradients;
* the formation of a viscous velocity profile.

These limitations explain why the project must proceed from integral analysis to differential conservation equations.

### Result

The first-stage study of the integral linear-momentum equation was completed.

The notebook is sufficiently organized and verified for upload to the project repository after final filename and documentation checks.

### Next step

Study the integral energy equation and compare it with Bernoulli’s equation.

The next stage should examine:

* energy accumulation in a control volume;
* energy transport by mass flow;
* flow work;
* kinetic and potential energy terms;
* heat transfer and shaft work;
* mechanical-energy losses;
* kinetic-energy correction factors;
* conditions under which Bernoulli’s equation is insufficient.

### Summary

비균일 속도 분포에서 평균 속도만으로 운동량 유량을 계산할 수 없는 이유와 운동량 보정계수의 역할을 정리하였다. 움직이는 검사체적에서는 절대 속도와 상대 속도를 구분하였고, 비관성계에서는 병진 및 회전에 따른 추가 가속도 항을 학습하였다.

구현한 함수와 대표 계산 결과에 대해 정상 사례, 극한 사례, 잘못된 입력, 비균일 속도 분포 및 운동량 residual 검증을 수행하였다. 이를 통해 적분 선형 운동량 해석 파트의 1차 개념 학습과 계산 노트 작성을 마무리하였다. 이후 적분 에너지 방정식을 학습하고 Bernoulli 방정식과의 차이점과 점성 손실의 의미를 분석할 예정이다.

## 2026-07-22

### Topic

Angular momentum balance for a control volume

### Reviewed

- Definition of angular momentum for a fluid system
- Moment of force about a reference point
- Material derivative of angular momentum
- Application of the Reynolds Transport Theorem
- Difference between angular momentum and its time rate of change
- Integral angular-momentum equation for a fixed control volume

### Work completed

- Started the draft notebook for the angular-momentum-balance section
- Derived the relation between the moment of external forces and the rate of change of angular momentum
- Applied the Reynolds Transport Theorem to angular momentum

### Difficulties

- Distinguishing angular momentum itself from its material time derivative
- Connecting the particle-level moment equation to the system-level integral equation
- Determining where the material derivative and system integral should appear
- Keeping the angular-momentum notation consistent with the expressions used in the lecture

### Result

Created a preliminary theory draft for the angular-momentum-balance notebook.

The draft now separates the angular momentum of the system from its time rate of change and connects the system equation to the Reynolds Transport Theorem.

### Remaining work

- Complete the computational implementation
- Add a one-dimensional steady-flow form
- Include an application example
- Verify vector directions, signs, and units
- Expand the physical interpretation of each term
- Review and complete the notebook structure

### Next step

On July 23, implement the angular-momentum flux calculation and organize the computational section.

On July 24, strengthen the derivation, physical interpretation, and application example to complete the angular-momentum-balance notebook.

### Summary

유동의 적분해석: 각운동량 보존법칙에 대해 공부하였다. 이에 대해 간단한 공식 유도 초안 노트를 작성하였다.

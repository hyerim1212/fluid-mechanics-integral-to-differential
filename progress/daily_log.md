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
- 
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
적분형 선형 운동량 방정식의 우도 -> 단순화된 선현 운동량 방정식 -> 선형 운동량 방정식의 적용 -> 유동 방향의 변화 -> 압력 및 속도 변화 -> 무게, 압력, 마찰 및 비균일 속도 -> 비균일 압력 ->움직이는 검사체적 까지 개념에 대한 공부를 진행하였으며, 이에 대한 계산 및 검증 내용을 담은 노트를 작성하였다. 이후 개념 부분에 대한 노트 정리와 비관성계에 관한 남은 개념을 공부하고, 유동의 적분해석: 선형 운동량 보존에 대한 파트 1차 개념 공부를 마무리할 예정이다.
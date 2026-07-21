import math

def cross_sectional_area(diameter):
    """ 
    Calculate the area when the flow through the circular pipe.
    
    parameters 
    ------------
    diameter: float, inner diameter of the pipe in [m].
    
    return
    ------------
    float, cross-sectional area in [m^2].
    """

    if diameter <= 0:
        raise ValueError("Diameter must be positive.")

    return (math.pi * diameter**2)/4

def mass_flow_rate(rho, area, normal_speed):
    """
    Calculate mass flow rate assuming uniform density and uniform normal velocity.

    parameter 
    ------------
    rho: float, In this case, rho is constant in [kg/m^3].
    area: float, cross-sectional area in [m^2].
    normal_speed: float,  Velocity component normal to the cross-sectional area in [m/s].

    return
    ------------
    float, mass flow rate in kg/s
    """
    
    if rho <= 0:
        raise ValueError("Density must be positive.")
    if area <= 0 :
        raise ValueError("Area must be positive.")
    if normal_speed < 0:
        raise ValueError("Velocity magnitude must be nonnegative.")

    return rho*area*normal_speed

def mass_balance(inlet_rates, outlet_rates):
    """
    Calculate the mass balance of a control volume.

    parameters 
    ------------
    inlet_rates: float, mass flow rate of each entrance in [kg/s]. Please enter the rate with the list.
    outlet_rates: float, mass flow rate of each exit in [kg/s].  Please enter the rate with the list.

    All inlet and outlet rates are entered as nonnegative magnitudes.
    The accumulation rate is defined as total inflow minus total outflow.

    returns
    ------------
    total_inflow: float, summation of inlet rates of the whole entrance in [kg/s].
    total_outflow: float, summation of outlet rates of the whole exit in [kg/s].
    accumulation_rate: float, net mass flow rate of control volume in [kg/s].
    """

    if not isinstance(inlet_rates, list):
        raise TypeError("inlet_rates must be list.")

    if not isinstance(outlet_rates, list):
        raise TypeError("outlet_rates must be list.")

    if not all(isinstance(rate, (int, float)) for rate in inlet_rates):
        raise TypeError("All inlet rates must be numbers.")

    if not all(isinstance(rate, (int, float)) for rate in outlet_rates):
        raise TypeError("All outlet rates must be numbers.")

    if any(rate < 0 for rate in inlet_rates):
        raise ValueError("Inlet rates must be nonnegative.")

    if any(rate < 0 for rate in outlet_rates):
        raise ValueError("Outlet rates must be nonnegative.")


    net_inlet = sum(inlet_rates)
    net_outlet = sum(outlet_rates)

    accumulation_rate = net_inlet - net_outlet

    return {
        "total_inflow": net_inlet,
        "total_outflow": net_outlet,
        "accumulation_rate": accumulation_rate
    }

def outlet_velocity(total_inflow, known_outflow, outlet_density, outlet_area):
    """
    Calculate an unknown outlet velocity from steady mass conservation.

    parameters
    ------------
    total_inflow: float, summation of the mass flow rate of the whole entrance in [kg/s]
    known_outflow: float, summation of the mass flow rate of the whole existing system that we already know, in [kg/s].
    outlet_density: float, density of the exit that we are unknown in [kg/m^3].
    outlet_area: float, area of the exit that we are unknown in [m^2]

    All inlet and outlet rates are entered as nonnegative magnitudes.

    returns
    ------------
    float, average velocity of unknown outlet in [m/s].
    
    """
    if total_inflow < 0: 
        raise ValueError("total_inflow must be nonnegative.")
    if known_outflow < 0:
        raise ValueError("known_outflow must be nonnegative.")
    if outlet_density <= 0:
        raise ValueError("Density must be positive.")
    if outlet_area <= 0:
        raise ValueError("Area must be positive.")

    unknown_outlet_flow = (total_inflow - known_outflow)

    if unknown_outlet_flow < 0:
        raise ValueError("Those entered conditions are not correct for the flow direction.")

    average_velocity = unknown_outlet_flow/(outlet_density*outlet_area)

    return average_velocity

def tank_height(initial_height, inlet_flow_rate, outlet_flow_rate, tank_area, time):
    """    
    Calculate the liquid height in a constant-area tank with constant inlet and outlet volume flow rates.
    This function only works under these conditions: 
    1. Tank's area is constant.
    2. Fluid is an incompressible fluid.
    3. In volumetric flow and out volumetric flow are constant over time.
    4. Exit volumetric flow does not depend on the level of water.
    5. The free surface of the inner tank fluid is horizontal.

    parameters
    ------------
    initial_height: float, Initial water level in [m]. 
    inlet_flow_rate: float, The volumetric flow that enters the tank in [m^3/s].
    outlet_flow_rate: float, The volumetric flow that exits the tank in [m^3/s].
    tank_area: float, Horizontal area of the tank in [m^2].
    time: float, elapsed time in [s].
    
 
    returns
    ------------
    float, water level at that time [m].
    
    """

    if initial_height < 0: 
        raise ValueError("initial_height must be nonnegative.")

    if inlet_flow_rate < 0: 
        raise ValueError("inlet_flow_rate must be nonnegative.")

    if outlet_flow_rate < 0: 
        raise ValueError("outlet_flow_rate must be nonnegative.")

    if tank_area <= 0:
        raise ValueError("Area must be positive.")

    if time < 0:
        raise ValueError("Time must be nonnegative.")

    height = initial_height + ((inlet_flow_rate - outlet_flow_rate)/tank_area)*time
    
    if height < 0:

        empty_time = tank_area * initial_height / (outlet_flow_rate - inlet_flow_rate)
        
        raise ValueError(
            "The calculated height is negative. "
            "The tank becomes empty before the specified time."
            f"The tank becomes empty at t = {empty_time:.3f} s.")

    return height

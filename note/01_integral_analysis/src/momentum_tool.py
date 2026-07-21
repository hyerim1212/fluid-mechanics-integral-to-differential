import numpy as np

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
    float, mass flow rate in [kg/s]
    """
    
    if rho <= 0:
        raise ValueError("Density must be positive.")
    if area <= 0 :
        raise ValueError("Area must be positive.")
    if normal_speed < 0:
        raise ValueError("Velocity magnitude must be nonnegative.")

    return rho*area*normal_speed

def net_momentum_flux(inlets:list[dict], outlets:list[dict])->np.ndarray: 
    """
    Calculate the net momentum flux for a steady control volume with multiple inlets and outlets.

    Each inlet or outlet is a dictionary:
    { 
      "velocity": [vx,vy,vz],
      "mass_flow_rate": float in [kg/s],
    }

    Please write information for each in/outlet into the dictionary, and create an in/out list containing those dictionaries. 

    return
    ------------
    numpy.ndarray
    Net momentum flux vector of multiple in/outlets in [kg*m/s^2]
    """
    
    in_momentum = np.zeros(3, dtype = float)
    out_momentum = np.zeros(3, dtype = float)

    for inlet in inlets:
        
        velocity = np.asarray(inlet["velocity"], dtype = float)
        if velocity.shape != (3,):
            raise ValueError("Each inlet velocity must have three components.")
            
        mdot = float(inlet["mass_flow_rate"])      
        if mdot < 0: 
            raise ValueError("Mass flow rate must be nonnegative.")
            
        in_momentum += velocity*mdot
        
    for outlet in outlets:
        
        velocity = np.asarray(outlet["velocity"], dtype = float)
        if velocity.shape != (3,):
            raise ValueError("Each outlet velocity must have three components.")
            
        mdot = float(outlet["mass_flow_rate"])
        if mdot < 0: 
            raise ValueError("Mass flow rate must be nonnegative.")
            
        out_momentum += velocity*mdot

    net_momentum = out_momentum - in_momentum
    
    return net_momentum # [x, y, z]

def relative_velocity(flow_velocity:list, inspection_surface_velocity:list) -> np.ndarray:
    """
    Calculate the relative velocity.

    parameters
    ------------
    flow_velocity: please write velocity to [vx, vy, vz], [m/s]
    inspection_surface_velocity: please write velocity to [vx, vy, vz], [m/s]

    return
    ------------
    numpy.ndarray
        Relative velocity vector [vx, vy, vz] in m/s
    """

    flow_velocity = np.array(flow_velocity, dtype = float)
    if flow_velocity.shape != (3,):
        raise ValueError(
            "flow_velocity must contain exactly three components."
        )

    inspection_surface_velocity = np.array(inspection_surface_velocity, dtype = float)
    if inspection_surface_velocity.shape != (3,):
        raise ValueError(
            "inspection_surface_velocity must contain exactly three components."
        )
    
    relative_velocity = flow_velocity - inspection_surface_velocity # [x, y, z]

    return relative_velocity
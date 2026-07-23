import numpy as np

def mass_flow_rate(rho, area, velocity:tuple, normal:tuple):
    """
    Calculate mass flow rate assuming uniform density and uniform normal velocity.

    parameter 
    ------------
    rho: float, In this case, rho is constant in [kg/m^3].
    area: float, cross-sectional area in [m^2].
    velocity: tuple, velocity of fluid in [m/s]
    normal: tuple,  normal: tuple, outward unit normal vector of the control surface, dimensionless.

    return
    ------------
    float, signed mass flow rate in [kg/s]
    """

    if rho <= 0 :
        raise ValueError("rho must be positive.")

    if area <= 0 :
        raise ValueError("area must be positive.")

    velocity = np.array(velocity, dtype = float)
    normal = np.array(normal, dtype = float)

    if not velocity.shape == (3,):
        raise ValueError("velocity must have three components.")
        
    if not normal.shape == (3,):
        raise ValueError("normal must have three components.")

    if not np.isclose(np.linalg.norm(normal), 1.0):
        raise ValueError("magnitude of normal vector must be 1.")
    
    dot_product = np.dot(velocity, normal)

    mdot = rho*area*dot_product

    return mdot

def specific_angular_momentum(position: tuple, velocity: tuple):
    """
    Calculate specific angular momentum.

    parameter 
    ------------
    position: tuple, position: tuple, position vector measured from the reference point O, in [m].
    velocity: tuple, velocity of fluid in [m/s]

    return
    ------------
    np.ndarray, specific angular momentum in [m^2/s]

    """
    
    position = np.array(position, dtype = float)
    velocity = np.array(velocity, dtype = float)

    if not position.shape == (3,):
        raise ValueError("position must have three components.")
        
    if not velocity.shape == (3,):
        raise ValueError("velocity must have three components.")
    
    specific_angular_momentum = np.cross(position, velocity)

    return specific_angular_momentum



def angular_momentum_flux(rho, area, position, velocity, normal):
    """
    Calculate the signed angular-momentum flux through a control surface.

    parameter 
    ------------
    rho: float, In this case, rho is constant in [kg/m^3].
    area: float, cross-sectional area in [m^2].
    position: tuple, position: array-like, position vector measured from reference point O, in [m].
    velocity: a tuple, the velocity of the fluid in [m/s]
    normal: array-like, outward unit normal vector, dimensionless.

    return
    ------------
    np.ndarray, angular momentum flux in [N*m]
    """

    position = np.array(position, dtype = float)
    velocity = np.array(velocity, dtype = float)
    normal = np.array(normal, dtype = float)

    if not position.shape == (3,):
        raise ValueError("position must have three components.")
        
    angular_momentum_flux = mass_flow_rate(rho, area, velocity, normal)*specific_angular_momentum(position, velocity)
    
    return angular_momentum_flux


def net_external_torque(streams):
    """
    Calculate net external torque. For a fixed control volume under steady-flow conditions.

    parameter 
    ------------

      Each stream is a dictionary:
    { 
      "rho": float, In this case, rho is constant in [kg/m^3],
      "area": float, cross-sectional area in [m^2],
      "position": array-like, position vector measured from the reference point O, in [m].
      "velocity": a tuple, the velocity of the fluid in [m/s]
      "normal": tuple, outward unit normal vector of the control surface, dimensionless.
    }

    return
    ------------
    np.ndarray, torque in [N*m]
    """
    
    torque = np.zeros(3, dtype=float)

    for stream in streams :
        
        rho = stream["rho"]
        area = stream["area"]
        position = stream["position"]
        velocity = stream["velocity"]
        normal = stream["normal"]
        
        torque += angular_momentum_flux(rho, area, position, velocity, normal)

    return torque
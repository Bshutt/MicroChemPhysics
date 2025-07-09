"""
Physics calculation functions for MicroPython
Optimized for memory efficiency on graphing calculators
"""

import math
from constants import *

def constant_acceleration(v0, a, t):
    """
    Kinematic equations for constant acceleration
    Returns position, velocity, and acceleration
    """
    v = v0 + a * t
    x = v0 * t + 0.5 * a * t**2
    
    return {
        'position': x,
        'velocity': v,
        'acceleration': a,
        'time': t
    }

def projectile_motion(v0, angle_deg):
    """
    Projectile motion calculations
    Returns range, max height, and flight time
    """
    angle_rad = math.radians(angle_deg)
    g = GRAVITY
    
    # Components of initial velocity
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    # Flight time
    flight_time = 2 * v0y / g
    
    # Maximum height
    max_height = (v0y**2) / (2 * g)
    
    # Range
    range_x = v0x * flight_time
    
    return {
        'range': range_x,
        'max_height': max_height,
        'flight_time': flight_time,
        'v0x': v0x,
        'v0y': v0y
    }

def newtons_second_law(mass, acceleration):
    """
    Newton's second law: F = ma
    """
    if mass <= 0:
        raise ValueError("Mass must be positive")
    
    return mass * acceleration

def friction_force(coefficient, normal_force):
    """
    Friction force: f = μN
    """
    if coefficient < 0 or normal_force < 0:
        raise ValueError("Coefficient and normal force must be non-negative")
    
    return coefficient * normal_force

def centripetal_force(mass, velocity, radius):
    """
    Centripetal force: F = mv²/r
    """
    if mass <= 0 or radius <= 0:
        raise ValueError("Mass and radius must be positive")
    
    return (mass * velocity**2) / radius

def kinetic_energy(mass, velocity):
    """
    Kinetic energy: KE = ½mv²
    """
    if mass <= 0:
        raise ValueError("Mass must be positive")
    
    return 0.5 * mass * velocity**2

def gravitational_potential_energy(mass, height, g=GRAVITY):
    """
    Gravitational potential energy: PE = mgh
    """
    if mass <= 0:
        raise ValueError("Mass must be positive")
    
    return mass * g * height

def work_done(force, distance, angle_deg=0):
    """
    Work done: W = F·d·cos(θ)
    """
    angle_rad = math.radians(angle_deg)
    return force * distance * math.cos(angle_rad)

def power_calculation(work, time):
    """
    Power: P = W/t
    """
    if time <= 0:
        raise ValueError("Time must be positive")
    
    return work / time

def heat_transfer(mass, specific_heat, temp_change):
    """
    Heat transfer: Q = mcΔT
    """
    if mass <= 0 or specific_heat <= 0:
        raise ValueError("Mass and specific heat must be positive")
    
    return mass * specific_heat * temp_change

def thermal_expansion(initial_length, expansion_coeff, temp_change):
    """
    Linear thermal expansion: ΔL = αL₀ΔT
    """
    if initial_length <= 0:
        raise ValueError("Initial length must be positive")
    
    return expansion_coeff * initial_length * temp_change

def ideal_gas_work(pressure, volume_change):
    """
    Work done by ideal gas at constant pressure: W = PΔV
    """
    return pressure * volume_change

def carnot_efficiency(hot_temp, cold_temp):
    """
    Carnot engine efficiency: η = 1 - Tc/Th
    """
    if hot_temp <= 0 or cold_temp <= 0:
        raise ValueError("Temperatures must be positive (Kelvin)")
    
    if cold_temp >= hot_temp:
        raise ValueError("Cold temperature must be less than hot temperature")
    
    return 1 - (cold_temp / hot_temp)

def wave_speed(frequency, wavelength):
    """
    Wave speed: v = fλ
    """
    if frequency <= 0 or wavelength <= 0:
        raise ValueError("Frequency and wavelength must be positive")
    
    return frequency * wavelength

def simple_harmonic_motion(amplitude, angular_freq, time, phase=0):
    """
    Simple harmonic motion: x = A·cos(ωt + φ)
    """
    return amplitude * math.cos(angular_freq * time + phase)

def pendulum_period(length, g=GRAVITY):
    """
    Simple pendulum period: T = 2π√(L/g)
    """
    if length <= 0:
        raise ValueError("Length must be positive")
    
    return 2 * math.pi * math.sqrt(length / g)

def spring_period(mass, spring_constant):
    """
    Mass-spring system period: T = 2π√(m/k)
    """
    if mass <= 0 or spring_constant <= 0:
        raise ValueError("Mass and spring constant must be positive")
    
    return 2 * math.pi * math.sqrt(mass / spring_constant)

def coulomb_force(q1, q2, distance):
    """
    Coulomb's law: F = k·q1·q2/r²
    """
    if distance <= 0:
        raise ValueError("Distance must be positive")
    
    return COULOMB_CONSTANT * q1 * q2 / (distance**2)

def electric_field(charge, distance):
    """
    Electric field: E = k·q/r²
    """
    if distance <= 0:
        raise ValueError("Distance must be positive")
    
    return COULOMB_CONSTANT * charge / (distance**2)

def electric_potential(charge, distance):
    """
    Electric potential: V = k·q/r
    """
    if distance <= 0:
        raise ValueError("Distance must be positive")
    
    return COULOMB_CONSTANT * charge / distance

def ohms_law(voltage=0, current=0, resistance=0):
    """
    Ohm's law: V = IR
    Calculate missing variable when 2 are known
    """
    known_count = sum(1 for x in [voltage, current, resistance] if x != 0)
    
    if known_count != 2:
        raise ValueError("Exactly 2 variables must be non-zero")
    
    result = {'V': voltage, 'I': current, 'R': resistance}
    
    if voltage == 0:
        result['V'] = current * resistance
    elif current == 0:
        if resistance == 0:
            raise ValueError("Cannot calculate current with zero resistance")
        result['I'] = voltage / resistance
    elif resistance == 0:
        if current == 0:
            raise ValueError("Cannot calculate resistance with zero current")
        result['R'] = voltage / current
    
    return result

def electrical_power(voltage=0, current=0, resistance=0):
    """
    Electrical power calculations
    P = VI = I²R = V²/R
    """
    if voltage != 0 and current != 0:
        return voltage * current
    elif current != 0 and resistance != 0:
        return current**2 * resistance
    elif voltage != 0 and resistance != 0:
        return voltage**2 / resistance
    else:
        raise ValueError("Need at least 2 non-zero parameters")

def magnetic_force(charge, velocity, magnetic_field, angle_deg=90):
    """
    Magnetic force on moving charge: F = qvB·sin(θ)
    """
    angle_rad = math.radians(angle_deg)
    return abs(charge) * velocity * magnetic_field * math.sin(angle_rad)

def faraday_law(magnetic_flux_change, time):
    """
    Faraday's law of induction: ε = -dΦ/dt
    """
    if time <= 0:
        raise ValueError("Time must be positive")
    
    return -magnetic_flux_change / time

def lens_equation(focal_length=0, object_distance=0, image_distance=0):
    """
    Thin lens equation: 1/f = 1/do + 1/di
    Calculate missing variable when 2 are known
    """
    known_count = sum(1 for x in [focal_length, object_distance, image_distance] if x != 0)
    
    if known_count != 2:
        raise ValueError("Exactly 2 variables must be non-zero")
    
    result = {'f': focal_length, 'do': object_distance, 'di': image_distance}
    
    if focal_length == 0:
        result['f'] = 1 / (1/object_distance + 1/image_distance)
    elif object_distance == 0:
        result['do'] = 1 / (1/focal_length - 1/image_distance)
    elif image_distance == 0:
        result['di'] = 1 / (1/focal_length - 1/object_distance)
    
    return result

def doppler_effect(source_freq, source_velocity, observer_velocity, wave_speed):
    """
    Doppler effect: f' = f(v ± vo)/(v ± vs)
    Positive velocities: moving toward each other
    """
    return source_freq * (wave_speed + observer_velocity) / (wave_speed - source_velocity)

def relativistic_energy(mass, velocity):
    """
    Relativistic total energy: E = γmc²
    """
    c = SPEED_OF_LIGHT
    
    if velocity >= c:
        raise ValueError("Velocity must be less than speed of light")
    
    gamma = 1 / math.sqrt(1 - (velocity/c)**2)
    return gamma * mass * c**2

def de_broglie_wavelength(mass, velocity):
    """
    de Broglie wavelength: λ = h/mv
    """
    if mass <= 0 or velocity <= 0:
        raise ValueError("Mass and velocity must be positive")
    
    return PLANCK_CONSTANT / (mass * velocity)

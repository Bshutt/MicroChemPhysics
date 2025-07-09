"""
Physical and mathematical constants for chemistry and physics calculations
Optimized for MicroPython memory efficiency
"""

import math

# Mathematical constants
PI = math.pi
E = math.e

# Physical constants (SI units unless noted)
SPEED_OF_LIGHT = 2.998e8          # m/s
PLANCK_CONSTANT = 6.626e-34       # J·s
PLANCK_REDUCED = 1.055e-34        # ħ = h/(2π), J·s
BOLTZMANN_CONSTANT = 1.381e-23    # J/K
AVOGADRO_NUMBER = 6.022e23        # mol⁻¹
ELECTRON_CHARGE = 1.602e-19       # C
ELECTRON_MASS = 9.109e-31         # kg
PROTON_MASS = 1.673e-27           # kg
NEUTRON_MASS = 1.675e-27          # kg
ATOMIC_MASS_UNIT = 1.661e-27      # kg

# Gas constant (multiple units for convenience)
GAS_CONSTANT = 0.08206            # L·atm/(mol·K)
GAS_CONSTANT_J = 8.314            # J/(mol·K)

# Gravitational constants
GRAVITY = 9.807                   # m/s² (standard gravity)
GRAVITATIONAL_CONSTANT = 6.674e-11  # N·m²/kg²

# Electromagnetic constants
COULOMB_CONSTANT = 8.988e9        # N·m²/C²
VACUUM_PERMITTIVITY = 8.854e-12   # C²/(N·m²)
VACUUM_PERMEABILITY = 4e-7 * PI   # N/A²
FARADAY_CONSTANT = 96485          # C/mol

# Energy conversion factors
ELECTRON_VOLT = 1.602e-19         # J (1 eV in Joules)
CALORIE = 4.184                   # J (1 cal in Joules)
BTU = 1055                        # J (1 BTU in Joules)

# Atomic and molecular constants
BOHR_RADIUS = 5.292e-11           # m
RYDBERG_CONSTANT = 1.097e7        # m⁻¹
FINE_STRUCTURE_CONSTANT = 7.297e-3  # dimensionless

# Thermodynamic constants
STEFAN_BOLTZMANN = 5.670e-8       # W/(m²·K⁴)
WIEN_DISPLACEMENT = 2.898e-3      # m·K

# Standard conditions
STP_TEMPERATURE = 273.15          # K (0°C)
STP_PRESSURE = 101325             # Pa (1 atm)
STANDARD_ATMOSPHERE = 101325      # Pa

# Mathematical conversion factors
DEGREES_TO_RADIANS = PI / 180
RADIANS_TO_DEGREES = 180 / PI

# Common logarithms
LN_10 = math.log(10)              # Natural log of 10
LOG10_E = math.log10(E)           # Log base 10 of e

# Chemistry-specific constants
WATER_DENSITY = 1000              # kg/m³ at 4°C
WATER_MOLAR_MASS = 18.015         # g/mol
IDEAL_GAS_MOLAR_VOLUME = 22.414   # L/mol at STP

# Physics-specific constants
MAGNETIC_FLUX_QUANTUM = 2.068e-15 # Wb
CONDUCTANCE_QUANTUM = 7.748e-5    # S
RESISTANCE_QUANTUM = 12906        # Ω

# Unit conversion factors
# Length
CM_TO_M = 0.01
MM_TO_M = 0.001
KM_TO_M = 1000
INCH_TO_M = 0.0254
FOOT_TO_M = 0.3048

# Mass
G_TO_KG = 0.001
LB_TO_KG = 0.453592

# Energy
CAL_TO_J = 4.184
KCAL_TO_J = 4184
KWH_TO_J = 3.6e6

# Pressure
ATM_TO_PA = 101325
TORR_TO_PA = 133.322
PSI_TO_PA = 6895

# Temperature conversion functions
def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9/5 + 32

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Common physical properties (for quick reference)
COMMON_DENSITIES = {
    'water': 1000,      # kg/m³
    'air': 1.225,       # kg/m³ at STP
    'aluminum': 2700,   # kg/m³
    'iron': 7870,       # kg/m³
    'copper': 8960,     # kg/m³
    'gold': 19300,      # kg/m³
    'lead': 11340       # kg/m³
}

COMMON_SPECIFIC_HEATS = {
    'water': 4186,      # J/(kg·K)
    'air': 1005,        # J/(kg·K)
    'aluminum': 897,    # J/(kg·K)
    'iron': 449,        # J/(kg·K)
    'copper': 385,      # J/(kg·K)
    'gold': 129,        # J/(kg·K)
    'ice': 2090         # J/(kg·K)
}

# Periodic table data (simplified for memory efficiency)
PERIODIC_SYMBOLS = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca'
]

ATOMIC_NUMBERS = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8,
    'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15,
    'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20
}

# Error tolerance for floating point comparisons
FLOAT_TOLERANCE = 1e-10

def approx_equal(a, b, tolerance=FLOAT_TOLERANCE):
    """Check if two floating point numbers are approximately equal"""
    return abs(a - b) < tolerance

# Common mathematical functions optimized for calculators
def safe_sqrt(x):
    """Square root with domain checking"""
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def safe_log(x, base=E):
    """Logarithm with domain checking"""
    if x <= 0:
        raise ValueError("Cannot take logarithm of non-positive number")
    if base == E:
        return math.log(x)
    elif base == 10:
        return math.log10(x)
    else:
        return math.log(x) / math.log(base)

def safe_asin(x):
    """Arcsine with domain checking"""
    if abs(x) > 1:
        raise ValueError("Arcsine domain error: |x| must be ≤ 1")
    return math.asin(x)

def safe_acos(x):
    """Arccosine with domain checking"""
    if abs(x) > 1:
        raise ValueError("Arccosine domain error: |x| must be ≤ 1")
    return math.acos(x)

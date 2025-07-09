"""
Chemistry calculation functions for MicroPython
Optimized for memory efficiency on graphing calculators
"""

import math
from constants import *

# Atomic masses dictionary (simplified for memory efficiency)
ATOMIC_MASSES = {
    'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
    'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
    'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.086, 'P': 30.974,
    'S': 32.066, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.38, 'Br': 79.904, 'I': 126.904
}

def molecular_weight(formula):
    """
    Calculate molecular weight from chemical formula
    Example: molecular_weight("H2O") returns 18.015
    """
    if not formula:
        raise ValueError("Formula cannot be empty")
    
    total_mass = 0
    i = 0
    
    while i < len(formula):
        # Get element symbol
        if i + 1 < len(formula) and formula[i + 1].islower():
            element = formula[i:i + 2]
            i += 2
        else:
            element = formula[i]
            i += 1
        
        # Get count
        count_str = ""
        while i < len(formula) and formula[i].isdigit():
            count_str += formula[i]
            i += 1
        
        count = int(count_str) if count_str else 1
        
        if element not in ATOMIC_MASSES:
            raise ValueError(f"Unknown element: {element}")
        
        total_mass += ATOMIC_MASSES[element] * count
    
    return total_mass

def ideal_gas_law(P=0, V=0, n=0, T=0):
    """
    Ideal Gas Law: PV = nRT
    Calculate missing variable when 3 are known
    Returns dictionary with all values
    """
    known_count = sum(1 for x in [P, V, n, T] if x != 0)
    
    if known_count != 3:
        raise ValueError("Exactly 3 variables must be non-zero")
    
    R = GAS_CONSTANT  # 0.08206 L·atm/(mol·K)
    
    result = {'P': P, 'V': V, 'n': n, 'T': T}
    
    if P == 0:
        result['P'] = (n * R * T) / V
    elif V == 0:
        result['V'] = (n * R * T) / P
    elif n == 0:
        result['n'] = (P * V) / (R * T)
    elif T == 0:
        result['T'] = (P * V) / (n * R)
    
    return result

def calculate_ph(h_concentration):
    """
    Calculate pH from H+ concentration
    pH = -log[H+]
    """
    if h_concentration <= 0:
        raise ValueError("H+ concentration must be positive")
    
    return -math.log10(h_concentration)

def ph_to_concentration(ph):
    """
    Calculate H+ concentration from pH
    [H+] = 10^(-pH)
    """
    if ph < 0 or ph > 14:
        raise ValueError("pH must be between 0 and 14")
    
    return 10**(-ph)

def dilution_calculation(C1, V1, C2=0, V2=0):
    """
    Dilution calculation: C1V1 = C2V2
    Calculate missing variable
    """
    if C1 <= 0 or V1 <= 0:
        raise ValueError("Initial concentration and volume must be positive")
    
    if C2 == 0 and V2 == 0:
        raise ValueError("Either final concentration or final volume must be specified")
    
    result = {'C1': C1, 'V1': V1, 'C2': C2, 'V2': V2}
    
    if C2 == 0:
        result['C2'] = (C1 * V1) / V2
    elif V2 == 0:
        result['V2'] = (C1 * V1) / C2
    
    return result

def rate_constant(rate, conc_a, conc_b, order_a, order_b):
    """
    Calculate rate constant from rate law
    Rate = k[A]^m[B]^n
    k = Rate / ([A]^m * [B]^n)
    """
    if rate <= 0 or conc_a <= 0 or conc_b <= 0:
        raise ValueError("Rate and concentrations must be positive")
    
    denominator = (conc_a ** order_a) * (conc_b ** order_b)
    
    if denominator == 0:
        raise ValueError("Concentration terms cannot be zero")
    
    return rate / denominator

def particle_in_box_energy(n, L, mass):
    """
    Energy of particle in 1D box
    E = n²h²/(8mL²)
    """
    if n <= 0 or L <= 0 or mass <= 0:
        raise ValueError("All parameters must be positive")
    
    return (n**2 * PLANCK_CONSTANT**2) / (8 * mass * L**2)

def harmonic_oscillator_energy(v, frequency):
    """
    Harmonic oscillator energy levels
    E = hf(v + 1/2)
    """
    if v < 0 or frequency <= 0:
        raise ValueError("v must be non-negative, frequency must be positive")
    
    return PLANCK_CONSTANT * frequency * (v + 0.5)

def hydrogen_energy_level(n):
    """
    Hydrogen atom energy levels
    E = -13.6 eV / n²
    """
    if n <= 0:
        raise ValueError("Principal quantum number must be positive")
    
    return -13.6 * ELECTRON_VOLT / (n**2)

def arrhenius_equation(A, Ea, T):
    """
    Arrhenius equation for reaction rate
    k = A * exp(-Ea/RT)
    """
    if A <= 0 or Ea < 0 or T <= 0:
        raise ValueError("A and T must be positive, Ea must be non-negative")
    
    return A * math.exp(-Ea / (GAS_CONSTANT_J * T))

def henderson_hasselbalch(pKa, conc_base, conc_acid):
    """
    Henderson-Hasselbalch equation
    pH = pKa + log([A-]/[HA])
    """
    if conc_base <= 0 or conc_acid <= 0:
        raise ValueError("Concentrations must be positive")
    
    return pKa + math.log10(conc_base / conc_acid)

def nernst_equation(E_standard, n, Q, T=298.15):
    """
    Nernst equation for cell potential
    E = E° - (RT/nF)ln(Q)
    """
    if n <= 0:
        raise ValueError("Number of electrons must be positive")
    
    R = GAS_CONSTANT_J  # J/(mol·K)
    F = FARADAY_CONSTANT  # C/mol
    
    return E_standard - (R * T / (n * F)) * math.log(Q)

def beer_lambert_law(epsilon, path_length, concentration):
    """
    Beer-Lambert law for absorbance
    A = ε * l * c
    """
    if epsilon < 0 or path_length <= 0 or concentration < 0:
        raise ValueError("Invalid parameters for Beer-Lambert law")
    
    return epsilon * path_length * concentration

def van_der_waals_pressure(n, V, T, a, b):
    """
    Van der Waals equation of state
    P = (nRT)/(V-nb) - an²/V²
    """
    if n <= 0 or V <= 0 or T <= 0:
        raise ValueError("n, V, and T must be positive")
    
    if V <= n * b:
        raise ValueError("Volume too small for van der Waals equation")
    
    R = GAS_CONSTANT_J
    term1 = (n * R * T) / (V - n * b)
    term2 = (a * n**2) / (V**2)
    
    return term1 - term2

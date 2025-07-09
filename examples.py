"""
Example calculations and use cases for the computational chemistry and physics calculator
Demonstrates practical applications for graphing calculator users
"""

from chemistry import *
from physics import *
from constants import *
from utils import format_number, create_simple_table

def show_examples():
    """Display various example calculations"""
    print("=== Example Calculations ===")
    print("")
    
    print("CHEMISTRY EXAMPLES:")
    print("-" * 20)
    chemistry_examples()
    
    print("\nPHYSICS EXAMPLES:")
    print("-" * 17)
    physics_examples()
    
    print("\nUNIT CONVERSION EXAMPLES:")
    print("-" * 25)
    conversion_examples()

def chemistry_examples():
    """Chemistry calculation examples"""
    
    # Example 1: Molecular weight
    print("1. Molecular Weight Calculation")
    formula = "C6H12O6"  # Glucose
    mw = molecular_weight(formula)
    print(f"   {formula} = {mw:.2f} g/mol")
    
    # Example 2: Ideal Gas Law
    print("\n2. Ideal Gas Law")
    print("   Given: P=1 atm, V=22.4 L, T=273K")
    result = ideal_gas_law(P=1, V=22.4, T=273)
    print(f"   Moles = {result['n']:.3f} mol")
    
    # Example 3: pH calculation
    print("\n3. pH Calculation")
    h_conc = 1e-7  # Neutral water
    ph = calculate_ph(h_conc)
    print(f"   [H+] = {h_conc:.0e} M → pH = {ph:.1f}")
    
    # Example 4: Dilution
    print("\n4. Dilution Calculation")
    print("   Dilute 10 mL of 2M HCl to 100 mL")
    result = dilution_calculation(2, 10, V2=100)
    print(f"   Final concentration = {result['C2']:.2f} M")
    
    # Example 5: Quantum energy
    print("\n5. Particle in a Box Energy")
    n, L, m = 1, 1e-9, 9.109e-31  # electron, 1 nm box
    energy = particle_in_box_energy(n, L, m)
    print(f"   n=1, L=1nm: E = {energy:.2e} J")

def physics_examples():
    """Physics calculation examples"""
    
    # Example 1: Projectile motion
    print("1. Projectile Motion")
    print("   Ball thrown at 20 m/s, 45° angle")
    result = projectile_motion(20, 45)
    print(f"   Range = {result['range']:.1f} m")
    print(f"   Max height = {result['max_height']:.1f} m")
    
    # Example 2: Energy calculations
    print("\n2. Energy Calculations")
    mass, velocity = 2, 10  # 2 kg object at 10 m/s
    ke = kinetic_energy(mass, velocity)
    pe = gravitational_potential_energy(mass, 5)  # 5 m high
    print(f"   KE = {ke:.0f} J, PE = {pe:.0f} J")
    print(f"   Total mechanical energy = {ke + pe:.0f} J")
    
    # Example 3: Electrical calculations
    print("\n3. Ohm's Law")
    print("   12V battery, 3Ω resistor")
    result = ohms_law(voltage=12, resistance=3)
    current = result['I']
    power = electrical_power(voltage=12, current=current)
    print(f"   Current = {current:.1f} A")
    print(f"   Power = {power:.0f} W")
    
    # Example 4: Wave calculations
    print("\n4. Wave Properties")
    freq, wavelength = 440, 0.78  # A4 note in air
    speed = wave_speed(freq, wavelength)
    print(f"   f = {freq} Hz, λ = {wavelength} m")
    print(f"   Wave speed = {speed:.0f} m/s")
    
    # Example 5: Pendulum
    print("\n5. Simple Pendulum")
    length = 1.0  # 1 meter pendulum
    period = pendulum_period(length)
    print(f"   L = {length} m → T = {period:.2f} s")

def conversion_examples():
    """Unit conversion examples"""
    
    print("1. Temperature Conversions")
    temp_c = 25  # Room temperature
    temp_k = celsius_to_kelvin(temp_c)
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"   {temp_c}°C = {temp_k:.1f} K = {temp_f:.1f}°F")
    
    print("\n2. Energy Conversions")
    energy_j = 1000  # 1 kJ
    energy_cal = energy_j / CALORIE
    energy_ev = energy_j / ELECTRON_VOLT
    print(f"   {energy_j} J = {energy_cal:.0f} cal = {energy_ev:.2e} eV")
    
    print("\n3. Pressure Conversions")
    pressure_pa = 101325  # 1 atm
    pressure_atm = pressure_pa / ATM_TO_PA
    pressure_torr = pressure_pa / TORR_TO_PA
    print(f"   {pressure_pa} Pa = {pressure_atm:.0f} atm = {pressure_torr:.0f} Torr")

def worked_chemistry_problems():
    """Complete worked chemistry problems"""
    
    print("=== WORKED CHEMISTRY PROBLEMS ===")
    
    # Problem 1: Stoichiometry
    print("\nProblem 1: Combustion of Methane")
    print("CH4 + 2O2 → CO2 + 2H2O")
    print("How many grams of CO2 from 5.0 g CH4?")
    print("")
    
    # Calculate molar masses
    mw_ch4 = molecular_weight("CH4")
    mw_co2 = molecular_weight("CO2")
    
    print(f"Step 1: Molar masses")
    print(f"   CH4 = {mw_ch4:.1f} g/mol")
    print(f"   CO2 = {mw_co2:.1f} g/mol")
    
    # Convert to moles
    moles_ch4 = 5.0 / mw_ch4
    print(f"Step 2: Moles CH4 = 5.0g ÷ {mw_ch4:.1f} = {moles_ch4:.3f} mol")
    
    # Stoichiometry (1:1 ratio)
    moles_co2 = moles_ch4
    mass_co2 = moles_co2 * mw_co2
    print(f"Step 3: Moles CO2 = {moles_co2:.3f} mol")
    print(f"Step 4: Mass CO2 = {moles_co2:.3f} × {mw_co2:.1f} = {mass_co2:.1f} g")
    
    # Problem 2: Gas Law Problem
    print("\n" + "="*40)
    print("Problem 2: Gas Law Application")
    print("A gas occupies 2.5 L at 25°C and 1.2 atm.")
    print("What volume at STP?")
    print("")
    
    # Initial conditions
    V1, T1, P1 = 2.5, celsius_to_kelvin(25), 1.2
    # Final conditions (STP)
    T2, P2 = STP_TEMPERATURE, 1.0
    
    print(f"Initial: V1={V1} L, T1={T1:.1f} K, P1={P1} atm")
    print(f"Final (STP): T2={T2:.1f} K, P2={P2} atm")
    
    # Combined gas law: P1V1/T1 = P2V2/T2
    V2 = (P1 * V1 * T2) / (P2 * T1)
    print(f"Combined gas law: V2 = P1V1T2/(P2T1)")
    print(f"V2 = ({P1} × {V1} × {T2:.1f})/({P2} × {T1:.1f}) = {V2:.2f} L")

def worked_physics_problems():
    """Complete worked physics problems"""
    
    print("=== WORKED PHYSICS PROBLEMS ===")
    
    # Problem 1: Projectile Motion
    print("\nProblem 1: Projectile Motion")
    print("A ball is kicked at 15 m/s at 30° above horizontal.")
    print("Find: a) maximum height, b) range, c) time of flight")
    print("")
    
    v0, angle = 15, 30
    result = projectile_motion(v0, angle)
    
    print(f"Given: v₀ = {v0} m/s, θ = {angle}°")
    print(f"Components: v₀ₓ = {result['v0x']:.2f} m/s, v₀ᵧ = {result['v0y']:.2f} m/s")
    print("")
    print(f"a) Maximum height = {result['max_height']:.2f} m")
    print(f"b) Range = {result['range']:.2f} m") 
    print(f"c) Time of flight = {result['flight_time']:.2f} s")
    
    # Problem 2: Energy Conservation
    print("\n" + "="*40)
    print("Problem 2: Energy Conservation")
    print("A 0.5 kg ball falls from 10 m height.")
    print("Find velocity just before hitting ground.")
    print("")
    
    mass, height = 0.5, 10
    
    # Initial energy (all potential)
    pe_initial = gravitational_potential_energy(mass, height)
    print(f"Initial PE = mgh = {mass} × {GRAVITY:.1f} × {height} = {pe_initial:.1f} J")
    
    # Final energy (all kinetic)
    # PE_initial = KE_final
    # mgh = ½mv²
    # v = √(2gh)
    velocity = math.sqrt(2 * GRAVITY * height)
    ke_final = kinetic_energy(mass, velocity)
    
    print(f"At ground: PE = 0, KE = ½mv²")
    print(f"Energy conservation: {pe_initial:.1f} = ½ × {mass} × v²")
    print(f"Solving for v: v = √(2gh) = √(2 × {GRAVITY:.1f} × {height}) = {velocity:.1f} m/s")
    print(f"Check: KE = ½mv² = {ke_final:.1f} J ✓")

def calculator_specific_tips():
    """Tips for using on different calculator models"""
    
    print("=== CALCULATOR-SPECIFIC TIPS ===")
    print("")
    
    print("TI-84 Plus CE Python:")
    print("• Transfer .py files via TI Connect CE")
    print("• Use shell 'run main.py' to start")
    print("• Memory limit: ~32KB for user programs")
    print("• Screen: 320×240 pixels, ~40 chars wide")
    print("")
    
    print("NumWorks:")
    print("• Copy-paste code into Python app")
    print("• Built-in modules: math, random, time")
    print("• Screen: ~25 lines × 40 characters")
    print("• Use NumWorks online simulator for testing")
    print("")
    
    print("Casio Graph 90+E:")
    print("• Import via Casio FA-124 software")
    print("• Limited to basic MicroPython features")
    print("• Screen: ~8 lines × 21 characters")
    print("• Focus on simpler, shorter calculations")
    print("")
    
    print("General Tips:")
    print("• Break complex formulas into steps")
    print("• Use scientific notation for large/small numbers")
    print("• Save intermediate results in variables")
    print("• Test calculations with known values first")

def common_formulas_reference():
    """Quick reference of common formulas"""
    
    print("=== FORMULA QUICK REFERENCE ===")
    print("")
    
    print("CHEMISTRY:")
    print("Ideal Gas Law: PV = nRT")
    print("pH: pH = -log[H⁺]")
    print("Dilution: C₁V₁ = C₂V₂")
    print("Rate Law: Rate = k[A]ᵐ[B]ⁿ")
    print("Arrhenius: k = A·exp(-Ea/RT)")
    print("Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA])")
    print("")
    
    print("PHYSICS:")
    print("Kinematics: v = v₀ + at, x = v₀t + ½at²")
    print("Newton's 2nd Law: F = ma")
    print("Work-Energy: W = F·d·cos(θ), KE = ½mv²")
    print("Gravitational PE: PE = mgh")
    print("Wave Equation: v = fλ")
    print("Ohm's Law: V = IR")
    print("Coulomb's Law: F = kq₁q₂/r²")
    print("Projectile Range: R = v₀²sin(2θ)/g")

def memory_optimization_tips():
    """Tips for optimizing memory usage on calculators"""
    
    print("=== MEMORY OPTIMIZATION TIPS ===")
    print("")
    
    print("1. Variable Management:")
    print("   • Delete unused variables: del variable_name")
    print("   • Use shorter variable names")
    print("   • Reuse variables when possible")
    print("")
    
    print("2. Function Calls:")
    print("   • Import only needed functions")
    print("   • Use: from math import sqrt, sin, cos")
    print("   • Avoid: import math (imports everything)")
    print("")
    
    print("3. Data Structures:")
    print("   • Use tuples instead of lists when data won't change")
    print("   • Avoid large dictionaries")
    print("   • Use generators for sequences")
    print("")
    
    print("4. Code Structure:")
    print("   • Write modular functions")
    print("   • Avoid deep nesting")
    print("   • Use local variables in functions")
    print("")
    
    print("5. Calculator-Specific:")
    print("   • TI-84: Keep programs under 24KB")
    print("   • NumWorks: Use built-in modules when possible")
    print("   • Casio: Focus on essential calculations only")

# Example calculation templates that users can modify
CALCULATION_TEMPLATES = {
    "stoichiometry": """
# Stoichiometry Template
reactant_mass = float(input("Reactant mass (g): "))
reactant_mw = molecular_weight(input("Reactant formula: "))
product_mw = molecular_weight(input("Product formula: "))
mole_ratio = float(input("Mole ratio (product/reactant): "))

moles_reactant = reactant_mass / reactant_mw
moles_product = moles_reactant * mole_ratio
product_mass = moles_product * product_mw

print(f"Product mass: {product_mass:.2f} g")
""",
    
    "trajectory": """
# Projectile Trajectory Template
v0 = float(input("Initial velocity (m/s): "))
angle = float(input("Launch angle (degrees): "))
target_x = float(input("Target distance (m): "))

result = projectile_motion(v0, angle)
print(f"Range: {result['range']:.1f} m")
print(f"Max height: {result['max_height']:.1f} m")

if abs(result['range'] - target_x) < 1:
    print("Target hit!")
else:
    print(f"Miss by {abs(result['range'] - target_x):.1f} m")
""",
    
    "circuit": """
# Circuit Analysis Template
print("Enter two known values (0 for unknown):")
V = float(input("Voltage (V): ") or "0")
I = float(input("Current (A): ") or "0") 
R = float(input("Resistance (Ω): ") or "0")

result = ohms_law(V, I, R)
power = electrical_power(**{k:v for k,v in result.items() if v != 0})

print(f"V = {result['V']:.2f} V")
print(f"I = {result['I']:.3f} A") 
print(f"R = {result['R']:.2f} Ω")
print(f"P = {power:.2f} W")
"""
}

def show_templates():
    """Display code templates for common calculations"""
    print("=== CALCULATION TEMPLATES ===")
    print("Copy these templates and modify for your needs:")
    print("")
    
    for name, template in CALCULATION_TEMPLATES.items():
        print(f"{name.upper()} TEMPLATE:")
        print("-" * (len(name) + 10))
        print(template)
        print("")

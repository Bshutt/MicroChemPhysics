"""
Main interface for MicroPython Computational Chemistry and Physics
Optimized for graphing calculators (TI-84 Plus CE Python, NumWorks, Casio Graph 90+E)
"""

import chemistry
import physics
import examples
from utils import display_menu, get_user_input, clear_screen

def main_menu():
    """Display main menu and handle user selection"""
    while True:
        clear_screen()
        print("=== Computational Chem/Physics ===")
        print("1. Chemistry Calculations")
        print("2. Physics Calculations")
        print("3. View Examples")
        print("4. About/Help")
        print("0. Exit")
        print("=" * 35)
        
        choice = get_user_input("Select option (0-4): ")
        
        if choice == "1":
            chemistry_menu()
        elif choice == "2":
            physics_menu()
        elif choice == "3":
            examples_menu()
        elif choice == "4":
            show_help()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Press any key...")
            input()

def chemistry_menu():
    """Chemistry calculations submenu"""
    while True:
        clear_screen()
        print("=== Chemistry Calculations ===")
        print("1. Molecular Weight")
        print("2. Ideal Gas Law")
        print("3. pH Calculations")
        print("4. Concentration/Dilution")
        print("5. Rate Law")
        print("6. Quantum Energy Levels")
        print("0. Back to Main Menu")
        print("=" * 31)
        
        choice = get_user_input("Select calculation (0-6): ")
        
        if choice == "1":
            mol_weight_calc()
        elif choice == "2":
            ideal_gas_calc()
        elif choice == "3":
            ph_calc()
        elif choice == "4":
            concentration_calc()
        elif choice == "5":
            rate_law_calc()
        elif choice == "6":
            quantum_calc()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Press any key...")
            input()

def physics_menu():
    """Physics calculations submenu"""
    while True:
        clear_screen()
        print("=== Physics Calculations ===")
        print("1. Kinematics")
        print("2. Force & Motion")
        print("3. Energy & Work")
        print("4. Thermodynamics")
        print("5. Waves & Oscillations")
        print("6. Electromagnetism")
        print("0. Back to Main Menu")
        print("=" * 29)
        
        choice = get_user_input("Select calculation (0-6): ")
        
        if choice == "1":
            kinematics_calc()
        elif choice == "2":
            force_calc()
        elif choice == "3":
            energy_calc()
        elif choice == "4":
            thermo_calc()
        elif choice == "5":
            wave_calc()
        elif choice == "6":
            electro_calc()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Press any key...")
            input()

def mol_weight_calc():
    """Calculate molecular weight from formula"""
    clear_screen()
    print("=== Molecular Weight Calculator ===")
    formula = get_user_input("Enter formula (e.g., H2O, C6H12O6): ")
    
    try:
        mw = chemistry.molecular_weight(formula)
        print(f"\nMolecular weight of {formula}: {mw:.2f} g/mol")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def ideal_gas_calc():
    """Ideal Gas Law calculations"""
    clear_screen()
    print("=== Ideal Gas Law (PV = nRT) ===")
    print("Enter known values (0 for unknown):")
    
    P = float(get_user_input("Pressure (atm): ") or "0")
    V = float(get_user_input("Volume (L): ") or "0")
    n = float(get_user_input("Moles: ") or "0")
    T = float(get_user_input("Temperature (K): ") or "0")
    
    try:
        result = chemistry.ideal_gas_law(P, V, n, T)
        for key, value in result.items():
            if value is not None:
                print(f"{key}: {value:.4f}")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def ph_calc():
    """pH and pOH calculations"""
    clear_screen()
    print("=== pH Calculator ===")
    print("1. Calculate pH from [H+]")
    print("2. Calculate [H+] from pH")
    print("3. Calculate pOH from pH")
    
    choice = get_user_input("Select (1-3): ")
    
    try:
        if choice == "1":
            h_conc = float(get_user_input("Enter [H+] concentration (M): "))
            ph = chemistry.calculate_ph(h_conc)
            print(f"pH = {ph:.2f}")
        elif choice == "2":
            ph = float(get_user_input("Enter pH: "))
            h_conc = chemistry.ph_to_concentration(ph)
            print(f"[H+] = {h_conc:.2e} M")
        elif choice == "3":
            ph = float(get_user_input("Enter pH: "))
            poh = 14 - ph
            print(f"pOH = {poh:.2f}")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def concentration_calc():
    """Concentration and dilution calculations"""
    clear_screen()
    print("=== Concentration Calculator ===")
    print("Dilution: C1V1 = C2V2")
    
    C1 = float(get_user_input("Initial concentration (M): "))
    V1 = float(get_user_input("Initial volume (L): "))
    C2 = float(get_user_input("Final concentration (M, 0 if unknown): ") or "0")
    V2 = float(get_user_input("Final volume (L, 0 if unknown): ") or "0")
    
    try:
        result = chemistry.dilution_calculation(C1, V1, C2, V2)
        for key, value in result.items():
            if value is not None:
                print(f"{key}: {value:.4f}")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def rate_law_calc():
    """Rate law calculations"""
    clear_screen()
    print("=== Rate Law Calculator ===")
    print("Rate = k[A]^m[B]^n")
    
    try:
        rate = float(get_user_input("Reaction rate (M/s): "))
        conc_a = float(get_user_input("Concentration of A (M): "))
        conc_b = float(get_user_input("Concentration of B (M): "))
        order_a = float(get_user_input("Order with respect to A: "))
        order_b = float(get_user_input("Order with respect to B: "))
        
        k = chemistry.rate_constant(rate, conc_a, conc_b, order_a, order_b)
        overall_order = order_a + order_b
        
        print(f"\nRate constant k = {k:.4e}")
        print(f"Overall order = {overall_order}")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def quantum_calc():
    """Quantum energy level calculations"""
    clear_screen()
    print("=== Quantum Energy Levels ===")
    print("1. Particle in a box")
    print("2. Harmonic oscillator")
    print("3. Hydrogen atom")
    
    choice = get_user_input("Select model (1-3): ")
    
    try:
        if choice == "1":
            n = int(get_user_input("Quantum number n: "))
            L = float(get_user_input("Box length (m): "))
            mass = float(get_user_input("Particle mass (kg): "))
            energy = chemistry.particle_in_box_energy(n, L, mass)
            print(f"Energy = {energy:.2e} J")
        elif choice == "2":
            v = int(get_user_input("Vibrational quantum number v: "))
            freq = float(get_user_input("Frequency (Hz): "))
            energy = chemistry.harmonic_oscillator_energy(v, freq)
            print(f"Energy = {energy:.2e} J")
        elif choice == "3":
            n = int(get_user_input("Principal quantum number n: "))
            energy = chemistry.hydrogen_energy_level(n)
            print(f"Energy = {energy:.2e} J")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def kinematics_calc():
    """Kinematics calculations"""
    clear_screen()
    print("=== Kinematics Calculator ===")
    print("1. Constant acceleration")
    print("2. Projectile motion")
    
    choice = get_user_input("Select type (1-2): ")
    
    try:
        if choice == "1":
            v0 = float(get_user_input("Initial velocity (m/s): "))
            a = float(get_user_input("Acceleration (m/s²): "))
            t = float(get_user_input("Time (s): "))
            
            result = physics.constant_acceleration(v0, a, t)
            for key, value in result.items():
                print(f"{key}: {value:.2f}")
        elif choice == "2":
            v0 = float(get_user_input("Initial velocity (m/s): "))
            angle = float(get_user_input("Launch angle (degrees): "))
            
            result = physics.projectile_motion(v0, angle)
            for key, value in result.items():
                print(f"{key}: {value:.2f}")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def force_calc():
    """Force and motion calculations"""
    clear_screen()
    print("=== Force & Motion Calculator ===")
    print("1. Newton's 2nd Law (F = ma)")
    print("2. Friction force")
    print("3. Centripetal force")
    
    choice = get_user_input("Select calculation (1-3): ")
    
    try:
        if choice == "1":
            mass = float(get_user_input("Mass (kg): "))
            accel = float(get_user_input("Acceleration (m/s²): "))
            force = physics.newtons_second_law(mass, accel)
            print(f"Force = {force:.2f} N")
        elif choice == "2":
            mu = float(get_user_input("Coefficient of friction: "))
            normal = float(get_user_input("Normal force (N): "))
            friction = physics.friction_force(mu, normal)
            print(f"Friction force = {friction:.2f} N")
        elif choice == "3":
            mass = float(get_user_input("Mass (kg): "))
            velocity = float(get_user_input("Velocity (m/s): "))
            radius = float(get_user_input("Radius (m): "))
            force = physics.centripetal_force(mass, velocity, radius)
            print(f"Centripetal force = {force:.2f} N")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def energy_calc():
    """Energy and work calculations"""
    clear_screen()
    print("=== Energy & Work Calculator ===")
    print("1. Kinetic energy")
    print("2. Potential energy")
    print("3. Work done")
    
    choice = get_user_input("Select calculation (1-3): ")
    
    try:
        if choice == "1":
            mass = float(get_user_input("Mass (kg): "))
            velocity = float(get_user_input("Velocity (m/s): "))
            ke = physics.kinetic_energy(mass, velocity)
            print(f"Kinetic energy = {ke:.2f} J")
        elif choice == "2":
            mass = float(get_user_input("Mass (kg): "))
            height = float(get_user_input("Height (m): "))
            pe = physics.gravitational_potential_energy(mass, height)
            print(f"Potential energy = {pe:.2f} J")
        elif choice == "3":
            force = float(get_user_input("Force (N): "))
            distance = float(get_user_input("Distance (m): "))
            angle = float(get_user_input("Angle (degrees, 0 if parallel): ") or "0")
            work = physics.work_done(force, distance, angle)
            print(f"Work done = {work:.2f} J")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def thermo_calc():
    """Thermodynamics calculations"""
    clear_screen()
    print("=== Thermodynamics Calculator ===")
    print("1. Heat transfer")
    print("2. Thermal expansion")
    print("3. Ideal gas work")
    
    choice = get_user_input("Select calculation (1-3): ")
    
    try:
        if choice == "1":
            mass = float(get_user_input("Mass (kg): "))
            c = float(get_user_input("Specific heat (J/kg·K): "))
            dt = float(get_user_input("Temperature change (K): "))
            heat = physics.heat_transfer(mass, c, dt)
            print(f"Heat transferred = {heat:.2f} J")
        elif choice == "2":
            L0 = float(get_user_input("Initial length (m): "))
            alpha = float(get_user_input("Linear expansion coeff (/K): "))
            dt = float(get_user_input("Temperature change (K): "))
            dL = physics.thermal_expansion(L0, alpha, dt)
            print(f"Length change = {dL:.6f} m")
        elif choice == "3":
            P = float(get_user_input("Pressure (Pa): "))
            dV = float(get_user_input("Volume change (m³): "))
            work = physics.ideal_gas_work(P, dV)
            print(f"Work done = {work:.2f} J")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def wave_calc():
    """Wave and oscillation calculations"""
    clear_screen()
    print("=== Waves & Oscillations ===")
    print("1. Wave properties")
    print("2. Simple harmonic motion")
    print("3. Pendulum period")
    
    choice = get_user_input("Select calculation (1-3): ")
    
    try:
        if choice == "1":
            freq = float(get_user_input("Frequency (Hz): "))
            wavelength = float(get_user_input("Wavelength (m): "))
            speed = physics.wave_speed(freq, wavelength)
            print(f"Wave speed = {speed:.2f} m/s")
        elif choice == "2":
            A = float(get_user_input("Amplitude (m): "))
            omega = float(get_user_input("Angular frequency (rad/s): "))
            t = float(get_user_input("Time (s): "))
            x = physics.simple_harmonic_motion(A, omega, t)
            print(f"Position = {x:.4f} m")
        elif choice == "3":
            L = float(get_user_input("Length (m): "))
            period = physics.pendulum_period(L)
            print(f"Period = {period:.3f} s")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def electro_calc():
    """Electromagnetic calculations"""
    clear_screen()
    print("=== Electromagnetism Calculator ===")
    print("1. Coulomb's law")
    print("2. Electric field")
    print("3. Ohm's law")
    print("4. Magnetic force")
    
    choice = get_user_input("Select calculation (1-4): ")
    
    try:
        if choice == "1":
            q1 = float(get_user_input("Charge 1 (C): "))
            q2 = float(get_user_input("Charge 2 (C): "))
            r = float(get_user_input("Distance (m): "))
            force = physics.coulomb_force(q1, q2, r)
            print(f"Coulomb force = {force:.2e} N")
        elif choice == "2":
            q = float(get_user_input("Charge (C): "))
            r = float(get_user_input("Distance (m): "))
            field = physics.electric_field(q, r)
            print(f"Electric field = {field:.2e} N/C")
        elif choice == "3":
            print("V = IR")
            V = float(get_user_input("Voltage (V, 0 if unknown): ") or "0")
            I = float(get_user_input("Current (A, 0 if unknown): ") or "0")
            R = float(get_user_input("Resistance (Ω, 0 if unknown): ") or "0")
            
            result = physics.ohms_law(V, I, R)
            for key, value in result.items():
                if value is not None:
                    print(f"{key}: {value:.4f}")
        elif choice == "4":
            q = float(get_user_input("Charge (C): "))
            v = float(get_user_input("Velocity (m/s): "))
            B = float(get_user_input("Magnetic field (T): "))
            force = physics.magnetic_force(q, v, B)
            print(f"Magnetic force = {force:.2e} N")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress any key to continue...")

def examples_menu():
    """Show example calculations"""
    clear_screen()
    print("=== Example Calculations ===")
    examples.show_examples()
    input("\nPress any key to continue...")

def show_help():
    """Display help information"""
    clear_screen()
    print("=== Help & About ===")
    print("MicroPython Computational Chemistry & Physics")
    print("Version 1.0")
    print("")
    print("This calculator provides essential computational")
    print("tools for chemistry and physics calculations")
    print("optimized for graphing calculators.")
    print("")
    print("Compatible with:")
    print("- TI-84 Plus CE Python")
    print("- NumWorks")
    print("- Casio Graph 90+E")
    print("")
    print("For installation instructions, see")
    print("install_guide.md")
    print("")
    print("Memory usage optimized for calculator")
    print("hardware limitations.")
    
    input("\nPress any key to continue...")

# Run the application
if __name__ == "__main__":
    main_menu()

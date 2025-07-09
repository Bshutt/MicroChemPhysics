# MicroPython Computational Chemistry and Physics Calculator

## Overview

This project is a comprehensive computational chemistry and physics calculator designed specifically for graphing calculators including TI-84 Plus CE Python, NumWorks, and Casio Graph 90+E. The application provides a suite of scientific calculation tools optimized for memory-constrained environments with simple menu-driven interfaces suitable for calculator screens.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Modular Design
The application follows a modular architecture pattern to optimize memory usage and enable easy deployment across different calculator platforms. Each module serves a specific purpose:

- **main.py**: Central interface and menu system
- **chemistry.py**: Chemistry-specific calculations and functions
- **physics.py**: Physics-specific calculations and functions
- **constants.py**: Centralized physical and mathematical constants
- **utils.py**: Common utility functions for UI and input handling
- **examples.py**: Demonstration calculations and use cases

### Memory Optimization Strategy
The system is designed with strict memory constraints in mind:
- Simplified data structures and algorithms
- No external dependencies beyond built-in math module
- Efficient atomic masses dictionary with only essential elements
- Streamlined constant definitions
- Modular loading to reduce memory footprint

## Key Components

### Chemistry Module
- **Molecular weight calculator**: Parses chemical formulas and calculates molecular weights using atomic masses dictionary
- **Ideal Gas Law solver**: Implements PV = nRT calculations with multiple unit support
- **pH/pOH calculations**: Handles acid-base chemistry computations
- **Concentration/dilution**: Implements C₁V₁ = C₂V₂ calculations
- **Rate law calculations**: Chemical kinetics computations
- **Quantum energy levels**: Particle in box, harmonic oscillator, and hydrogen atom calculations

### Physics Module
- **Kinematics**: Constant acceleration and projectile motion calculations
- **Force and motion**: Newton's laws, friction, and centripetal force
- **Energy calculations**: Kinetic, potential, and work-energy theorem
- **Thermodynamics**: Heat transfer and thermal expansion
- **Wave mechanics**: Wave properties, simple harmonic motion, pendulum calculations
- **Electromagnetism**: Coulomb's law, electric fields, Ohm's law, magnetic forces

### Constants Library
Centralized repository of physical and mathematical constants organized by category:
- Mathematical constants (π, e)
- Physical constants (speed of light, Planck constant, etc.)
- Gas constants in multiple units
- Gravitational constants
- Electromagnetic constants
- Energy conversion factors
- Atomic and molecular constants

### User Interface System
Simple menu-driven interface optimized for calculator displays:
- Hierarchical menu navigation
- Input validation and error handling
- Screen clearing functionality
- Formatted output for small displays

## Data Flow

1. **Application Start**: main.py initializes and displays the primary menu
2. **Module Selection**: User navigates through hierarchical menus to select calculation type
3. **Input Collection**: utils.py handles user input with type validation
4. **Calculation Execution**: Appropriate module (chemistry.py or physics.py) performs calculations using constants.py
5. **Result Display**: Formatted results are presented to the user
6. **Navigation**: User can return to menus or exit the application

## External Dependencies

The application is designed to be completely self-contained with minimal dependencies:
- **Built-in math module**: Only external dependency, available on all target platforms
- **No network requirements**: All calculations performed locally
- **No file system dependencies**: Beyond the basic Python files themselves

## Deployment Strategy

### Cross-Platform Compatibility
The application supports multiple graphing calculator platforms:
- **TI-84 Plus CE Python**: Uses PyAdaptr app for Python execution
- **NumWorks**: Direct Python support through built-in interpreter
- **Casio Graph 90+E**: Compatible with MicroPython implementation

### Installation Process
1. Transfer all .py files to calculator storage
2. Execute main.py through platform-specific Python environment
3. Navigate using calculator's input methods
4. No compilation or build process required

### Memory Management
- Modular loading reduces initial memory requirements
- Simplified algorithms minimize runtime memory usage
- No persistent data storage requirements
- Garbage collection handled by MicroPython runtime

The architecture prioritizes simplicity, reliability, and resource efficiency to ensure optimal performance on resource-constrained calculator hardware while providing comprehensive scientific calculation capabilities.
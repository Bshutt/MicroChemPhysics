# Installation Guide for MicroPython Chemistry/Physics Calculator

This guide provides step-by-step instructions for installing and running the computational chemistry and physics calculator on different graphing calculator models.

## Table of Contents
1. [TI-84 Plus CE Python](#ti-84-plus-ce-python)
2. [NumWorks](#numworks)
3. [Casio Graph 90+E](#casio-graph-90e)
4. [General Testing](#general-testing)
5. [Troubleshooting](#troubleshooting)

---

## TI-84 Plus CE Python

### Prerequisites
- TI-84 Plus CE calculator (hardware revision M or newer)
- TI Connect CE software installed on computer
- USB cable for TI-84 Plus CE

### Step 1: Verify Python Support
1. Turn on your TI-84 Plus CE
2. Press `[apps]` button
3. Look for "PyAdaptr" or "Python" in the applications list
4. If not present, download from [TI's website](https://education.ti.com/en/software/details/en/CA9C74CAD02440A69FDC7189D7E1B6C2/swmathplotapppyada)

### Step 2: Install Python App
1. Connect calculator to computer via USB
2. Open TI Connect CE software
3. Navigate to the Python app download location
4. Drag the `.8xv` file to your calculator in TI Connect CE
5. Disconnect calculator and restart

### Step 3: Transfer Python Files
1. Connect calculator to computer
2. Open TI Connect CE
3. Navigate to the calculator's Python files folder
4. Copy all `.py` files from this project:
   - `main.py`
   - `chemistry.py`
   - `physics.py`
   - `constants.py`
   - `utils.py`
   - `examples.py`

### Step 4: Run the Application
1. On calculator, press `[apps]` → `PyAdaptr` (or Python)
2. Select "Shell" or "Editor"
3. Type: `exec(open('main.py').read())`
4. Press `[enter]` to start the application

### TI-84 Specific Tips
- **Memory management**: Delete unused programs to free space
- **Screen size**: Text limited to ~40 characters width
- **File naming**: Use short, descriptive names
- **Backup**: Save your programs to computer regularly

---

## NumWorks

### Prerequisites
- NumWorks calculator (any model with Python support)
- USB cable or use the web-based interface
- Optional: NumWorks online simulator

### Method 1: Direct Entry (Recommended)
1. Turn on NumWorks calculator
2. Select "Python" from home screen
3. Create a new script by pressing `[+]`
4. Copy and paste the code from each `.py` file:
   - Start with `constants.py`
   - Then `utils.py`
   - Then `chemistry.py` and `physics.py`
   - Finally `main.py`

### Method 2: Web Interface
1. Visit [my.numworks.com](https://my.numworks.com)
2. Connect your calculator via USB
3. Click "Add Python script"
4. Copy and paste each file's content
5. Name the scripts appropriately
6. Click "Install" to transfer to calculator

### Method 3: Online Simulator
1. Visit [numworks.com/simulator](https://www.numworks.com/simulator/)
2. Click on Python app
3. Create new scripts and paste code
4. Test functionality before transferring to physical calculator

### Step 4: Run the Application
1. In Python app, select the `main` script
2. Press `[OK]` or `[EXE]` to run
3. Navigate using arrow keys and `[OK]`

### NumWorks Specific Tips
- **Multiple files**: Create separate scripts for each module
- **Screen size**: ~25 lines × 40 characters
- **Built-in modules**: Utilize `math`, `random`, `time` modules
- **Syntax**: Full Python 3 support with some limitations

---

## Casio Graph 90+E

### Prerequisites
- Casio Graph 90+E calculator
- Casio FA-124 software or compatible transfer utility
- USB cable for data transfer

### Step 1: Prepare Files
1. Ensure calculator has latest firmware with Python support
2. Combine smaller modules into fewer files to save memory:
   ```python
   # Create combined_calc.py with all necessary functions
   # Include constants, basic chemistry, and physics functions
   ```

### Step 2: Transfer Files
1. Connect calculator to computer
2. Open Casio FA-124 software
3. Navigate to Python programs section
4. Import the simplified Python files
5. Transfer to calculator memory

### Step 3: Run on Calculator
1. Press `[MENU]` button
2. Select "Python" or programming icon
3. Choose your program file
4. Press `[EXE]` to run

### Casio Specific Limitations
- **Memory constraints**: Very limited program memory
- **Screen size**: ~8 lines × 21 characters
- **MicroPython subset**: Limited standard library
- **Simplified interface**: Focus on essential calculations only

### Recommended Casio Configuration
Create a simplified version with only essential functions:
```python
# Essential functions only for Casio
import math

# Basic constants
PI = 3.14159
G = 9.81
R = 8.314

# Simple molecular weight calculator
def mw(formula):
    # Simplified version for common molecules
    weights = {'H':1, 'C':12, 'N':14, 'O':16}
    # Implementation here...

# Basic physics calculations
def projectile(v0, angle):
    # Simplified projectile motion
    t = 2 * v0 * math.sin(math.radians(angle)) / G
    r = v0 * v0 * math.sin(2 * math.radians(angle)) / G
    return t, r

# Simple menu
print("1:Mol Weight 2:Projectile")
choice = input("Choice: ")
if choice == "1":
    # Molecular weight calculation
    pass
elif choice == "2":
    # Projectile calculation
    pass

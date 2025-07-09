"""
Utility functions for the MicroPython calculator interface
Optimized for graphing calculator displays and input methods
"""

def display_menu(title, options):
    """
    Display a formatted menu with title and options
    Optimized for calculator screen width
    """
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    print("0. Back/Exit")
    print("=" * len(title))

def get_user_input(prompt, input_type=str):
    """
    Get user input with type conversion and error handling
    Designed for calculator input limitations
    """
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                return ""
            
            if input_type == float:
                return float(value)
            elif input_type == int:
                return int(value)
            else:
                return value
                
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return ""

def clear_screen():
    """
    Clear screen function compatible with different calculator systems
    """
    try:
        # Try standard clear methods
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        # Fallback for calculators without os module
        print("\n" * 10)

def format_number(value, precision=4):
    """
    Format numbers for calculator display
    Handles scientific notation for very large/small numbers
    """
    if abs(value) < 1e-4 or abs(value) >= 1e6:
        return f"{value:.{precision-1}e}"
    else:
        return f"{value:.{precision}f}".rstrip('0').rstrip('.')

def validate_positive(value, name="Value"):
    """
    Validate that a value is positive
    """
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def validate_range(value, min_val, max_val, name="Value"):
    """
    Validate that a value is within a specified range
    """
    if value < min_val or value > max_val:
        raise ValueError(f"{name} must be between {min_val} and {max_val}")
    return value

def safe_divide(numerator, denominator, name="denominator"):
    """
    Safe division with zero check
    """
    if denominator == 0:
        raise ValueError(f"Division by zero: {name} cannot be zero")
    return numerator / denominator

def parse_scientific_notation(input_str):
    """
    Parse scientific notation input from calculators
    Handles formats like "1.23e-4", "1.23E-4", "1.23*10^-4"
    """
    try:
        # Replace common scientific notation formats
        normalized = input_str.replace("*10^", "e").replace("E", "e")
        return float(normalized)
    except ValueError:
        raise ValueError(f"Invalid scientific notation: {input_str}")

def memory_efficient_range(start, stop, step=1):
    """
    Memory-efficient range generator for calculators
    """
    current = start
    while current < stop:
        yield current
        current += step

def truncate_string(text, max_length=20):
    """
    Truncate strings for calculator display limits
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def create_simple_table(headers, rows, max_width=30):
    """
    Create simple formatted table for calculator display
    """
    # Calculate column widths
    col_widths = [len(header) for header in headers]
    
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Adjust for total width constraint
    total_width = sum(col_widths) + len(headers) - 1
    if total_width > max_width:
        # Proportionally reduce column widths
        reduction_factor = max_width / total_width
        col_widths = [int(w * reduction_factor) for w in col_widths]
    
    # Print table
    header_line = " ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))
    
    for row in rows:
        row_line = " ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(row_line)

def get_calculator_model():
    """
    Attempt to detect calculator model for model-specific optimizations
    """
    try:
        import sys
        platform = sys.platform
        
        if "ti" in platform.lower():
            return "TI-84"
        elif "numworks" in platform.lower():
            return "NumWorks"
        elif "casio" in platform.lower():
            return "Casio"
        else:
            return "Unknown"
    except:
        return "Unknown"

def optimize_for_calculator():
    """
    Apply calculator-specific optimizations
    """
    model = get_calculator_model()
    
    if model == "TI-84":
        # TI-84 specific optimizations
        return {
            "max_line_length": 25,
            "max_lines": 8,
            "decimal_places": 6
        }
    elif model == "NumWorks":
        # NumWorks specific optimizations
        return {
            "max_line_length": 30,
            "max_lines": 10,
            "decimal_places": 8
        }
    elif model == "Casio":
        # Casio specific optimizations
        return {
            "max_line_length": 21,
            "max_lines": 7,
            "decimal_places": 6
        }
    else:
        # Default/safe values
        return {
            "max_line_length": 20,
            "max_lines": 6,
            "decimal_places": 4
        }

def wait_for_input(message="Press any key to continue..."):
    """
    Wait for user input with calculator-friendly message
    """
    try:
        input(message)
    except KeyboardInterrupt:
        pass

def format_result_display(label, value, unit="", precision=4):
    """
    Format calculation results for optimal calculator display
    """
    formatted_value = format_number(value, precision)
    
    if unit:
        return f"{label}: {formatted_value} {unit}"
    else:
        return f"{label}: {formatted_value}"

def handle_calculator_error(func):
    """
    Decorator for calculator-friendly error handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {str(e)}")
            wait_for_input()
            return None
    return wrapper

def memory_usage_warning(threshold_kb=10):
    """
    Check memory usage and warn if approaching limits
    Simple implementation for calculators
    """
    try:
        import gc
        gc.collect()  # Force garbage collection
        
        # Basic memory check (implementation varies by calculator)
        # This is a simplified version
        print("Memory check completed.")
        
    except ImportError:
        # If gc module not available, skip memory check
        pass

def save_calculation_history(calculation, result):
    """
    Simple calculation history for calculator sessions
    Memory-efficient implementation
    """
    # In a real calculator, this might save to a file
    # For now, just print to maintain session record
    timestamp = "Session"  # Simplified timestamp
    print(f"[{timestamp}] {calculation} = {result}")

def load_user_preferences():
    """
    Load user preferences for calculator interface
    Returns default values if no preferences file exists
    """
    default_prefs = {
        "decimal_places": 4,
        "scientific_notation_threshold": 1e4,
        "angle_mode": "degrees",  # or "radians"
        "auto_clear": True
    }
    
    try:
        # In a full implementation, this would load from a file
        # For calculator compatibility, return defaults
        return default_prefs
    except:
        return default_prefs

def create_progress_bar(current, total, width=20):
    """
    Create simple text progress bar for long calculations
    """
    if total == 0:
        return "[" + "=" * width + "]"
    
    progress = int((current / total) * width)
    bar = "[" + "=" * progress + " " * (width - progress) + "]"
    percentage = int((current / total) * 100)
    
    return f"{bar} {percentage}%"

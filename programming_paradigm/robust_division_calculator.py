# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for non-numeric inputs and division by zero."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt to perform division
        result = num / denom
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    # If successful, return the result
    return f"The result of the division is {result}"

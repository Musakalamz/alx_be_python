"""Robust division logic with input validation and exception handling.

Exposes a single function, `safe_divide`, that:
- Accepts raw inputs (strings) and converts them to floats
- Handles non-numeric input via ValueError
- Handles division by zero via ZeroDivisionError
- Returns a user-friendly message for both errors and successful results
"""


def safe_divide(numerator, denominator):
    """Safely divide two values with comprehensive error handling.

    Args:
        numerator: Raw numerator value (string or number-like)
        denominator: Raw denominator value (string or number-like)

    Returns:
        str: A user-friendly message describing the result or the error.
    """
    # Validate numeric inputs first
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Perform division with explicit zero handling
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"


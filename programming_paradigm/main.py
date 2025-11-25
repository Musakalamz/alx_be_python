"""Robust division calculator command-line interface.

This script consumes two arguments (numerator and denominator), delegates to
`safe_divide` for error handling, and prints a user-friendly result.
"""

import sys
from robust_division_calculator import safe_divide


def main():
    """Entry point for the robust division CLI."""
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)


if __name__ == "__main__":
    main()

import sys
from robust_division_calculator import safe_divide


def main():
    """
    Entry point for the command-line division calculator.

    This function:
    - Validates command-line arguments
    - Extracts numerator and denominator
    - Performs safe division using the imported utility
    - Prints the result to the console
    """

    # Ensure exactly two command-line arguments are provided
    # sys.argv[0] -> script name
    # sys.argv[1] -> numerator
    # sys.argv[2] -> denominator
    if len(sys.argv) != 3:
        print("Usage: python main-1.py <numerator> <denominator>")
        sys.exit(1)  # Exit with non-zero status to indicate incorrect usage

    # Retrieve numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform division using a robust helper function
    # safe_divide is responsible for input validation and error handling
    result = safe_divide(numerator, denominator)

    # Output the result (or error message) to the user
    print(result)


# Execute main() only when this script is run directly
# Prevents execution when imported as a module
if __name__ == "__main__":
    main()
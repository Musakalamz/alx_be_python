"""Demonstration of class and static methods via a simple Calculator.

Highlights:
- `@staticmethod` for self-contained operations that don't depend on class/instance
- `@classmethod` for behavior that needs class-level context (via `cls`)
"""


class Calculator:
    """Calculator providing arithmetic operations.

    Uses both a static method and a class method to illustrate the difference
    between context-free functions and class-aware routines.
    """

    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers without class/instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers while printing class context."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


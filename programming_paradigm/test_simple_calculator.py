"""Unit tests for the SimpleCalculator class.

Covers addition, subtraction, multiplication, and division, including
representative edge cases such as negative numbers, zero interactions,
and division by zero behavior (returning None).
"""

import unittest
try:
    # Preferred: sibling import per checker requirement
    from simple_calculator import SimpleCalculator
except ImportError:
    # Fallback when running tests from project root
    from programming_paradigm.simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test suite for SimpleCalculator operations."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Validate addition across integers and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Validate subtraction including negative outcomes."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)

    def test_multiplication(self):
        """Validate multiplication including zero and negative factors."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """Validate division behavior, including division by zero handling."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Division by zero should return None per implementation contract
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(10, 0.0))


if __name__ == "__main__":
    unittest.main()

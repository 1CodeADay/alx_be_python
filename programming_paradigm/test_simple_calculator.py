import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -7), -10)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -7), 4)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Expected None for division by zero")

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        self.assertEqual(self.calc.add(1e100, 1e100), 2e100)  # Very large numbers
        self.assertEqual(self.calc.subtract(1e-100, 1e-100), 0)  # Very small numbers
        self.assertEqual(self.calc.multiply(1e50, 0), 0)  # Multiplication with zero
        self.assertEqual(self.calc.divide(1, 3), 1 / 3)  # Division resulting in a float

if __name__ == "__main__":
    unittest.main()

import unittest
from calculator.core.core_functions import *


class BasicTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 2), 3)
        self.assertEqual(addition(0, 2), 2)
        self.assertEqual(addition(1, 2, 3, 4), 10)

    def test_multiplication(self):
        self.assertEqual(multiplication(1, 2), 2)
        self.assertEqual(multiplication(0, 2), 0)
        self.assertEqual(multiplication(2, 5), 10)
        self.assertEqual(multiplication(2, 5, 4, 3), 120)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 0), 5)
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(5, 8), -3)

    def test_division(self):
        self.assertEqual(division(0, 5), 0)
        self.assertEqual(division(5, 1), 5)
        self.assertAlmostEqual(division(1, 2), 0.5)

    def test_power(self):
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(5, 1), 5)
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(5, 3), 125)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        with self.assertRaises(ArithmeticError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
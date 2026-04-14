# https://github.com/sathvikpallikkara/lab11-SP-RC
# Partner 1: Sathvic Pallikkara
# Partner 2: Ryan Carter

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 1, 10)
        self.assertRaises(ValueError, logarithm, -1, 10)

    # Partner 1's tests
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertAlmostEqual(divide(2, 10), 5.0)
        self.assertAlmostEqual(divide(4, 8), 2.0)

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm, 10, -1)
        self.assertRaises(ValueError, logarithm, 10, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertRaises(ValueError, square_root, -1)

if __name__ == '__main__':
    unittest.main()
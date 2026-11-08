import unittest
from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtract(self):
        self.assertEqual(calculate(7, 4, "-"), 3)

    def test_multiply(self):
        self.assertEqual(calculate(3, 4, "*"), 12)

    def test_divide(self):
        self.assertEqual(calculate(8, 2, "/"), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(1, 0, "/")


if __name__ == "__main__":
    unittest.main()

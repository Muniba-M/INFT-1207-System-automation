import unittest
from math import pi
from app.Lab3_Fariha_Muniba import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    # Test for circle area (valid case)
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    # Test for circle area (invalid case)
    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # Test for trapezium area (valid case)
    def test_trapezium_area_valid(self):
        self.assertAlmostEqual(trapezium_area(3, 4, 5), 17.5)

    # Test for trapezium area (invalid case)
    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-3, 4, 5), "Negative side length should raise error"

    # Test for ellipse area (valid case)
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3, 4), pi * 3 * 4)

    # Testing for ellipse floating point
    def test_ellipse_valid_floating_point(self):
        self.assertAlmostEqual(ellipse_area(3.5,2.8), pi * 3.5 * 2.8)

    # Test for ellipse area (invalid case)
    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-3, 4)  # Negative semi-major axis should raise error

    # Test for rhombus area (valid case)
    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(6, 8), 24)

    # Testing for rhombus floating point
    def test_rhombus_valid_floating_point(self):
        self.assertAlmostEqual(rhombus_area(4.6, 5.9), 0.5 * 4.6 * 5.9)

    # Test for rhombus area (invalid case)
    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(0, 8)  # Zero diagonal should raise error

if __name__ == "__main__":
    unittest.main()
import unittest

# Import the TestShapes class
from test_Lab3_Fariha_Muniba import TestShapes

def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':  # Correct comparison: string value vs. string value
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':  # Correct comparison
        suite.addTest(TestShapes('test_trapezium_area_valid'))
        suite.addTest(TestShapes('test_trapezium_area_invalid'))
    elif choice == 'e':  # Correct comparison
        suite.addTest(TestShapes('test_ellipse_area_valid'))
        suite.addTest(TestShapes('test_ellipse_area_invalid'))
        suite.addTest(TestShapes('test_ellipse_valid_floating_point'))
    elif choice == 'r':  # Correct comparison
        suite.addTest(TestShapes('test_rhombus_area_valid'))
        suite.addTest(TestShapes('test_rhombus_area_invalid'))
        suite.addTest(TestShapes('test_rhombus_valid_floating_point'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)
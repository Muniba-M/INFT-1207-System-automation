from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    if any(val <= 0 for val in [a, b, h]):
        raise ValueError("Sides and height must be positive values.")
    return 0.5 * (a + b) * h

def ellipse_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive values.")
    return pi * a * b

def rhombus_area(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive values.")
    return 0.5 * d1 * d2
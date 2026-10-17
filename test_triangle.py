import math
from triangle import classify_triangle, is_valid_triangle

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"

# Copilot used (3, 4, 5), which forms a right scalene
# triangle. I changed the sides to (4, 5, 6) to test a regular
# scalene triangle instead.
def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_invalid_triangle():
    assert is_valid_triangle(1, 2, 5) == False 

# Copilot suggested zero and negative side lengths instead of
# a degenerate triangle. I changed the test to (2, 3, 5),
# where the sum of two sides equals the third.
def test_degenerate_triangle():
     assert is_valid_triangle(2, 3, 5) is False
     assert classify_triangle(2, 3, 5) == "Invalid"

# Copilot expected "Right" instead of "Right Scalene".
# I also changed the inputs to (5, 5, 5 * sqrt(2)) to test
# a right iscoceles triangle with a non-integer side length.
def test_right_triangle_noninteger():
    a = 5
    b = 5
    c = 5 * math.sqrt(2)

    assert is_valid_triangle(a, b, c) is True
    assert classify_triangle(a, b, c) == "Right Isosceles"

# Copilots original suggestion for the degenerate triangel test.
def test_nonpositive_sides():
    assert is_valid_triangle(0, 5, 5) is False
    assert is_valid_triangle(-1, 5, 5) is False
    assert is_valid_triangle(5, -1, 5) is False
    assert is_valid_triangle(5, 5, -1) is False
    assert classify_triangle(0, 5, 5) == "Invalid"

def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
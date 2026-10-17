# Triangle Classifier

This Python program determines whether three side lengths form a triangle. It classifies valid triangles as equilateral, isosceles, or scalene and identifies right triangles. Invalid side lengths will return "Invalid" instead of returning an error. 

## Acceptance Criteria

1. If a customer enters three equal positive side lengths that form a valid triangle, the program will return "Equilateral".
2. If a customer enters three side lengths that don't form a valid triangle, the program will return "Invalid" instead of resulting in an error.
3. If a customer enters three side lengths that form a right triangle, the program will return "Right ", followed by the correct triangle type.

# How to Run the Tests

1. Install the required dependencies: 
python -m pip install -r requirements.txt

2. Run the tests in terminal: 
python -m pytest -v

## Equivalence Classes and Boundary Cases

The tests cover multiple equivalence classes such as equilateral triangles, isosceles triangles, and scalene triangles. They also cover right and invalid triangles.

Boundary cases include degenerate triangles such as (2, 3, 5) since the sum of two sides equals the third side. This would be invalid because the sum must be greater than the third side. 

The tests also check zero and negative side lengths to ensure all sides are positive.

## Copilot Review Log

When writing the scalene triangle test, Copilot suggested side lengths of (3, 4, 5) which would result in a right scalene triangle, not a regular scalene so I changed the values to (4, 5, 6).

When writing the degenerate triangle test, Copilot gave a test for zero and negative sides, we needed to check what happens if two of the triangles side summed up to the third side. I changed the values there to (2, 3, 5).

When writing the non-integer right triangle test, Copilot wrote to return "Right" for a (3, 4, 5) triangle however we were testing non-integers. I changed that test to use (5, 5, 5 * sqrt(2)) instead.

The other tests (test_isosceles, test_equilateral, test_invalid_triangle, test_right_scalene) were accepted as they provided the right criteria for the tests. 

For test_nonpositive_sides, I reused the original suggestion from the non-integer test since it fit the criteria. 

## Why Equilateral Triangles Cannot Be Right

A right triangle requires one 90 degree angle, therefore an equilateral triangle cannot be considered a right triangle. An equilateral triangle has three 60 degree angles since all sides have the same length.

## AI Disclosure

I used GitHub Copilot to generate suggestions for the unit tests in test_triangle.py. I reviewed each suggestion and made the appropriate changes before accepting the code. 

I also used ChatGPT to clear up questions I had and to review that my work was complete and ready to submit. 
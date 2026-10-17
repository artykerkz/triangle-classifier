# "We run a stained-glass studio. Customers enter three side lengths 
# and we tell them the shape and whether it’s buildable. If it’s not 
# a valid triangle, show a message, don’t crash. Also flag right-angle 
# pieces — they need reinforced corners. It has to be correct every time; 
# a wrong answer means a ruined pane."

from triangle import classify_triangle

def test_stained_glass_requirements():
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    
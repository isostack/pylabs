import math
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    """Return the area of a regular polygon inside a circle of radius circle_radius
    with number_of_sides sides.
    """
    side_length = 2 * circle_radius * math.sin(math.pi / number_of_sides)
    apothem = circle_radius * math.cos(math.pi / number_of_sides)
    area = number_of_sides * side_length * apothem / 2
    return round(area, 3)

print(area_of_polygon_inside_circle(3, 3))
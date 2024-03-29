from HW_2.src.Rectangle import Rectangle
from HW_2.src.Circle import Circle
from HW_2.src.Triangle import Triangle
from HW_2.src.Square import Square

import pytest
from datetime import datetime


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(4, 5, 20),
                          (4.5, 5.5, 24.75)],
                         ids=["integer", "float"])
def test_positive_rectangle(side_a, side_b, area):
    r = Rectangle(side_a, side_b, "Rectangle")
    assert r.get_area() == area


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(-4, -5, 20),
                          (-4, 5, -20),
                          (4, -5, -20)],
                         ids=["first_negative", "second_negative", "third_negative"])
def test_negative_rectangle(side_a, side_b, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b, "Rectangle")


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(4, 5, 3, 6),
                          (4.5, 5.5, 3.5, 7.85)],
                         ids=["integer", "float"])
def test_positive_triangle(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c, "Triangle")
    assert r.get_area() == area


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(-4, -5, 3, 6),
                          (-4.5, -5.5, -3.5, -7.85)],
                         ids=["integer", "float"])
def test_negative_triangle(side_a, side_b, side_c, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c, "Triangle")


@pytest.mark.parametrize(("radius", "area"),
                         [(4, 50.27),
                          (4.5, 63.62)],
                         ids=["integer", "float"])
def test_positive_circle(radius, area):
    r = Circle(radius, "Circle")
    assert r.get_area() == area


@pytest.mark.parametrize(("radius", "area"),
                         [(-4, 50.27),
                          (-4.5, 63.62)],
                         ids=["integer", "float"])
def test_negative_circle(radius, area):
    with pytest.raises(ValueError):
        Circle(radius, "Circle")


@pytest.mark.parametrize(("side_a", "area"),
                         [(4, 16),
                          (4.5, 20.25)],
                         ids=["integer", "float"])
def test_positive_square(side_a, area):
    r = Square(side_a, "Square")
    assert r.get_area() == area


@pytest.mark.parametrize(("side_a", "area"),
                         [(-4, 16),
                          (-4.5, 20.25)],
                         ids=["integer", "float"])
def test_negative_square(side_a, area):
    with pytest.raises(ValueError):
        Square(side_a, "Square")

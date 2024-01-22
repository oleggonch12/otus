from HW_2.src.Rectangle import Rectangle
from HW_2.src.Circle import Circle
from HW_2.src.Triangle import Triangle
from HW_2.src.Square import Square

import pytest
from datetime import datetime


def test_positive_rectangle(get_rectangle_positive):
    a, b, area = get_rectangle_positive
    r = Rectangle(a, b, "Rectangle")
    assert r.get_area() == area


def test_negative_rectangle(get_rectangle_negative):
    a, b, area = get_rectangle_negative
    with pytest.raises(ValueError):
        Rectangle(a, b, "Rectangle")


def test_positive_triangle(get_triangle_positive):
    a, b, c, area = get_triangle_positive
    r = Triangle(a, b, c, "Triangle")
    assert r.get_area() == area


def test_negative_triangle(get_triangle_negative):
    a, b, c, area = get_triangle_negative
    with pytest.raises(ValueError):
        Triangle(a, b, c,  "Triangle")


def test_positive_circle(get_circle_positive):
    a, area = get_circle_positive
    r = Circle(a, "Circle")
    assert r.get_area() == area


def test_negative_circle(get_circle_negative):
    a, area = get_circle_negative
    with pytest.raises(ValueError):
        Circle(a, "Triangle")


def test_positive_square(get_square_positive):
    a, area = get_square_positive
    r = Square(a, "Square")
    assert r.get_area() == area


def test_negative_square(get_square_negative):
    a, area = get_square_negative
    with pytest.raises(ValueError):
        Square(a, "Square")


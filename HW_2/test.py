from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square


rectangle = Rectangle(3, 4, "Rectangle")
circle = Circle(3, "Circle")
triangle = Triangle(3, 5, 7, "Triangle")
square = Square(5, "Square")

print(f"Площадь прямоугольника равна {round(rectangle.get_area(),2)} м^2")
print(f"Периметр прямоугольника равен {round(rectangle.get_perimetr(),2)} м")
print(" ")

print(f"Площадь круга равна {round(circle.get_area(),2)} м^2")
print(f"Периметр круга равен {round(circle.get_perimetr(),2)} м")
print(" ")

print(f"Площадь треугольника равна {round(triangle.get_area(),2)} м^2")
print(f"Периметр треугольника равен {round(triangle.get_perimetr(),2)} м")
print(" ")

print(f"Площадь квадрата равна {round(square.get_area(),2)} м^2")
print(f"Периметр квадрата равен {round(square.get_perimetr(),2)} м")
print(" ")

figures_except_square = [circle, triangle, rectangle]
sum_square = round(square.add_area(*figures_except_square), 2)
print(f"Сумма всех площадей равна {sum_square} м^2")

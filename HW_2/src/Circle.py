import math
from HW_2.src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("нельзя создать круг")
        self.radius = radius

    def get_area(self):
        """
        Вычисляем площадь круга
        """
        return round(math.pi*self.radius**2,2)

    def get_perimetr(self):
        """
        Вычисляем периметр окружности
        """
        return 2 * math.pi*self.radius

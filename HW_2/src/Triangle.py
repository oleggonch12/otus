import math
from HW_2.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if (side_a <= 0 or side_b <= 0 or side_c <= 0) \
                and self._check_if_triangle_exists():
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        """
        Вычисляем площадь треугольника
        """
        return math.sqrt(self.get_perimetr() *
                         (self.get_perimetr()-self.side_a) *
                         (self.get_perimetr() - self.side_b) *
                         (self.get_perimetr() - self.side_c))

    def get_perimetr(self):
        """
        Вычисляем периметр треугольника
        """
        return 1/2*(self.side_a+self.side_b+self.side_c)

    def _check_if_triangle_exists(self):
        """
        # Треугольник будет существовать если сумма двух меньших
        сторон больше третьей самой большой
        """
        sorted_sides = sorted([self.side_a, self.side_b, self.side_c])
        if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
            return True
        else:
            return False

from HW_2.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        super().__init__(name="Rectangle")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        """
        Вычисляем площадь прямоугольника
        """
        return self.side_a * self.side_b

    def get_perimetr(self):
        """
        Вычисляем периметр прямоугольника
        """
        return 2 * (self.side_a + self.side_b)

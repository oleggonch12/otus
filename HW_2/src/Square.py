from HW_2.src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a, name):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a, "Square")

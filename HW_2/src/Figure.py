from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure_2, other_figure_3, other_figure_4):
        if not isinstance(other_figure_2, Figure) and \
                isinstance(other_figure_3, Figure) and \
                isinstance(other_figure_4, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure_2.get_area() \
            + other_figure_3.get_area() + other_figure_4.get_area()

# ShapeManager: държи списък от фигури, метод total_area() и largest_shape()
from exercises_hard_tasks.geometry_shapes.shape import Shape


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, current_shape=object) -> None:
        self.shapes.append(current_shape)

    def total_area(self) -> int or float:
        return sum(shape.area() for shape in self.shapes)

    def largest_shape(self) -> object:
        max_area = 0
        top_shape = None
        for shape in self.shapes:
            if max_area <= shape.area():
                max_area = shape.area()
                top_shape = shape

        return top_shape
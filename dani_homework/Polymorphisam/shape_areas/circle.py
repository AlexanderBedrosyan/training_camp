# Circle: изчислява площ: π * r^2
from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius:int or float):
        self.radius = radius

    def area(self):
       return float(f"{pi * (self.radius ** 2):.2f}")
# Circle (private __radius, property/setter с валидация), метод area() = π * r²
from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius=int):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must by greater than 0")
        self.__radius = value

    def area(self) -> int or float:
        return pi * self.__radius * self.__radius
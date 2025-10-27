# Circle (private __radius,
# property/setter с валидация),
# метод area() = π * r²

import math
from shape import Shape

pi_value = math.pi
print(f"The value of pi is approximately: {pi_value}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        value = self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

# c1 = Circle(8)
# print(c1.radius)
# print(c1.area())
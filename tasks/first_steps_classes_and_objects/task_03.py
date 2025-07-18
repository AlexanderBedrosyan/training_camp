# Създай клас Circle с атрибут radius. Добави метод, който изчислява и връща лицето на кръга.
import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * pow(self.radius, 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

circle = Circle(2)
print(circle.area())
print(circle.perimeter())
print(circle.radius)
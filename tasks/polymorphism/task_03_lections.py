# Задача 3
# Използвайки abc.ABC, създайте абстрактен клас Shape с метод perimeter(). Имплементирайте го в класове Square и
# Triangle.
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    A = 4

    def perimeter(self):
        return 4 * Square.A

class Triangle(Shape):
    A = 4
    B = 5
    C = 6

    def perimeter(self):
        return Triangle.A + Triangle.B + Triangle.C

s = Square()
t = Triangle()

print(s.perimeter())
print(t.perimeter())
# Rectangle (protected _width, _height), метод area() = width * height
from shape import Shape

class Rectangle(Shape):
    def __init__(self, width=int, height=int):
        self._width = width
        self._height = height

    def area(self) -> int:
        return self._width * self._width
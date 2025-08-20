# Rectangle (protected _width, _height), метод area() = width * height
from shape import Shape

class Rectangle(Shape):
    def __init__(self, width=int, height=int):
        super().__init__()
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


# rect = Rectangle(5, 10)
# print("Ширина:", rect._width)
# print("Височина:", rect._height)
# print("Лице:", rect.area())
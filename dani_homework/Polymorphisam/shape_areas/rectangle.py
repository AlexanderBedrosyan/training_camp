# Rectangle: изчислява площ: width * height
from shape import Shape


class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
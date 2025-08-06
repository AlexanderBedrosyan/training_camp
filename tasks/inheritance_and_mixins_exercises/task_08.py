# 🔹 Задача 8
# Създай клас Shape с метод area() връщащ 0.
# Създай клас Rectangle, наследяващ Shape, с атрибути width и height, и override-вай area() да връща width * height.

class Shape:

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

current_shape = Shape()
print(current_shape.area())

current_rectangle = Rectangle(5, 2)
print(current_rectangle.area())
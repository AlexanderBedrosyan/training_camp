# Задача 8
# Създай клас Shape с метод area() връщащ 0.
# Създай клас Rectangle, наследяващ Shape, с атрибути width и height,
# и override-вай area() да връща width * height.

class Shape:
    def area(self) -> int:
        return 0

class Rectangle(Shape):
    def __init__(self, width=int, height=int):
        self.width = int(width)
        self.height = int(height)

    def area(self) -> int:
        return self.width * self.height


current_shape = Shape()
print(current_shape.area())
current_rectangle = Rectangle(5,3)
print(current_rectangle.area())
current_rectangle = Rectangle(10, 20)
print(current_rectangle.area())
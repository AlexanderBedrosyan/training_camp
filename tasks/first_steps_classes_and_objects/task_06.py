# Направи клас Rectangle, който приема ширина и височина, и метод, който връща обиколката му.

class Rectangle:

    def __init__(self, width, height):
        self.widht = width
        self.height = height

    def perimeter(self):
        return 2 * (self.widht + self.height)


rectangle = Rectangle(2, 3)
print(rectangle.perimeter())
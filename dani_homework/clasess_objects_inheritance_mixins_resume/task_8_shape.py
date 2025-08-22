# Създай клас Shape с метод area() връщащ 0.
# Създай клас Rectangle, наследяващ Shape, с атрибути width и height,
# и override-вай area() да връща width * height.
# --------------------------------------------------------------------

class Shape:
    def area(self)-> float:
        shape_area = 0
        return shape_area

class Rectangle(Shape):
    def __init__(self, width: float, height:float)-> None:
        self.width: float = width
        self.height: float = height

    def area(self)->float:
        return self.width * self.height

r = Rectangle(25, 30)
print(r.area())

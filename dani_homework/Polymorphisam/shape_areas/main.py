from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
for s in shapes:
    print(s.area())
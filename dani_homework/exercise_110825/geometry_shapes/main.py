from circle import Circle
from rectangle import Rectangle
from shape_manager import ShapeManager

sm = ShapeManager()
sm.add_shape(Circle(5))
sm.add_shape(Rectangle(4, 6))
print(sm.total_area())
print(type(sm.largest_shape()).__name__)
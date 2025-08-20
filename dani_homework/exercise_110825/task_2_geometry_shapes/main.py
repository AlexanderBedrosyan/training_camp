
from shape_manager import ShapeManager
from circle import Circle
from rectangle import Rectangle


sm = ShapeManager()
sm.add_shape(Circle(5))
sm.add_shape(Rectangle(4, 6))
print(sm.total_area())
print(type(sm.largest_shape()).__name__)

sm = ShapeManager()
sm.add_shape(Circle(8))
sm.add_shape(Rectangle(4, 4))
print(sm.total_area())
print(type(sm.largest_shape()).__name__)
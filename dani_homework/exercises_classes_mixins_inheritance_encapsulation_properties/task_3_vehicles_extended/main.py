from car import Car
from truck import Truck

c = Car("BMW", 240)
print(c.info())  # BMW car with max speed 240

t = Truck(120, 5000)
print(t.can_transport(3000))  # True
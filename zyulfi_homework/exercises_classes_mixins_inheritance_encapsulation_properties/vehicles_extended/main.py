from car import Car
from truck import Truck

c = Car(240, "BMW")
print(c.info())  # BMW car with max speed 240

t = Truck(120, 5000)
print(t.can_transport(3000))  # True
print(t._max_speed)

print(t.can_transport(6000))
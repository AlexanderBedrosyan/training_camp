from car import Car

c = Car(240, "BMW")
print(c.info())  # BMW car with max speed 240

d = Car(0, "Trabant")
print(d.info())
d.max_speed = -30
print(d.info())
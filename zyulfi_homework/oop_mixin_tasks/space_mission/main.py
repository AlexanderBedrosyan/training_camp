from astronaut import Astronaut
from spaceship import Spaceship
from mission import Mission

a1 = Astronaut("Ivan"); a1.add_hours(100)
a2 = Astronaut("Maria"); a2.add_hours(200)

s = Spaceship("Apollo", 2)
m = Mission(s)
m.add_astronaut(a1)
m.add_astronaut(a2)

print(m.total_hours())  # 300
print(m.check_capacity())  # True

s1 = Spaceship("Voengar", 1)
m1 = Mission(s1)
m1.add_astronaut(a1)
m1.add_astronaut(a2)
print(m1.check_capacity())
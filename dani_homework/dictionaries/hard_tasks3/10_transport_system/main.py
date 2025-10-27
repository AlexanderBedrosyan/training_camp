from vehicle import Vehicle
from route import Route
from system import System

v1 = Vehicle("Car", 100)
v2 = Vehicle("Plane", 800)

r = Route("Sofia", "Varna", 400)

s = System()
s.add_vehicle(v1)
s.add_vehicle(v2)

print(s.fastest_vehicle(r))  # Plane
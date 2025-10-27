from planner import Planner
from vehicle import Vehicle
from route import Route

r1 = Route("Bourgas", "Sofia", 400)
r2 = Route("Rim", "Sofia", 1400)
print(r1)
print(r2)

v1 = Vehicle("Car", 180)
v2 = Vehicle("Train", 500)
print(v1.travel_time(r1))
print(v2.travel_time(r2))

p1 = Planner()
p1.add_vehicle(v1)
p1.add_vehicle(v2)
p1.add_route(r1)
p1.add_route(r2)

print(p1.fastest_vehicle(r1))
print(p1.sortest_route())

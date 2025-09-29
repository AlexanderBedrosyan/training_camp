from route import Route
from vehicle import Vehicle
from network import Network

r = Route("Sofia", "Plovdiv", 150)
v1 = Vehicle("Car", 100)
v2 = Vehicle("Bus", 80)

n = Network()
n.add_vehicle(v1)
n.add_vehicle(v2)

print(v1.travel_time(r))  # 1.5h
print(n.fastest_vehicle(r).model)  # Car

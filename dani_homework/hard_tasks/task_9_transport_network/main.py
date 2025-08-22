from route import Route
from vehicle import Vehicle
from network import Network

r1 = Route("City A", "City B", 150)
r2 = Route("City A", "City C", 300)

v1 = Vehicle(100)
v2 = Vehicle(150)

network = Network()
network.add_route(r1)
network.add_route(r2)
network.add_vehicle(v1)
network.add_vehicle(v2)

print("Fastest vehicle on route 1 speed:", network.fastest_vehicle(r1).__speed)  # might need getter


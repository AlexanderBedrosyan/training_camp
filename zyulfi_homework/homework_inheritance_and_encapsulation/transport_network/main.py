from route import Route
from vehicle import Vehicle
from network import Network

r = Route("Sofia", "Plovdiv", 150)
r2 = Route("Burgas", "Ruse", 300)

v1 = Vehicle("Car", 100)
v2 = Vehicle("Bus", 75)
v3 = Vehicle("Lend Rover", 99)

n = Network()
n.add_route(r)
n.add_route(r2)
n.add_vehicle(v1)
n.add_vehicle(v2)
n.add_vehicle(v3)

print(n.fastest_vehicle(r).name)  # Car
print(n.fastest_vehicle(r2).name)
print(str(r))
print(str(r2))

print(f"For the current {str(r2)} the fastest transport is: {n.fastest_vehicle(r2).name}")


from reading import Reading
from station import Station
from network import Network

r1 = Reading(20, 60)
r2 = Reading(25, 55)

s = Station()
s.add_reading(r1)
s.add_reading(r2)

n = Network()
n.add_station(s)

print(s.avg_temp())  # 22.5
print(n.overall_avg_temp())  # 22.5
from reading import Reading
from station import Station
from network import Network

r1 = Reading(20, 60)
r2 = Reading(25, 55)
s = Station("Central"); s.add_reading(r1); s.add_reading(r2)

net = Network(); net.add_station(s)

print(s.average_temp())            # 22.5
print(net.overall_average_temp())  # 22.5
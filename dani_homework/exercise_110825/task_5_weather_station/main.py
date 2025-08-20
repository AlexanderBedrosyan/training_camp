from reading import Reading
from station import Station
from network import Network

s1 = Station("Station 1")
s1.add_reading(Reading(20, 50))
s1.add_reading(Reading(22, 55))

s2 = Station("Station 2")
s2.add_reading(Reading(18, 60))
s2.add_reading(Reading(21, 52))

network = Network()
network.add_station(s1)
network.add_station(s2)

print("Station 1 avg temp:", s1.average_temp())
print("Overall avg temp:", network.overall_average_temp())

from reading import Reading
from station import Station
from network import Network

r1 = Reading(20, 60)
r2 = Reading(25, 55)
s = Station("Central"); s.add_reading(r1); s.add_reading(r2)

s2 = Station("Gugov")
r3 = Reading(25, 50)
r4 = Reading(20, 60)
r5 = Reading(30, 70)
s2.add_reading(r3)
s2.add_reading(r4)
s2.add_reading(r5)


net = Network(); net.add_station(s)


print(s.average_temp())            # 22.5
print(net.overall_average_temp())  # 22.5
print(f"For station {s.name} the average temperature is {s.average_temp()} and the average humidity is {s.average_humidity()}")
print(f"For station {s2.name} the average temperature is {s2.average_temp()} and the average humidity is {s2.average_humidity()}")
net.add_station(s2)
print(f'For all station "{s.name}" and "{s2.name}" the average temperature is {net.overall_average_temp()}')
print(f'For all station "{s.name}" and "{s2.name}" the average humidity is {net.overall_average_humidity()}')
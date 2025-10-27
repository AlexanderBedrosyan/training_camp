from car import Car
from bike import Bike
from bus import Bus

vehicles = [Car(100), Bike(20), Bus(60)]
for v in vehicles:
    print(v.travel_time(120))
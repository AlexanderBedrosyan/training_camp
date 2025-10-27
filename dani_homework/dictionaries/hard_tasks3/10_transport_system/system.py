# System Атрибути: private __vehicles
# Методи: add_vehicle(vehicle), fastest_vehicle(route)
from route import Route
from vehicle import Vehicle

class System:
    def __init__(self):
        self.__vehicles: list[Vehicle] = []

    def add_vehicle(self, curr_vehicle):
        self.__vehicles.append(curr_vehicle)

    def fastest_vehicle(self, curr_route:Route) -> Vehicle:
        if not self.__vehicles:
            raise ValueError("No vehicle in the system")

        fastest_v = min(
            self.__vehicles,
            key=lambda veh: veh.travel_time(curr_route.distance)
        )
        return fastest_v
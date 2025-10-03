# Network
# Атрибути: private __vehicles
# Методи: add_vehicle(), fastest_vehicle(route)
import sys

from oop_mixin_tasks.transport_network.route import Route
from oop_mixin_tasks.transport_network.vehicle import Vehicle


class Network:
    def __init__(self):
        self.__vehicles: list[Vehicle] = []

    def add_vehicle(self, curr_vehicle=Vehicle) -> None:
        self.__vehicles.append(curr_vehicle)

    def fastest_vehicle(self, route=Route):
        best_vehicle = None
        best_time = sys.maxsize

        for curr_vehicles in self.__vehicles:
            if curr_vehicles.travel_time(route) <= best_time:
                best_time = curr_vehicles.travel_time(route)
                best_vehicle = curr_vehicles
        return best_vehicle
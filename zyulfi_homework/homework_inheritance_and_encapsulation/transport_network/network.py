# Атрибути: private __routes, private __vehicles
# Методи:
# add_route(route) → добавя маршрут
# add_vehicle(vehicle) → добавя превозно средство
# fastest_vehicle(route) → връща най-бързото превозно средство за даден маршрут
import sys

from vehicle import Vehicle
from route import Route


class Network:
    def __init__(self):
        self.__routes: list[Route] = []
        self.__vehicles: list[Vehicle] = []

    def add_route(self, curr_route=object) -> None:
        self.__routes.append(curr_route)

    def add_vehicle(self, curr_vehicle) -> None:
        self.__vehicles.append(curr_vehicle)

    def fastest_vehicle(self, route=object):
        best_vehicle = None
        best_travel_time = sys.maxsize
        for curr_vehicle in self.__vehicles:
            if  curr_vehicle.travel_time(route) <= best_travel_time:
                best_travel_time = curr_vehicle.travel_time(route)
                best_vehicle = curr_vehicle
        return best_vehicle

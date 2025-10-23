# Network: списък от маршрути и превозни средства, метод fastest_vehicle(route)
from sys import maxsize
from route import Route
from vehicle import Vehicle


class Network:
    def __init__(self):
        self.list_of_route: list[Route] = []
        self.list_of_vehicle: list[Vehicle] = []

    def add_route(self, curr_route=object) -> None:
        self.list_of_route.append(curr_route)

    def add_vehicle(self, curr_vehicle=object) -> None:
        self.list_of_vehicle.append(curr_vehicle)

    def fastest_vehicle(self, route):
        best_time = maxsize
        best_vehicle = None

        for curr_vehicle in self.list_of_vehicle:
            if curr_vehicle.travel_time(route) <= best_time:
                best_time = curr_vehicle.travel_time(route)
                best_vehicle = curr_vehicle
        return best_vehicle





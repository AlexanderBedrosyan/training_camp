# Planner Атрибути: списък превозни средства и маршрути
# Методи: fastest_vehicle(route), shortest_route()
from vehicle import Vehicle
from route import Route

class Planner:
    def __init__(self):
        self.list_of_vehicles: list[Vehicle] = []
        self.list_of_routes: list[Route] = []

    def add_vehicle(self, current_vehicle):
        self.list_of_vehicles.append(current_vehicle)

    def add_route(self, current_route):
        self.list_of_routes.append(current_route)

    def fastest_vehicle(self, distance):
        fastest_v = None
        best_time = 0
        for current_vehicle in self.list_of_vehicles:
            if best_time <= current_vehicle.travel_time(distance):
                best_time = current_vehicle.travel_time(distance)
                fastest_v = current_vehicle
        return fastest_v.name

    def sortest_route(self):
        s_route = None
        s_distance = float('inf')
        for curr_route in self.list_of_routes:
            if curr_route.distance <= s_distance:
                s_distance = curr_route.distance
                s_route = curr_route
        return str(s_route)







#Network: списък от маршрути и превозни средства, метод fastest_vehicle(route)

class Network:
    def __init__(self):
        self.__routes = []
        self.__vehicles = []

    def add_route(self, route):
        self.__routes.append(route)

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def fastest_vehicle(self, route):
        if not self.__vehicles:
            raise ValueError("Няма добавени превозни средства в мрежата.")

        fastest = self.__vehicles[0]
        fastest_time = fastest.travel_time(route)

        for v in self.__vehicles[1:]:
            t = v.travel_time(route)
            if t < fastest_time:
                fastest = v
                fastest_time = t

        return fastest

    def routes(self):
        return list(self.__routes)

    def vehicles(self):
        return list(self.__vehicles)

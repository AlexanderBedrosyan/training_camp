# Network: списък от станции, метод overall_average_temp()
from station import Station

class Network:
    def __init__(self):
        self.stations = []

    def add_station(self, station: Station):
        # Добавя метеорологична станция към мрежата.
        self.stations.append(station)

    def overall_average_temp(self) -> float:
        # Изчислява средната температура от всички станции.
        if not self.stations:
            return 0.0
        temps = [s.average_temp() for s in self.stations if s.average_temp() != 0]
        if not temps:
            return 0.0
        return sum(temps) / len(temps)

    def overall_average_humidity(self) -> float:
        # (по желание) Изчислява средната влажност за всички станции.
        if not self.stations:
            return 0.0
        hums = [s.average_humidity() for s in self.stations if s.average_humidity() != 0]
        if not hums:
            return 0.0
        return sum(hums) / len(hums)

    def __str__(self):
        return f"Network({len(self.stations)} stations)"

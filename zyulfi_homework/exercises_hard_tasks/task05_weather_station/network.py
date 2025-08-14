# Network: списък от станции, метод overall_average_temp()
from station import Station

class Network:
    def __init__(self):
        self.list_station: list[Station] = []

    def add_station(self, current_station):
        self.list_station.append(current_station)

    def overall_average_temp(self):
        total_sum = 0
        for station in self.list_station:
            total_sum += station.average_temp()
        return total_sum / len(self.list_station)

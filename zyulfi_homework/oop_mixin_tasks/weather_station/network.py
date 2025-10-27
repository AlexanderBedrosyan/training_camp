# Network
# Атрибути: private __stations
# Методи: add_station(), overall_avg_temp()
from oop_mixin_tasks.weather_station.station import Station


class Network:
    def __init__(self):
        self.__stations: list[Station] = []

    def add_station(self, curr_station) -> None:
        self.__stations.append(curr_station)

    def overall_avg_temp(self):
        best_station = None
        best_avg_tem = 0

        for curr_station in self.__stations:
            if curr_station.avg_temp() >= best_avg_tem:
                best_avg_tem = curr_station.avg_temp()
                best_station = curr_station
        return best_station.avg_temp()
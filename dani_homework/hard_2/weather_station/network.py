#  списък от станции; метод overall_average_temp()
from typing import List
from station import Station

class Network:
    def __init__(self):
        self.list_station: List[Station] = []

    def add_station(self, current_station):
        self.list_station.append(current_station)

    def overall_average_temp(self):
        all_av_temp = 0
        for current_stat in self.list_station:
            all_av_temp += current_stat.average_temp()

        return all_av_temp / len(self.list_station)


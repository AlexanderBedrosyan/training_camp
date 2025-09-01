# списък от станции; метод overall_average_temp()
from station import Station

class Network:
    def __init__(self, name=str):
        self.name = name
        self.list_of_station: list[Station] = []

    def add_station(self, curr_station=object) -> None:
        self.list_of_station.append(curr_station)

    def overall_average_temp(self) -> float:
        return sum([curr_temp.average_temp() for curr_temp in self.list_of_station]) / len(self.list_of_station)

    def overall_average_humidity(self) -> float:
        return sum([curr_humidity.average_humidity() for curr_humidity in self.list_of_station]) / len(self.list_of_station)
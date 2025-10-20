# Station (AvgMixin)
# Атрибути: private __readings
# Методи: add_reading(), avg_temp(), avg_humidity()
from oop_mixin_tasks.weather_station.avg_mixin import AvgMixin
from oop_mixin_tasks.weather_station.reading import Reading


class Station(AvgMixin):
    def __init__(self):
        self.__readings: list[Reading] = []

    def add_reading(self, curr_reading) -> None:
        self.__readings.append(curr_reading)

    def avg_temp(self):
        return sum([curr_reading.temperature for curr_reading in self.__readings]) / len(self.__readings)

    def avg_humidity(self):
        return sum([curr_reading.humidity for curr_reading in self.__readings]) / len(self.__readings)

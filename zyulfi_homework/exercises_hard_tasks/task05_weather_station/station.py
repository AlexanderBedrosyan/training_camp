# Station: списък от Reading обекти, методи average_temp(), average_humidity()
from reading import Reading


class Station:
    def __init__(self, name):
        self.name = name
        self.list_of_reading: list[Reading] = []

    def add_reading(self, current_obj):
        self.list_of_reading.append(current_obj)

    def average_temp(self):
        total_temp = 0
        for reading_obj in self.list_of_reading:
            total_temp += reading_obj._Reading__temperature
        return total_temp / len(self.list_of_reading)

    def average_humidity(self):
        total_humidity = 0
        for reading_obj in self.list_of_reading:
            total_humidity += reading_obj._Reading__humidity
        return total_humidity / len(self.list_of_reading)




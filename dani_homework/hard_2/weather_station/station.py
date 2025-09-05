# списък от Reading; методи average_temp(), average_humidity()
from typing import List
from reading import Reading


class Station:
    def __init__(self, name=str):
        self.name = name
        self.list_reading: List[Reading] = []

    def add_reading(self, current_reading:object):
        self.list_reading.append(current_reading)

    def average_temp(self):
        current_temp = 0
        for current_reading in self.list_reading:
            current_temp += current_reading.return_temp()

        return current_temp / len(self.list_reading)

    def average_humidity(self):
        current_humidity = 0
        for current_reading in self.list_reading:
            current_humidity += current_reading.return_humidity()

        return current_humidity / len(self.list_reading)




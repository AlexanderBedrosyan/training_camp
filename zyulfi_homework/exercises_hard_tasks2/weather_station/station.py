# списък от Reading; методи average_temp(), average_humidity()
from reading import Reading

class Station:
    def __init__(self, name=str):
        self.name = name
        self.list_of_reading: list[Reading] = []

    def add_reading(self, curr_reading=object) -> None:
        self.list_of_reading.append(curr_reading)

    def average_temp(self) -> float:
        return sum([curr_temp.get_temperature() for curr_temp in self.list_of_reading]) / len(self.list_of_reading)

    def average_humidity(self) -> float:
        return sum([curr_humidity.get_humidity() for curr_humidity in self.list_of_reading]) / len(self.list_of_reading)




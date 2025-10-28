# Station: списък от Reading обекти, методи average_temp(), average_humidity()
from reading import Reading

class Station:
    def __init__(self, name: str):
        self.name = name
        self.readings = []

    def add_reading(self, reading: Reading):
        # Добавя измерване към станцията.
        self.readings.append(reading)

    def average_temp(self) -> float:
        # Връща средната температура от всички измервания.
        if not self.readings:
            return 0.0
        return sum(r.get_temperature() for r in self.readings) / len(self.readings)

    def average_humidity(self) -> float:
        # Връща средната влажност от всички измервания.
        if not self.readings:
            return 0.0
        return sum(r.get_humidity() for r in self.readings) / len(self.readings)

    def __str__(self):
        return f"Station({self.name}, readings={len(self.readings)})"

# Thermostat наследява Device, има @property temperature,
# който се валидира (10-30 градуса) main.py:

from device import Device

class Thermostat(Device):
    def __init(self, status=False, temperature=int):
        super().__init__(status)
        self._temperature = None
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 10 <= value <= 30:
            self._temperature = value
        else:
            raise ValueError("Temperature must be between 10 and 30 degrees.")

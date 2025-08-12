# Thermostat наследява Device, има @property temperature, който се валидира (10-30 градуса)

from device import Device

class Thermostat(Device):
    def __init__(self):
        super().__init__()
        self.temperature = 20

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 10 <= value <= 30:
            self._temperature = value
        else:
            raise ValueError("Temperature must be between 10 and 30")


# Клас Device с: class атрибут devices_on = 0
# методи power_on() / power_off()

class Device:
    devices_on = 0

    def __init__(self):
        self._is_on = False  # state

    def power_on(self):
        if not self._is_on:
            self._is_on = True
            Device.devices_on += 1

    def power_off(self):
        if self._is_on:
            self._is_on = False
            Device.devices_on -= 1
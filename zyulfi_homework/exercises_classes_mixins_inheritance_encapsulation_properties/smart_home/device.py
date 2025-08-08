# Device: базов клас с protected атрибут _status и методи turn_on() и turn_off()

class Device:
    def __init__(self):
        self._status = False

    def turn_on(self):
        self._status = True

    def turn_off(self):
        self._status = False

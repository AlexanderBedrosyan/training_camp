# Device: базов клас с protected атрибут _status и методи turn_on() и turn_off()

class Device:
    def __init__(self, status=False):
        self._status = status

    def turn_on(self):
        if not self._status:
            self._status = True
            print("Device is now ON")
        else:
            print("Device is already ON")

    def turn_off(self):
        if self._status:
            self._status = False
            print("Device is now OFF")
        else:
            print("Device is already OFF")
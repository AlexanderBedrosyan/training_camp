# Light наследява Device, има private атрибут __brightness с @property и @setter

from device import Device

class Light(Device):
    def __init__(self):
        super().__init__()
        self.__brightness = 0

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
            if value == 0:
                self.turn_off()
            else:
                self.turn_on()
        else:
            raise ValueError("Brightness must be between 0 and 100")
# Light наследява Device, има private атрибут __brightness с @property и @setter

from device import Device


class Light(Device):
    def __init__(self, status=bool, brightness=int):
        super().__init__(status)
        self.__brightness = brightness

        @property
        def brightness(self):
            return self.__brightness

        @brightness.setter
        def brightness(self, value):
            if 0<= value <= 100:
                self.__brightness = value
            else:
                raise ValueError("Brightness must be between 0 and 100")
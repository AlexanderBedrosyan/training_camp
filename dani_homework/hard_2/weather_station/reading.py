# private __temperature, __humidity; методи за достъп

class Reading:
    def __init__(self, temperature, humidity):
        self.__temperature = temperature
        self.__humidity = humidity

    def return_temp(self):
        return self.__temperature

    def return_humidity(self):
        return self.__humidity

# r=Reading(25,35)
# print(r.return_temp())
# print(r.return_humidity())


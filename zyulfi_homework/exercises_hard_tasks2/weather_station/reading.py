#private __temperature, __humidity; методи за достъп

class Reading:
    def __init__(self, temperature=float, humidity=float):
        self.__temperature = temperature
        self.__humidity = humidity

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity
        
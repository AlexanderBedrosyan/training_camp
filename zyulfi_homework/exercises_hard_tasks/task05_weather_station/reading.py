# Reading: private __temperature, __humidity, методи за достъп

class Reading:
    def __init__(self, temperature, humidity):
        self.__temperature = temperature
        self.__humidity = humidity
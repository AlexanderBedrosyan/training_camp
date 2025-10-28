# Reading: private __temperature, __humidity, методи за достъп
class Reading:
    def __init__(self, temperature: float, humidity: float):
        self.__temperature = temperature
        self.__humidity = humidity

    def get_temperature(self) -> float:
        # Връща измерената температура.
        return self.__temperature

    def get_humidity(self) -> float:
        # Връща измерената влажност.
        return self.__humidity

    def __str__(self):
        return f"Reading(T={self.__temperature}°C, H={self.__humidity}%)"

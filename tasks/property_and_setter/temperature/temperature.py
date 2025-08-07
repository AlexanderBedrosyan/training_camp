# Клас Temperature с:
# protected атрибут _celsius
# @property fahrenheit, който изчислява: F = C * 1.8 + 32

class Temperature:

    def __init__(self, celsius=float):
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 1.8 + 32

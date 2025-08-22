# engine.py:
# Клас Engine с:
# private атрибут __power
# @property за достъп до него
# Свържи двата чрез нов клас Car(Vehicle, Engine), който стартира двигателя.


class Engine:
    def __init__(self, power):
        self.__power = power

    @property
    def power(self):
        return self.__power


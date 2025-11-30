# 1. Клас BaseRobot
# Файл: base_robot.py
# Базов клас за роботи. Не може да се инстанцира.
#
# Атрибути:
# • name: str – име на робота
#   – Ако е празно или само с интервали → ValueError: "Robot name cannot be empty!"
# • kind: str – вид на робота
#   – Ако е празно или само интервали → ValueError: "Robot kind cannot be empty!"
# • price: float – цена на робота
#   – Ако <= 0.0 → ValueError: "Robot price cannot be less than or equal to 0.0!"
# • weight: int – килограми

#
# Методи:
# • __init__(name, kind, price, weight)
# • eating() – увеличава килограмите на робота (различно при мъжки/женски робот)


from abc import ABC, abstractmethod

class BaseRobot(ABC):
    def __init__(self, name, kind, price, weight):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")
        self.__name = value


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value.strip():
            raise ValueError("Robot kind cannot be empty!")
        self.__kind = value


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self.__price = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Robot weight cannot be less than or equal to 0.0!")
        self.__weight = value

    @abstractmethod
    def eating(self):
        pass

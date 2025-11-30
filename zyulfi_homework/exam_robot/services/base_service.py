# 4. Клас BaseService
# Файл: base_service.py
# Базов клас за сервизи. Не може да се инстанцира.
#
# Атрибути:
# • name: str
#   – Ако е празно → ValueError: "Service name cannot be empty!"
# • capacity: int
#   – Ако <= 0 → ValueError: "Service capacity cannot be less than or equal to 0!"
# • robots: list – списък с роботи
#
# Методи:
# • __init__(name, capacity)
# • details() – информация за сервиза

from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.robots = []

    def add_robot(self, curr_robot):
        self.robots.append(curr_robot)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass

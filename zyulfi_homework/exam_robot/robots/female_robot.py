# 2. Клас FemaleRobot
# Файл: female_robot.py
# Наследява BaseRobot. Начално тегло: 7 кг.
#
# Методи:
# • __init__(name, kind, price)
# • eating() – увеличава теглото с 1 кг
from robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, 7)

    def eating(self):
        self.weight += 1


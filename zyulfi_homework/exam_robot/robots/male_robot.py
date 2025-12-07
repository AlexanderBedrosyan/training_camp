# 3. Клас MaleRobot
# Файл: male_robot.py
# Наследява BaseRobot. Начално тегло: 9 кг.
#
# Методи:
# • __init__(name, kind, price)
# • eating() – увеличава теглото с 3 кг

from robots.base_robot import BaseRobot

class MaleRobot(BaseRobot):
    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, 9)

    def eating(self):
        self.weight += 3


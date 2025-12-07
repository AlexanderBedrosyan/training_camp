# 5. Клас MainService
# Файл: main_service.py
# Наследява BaseService. Капацитет: 30
#
# Методи:
# • __init__(name)
# • details() – "{service_name} Main Service:
# Robots: ..."
from services.base_service import BaseService
from robots.female_robot import FemaleRobot
from robots.male_robot import MaleRobot


class MainService(BaseService):
    def __init__(self, name):
        super().__init__(name, 30)


    def details(self):
        name_robot = ""
        for curr_robot in self.robots:
            name_robot += curr_robot.name + ", "
        if name_robot:
            name_robot = name_robot.rstrip(", ")

        return f"{self.name} Main Service:\nRobots: {name_robot}"

# r1 = MaleRobot("dragancho", "elf", 10)
# r2 = FemaleRobot("geri", "elf", 5)
# ms = MainService("Ivomir")
# ms.add_robot(r1)
# ms.add_robot(r2)
# print(ms.details())

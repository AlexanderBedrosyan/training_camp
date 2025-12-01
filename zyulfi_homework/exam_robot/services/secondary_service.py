# 6. Клас SecondaryService
# Файл: secondary_service.py
# Наследява BaseService. Капацитет: 15
#
# Методи:
# • __init__(name)
# • details() – "{service_name} Secondary Service:
# Robots: ..."
from services.base_service import BaseService
from robots.male_robot import MaleRobot
from robots.female_robot import FemaleRobot

class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, 15)


    def details(self):
        name_robot = ""
        for curr_robot in self.robots:
            name_robot += curr_robot.name + ", "
        if name_robot:
            name_robot = name_robot.rstrip(", ")

        return f"{self.name} Secondary Service:\nRobots: {name_robot}"

# r1 = MaleRobot("dragancho", "elf", 10)
# r2 = FemaleRobot("geri", "elf", 5)
# ms = SecondaryService("Lyobcho")
# ms.add_robot(r1)
# ms.add_robot(r2)
# print(ms.details())
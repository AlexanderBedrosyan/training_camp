# 7. Клас RobotsManagingApp
# Файл: robots_managing_app.py
# Управлява цялата система.
#
# Атрибути:
# • robots: list – всички създадени роботи
# • services: list – всички сервизи
#
# Методи:
# • __init__()
# • add_service(type, name)
#   – Ако невалиден тип → Exception: "Invalid service type!"
#   – Иначе → "{service_type} is successfully added."
#
# • add_robot(type, name, kind, price)
#   – Ако невалиден тип → Exception: "Invalid robot type!"
#   – Иначе → "{robot_type} is successfully added."
#
# • add_robot_to_service(robot_name, service_name)
#   – Женски роботи → само SecondaryService
#   – Мъжки роботи → само MainService
#   – Ако несъвместим → "Unsuitable service."
#   – Ако няма капацитет → Exception: "Not enough capacity for this robot!"
#   – Иначе → "Successfully added {robot_name} to {service_name}."
#
# • remove_robot_from_service(robot_name, service_name)
#   – Ако роботът не е в сервиза → Exception: "No such robot in this service!"
#   – Иначе → "Successfully removed {robot_name} from {service_name}."
#
# • feed_all_robots_from_service(service_name)
#   – Храни всички роботи → "Robots fed: {count}."
#
# • service_price(service_name)
#   – Връща: "The value of service {service_name} is {price}."
#
# • __str__()
#   – Показва информация за всички сервизи
#
# "{service_name1} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# {service_name2} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# …
# {service_nameN} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}"
from robots.female_robot import FemaleRobot
from robots.male_robot import MaleRobot
from services.main_service import MainService
from services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, type, name):
        curr_service = None
        if type == "SecondaryService":
            curr_service = SecondaryService(name)
        elif type == "MainService":
            curr_service = MainService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(curr_service)
        return f"{type} is successfully added."

    def add_robot(self, type, name, kind, price):
        curr_robot = None

        if type == "MaleRobot":
            curr_robot = MaleRobot(name, kind, price)
        elif type == "FemaleRobot":
            curr_robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(curr_robot)
        return f"{type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot_needed = None
        service_needed = None
        for curr_robot in self.robots:
            if curr_robot.name == robot_name:
                robot_needed = curr_robot

        for curr_service in self.services:
            if curr_service.name == service_name:
                service_needed = curr_service

        if not robot_needed:
            return "Missing robot"

        if not service_needed:
            return "Missing service"

        if robot_needed.__class__.__name__ == "FemaleRobot" and service_needed.__class__.__name__ == "SecondaryService":
            if len(service_needed.robots) >= service_needed.capacity:
                raise Exception("Not enough capacity for this robot!")

        elif robot_needed.__class__.__name__ == "MaleRobot" and service_needed.__class__.__name__ == "MainService":
            if len(service_needed.robots) >= service_needed.capacity:
                raise Exception("Not enough capacity for this robot!")

        else:
            return "Unsuitable service."

        service_needed.add_robot(robot_needed)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        needed_service = None
        ind_robot = None
        for current_service in self.services:
            if current_service.name == service_name:
                needed_service = current_service
                break
        if not needed_service:
            raise Exception("No such robot in this service!")
        for i in range(len(needed_service.robots)):
            current_robot = needed_service.robots[i]

            if current_robot.name == robot_name:
                ind_robot = i

        if ind_robot is not None:
            needed_service.robots.pop(i)
            return f"Successfully removed {robot_name} from {service_name}."

        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name):
        service_needed = None
        for curr_service in self.services:
            if curr_service.name == service_name:
                service_needed = curr_service

        if not service_needed:
            return "Missing service"

        counter = 0
        for curr_robot in service_needed.robots:
            counter += 1
            curr_robot.eating()

        return f"Robots fed: {counter}."

    def service_price(self, service_name):
        service_needed = None
        for curr_service in self.services:
            if curr_service.name == service_name:
               service_needed = curr_service

        if not service_needed:
            return "Missing service"

        all_price = 0
        for curr_robot in service_needed.robots:
            all_price += curr_robot.price

        return f"The value of service {service_name} is {all_price}."

    def __str__(self):

        list_service = []

        for curr_service in self.services:
            list_service.append(f"{curr_service.name} {curr_service.__class__.__name__}:")
            all_robots = "Robots:"
            for curr_robot in curr_service.robots:
                all_robots += f" {curr_robot.name}"

            list_service.append(all_robots)

        return '\n'.join(list_service)


# • __str__()
#   – Показва информация за всички сервизи
#
# "{service_name1} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# {service_name2} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}
# …
# {service_nameN} {service_type}:
# Robots: {robot_name1} {robot_name2} … {robot_nameN}"
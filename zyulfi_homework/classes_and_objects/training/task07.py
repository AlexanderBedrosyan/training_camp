# Задача 7
# Създай клас Robot с метод __compute() и атрибут __power_level.
# Достъпи и двете от външен код чрез name mangling.

class Robot:
    def __init__(self, power_level=int):
        self.__power_level = power_level

    def __compute(self) -> None:
        print(self.__power_level + 1)

current_robot = Robot(5)

current_robot._Robot__compute()
print(current_robot._Robot__power_level)


# current_user._User__display()
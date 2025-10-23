# Атрибути: name, private __animals
# Методи:
# add_animal(animal)
# list_animals()
from exercises_hard_task3.zoo_management.animal import Animal


class Zookeeper:
    def __init__(self, name):
        self.name = name
        self.__animals: list[Animal] = []

    def add_animal(self, curr_animal:Animal):
        self.__animals.append(curr_animal)

    def list_animals(self) -> list[Animal]:
        return self.__animals
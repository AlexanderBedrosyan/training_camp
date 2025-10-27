# Атрибути: private __zookeepers
# Методи:
# add_keeper(keeper)
# all_animals()
from exercises_hard_task3.zoo_management.zookeeper import Zookeeper


class Zoo:
    def __init__(self):
        self.__zookeepers: list[Zookeeper] = []

    def add_keeper(self, cuur_zookeeper:Zookeeper):
        self.__zookeepers.append(cuur_zookeeper)

    def all_animals(self):
        list_of_animals = []
        for cuur_zookeeper in self.__zookeepers:
            for curr_animal in cuur_zookeeper.list_animals():
                list_of_animals.append(curr_animal)

        return list_of_animals

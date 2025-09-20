# Zoo Атрибути: private __zookeepers
# Методи: add_keeper(keeper)
# all_animals()
from zookeeper import Zookeeper


class Zoo:
    def __init__(self):
        self.__zookeepers: list[Zookeeper] = []

    def add_keeper(self,current_keeper:Zookeeper):
        self.__zookeepers.append(current_keeper)

    def all_animals(self) -> list[str]:
        return [animal.species
            for current_keeper in self.__zookeepers
            for animal in current_keeper.list_animals()]


        # return [f"{animal.species} ({animal.age})"
        #     for keeper in self.__zookeepers
        #     for animal in keeper.list_animals()]

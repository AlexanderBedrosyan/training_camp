# Zookeeper Атрибути: name, private __animals
# Методи: add_animal(animal)
# list_animals()
from animal import Animal


class Zookeeper:
    def __init__(self, name:str):
        self.name = name
        self.__animals: list[Animal] = []

    def add_animal(self, curr_animal:Animal) -> None:
        self.__animals.append(curr_animal)

    def list_animals(self) -> list[Animal]:
        return list(self.__animals)


#test
z1=Zookeeper("Dragan")
a1=Animal("Tiger", 2)
a2=Animal("Elephnat", 10)

z1.add_animal(a1)
z1.add_animal(a2)

for animal in z1.list_animals():
    print(animal)
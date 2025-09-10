from hard3.zoo_management.zookeeper import animal
from animal import Animal
from cage import Cage
from zoo import Zoo


def main():
    # Създаваме животни
    lion = Animal("Симба", "лъв")
    zebra = Animal("Мартин", "зебра")
    parrot = Animal("Пол", "папагал")
    tiger = Animal("Шер Хан", "тигър")

    # Създаваме клетки
    c1 = Cage(1, 2)
    c2 = Cage(2, 3)

    # Добавяме животни
    c1.add_animal(lion)
    c1.add_animal(zebra)
    c2.add_animal(parrot)
    c2.add_animal(tiger)

    # Създаваме зоологическа градина
    zoo = Zoo()
    zoo.add_cage(c1)
    zoo.add_cage(c2)

    # Печат
    print(zoo)
    print("Най-голямата клетка е:", zoo.largest_cage().number)
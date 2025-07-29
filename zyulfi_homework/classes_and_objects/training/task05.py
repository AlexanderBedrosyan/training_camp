# Задача 5
# Създай клас Person с инстанс атрибут name и клас атрибут species = "Human".
# Създай няколко обекта и покажи как species е споделен.

class Person:
    species = "Human"

    def __init__(self, name=str):
        self.name = name

person1 = Person("Dragancho")
person2 = Person("Trosho")
person3 = Person("Pesho")

print(person1.name)
print(Person.species)

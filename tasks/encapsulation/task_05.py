# Създай клас Person с инстанс атрибут name и клас атрибут species = "Human". Създай няколко обекта и покажи как species
# е споделен.

class Person:
    species = "Human"

    def __init__(self, name=str):
        self.name = name


person1 = Person("Gosho")
person2 = Person("Trosho")
person3 = Person("Sosho")

print(Person.species)
print(person1.name)

print(Person.species)
print(person2.name)

print(Person.species)
print(person3.name)
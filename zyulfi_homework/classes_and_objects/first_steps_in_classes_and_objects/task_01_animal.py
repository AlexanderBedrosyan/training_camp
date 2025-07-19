# Задача 1
# Създай клас Animal, който има атрибут species. Създай обект и принтирай вида на животното.

class Animal:
    def __init__(self, species):
        self.species = species

current_animal = Animal("cat")

print(current_animal.species)
# Animal
# Атрибути: name, species
# Метод: __str__()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"The {self.name} is {self.species}"
# Атрибути: species, age
# Метод: __str__()

class Animal:
    def __init__(self, species, age=float):
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.species} - {self.age}"
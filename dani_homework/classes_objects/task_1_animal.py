# Създай клас Animal, който има атрибут species.
# Създай обект и принтирай вида на животното.

class Animal:
    def __init__(self, species):
        self.species = species  # атрибут

    def print_animal(self):
        print(f"Animal speices is: {self.species}")

# Създаване на обекти
animal_1 = Animal ("Fishe")
animal_2 = Animal ("Birds")
animal_3 = Animal ("Arthropods")

animal_1.print_animal()
animal_2.print_animal()
animal_3.print_animal()
# Animal Атрибути: species, age
# Метод: __str__()

class Animal:
    def __init__(self, species:str, age:int):
        self.species = species
        self.age = age

    def __str__(self) -> str:
        return f"the animal is of type {self.species} and it is {self.age} years old"

a1=Animal("Leo", 3)
print(a1)
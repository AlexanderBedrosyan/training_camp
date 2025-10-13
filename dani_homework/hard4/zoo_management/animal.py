# Animal # Атрибути: name, species
# Метод: __str__()

class Animal:
    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species

    def __str__(self):
        return f'The animal {self.name} is type of {self.species}'

#test
a1=Animal("Leo", "BigCat")
print(a1)
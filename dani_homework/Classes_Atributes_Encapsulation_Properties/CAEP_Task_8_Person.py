# Създай клас Person с:
# обикновен атрибут name
# класов атрибут species = "Human"
# метод info() – връща "{name} is a {species}"
# метод change_species(new_species) – създава инстанс атрибут,
# който засенчва класовия
# Примерен вход:
# p1 = Person("Mira")
# p2 = Person("Alex")
# p2.change_species("Alien")
# print(p1.info())  # Mira is a Human
# print(p2.info())  # Alex is a Alien
#--------------------------------------------------------

class Person:
    species = "Human"  # класов атрибут

    def __init__(self, name = str) -> None:
        self.name = name                        # обикновен атрибут

    def info(self) -> str:                      # Връща "{name} is a {species}"
                                                # Ако инстансът има атрибут species, ползва него, иначе класовия
        species = getattr(self, 'species', Person.species)
        return f"{self.name} is a {species}"

    def change_species(self, new_species: str) -> None: # Създава инстанс атрибут species, който засенчва класовия
        self.species = new_species

# Употреба
p1 = Person("Mara")
p2 = Person("Alexandro")
p2.change_species("Alien")

print(p1.info())  #
print(p2.info())  #

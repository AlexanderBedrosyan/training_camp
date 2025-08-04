# Създай клас Person с инстанс атрибут name и клас атрибут species = "Human".
# Създай няколко обекта и покажи как species е споделен.
# ----------------------------------------------------------

class Person:
    species = "Human"  # Класов атрибут (споделен от всички обекти)

    def __init__(self, name):
        self.name = name  # Инстансен атрибут (индивидуален за всеки обект)

# Създаваме обекти
user_1 = Person("Alice")
user_2 = Person("Bob")

# Достъп до species от всеки обект
print("user_1.name:", user_1.name)              # -> Alice (тип: str)
print("user_2.name:", user_2.name)              # -> Bob (тип: str)

print("user_1.species:", user_1.species)        # -> Human (тип: str)
print("user_2.species:", user_2.species)        # -> Human (тип: str)
print("Person.species:", Person.species)  # -> Human (тип: str)

# Промяна на species на ниво клас (ще се отрази на всички обекти)
Person.species = "Homo sapiens"

print("След промяна:")
print("user_1.species:", user_1.species)        # -> Homo sapiens
print("user_2.species:", user_2.species)        # -> Homo sapiens
print("Person.species:", Person.species)        # -> Homo sapiens

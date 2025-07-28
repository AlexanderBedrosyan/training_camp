# Single Inheritance

# Създай клас Animal с метод eat(), който принтира "eating...".
# Създай клас Dog, който наследява Animal и има метод bark(), който принтира "barking...".
# Създай обект на Dog и извикай двата метода.
# -------------------------------------------------------------


class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} eating...")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barking...")

# въвеждане на обект и тестване

animal_1 = Dog("The Dog Muncho")
animal_1.eat()  #
animal_1.bark()  #
# Създайте програма, която приема списък от обекти (Dog, Cat, Bird) и
# за всеки извиква метод make_sound(). Добавете нов клас Fish, който няма make_sound(),
# и се уверете, че програмата може да обработи това чрез проверка с hasattr().

from abc import  ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bau, bau"

class Cat(Animal):
    def make_sound(self):
        return "Mau, mau"

class Bird(Animal):
    def make_sound(self):
        return "Cik, chirik"

class Fish:
    pass

d = Dog()
c = Cat()
b = Bird()
f = Fish()

list_of_animals = [d, c, b, f]

for curr_animal in list_of_animals:
    if hasattr(curr_animal,"make_sound"):
        print(curr_animal.make_sound())
    else:
        print("No sound")


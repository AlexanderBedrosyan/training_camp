# Задача 2
# Направете функция animal_sound(animal), която приема обект и извиква неговия метод make_sound(). Тествайте я
# с класове Dog, Cat, Cow.
from abc import ABC, abstractmethod


def animal_sound(animal:object):
    return animal.make_sound()

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Barking...")

class Cow(Animal):
    def make_sound(self):
        print("Muuuh...")

class Cat(Animal):
    def make_sound(self):
        print("Myaw...")


d = Dog()
cow = Cow()
cat = Cat()

animal_sound(d)
animal_sound(cow)
animal_sound(cat)
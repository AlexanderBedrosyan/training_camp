# 🔹 Задача 2
# Създай клас Animal с метод make_sound(), връщащ "Some sound".
# Създай клас Cat, който наследява Animal и override-ва make_sound() да връща "Meow".

class Animal:

    def make_sound(self):
        return "Some sound"

class Cat(Animal):

    def make_sound(self):
        return "Meow"

animal = Animal()
cat = Cat()

print(animal.make_sound())
print(cat.make_sound())
# Задача 2
# Създай клас Animal с метод make_sound(), връщащ "Some sound".
# Създай клас Cat, който наследява Animal и override-ва make_sound() да връща "Meow".

class Animal:
    def make_sound(self) -> str:
        return f"Some sound"

class Cat(Animal):
    def make_sound(self) -> str:
        return f"Meow"

current_animal = Animal()
current_cat = Cat()

print(current_animal.make_sound())
print(current_cat.make_sound())

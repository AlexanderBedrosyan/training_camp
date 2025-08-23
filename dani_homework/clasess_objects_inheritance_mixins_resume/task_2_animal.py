# Създай клас Animal с метод make_sound(), връщащ "Some sound".
# Създай клас Cat, който наследява Animal и
# override-ва make_sound() да връща "Meow".
# ------------------------------------------------------------------------

class Animal:
    def make_sound(self)->str:
        return "Some sound"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"
c = Cat()
print(c.make_sound())

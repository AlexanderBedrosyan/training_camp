# ✅ Задача 1 – Single Inheritance Създай клас Animal с метод eat(), който принтира "eating...". Създай клас Dog,
# който наследява Animal и има метод bark(), който принтира "barking...". Създай обект на Dog и извикай двата метода.

class Animal: # Parent
    def eat(self):
        print("eating...")

class Dog(Animal): # Child
    def bark(self):
        print("barking...")


dog = Dog()
dog.eat()
dog.bark()
# ✅ Задача 1
# Създай клас Person, който има атрибути name и age. Създай обект и принтирай
# "Hello, my name is {name} and I am {age} years old."

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Traycho", 78)
person2 = Person("Gergincho", 62)

# Part 1
print(person.say_hello())
print(person2.say_hello())

# Part 2
print(f"Hello, my name is {person.name} and I am {person.age} years old.")
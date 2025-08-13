# Създай клас Student, който има атрибут name.
# Добави метод greet(), който принтира "Hello, my name is {name}."

class Student:
    def __init__(self, name):
        self.name = name  # атрибут

    def greet(self):
        print(f"Hello, my name is {self.name}.")

student1 = Student ('Ann')
student1.greet()

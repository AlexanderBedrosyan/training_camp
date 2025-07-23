# Задача 6
# Създай клас Student, който има атрибут name. Добави метод greet(),
# който принтира "Hello, my name is {name}."

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

current_student = Student(input("Please enter а student name: "))

Student.greet(current_student)
# Teacher (наследява Person): subject, private __students;
# методи add_student(), class_average()
from inheritance.task_5_person import student
from person import Person


class Teacher(Person):
    def __init__(self, name:str, age:int, subject:str):
        super().__init__(name, age)
        self.subject = subject
        self.__students = []

    def add_student(self, cur_student):
        self.__students.append(cur_student)

    def class_average(self):
        if not self.__students:
            return 0
        total = sum(cur_student.average() for cur_student in self.__students)
        return total / len(self.__students)

    def __str__(self):
        return f"Teacher {self.name}, {self.age} years old, teaches {self.subject} "
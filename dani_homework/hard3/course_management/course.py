# Course
# Атрибути: name, private __students
# Методи: add_student(student) # average_grade()
from student import Student


class Course:
    def __init__(self, name:str):
        self.name = name
        self.__students: list[Student] = []

    def add_student(self, student:Student):
        self.__students.append(student)
        #return self.__students

    def average_grade(self) -> float:
        if not self.__students:
            return 0
        return sum(s.average() for s in self.__students) / len(self.__students)

    def get_students(self) -> list[Student]:
        return self.__students
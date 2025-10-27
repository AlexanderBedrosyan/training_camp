# Атрибути: name, private __students
# Методи:
# add_student(student)
# average_grade()
from exercises_hard_task3.course_management.student import Student


class Course:
    def __init__(self, name):
        self.name = name
        self.__students: list[Student] = []

    def add_student(self, curr_student):
        self.__students.append(curr_student)

    def average_grade(self):
        return sum([curr_student.average() for curr_student in self.__students]) / len(self.__students)

    def curse_best_student(self):
        best_student = None
        best_grade = 0
        for curr_student in self.__students:
            if curr_student.average() >= best_grade:
                best_grade = curr_student.average()
                best_student = curr_student
        return best_student

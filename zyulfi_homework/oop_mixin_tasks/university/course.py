# Course (GradeMixin)
# Атрибути: name, private __students
# Методи: add_student(), course_average()
from oop_mixin_tasks.university.grade_mixin import GradeMixin
from oop_mixin_tasks.university.student import Student


class Course(GradeMixin):
    def __init__(self, name=str):
        self.name = name
        self.__students: list[Student] = []

    def add_student(self, curr_student):
        self.__students.append(curr_student)

    def course_average(self):
        return sum([curr_student.average() for curr_student in self.__students]) / len(self.__students)

    def best_student_of_course(self):
        best_student = None
        best_average_grade = 0
        for curr_student in self.__students:
            if curr_student.average() >= best_average_grade:
                best_average_grade = curr_student.average()
                best_student = curr_student
        return best_student


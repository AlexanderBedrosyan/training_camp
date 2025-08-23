# Course: име, списък от студенти, метод average_grade()
from student import Student


class Course:
    def __init__(self, name_course=str):
        self.name_course = name_course
        self.list_of_student: list[Student] = []

    def add_student(self, curr_student=object):
        self.list_of_student.append(curr_student)

    def average_grade(self) -> float:
        total_grades_of_student = 0
        for curr_student in self.list_of_student:
            total_grades_of_student += curr_student.average()
        return total_grades_of_student / len(self.list_of_student)



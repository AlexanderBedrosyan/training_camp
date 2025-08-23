# Course: име, списък от студенти, метод average_grade()
from student import Student


class Course:
    def __init__(self, name):
        self.name = name
        self.list_of_student: list[Student] = []

    def add_student(self, current_student):
        self.list_of_student.append(current_student)

    def average_grade(self):
        total_grade_allstudents = 0
        for current_student in self.list_of_student:
            total_grade_allstudents += current_student.average()
        return total_grade_allstudents / len(self.list_of_student)

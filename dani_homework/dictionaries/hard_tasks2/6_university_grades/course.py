# Course: име, списък от студенти; метод average_grade()
from student import Student

class Course:
    def __init__(self, name:str):
        self.name = name
        self.list_of_students: list[Student] = []

    def add_student(self, current_student):
        self.list_of_students.append(current_student)

    def average_grade(self):
        av_grade = 0
        for current_student in self.list_of_students:
            av_grade += sum(current_student.get_grades()[self.name]) / len(current_student.get_grades()[self.name])

        return av_grade / len(self.list_of_students)

    def best_student(self):
        return list(sorted(self.list_of_students, key=lambda current_student: -current_student.average()))[0]


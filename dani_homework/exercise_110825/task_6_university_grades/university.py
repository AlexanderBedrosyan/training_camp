# University: списък от курсове, метод best_student()
from course import Course


class University:
    def __init__(self):
        self.list_of_courses: list[Course] = []

    def add_course(self, courrent_course):
        self.list_of_courses.append(courrent_course)

    def best_student(self):
        best_st = None
        best_gr = 0
        for courrent_course in self.list_of_courses:
            for student in courrent_course.list_of_student:
                if student.average() >= best_gr:
                    best_st = student
                    best_gr = student.average()
        return best_st


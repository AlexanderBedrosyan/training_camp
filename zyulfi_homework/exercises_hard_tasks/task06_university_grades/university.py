# University: списък от курсове, метод best_student()
from course import Course


class University:
    def __init__(self):
        self.list_of_courses: list[Course] = []

    def add_course(self, curr_course=object):
        self.list_of_courses.append(curr_course)

    def best_student(self) -> object:
        top_student = None
        top_grade = 0
        for curr_course in self.list_of_courses:
            for curr_student in curr_course.list_of_student:
                if curr_student.average() >= top_grade:
                    top_grade = curr_student.average()
                    top_student = curr_student
        return top_student


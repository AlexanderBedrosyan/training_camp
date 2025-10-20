# Атрибути: private __courses
# Методи:
# add_course(course)
# best_student()
from exercises_hard_task3.course_management.course import Course


class University:
    def __init__(self):
        self.__courses: list[Course] = []

    def add_course(self, curr_course):
        self.__courses.append(curr_course)

    def best_student(self):
        best_student = None
        best_grade = 0
        for curr_course in self.__courses:
            best_student_of_curr_course = curr_course.curse_best_student()
            if best_student_of_curr_course.average() >= best_grade:
                best_grade = best_student_of_curr_course.average()
                best_student = best_student_of_curr_course.name
        return best_student
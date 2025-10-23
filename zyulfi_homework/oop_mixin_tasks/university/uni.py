# Атрибути: private __courses
# Методи: add_course(), best_overall()
from oop_mixin_tasks.university.course import Course


class Uni:
    def __init__(self):
        self.__courses: list[Course] = []

    def add_course(self, curr_course) -> None:
        self.__courses.append(curr_course)

    def best_overall(self):
        best_overall_student = None
        best_overall_average = 0

        for curr_course in self.__courses:
            if curr_course.best_student_of_course().average() >= best_overall_average:
                best_overall_average = curr_course.best_student_of_course().average()
                best_overall_student = curr_course.best_student_of_course()
        return best_overall_student


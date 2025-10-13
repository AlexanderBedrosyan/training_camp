# GradeBook Атрибути: списък от курсове
# Методи: best_student(), top_course()
from course import Course


class GradeBook:
    def __init__(self):
        self.courses: list[Course] = []

    def add_courses(self, curr_c):
        self.courses.append(curr_c)

    def best_student(self):
        best_student = None
        best_st_gr = 0
        for curr_c in self.courses:
            cbs = curr_c.best_student_course()
            if cbs is None:
                continue
            if best_st_gr <= cbs.average():
                best_st_gr = cbs.average()
                best_student = cbs.name

        return best_student

    def top_course(self):
        top_course = None
        top_course_av = 0

        for curr_c in self.courses:
            if top_course_av <= curr_c.course_average():
                top_course_av = curr_c.course_average()
                top_course = curr_c

        return top_course.title

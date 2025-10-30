# University: списък от курсове; метод best_student()
from dictionaries.hard_tasks2.university_grades.course import Course


class University:
    def __init__(self):
        self.list_of_course: list[Course] = []

    def add_course(self, curr_course):
        self.list_of_course.append(curr_course)

    def best_student(self):
        return list(sorted(self.list_of_course, key=lambda curr_course: -curr_course.best_student().average()))[0].best_student()
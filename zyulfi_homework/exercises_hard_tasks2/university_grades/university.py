# University: списък от курсове; метод best_student()
from exercises_hard_tasks2.university_grades.course import Course


class University:
    def __init__(self):
        self.list_or_courses: list[Course] = []

    def add_course(self, curr_course=object) -> None:
        self.list_or_courses.append(curr_course)

    def best_student(self):
        best_stud = None
        best_grade = 0

        for curr_course in self.list_or_courses:
            if curr_course.best_student_of_course().average() >= best_grade:
                best_grade = curr_course.best_student_of_course().average()
                best_stud = curr_course.best_student_of_course()
        return best_stud
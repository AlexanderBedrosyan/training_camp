# University
# Атрибути: private __courses
# Методи: add_course(course) # best_student()
from course import Course
from student import Student

class University:
    def __init__(self):
        self.__courses: list[Course] = []

    def add_course(self, course:Course):
        if course:
            self.__courses.append(course)
        #return self.__courses

    def best_student(self):
        best_st = None
        best_avg = 0

        for course in self.__courses:
            for student in course.get_students():
                avg = student.average()
                if avg > best_avg:
                    best_st = student
                    best_avg = avg
            return best_st



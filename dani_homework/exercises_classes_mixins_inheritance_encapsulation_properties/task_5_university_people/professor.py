# Professor: private __courses, метод list_courses()
from person import Person

class Professor(Person):
    def __init__(self, name, age, courses=None):
        super().__init__(name, age)

        if courses is None:
            self.__courses =[]
        else:
            self.__courses = courses

    def add_course(self, course):
        self.__courses.append(course)

    def list_courses(self):
        return self.__courses

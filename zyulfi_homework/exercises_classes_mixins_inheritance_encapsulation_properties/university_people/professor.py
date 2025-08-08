# Professor: private __courses, метод list_courses()
from person import Person


class Professor(Person):
    def __init__(self, name=str, age=int):
        super().__init__(name, age)
        self.__courses = []

    def add_course(self, current_curse):
        self.__courses.append(current_curse)

    def list_courses(self):
        return self.__courses
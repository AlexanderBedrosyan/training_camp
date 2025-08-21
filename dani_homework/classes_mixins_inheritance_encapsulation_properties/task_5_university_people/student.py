# Student: private __grades, метод average()

from person import Person

class Student(Person):
    def __init__(self, name, age, grades=None):
        super().__init__(name, age)
        if grades is None:
            self.__grades = []
        else:
            self.__grades = grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)
# Student: private __grades, метод average()
from person import Person

class Student(Person):
    def __init__(self, name=str, age=int):
        super().__init__(name, age)
        self.__grades = []

    def add_grade(self, current_grade=int):
        self._Student__grades.append(current_grade)

    def average(self):
        return sum(self._Student__grades) / len(self._Student__grades)
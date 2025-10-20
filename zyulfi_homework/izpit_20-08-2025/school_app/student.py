# Student: наследява Person.
# Student: private атрибут __grade
#Добави property grade в Student, което да позволява само числа 2.0–6.0.

from person import Person
from mixins import InfoMixin

class Student(Person, InfoMixin):
    def __init__(self, name, grade):
        super().__init__(name)
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value > 6:
            raise ValueError("Grade cannot be out of 2-6 range")
        elif value < 2:
            raise ValueError("Grade cannot be out of 2-6 range")
        else:
            self.__grade = value

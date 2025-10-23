#Teacher: наследява Person
# Teacher: private атрибут __subject

# Добави property subject в Teacher, което не приема None.
# o	Ако подадения стринг на teacher e None, то програмата трябва да връща:
# „Teacher cannot be None”
# o	Ако не е None, то да закача атрибута.

from person import Person
from mixins import InfoMixin

class Teacher(Person, InfoMixin):
    def __init__(self, name, subject):
        super().__init__(name)
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if value is None:
            raise ValueError ("Teacher cannot be None")
        else:
            self.__subject = value




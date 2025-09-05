from person import Person
from mixins import InfoMixin

class Student(Person, InfoMixin):
    def __init__(self, name: str, grade: float)-> None:
        super().__init__(name)
        self._grade: float = grade

    def get_info(self)-> None:
        return f"Student: {self._name}, grade: {self._grade}"

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 2.0 < value < 6.0:
            raise ValueError("Grade cannot be out of 2-6 range")
        self._grade = value


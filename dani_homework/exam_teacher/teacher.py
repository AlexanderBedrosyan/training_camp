from person import Person
from mixins import InfoMixin

class Teacher(Person, InfoMixin):
    def __init__(self, name: str, subject: str )-> None:
        super().__init__(name)
        self._subject: str = subject

    def get_info(self)-> None:
        return f"Teacher: {self._name}, subject: {self._subject}"


    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if value is None:
            raise ValueError("Teacher cannot be None")
        self._subject = value


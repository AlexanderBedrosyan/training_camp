
from base import Person
from bio import  BioMixin


class Student(Person, BioMixin):
    pass
student = Student("Maria", 20)
print(student.bio())  # Maria, age 20

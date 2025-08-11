# Създай Student(Person, BioMixin)
#
# Примерен вход:
#
from base import Person
from bio import BioMixin

class Student(Person, BioMixin):
    pass

s = Student("Maria", 20)
print(s.bio())  # Maria, age 20
# Teacher (Person)
# Атрибути: subject, salary
# Метод: give_grade(student, grade)
from person import Person


class Teacher(Person):
    def __init__(self, name:str, age:int, subject:str, salary:float):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def give_grade(self, student:object, grade:float):
        student.list_of_grades.append(grade)





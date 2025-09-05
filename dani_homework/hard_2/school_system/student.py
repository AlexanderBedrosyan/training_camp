#Student (наследява Person): private __grades;
# методи add_grade(), average()
from person import Person


class Student(Person):
    def __init__(self, name:str, age:int):
        super().__init__(name, age)
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def average(self):
        if len(self.__grades)== 0:
            return 0

        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"{self.name} is {self.age} years old, average is {self.average()}"

#test
s1=Student("Anna", 18)
print(s1)
s2=Student("Boris", 19)
print(s2)

s1.add_grade(4.00)
s1.add_grade(5.00)
print(s1.average())

s2.add_grade(5.00)
s2.add_grade(6.00)
print(s2.average())
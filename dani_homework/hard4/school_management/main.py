from hard4.school_management.classroom import Classroom
from hard4.school_management.person import Person
from teacher import Teacher
from student import Student

p1 = Person("Ivan", 25)
print(p1)

s1 = Student("Petko",23)
print(s1)
s2 = Student("Mito",22)
print(s2)

t1 = Teacher("Penchev", 45, "Math", 2500)
t1.give_grade(s1, 5.5)
t1.give_grade(s2, 3.5)

print(s1.list_of_grades)
print(s2.list_of_grades)

c1 = Classroom("Ivanov")
c1.add_student(s1)
c1.add_student(s2)
print(c1.average_grade())
print(c1.best_student())

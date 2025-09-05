from student import Student
from course import Course
from university import University

s1 = Student("Ivan")
s1.add_grade("Math", 6)
s1.add_grade("CS", 5)

s2 = Student("Maria")
s2.add_grade("Math", 4)
s2.add_grade("CS", 5)

c = Course("Informatics")
c.add_student(s1)
c.add_student(s2)

u = University("SU")
u.add_course(c)

print(c.best_student().name)      # Ivan
print(u.average_university())     # 5.0
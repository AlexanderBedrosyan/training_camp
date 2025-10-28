from student import Student
from course import Course
from university import University

s1 = Student("Ivan")
s1.add_grade("Math", 5)
s1.add_grade("Math", 6)

c = Course("Math")
c.add_student(s1)

u = University()
u.add_course(c)

print(s1.average())      # 5.5
print(u.best_student())  # Ivan
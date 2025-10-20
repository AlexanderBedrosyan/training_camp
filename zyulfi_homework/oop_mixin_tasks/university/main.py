from student import Student
from course import Course
from uni import Uni

s1 = Student("Mila")
s1.add_grade(5); s1.add_grade(6)
s2 = Student("Ivan")
s2.add_grade(4); s2.add_grade(5)

c = Course("Math")
c.add_student(s1); c.add_student(s2)

u = Uni()
u.add_course(c)

print(c.course_average())  # 5.0
print(u.best_overall().name)  # Mila
#from student import Student
from teacher import Teacher
from student import Student

s1 = Student("Anna", 18)
s1.add_grade(5)
s1.add_grade(6)

s2 = Student("Boris", 19)
s2.add_grade(4)
s2.add_grade(5)

t = Teacher("Mr. Ivanov", 51, "Math")
t.add_student(s1); t.add_student(s2)

print(s1.average())          # 5.5
print(t.class_average())     # 5.0
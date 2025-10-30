from student import Student
from course import Course
from university import University

s1 = Student("Anna");
s1.add_grade("Math", 5);
s1.add_grade("Physics", 6)

s2 = Student("Boris");
s2.add_grade("Math", 4);
s2.add_grade("Physics", 5)

math = Course("Math");
math.add_student(s1);
math.add_student(s2)

p = Course("Physics")
p.add_student(s1)
p.add_student(s2)

uni = University();
uni.add_course(math)

print(s1.average())        # 5.5
print(math.average_grade())# 4.5

print(p.average_grade())    # 5.5
print(uni.best_student().name) # Anna
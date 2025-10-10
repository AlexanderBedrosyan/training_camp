class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented


# Примерно използване:
s1 = Student("Ivan", 5.5)
s2 = Student("Maria", 6.0)

print(s1 < s2)   # True
print(s1 == s2)  # False

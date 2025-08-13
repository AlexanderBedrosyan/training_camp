# Създай клас Student с:
# обикновен атрибут name
# private атрибут __grades (списък)
# метод add_grade(grade)
# @property за average, който връща средната стойност
# Примерен вход:
# s = Student("Toni")
# s.add_grade(5)
# s.add_grade(6)
# print(s.average)  # 5.5
#_________________________________________________________-

class Student:
    def __init__(self, name = str):
        self.name = name                  # обикновен атрибут
        self.__grades = []               # private атрибут (списък)

    def add_grade(self, grade = float) -> None:
        """Добавя оценка към списъка с оценки."""
        self.__grades.append(grade)

    @property
    def average(self) -> float:
        """Връща средната оценка или 0.0, ако няма оценки."""
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

# Употреба
s = Student("Toni")
s.add_grade(5)
s.add_grade(6)
print(s.average)  # 5.5


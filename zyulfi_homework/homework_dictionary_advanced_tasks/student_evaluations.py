# Задача 2: Оценки на студенти
# Изисквания:
# Изчисли средната оценка на всеки студент.
# Създай речник само с отличниците (среден успех ≥ 5.50).
# Подреди резултатите по успех (низходящо).

class Students:
    def __init__(self, curr_dict):
        self.curr_dict_grades = curr_dict

    def average_grade(self):
        dict_average_grade ={}
        for key_student, value_grades in self.curr_dict_grades.items():
            average_gr = round(sum(value_grades) / len(value_grades), 2)
            dict_average_grade[key_student] = average_gr

        return dict_average_grade

    def best_students(self):
        best_students_dict = {}
        for key_student, value_grade in self.average_grade().items():
            if value_grade >= 5.50:
                best_students_dict[key_student] = value_grade
        return best_students_dict

        # return dict([(student, grade) for student, grade in self.average_grade().items() if grade >= 5.50])

    def sorted_descending(self):
        return dict(sorted(self.average_grade().items(), key=lambda item: -item[1]))

grades = {
    "Anna": [5, 6, 6],
    "Boris": [4, 5],
    "Ivan": [6, 6, 6],
    "Maria": [3, 4, 5]
}

s = Students(grades)
# print(s.curr_dict_grades)
print(s.average_grade())
print(s.best_students())
print(s.sorted_descending())
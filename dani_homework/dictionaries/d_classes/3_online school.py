# Задача 3: Онлайн училище
# Създай клас School, който управлява ученици и техните оценки.
#
# Условия:
# Речник {ученик: [оценки]}.
# Метод add_grade(student, grade) добавя оценка.
# Метод best_student() връща ученика с най-висок среден успех.
# Метод class_average() връща средния успех на целия клас.
class School:
    def __init__(self):
        self.st_dict = {}

    def add_grade(self, student, grade):
        if student not in self.st_dict:
            self.st_dict[student] = []
        self.st_dict[student].append(grade)

    def best_student(self):
        return sorted(self.st_dict.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)[0][0]

    def class_average(self):
        avg_grade = 0
        count = 0
        for grade in self.st_dict.values():
            avg_grade += sum(grade)
            count += len(grade)

        return avg_grade / count

# Тест:
s = School()
s.add_grade("Anna", 6)
s.add_grade("Anna", 5)
s.add_grade("Boris", 6)
s.add_grade("Boris", 6)
print(s.st_dict)
print(s.best_student())  # Anna
print(round(s.class_average(), 2))  # 5.0
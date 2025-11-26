# Задача 3: Онлайн училище
# Създай клас School, който управлява ученици и техните оценки.
# Условия:
# Речник {ученик: [оценки]}.
# Метод add_grade(student, grade) добавя оценка.
# Метод best_student() връща ученика с най-висок среден успех.
# Метод class_average() връща средния успех на целия клас.

class School:
    def __init__(self):
        self.student_dict = {}

    def add_grade(self, student, grade):
        if student not in self.student_dict:
            self.student_dict[student] = []
        self.student_dict[student].append(grade)

    def best_student(self):
        return sorted(self.student_dict.items(), key=lambda x: -sum(x[1])/len(x[1]))[0][0]

        print(self.student_dict)





# Тест:
s = School()
s.add_grade("Anna", 6)
s.add_grade("Anna", 5)
s.add_grade("Boris", 4)
print(s.best_student())  # Anna
# print(round(s.class_average(), 2))  # 5.0
# Задача 2: Среден успех и отличник
# Условие:
# Функция class_statistics(grades) приема речник име -> [оценки]. Трябва да върне:
# речник (име -> среден успех, закръглен до 2),
# името на ученика с най-висок среден успех,
# среден успех на класа.
# {'averages': {'Иван': 5.67, 'Мария': 5.67, 'Петър': 4.33}, 'top_student': 'Иван' (или 'Мария'),

def class_statistics(grades):
    new_dict = {}
    new_dict["averages"] = {}
    new_dict["top_student"] = ""
    new_dict["class_avg"] = ""

    for key, values in grades.items():
        aver_grade = round(sum(values) / len(values), 2)
        new_dict["averages"][key] = aver_grade

    top_st = sorted(new_dict["averages"].items(), key=lambda item: item[1])[-1][0]
    new_dict["top_student"] = top_st

    cl_av = round(sum(new_dict["averages"].values()) / len(new_dict["averages"]), 2)

    new_dict["class_avg"] = cl_av

    return new_dict



grades = {"Иван": [5,6,6], "Мария": [6,6,5], "Петър": [4,5,4]}
print(class_statistics(grades))
# Очакван изход:
# {'averages': {'Иван': 5.67, 'Мария': 5.67, 'Петър': 4.33}, 'top_student': 'Иван' (или 'Мария'),
# 'class_avg': 5.22}



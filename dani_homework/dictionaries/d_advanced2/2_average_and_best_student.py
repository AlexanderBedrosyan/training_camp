# Задача 2: Среден успех и отличник
# Условие: Функция class_statistics(grades) приема речник име -> [оценки].
# Трябва да върне: речник с (име -> среден успех, закръглен до 2),
# името на ученика с най-висок среден успех, среден успех на класа.
# Примерен тест:
# def class_statistics(grades):
# avgs = {n: round(sum(s)/len(s), 2) for n, s in grades.items()}
# top = max(avgs, key=avgs.get)
# class_avg = round(sum(avgs.values())/len(avgs),
# return {"averages": avgs, "top_student": top, "class_avg": class_avg}
from pprint import pprint

def class_statistics(grades):
    avg_grades = {name: round(sum(grades) / len(grades), 2) for name, grades in grades.items()}
    avg_class = {name: round(sum(grades)/len(grades), 2) for name, grades in grades.items()}
    top_student = max(avg_class, key=avg_class.get)
    result = {
      "avg_grades": avg_grades,
      "top_student": top_student,
      "avg_class": avg_class
  }
    return result

grades = {"Иван": [5,6,6], "Мария": [6,6,5], "Петър": [4,5,4]}
pprint(class_statistics(grades))

# Очакван изход:{'averages': {'Иван': 5.67, 'Мария': 5.67, 'Петър': 4.33}, 'top_student': 'Иван' (или 'Мария'), 'class_avg': 5.22}
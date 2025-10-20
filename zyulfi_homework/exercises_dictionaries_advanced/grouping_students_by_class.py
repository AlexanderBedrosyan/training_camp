# Задача 13: Групиране на ученици по клас
# Условие:
# group_by_class(data) приема списък от tuples (име, клас) и връща речник клас -> [име].

def group_by_class(students):
    class_dict = {}

    for element in students:
        name = element[0]
        curr_class = element[1]
        if curr_class not in class_dict:
            class_dict[curr_class] = list()
        class_dict[curr_class].append(name)

    return class_dict

students = [("Иван",10),("Мария",11),("Петър",10)]
print(group_by_class(students))

# Очакван изход:
# {10: ['Иван','Петър'], 11: ['Мария']}
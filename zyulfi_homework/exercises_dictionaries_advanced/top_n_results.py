# Задача 10: Топ N резултати
# Условие:
# top_n_scores(scores, n) приема речник име -> точки и връща списък от n топ елемента като
# (име, точки) сортирани низходящо.

def top_n_scores(curr_dict, n):
    return list(sorted(curr_dict.items(), key=lambda item: -item[1]))[0:n]
    # return [(name, point) for name, point in dict(sorted(curr_dict.items(), key=lambda item: -item[1])).items()][0:n]


scores = {"Иван":85,"Мария":92,"Петър":78}
print(top_n_scores(scores, 2))


# Очакван изход:
# [('Мария', 92), ('Иван', 85)]

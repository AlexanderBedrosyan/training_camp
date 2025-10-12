# Задача 15: Комбиниране на списъци в речник и средна стойност
# Условие:
# combine_to_dict(names, values) прави {name: value} и връща речника + средната стойност на values (round 2).


def combine_to_dict(names, values):
    # new_dict = dict(zip(names, values))
    # return [new_dict, sum(new_dict.values()) / len(new_dict)]
    if len(names) != len(values):
        return "Wrong"

    curr_dict = {}
    for i in range(len(names)):
        curr_dict[names[i]] = values[i]
    return curr_dict, sum(curr_dict.values()) / len(curr_dict)

students = ["Иван","Мария","Петър"]
scores = [85,92,78]
print(combine_to_dict(students, scores))
# Очакван изход:
# ({'Иван':85,'Мария':92,'Петър':78}, 85.0)
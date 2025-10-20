# Условие:
# vote_count(votes) приема списък от имена и връща речник {име: брой} и победителя (най-много гласове).
# При равенство върни някой от лидерите.

votes = ["Иван","Мария","Иван","Петър","Мария","Иван"]

def vote_count(votes):
    new_dict = {}

    for name in votes:
        if name not in new_dict:
            new_dict[name] = 0
        new_dict[name] += 1

    best_name = sorted(new_dict.items(), key=lambda item: -item[1])[0][0]

    return f"({new_dict}, {best_name})"



print(vote_count(votes))


# Очакван изход:
# ({'Иван': 3, 'Мария': 2, 'Петър': 1}, 'Иван')

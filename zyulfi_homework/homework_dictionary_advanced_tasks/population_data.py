#  Задача 7: Данни за население

# countries = {
#     "Bulgaria": {"population": 6.8, "area": 110.9},
#     "Germany": {"population": 83.2, "area": 357.6},
#     "Italy": {"population": 59.0, "area": 301.3}
# }

# Изисквания:
# Изчисли гъстотата на населението (population / area).
# Намери страната с най-голяма гъстота.
# Изведи сортиран списък по гъстота.

class Countries:
    def __init__(self, curr_countries):
        self.curr_countries = curr_countries

    def population_density(self):
        density_dict = {}
        for country, area in self.curr_countries.items():
            density_dict[country] = round((list(area.values())[0] / list(area.values())[1]), 2)
        return density_dict

    def sorted_density(self):
        return dict(sorted(self.population_density().items(), key=lambda item: item[1]))

    def most_populated_country(self):
        return list(self.sorted_density())[-1]


countries = {
    "Bulgaria": {"population": 6.8, "area": 110.9},
    "Germany": {"population": 83.2, "area": 357.6},
    "Italy": {"population": 59.0, "area": 301.3}
}

country1 = Countries(countries)
print(country1.population_density())
print(country1.sorted_density())
print(country1.most_populated_country())
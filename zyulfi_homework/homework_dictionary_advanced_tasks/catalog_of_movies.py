#  Задача 8: Каталог на филми

# movies = {
#     "Inception": {"rating": 8.8, "year": 2010},
#     "Interstellar": {"rating": 8.6, "year": 2014},
#     "Memento": {"rating": 8.4, "year": 2000},
#     "Tenet": {"rating": 7.5, "year": 2020}
# }

# Изисквания:
# Изведи филмите, подредени по рейтинг.
# Покажи само тези след 2010 г.
# Изчисли средния рейтинг на всички филми.

class Movies:
    def __init__(self, movies):
        self.movies = movies

    def rating_movie(self):
        return dict(sorted(self.movies.items(), key=lambda item: -item[1]["rating"]))

    def movies_after_2010(self):
        new_dict = {}
        for movie, rating in self.movies.items():
            if rating["year"] > 2010:
                new_dict[movie] = rating
        return new_dict

    def average_rating(self):
        average = 0
        for movie, rating in self.movies.items():
            average += list(rating.values())[0]

        return round(average / len(self.movies),2)


movies = {
    "Inception": {"rating": 6.8, "year": 2010},
    "Interstellar": {"rating": 8.6, "year": 2014},
    "Memento": {"rating": 4.4, "year": 2000},
    "Tenet": {"rating": 7.5, "year": 2020}
}

movies1 = Movies(movies)
print(movies1.rating_movie())
print(movies1.movies_after_2010())
print(movies1.average_rating())

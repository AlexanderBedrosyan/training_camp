# System
# Атрибути: private __movies
# Методи: add_movie(), top_movie()
from oop_mixin_tasks.movie_ratings.movie import Movie


class System:
    def __init__(self):
        self.__movies: list[Movie] = []

    def add_movie(self, curr_movie):
        self.__movies.append(curr_movie)

    def top_movie(self):
        best_movie = None
        best_average = 0

        for curr_movie in self.__movies:
            if curr_movie.average_rating() >= best_average:
                best_average = curr_movie.average_rating()
                best_movie = curr_movie
        return best_movie
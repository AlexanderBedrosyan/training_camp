# Атрибути: private __movies
# Методи:
# add_movie(movie) → добавя филм
# top_rated() → филмът с най-висока средна оценка
# lowest_rated() → филмът с най-ниска средна оценка
import sys
from movie import Movie

class RatingSystem:
    def __init__(self):
        self.__movies: list[Movie] = []

    def add_movie(self, movie=object):
        self.__movies.append(movie)

    def top_rated(self) -> object:
        top_movie = None
        top_rating = 0
        for curr_movie in self.__movies:
            if top_rating <= curr_movie.average_rating():
                top_rating = curr_movie.average_rating()
                top_movie = curr_movie
        return top_movie

    def lowest_rated(self) -> object:
        low_movie = None
        low_rating = sys.maxsize
        for curr_movie in self.__movies:
            if curr_movie.average_rating() <= low_rating:
                low_rating = curr_movie.average_rating()
                low_movie = curr_movie
        return low_movie



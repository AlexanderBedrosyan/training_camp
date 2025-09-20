# RatingSystem: държи списък от филми, метод top_rated_movie()
from movie import Movie


class RatingSystem:
    def __init__(self):
        self.list_of_movie: list[Movie] = []

    def add_movie(self, curr_movie):
        self.list_of_movie.append(curr_movie)

    def top_rated_movie(self):
        best_rating = 0
        best_movie = None
        for curr_movie in self.list_of_movie:
            if curr_movie.average_rating() >= best_rating:
                best_rating = curr_movie.average_rating()
                best_movie = curr_movie

        return best_movie



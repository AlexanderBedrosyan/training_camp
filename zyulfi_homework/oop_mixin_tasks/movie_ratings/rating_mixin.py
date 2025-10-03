# RatingMixin
# Метод: rate(movie, rating)
from movie import Movie

class RatingMixin:
    def rate(self, movie=Movie, rating=float or int):
        if 0 < rating <= 10:
            movie.add_rating(rating)
        else:
            print("Error")
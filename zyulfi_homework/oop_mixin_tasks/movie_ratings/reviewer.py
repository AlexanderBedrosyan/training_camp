# Reviewer (RatingMixin)
# Атрибути: name
from oop_mixin_tasks.movie_ratings.rating_mixin import RatingMixin
from movie import Movie


class Reviewer(RatingMixin):
    def __init__(self, name):
        self.name = name

    def rate_move(self, curr_movie=Movie, rate=int):
        curr_movie.add_rating(RatingMixin(rate))






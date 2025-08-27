# Атрибути: name
# Методи:
# rate_movie(movie, rating) → добавя оценка към филм
from movie import Movie

class Reviewer:
    def __init__(self, name=str):
        self.name = name

    def rate_movie(self, movie, rating) -> None:
        movie.add_rating(rating)

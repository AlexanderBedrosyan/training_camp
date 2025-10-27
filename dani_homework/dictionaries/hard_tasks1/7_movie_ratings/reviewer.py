# Reviewer: име, метод rate_movie(movie, rating)

class Reviewer:
    def __init__(self, name):
       self.name = name

    def rate_movie(self, movie, rating):
        movie.add_rating(rating)
# Reviewer: име, метод rate_movie(movie, rating)

class Reviewer:
    def __init__(self, name_reviewer):
        self.name_reviewer = name_reviewer

    def rate_movie(self, movie=object, rating=int):
        movie.add_rating(rating)






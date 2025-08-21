# RatingSystem: държи списък от филми, метод top_rated_movie()

class RatingSystem:
    def __init__(self):
        self.list_of_moves = []


    def add_movie(self, movie):
        self.list_of_moves.append(movie)

    def top_rated_movie(self):
        if not self.list_of_moves:
           return None

        top_movie = self.list_of_moves [0]
        for movie in self.list_of_moves[1:]:
            top_movie = movie
        return top_movie
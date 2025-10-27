# Cinema
# Атрибути: private __movies
# Методи: add_movie(movie) # available_movies()
from movie import Movie


class Cinema:
    def __init__(self):
        self.__movies: list[Movie] = []

    def add_movie(self, current_movie: Movie) -> None:
        self.__movies.append(current_movie)

    def available_movies(self) -> list[Movie]:
        return self.__movies

#test
m2=Movie("KKK", 8)
m3=Movie("ppppp", 5)

c=Cinema()
c.add_movie(m2)
c.add_movie(m3)

for movie in c.available_movies():
    print(f'{movie.title}, ({movie.get_seats()} seats)')



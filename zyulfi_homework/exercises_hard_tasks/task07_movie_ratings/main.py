from movie import Movie
from reviewer import Reviewer
from rating_system import RatingSystem

m1 = Movie("Inception")
m2 = Movie("The Matrix")

r1 = Reviewer("John")
r2 = Reviewer("Emma")

r1.rate_movie(m1, 9)
r2.rate_movie(m1, 8)
r1.rate_movie(m2, 10)
r2.rate_movie(m2, 9)

print(m1._Movie__ratings)
print(m2._Movie__ratings)


system = RatingSystem()
system.add_movie(m1)
system.add_movie(m2)

print("Top rated movie:", system.top_rated_movie().name)

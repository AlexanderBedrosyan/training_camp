from movie import Movie
from reviewer import Reviewer
from system import System

m1 = Movie("Inception")
m2 = Movie("Matrix")

s = System()
s.add_movie(m1); s.add_movie(m2)

r = Reviewer("Anna")
r.rate(m1, 9)
r.rate(m2, 7)

r2 = Reviewer("Gugov")
r2.rate(m1, 10)
r2.rate(m2, 5)


print(m1.average_rating())  # 9.0
print(s.top_movie().title)  # Inception
print(m2.average_rating())


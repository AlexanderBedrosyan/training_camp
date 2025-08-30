from movie import Movie
from reviewer import Reviewer
from system import RatingSystem

m1 = Movie("Inception")
m2 = Movie("Titanic")


r = Reviewer("Ivan")
r.rate_movie(m1, 9)
r.rate_movie(m2, 7)

r2 = Reviewer("Gugov")
r2.rate_movie(m1, 5)
r2.rate_movie(m2, 4)

system = RatingSystem()
system.add_movie(m1)
system.add_movie(m2)

print(system.top_rated().title)    # Inception
print(system.lowest_rated().title) # Titanic
print(str(m1))
print(str(m2))

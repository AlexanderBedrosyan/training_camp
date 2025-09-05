from movie import Movie
from customer import Customer
from cinema import Cinema

m1 = Movie("Matrix", 2)
c = Customer("Ivan")

cin = Cinema()
cin.add_movie(m1)

c.book_movie(m1)
c.book_movie(m1)
c.book_movie(m1)  # няма места

print(cin.available_movies())  # []
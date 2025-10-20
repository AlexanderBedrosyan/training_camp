from trip import Trip
from customer import Customer
from agency import Agency

t1 = Trip("Paris", 1200)
t2 = Trip("Rome", 900)

a = Agency()
a.add_trip(t1); a.add_trip(t2)

c = Customer("Nikolay")
c.book_trip(t1)
print([trip.destination for trip in c.list_trips()])  # ['Paris']
c.cancel_trip(t1)
print(t1.is_booked())  # False
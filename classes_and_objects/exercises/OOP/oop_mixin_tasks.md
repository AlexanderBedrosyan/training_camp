# 🏆 10 ООП Задачи с Mixin-и, наследяване и тестове

---

## 📌 Задача 1: Library System

**Структура:**
library_system/
├── book.py
├── member.py
├── borrow_mixin.py
├── library.py
└── main.py

markdown
Always show details

Copy code

**Описание:**

- **Book**
  - Атрибути: `title`, `author`, private `__available=True`
  - Методи: `is_available()`, `set_unavailable()`, `set_available()`

- **BorrowMixin**
  - Методи: `borrow(book)`, `return_book(book)`

- **Member (BorrowMixin)**
  - Атрибути: `name`, private `__borrowed_books`
  - Методи: `list_books()`

- **Library**
  - Атрибути: private `__books`
  - Методи: `add_book()`, `available_books()`, `find_book(title)`

**main.py**
```python
from book import Book
from member import Member
from library import Library

b1 = Book("1984", "George Orwell")
b2 = Book("Dune", "Frank Herbert")

lib = Library()
lib.add_book(b1); lib.add_book(b2)

m = Member("Ivan")
m.borrow(b1)
print([book.title for book in m.list_books()])  # ['1984']
print([book.title for book in lib.available_books()])  # ['Dune']
m.return_book(b1)
print(b1.is_available())  # True
```

## 📌 Задача 2: Online Shop
Структура:

online_shop/
├── product.py
├── cart.py
├── discount_mixin.py
├── user.py
└── main.py
Описание:

Product

Атрибути: name, price

DiscountMixin

Метод: apply_discount(price, percent)

Cart (DiscountMixin)

Атрибути: private __items

Методи: add_product(product), total(), discounted_total(percent)

User

Атрибути: username, private __cart

Методи: get_cart()

main.py

```python
from product import Product
from user import User

p1 = Product("Phone", 800)
p2 = Product("Laptop", 1500)

u = User("Maria")
cart = u.get_cart()
cart.add_product(p1)
cart.add_product(p2)

print(cart.total())  # 2300
print(cart.discounted_total(10))  # 2070.0
```

## 📌 Задача 3: Travel Agency
# Структура:

travel_agency/
├── trip.py
├── customer.py
├── cancel_mixin.py
├── agency.py
└── main.py

Описание:

Trip

Атрибути: destination, price, private __booked=False

Методи: book(), cancel(), is_booked()

CancelMixin

Метод: cancel_trip(trip)

Customer (CancelMixin)

Атрибути: name, private __trips

Методи: book_trip(trip), list_trips()

Agency

Атрибути: private __trips

Методи: add_trip(), available_trips(), find_trip(destination)

main.py

```python
Always show details

Copy code
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
```

## 📌 Задача 4: Fitness App
# Структура:

fitness_app/
├── activity.py
├── tracker.py
├── calorie_mixin.py
├── user.py
└── main.py
Описание:

Activity

Атрибути: name, duration, calories_per_min

Метод: total_calories()

CalorieMixin

Метод: compare_calories(a1, a2)

Tracker (CalorieMixin)

Атрибути: private __activities

Методи: add_activity(), total_burned()

User

Атрибути: username, private __tracker

Метод: get_tracker()

main.py

```python
from activity import Activity
from user import User

a1 = Activity("Running", 30, 10)
a2 = Activity("Cycling", 40, 8)

u = User("Stefan")
tracker = u.get_tracker()
tracker.add_activity(a1)
tracker.add_activity(a2)

print(tracker.total_burned())  # 30*10 + 40*8 = 620
```

## 📌 Задача 5: Banking App
# Структура:

banking_app/
├── account.py
├── transaction_mixin.py
├── customer.py
├── bank.py
└── main.py
Описание:

Account

Атрибути: iban, private __balance=0

Методи: deposit(amount), withdraw(amount), get_balance()

TransactionMixin

Метод: transfer(from_acc, to_acc, amount)

Customer (TransactionMixin)

Атрибути: name, private __accounts

Методи: add_account(), total_balance()

Bank

Атрибути: private __customers

Методи: add_customer(), find_customer(name)

main.py

```python
Always show details

Copy code
from account import Account
from customer import Customer
from bank import Bank

a1 = Account("BG001")
a2 = Account("BG002")

c = Customer("Georgi")
c.add_account(a1)
c.add_account(a2)

a1.deposit(1000)
c.transfer(a1, a2, 400)

print(a1.get_balance())  # 600
print(a2.get_balance())  # 400
```

## 📌 Задача 6: Movie Ratings
# Структура:

movie_ratings/
├── movie.py
├── reviewer.py
├── rating_mixin.py
├── system.py
└── main.py

Описание:

Movie

Атрибути: title, private __ratings

Методи: add_rating(), average_rating()

RatingMixin

Метод: rate(movie, rating)

Reviewer (RatingMixin)

Атрибути: name

System

Атрибути: private __movies

Методи: add_movie(), top_movie()

main.py

```python
Always show details

Copy code
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

print(m1.average_rating())  # 9.0
print(s.top_movie().title)  # Inception
```

## 📌 Задача 7: Transport Network
# Структура:

transport_network/
├── route.py
├── vehicle.py
├── speed_mixin.py
├── network.py
└── main.py
Описание:

Route

Атрибути: start, end, distance

SpeedMixin

Метод: time(distance, speed)

Vehicle (SpeedMixin)

Атрибути: model, private __speed

Методи: travel_time(route)

Network

Атрибути: private __vehicles

Методи: add_vehicle(), fastest_vehicle(route)

main.py

```python
Always show details

Copy code
from route import Route
from vehicle import Vehicle
from network import Network

r = Route("Sofia", "Plovdiv", 150)
v1 = Vehicle("Car", 100)
v2 = Vehicle("Bus", 80)

n = Network()
n.add_vehicle(v1)
n.add_vehicle(v2)

print(v1.travel_time(r))  # 1.5h
print(n.fastest_vehicle(r).model)  # Car
```

## 📌 Задача 8: University
# Структура:

university/
├── student.py
├── course.py
├── grade_mixin.py
├── uni.py
└── main.py
Описание:

Student

Атрибути: name, private __grades

Методи: add_grade(), average()

GradeMixin

Метод: best_student(students)

Course (GradeMixin)

Атрибути: name, private __students

Методи: add_student(), course_average()

Uni

Атрибути: private __courses

Методи: add_course(), best_overall()

main.py

```python
Always show details

Copy code
from student import Student
from course import Course
from uni import Uni

s1 = Student("Mila")
s1.add_grade(5); s1.add_grade(6)
s2 = Student("Ivan")
s2.add_grade(4); s2.add_grade(5)

c = Course("Math")
c.add_student(s1); c.add_student(s2)

u = Uni()
u.add_course(c)

print(c.course_average())  # 5.0
print(u.best_overall().name)  # Mila
```

## 📌 Задача 9: Weather Station
# Структура:

weather_station/
├── reading.py
├── station.py
├── avg_mixin.py
├── network.py
└── main.py
Описание:

Reading

Атрибути: temperature, humidity

AvgMixin

Метод: average(values)

Station (AvgMixin)

Атрибути: private __readings

Методи: add_reading(), avg_temp(), avg_humidity()

Network

Атрибути: private __stations

Методи: add_station(), overall_avg_temp()

main.py

```python
Always show details

Copy code
from reading import Reading
from station import Station
from network import Network

r1 = Reading(20, 60)
r2 = Reading(25, 55)

s = Station()
s.add_reading(r1)
s.add_reading(r2)

n = Network()
n.add_station(s)

print(s.avg_temp())  # 22.5
print(n.overall_avg_temp())  # 22.5
```

## 📌 Задача 10: Space Mission
# Структура:

space_mission/
├── astronaut.py
├── spaceship.py
├── mission_mixin.py
├── mission.py
└── main.py
Описание:

Astronaut

Атрибути: name, private __hours

Методи: add_hours(), get_hours()

MissionMixin

Метод: is_over_capacity(ship, astronauts)

Spaceship

Атрибути: name, capacity

Mission (MissionMixin)

Атрибути: private __astronauts, private __ship

Методи: add_astronaut(), total_hours(), check_capacity()

main.py

```python
from astronaut import Astronaut
from spaceship import Spaceship
from mission import Mission

a1 = Astronaut("Ivan"); a1.add_hours(100)
a2 = Astronaut("Maria"); a2.add_hours(200)

s = Spaceship("Apollo", 2)
m = Mission(s)
m.add_astronaut(a1)
m.add_astronaut(a2)

print(m.total_hours())  # 300
print(m.check_capacity())  # True
```
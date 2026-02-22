# 🧠 Разширени задачи по OOP с математическа логика и колекции от обекти

---

## 🗂️ Задача 1: `sports_league/`

**Структура:**
```
sports_league/
├── team.py
├── player.py
├── league.py
└── main.py
```

**Описание:**
- `Player`: `name`, `position`, private `__goals`, методи `score_goal()`, `get_goals()`
- `Team`: списък от `Player` обекти, методи `add_player()`, `total_goals()`
- `League`: списък от `Team` обекти, метод `top_scorer()` (връща играча с най-много голове в лигата)

**main.py:**
```python
from player import Player
from team import Team
from league import League

p1 = Player("Ivan", "Forward")
p1.score_goal()
p1.score_goal()
t = Team("Tigers")
t.add_player(p1)

league = League()
league.add_team(t)
print(league.top_scorer().name)  # Ivan
```

---

## 🗂️ Задача 2: `geometry_shapes/`

**Структура:**
```
geometry_shapes/
├── shape.py
├── circle.py
├── rectangle.py
├── shape_manager.py
└── main.py
```

**Описание:**
- `Shape`: базов клас с абстрактен метод `area()`
- `Circle` (private `__radius`, property/setter с валидация), метод `area()` = π * r²
- `Rectangle` (protected `_width`, `_height`), метод `area()` = width * height
- `ShapeManager`: държи списък от фигури, метод `total_area()` и `largest_shape()`

**main.py:**
```python
from circle import Circle
from rectangle import Rectangle
from shape_manager import ShapeManager

sm = ShapeManager()
sm.add_shape(Circle(5))
sm.add_shape(Rectangle(4, 6))
print(sm.total_area())
print(type(sm.largest_shape()).__name__)
```

---

## 🗂️ Задача 3: `bank_portfolio/`

**Структура:**
```
bank_portfolio/
├── account.py
├── investment.py
├── portfolio.py
└── main.py
```

**Описание:**
- `Account`: private `__balance`, методи `deposit()`, `withdraw()`
- `Investment`: private `__amount`, `rate`, метод `calculate_return(years)`
- `Portfolio`: държи списък от сметки и инвестиции, методи:
  - `total_value()`
  - `projected_value(years)` (събира текущите баланси + прогнозни печалби от инвестиции)


```python
from account import Account
from investment import Investment
from portfolio import Portfolio

a1 = Account(1000)
a2 = Account(2000)

inv1 = Investment(5000, 0.05)
inv2 = Investment(3000, 0.07)

portfolio = Portfolio()
portfolio.add_account(a1)
portfolio.add_account(a2)
portfolio.add_investment(inv1)
portfolio.add_investment(inv2)

print("Total value now:", portfolio.total_value())
print("Projected value in 5 years:", portfolio.projected_value(5))

```
---

## 🗂️ Задача 4: `election_system/`

**Структура:**
```
election_system/
├── candidate.py
├── party.py
├── election.py
└── main.py
```

**Описание:**
- `Candidate`: `name`, private `__votes`, метод `add_votes(n)`
- `Party`: списък от кандидати, метод `total_votes()`
- `Election`: списък от партии, методи:
  - `winning_party()`
  - `top_candidate()`

```python
from candidate import Candidate
from party import Party
from election import Election

c1 = Candidate("Alice")
c2 = Candidate("Bob")
c3 = Candidate("Charlie")

c1.add_votes(1200)
c2.add_votes(1500)
c3.add_votes(900)

party1 = Party("Party A")
party1.add_candidate(c1)
party1.add_candidate(c2)

party2 = Party("Party B")
party2.add_candidate(c3)

election = Election()
election.add_party(party1)
election.add_party(party2)

print("Winning party:", election.winning_party().name)
print("Top candidate:", election.top_candidate().name)

```

---

## 🗂️ Задача 5: `weather_station/`

**Структура:**
```
weather_station/
├── reading.py
├── station.py
├── network.py
└── main.py
```

**Описание:**
- `Reading`: private `__temperature`, `__humidity`, методи за достъп
- `Station`: списък от `Reading` обекти, методи `average_temp()`, `average_humidity()`
- `Network`: списък от станции, метод `overall_average_temp()`

```python
from reading import Reading
from station import Station
from network import Network

s1 = Station("Station 1")
s1.add_reading(Reading(20, 50))
s1.add_reading(Reading(22, 55))

s2 = Station("Station 2")
s2.add_reading(Reading(18, 60))
s2.add_reading(Reading(21, 52))

network = Network()
network.add_station(s1)
network.add_station(s2)

print("Station 1 avg temp:", s1.average_temp())
print("Overall avg temp:", network.overall_average_temp())

```

---

## 🗂️ Задача 6: `university_grades/`

**Структура:**
```
university_grades/
├── student.py
├── course.py
├── university.py
└── main.py
```

**Описание:**
- `Student`: име, private `__grades` (dict: курс → оценка), методи `add_grade(course, grade)`, `average()`
- `Course`: име, списък от студенти, метод `average_grade()`
- `University`: списък от курсове, метод `best_student()`

```python
from student import Student
from course import Course
from university import University

s1 = Student("Anna")
s2 = Student("Mark")
s3 = Student("Lily")

c1 = Course("Math")
c1.add_student(s1)
c1.add_student(s2)

c2 = Course("Physics")
c2.add_student(s2)
c2.add_student(s3)

s1.add_grade("Math", 5.5)
s2.add_grade("Math", 6)
s2.add_grade("Physics", 5)
s3.add_grade("Physics", 5.8)

uni = University()
uni.add_course(c1)
uni.add_course(c2)

print("Best student:", uni.best_student().name)

```

---

## 🗂️ Задача 7: `movie_ratings/`

**Структура:**
```
movie_ratings/
├── movie.py
├── reviewer.py
├── rating_system.py
└── main.py
```

**Описание:**
- `Movie`: име, private `__ratings` (list от числа), методи `add_rating()`, `average_rating()`
- `Reviewer`: име, метод `rate_movie(movie, rating)`
- `RatingSystem`: държи списък от филми, метод `top_rated_movie()`

```python
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

system = RatingSystem()
system.add_movie(m1)
system.add_movie(m2)

print("Top rated movie:", system.top_rated_movie().name)

```

---

## 🗂️ Задача 8: `fitness_tracker/`

**Структура:**
```
fitness_tracker/
├── activity.py
├── user.py
├── tracker.py
└── main.py
```

**Описание:**
- `Activity`: име, продължителност (мин), калории
- `User`: списък от активности, метод `total_calories()`
- `Tracker`: списък от потребители, метод `most_active_user()`

```python
from activity import Activity
from user import User
from tracker import Tracker

u1 = User("Tom")
u2 = User("Sara")

u1.add_activity(Activity("Running", 30, 300))
u1.add_activity(Activity("Cycling", 60, 500))

u2.add_activity(Activity("Walking", 45, 200))
u2.add_activity(Activity("Running", 20, 250))

tracker = Tracker()
tracker.add_user(u1)
tracker.add_user(u2)

print("Most active user:", tracker.most_active_user().name)

```

---

## 🗂️ Задача 9: `transport_network/`

**Структура:**
```
transport_network/
├── route.py
├── vehicle.py
├── network.py
└── main.py
```

**Описание:**
- `Route`: начална и крайна точка, разстояние
- `Vehicle`: private `__speed`, метод `travel_time(route)`
- `Network`: списък от маршрути и превозни средства, метод `fastest_vehicle(route)`

```python
from route import Route
from vehicle import Vehicle
from network import Network

r1 = Route("City A", "City B", 150)
r2 = Route("City A", "City C", 300)

v1 = Vehicle(100)
v2 = Vehicle(150)

network = Network()
network.add_route(r1)
network.add_route(r2)
network.add_vehicle(v1)
network.add_vehicle(v2)

print("Fastest vehicle on route 1 speed:", network.fastest_vehicle(r1).__speed)  # might need getter


```

---

## 🗂️ Задача 10: `space_mission/`

**Структура:**
```
space_mission/
├── astronaut.py
├── spaceship.py
├── mission.py
└── main.py
```

**Описание:**
- `Astronaut`: име, private `__hours_in_space`, метод `add_hours(n)`
- `Spaceship`: име, капацитет, метод `can_carry(count)`
- `Mission`: списък от астронавти и кораб, методи:
  - `total_hours_in_space()`
  - `is_over_capacity()`


```python
from astronaut import Astronaut
from spaceship import Spaceship
from mission import Mission

a1 = Astronaut("Neil", 1000)
a2 = Astronaut("Buzz", 800)
a3 = Astronaut("Sally", 500)

ship = Spaceship("Apollo", 2)

mission = Mission(ship)
mission.add_astronaut(a1)
mission.add_astronaut(a2)
mission.add_astronaut(a3)  # should trigger over capacity check

print("Total hours in space:", mission.total_hours_in_space())
print("Over capacity?", mission.is_over_capacity())

```
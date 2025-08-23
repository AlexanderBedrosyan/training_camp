# 🏆 Задача 1: Sports League

**Структура:**
sports_league/
├── team.py
├── player.py
├── league.py
└── main.py


**Описание на класовете:**

- **Player**
  - Атрибути: `name`, `position`, private `__goals`
  - Методи:
    - `score_goal()` → увеличава `__goals` с 1
    - `get_goals()` → връща броя на головете
    - `__str__()` → връща "Player {name}, position: {position}, goals: {goals}"

- **Team**
  - Атрибути: `name`, private `__players` (списък от `Player`)
  - Методи:
    - `add_player(player)` → добавя играч
    - `total_goals()` → връща сумата на головете на всички играчи
    - `best_scorer()` → връща играча с най-много голове

- **League**
  - Атрибути: private `__teams` (списък от `Team`)
  - Методи:
    - `add_team(team)` → добавя отбор
    - `top_scorer()` → връща играча с най-много голове в лигата
    - `total_goals()` → връща сумата на всички голове в лигата

**main.py**
```python
from player import Player
from team import Team
from league import League

p1 = Player("Ivan", "Forward")
p1.score_goal(); p1.score_goal()
p2 = Player("Georgi", "Midfielder")
p2.score_goal()

t = Team("Tigers")
t.add_player(p1)
t.add_player(p2)

league = League()
league.add_team(t)

print(league.top_scorer().name)  # Ivan
print(league.total_goals())      # 3
```

# 🏦 Задача 2: Bank System
**Структура:**

bank_system/
├── account.py
├── customer.py
├── bank.py
└── main.py

**Описание на класовете:**

**Account**

  - Атрибути: private `__balance`
  - Методи:
    - `deposit(amount)` → увеличава баланса
    - `withdraw(amount)` → намалява баланса (само ако има достатъчно средства)
    - `get_balance()` → връща текущия баланс

**Customer**

  - Атрибути: `name`, private `__accounts` (списък от Account)
  - Методи:
    - `add_account(account)` → добавя сметка
    - `total_balance()` → връща общата сума по сметки
    - `richest_account()` → връща сметката с най-много пари

**Bank**

  - Атрибути: `name`, private `__customers` (списък от Customer)
  - Методи:
    - `add_customer(customer)` → добавя клиент
    - `total_assets()` → връща общата сума на всички сметки
    - `richest_customer()` → връща клиента с най-много пари

**main.py**

python

```python
from account import Account
from customer import Customer
from bank import Bank

acc1 = Account()
acc1.deposit(500)
acc2 = Account()
acc2.deposit(300)

c = Customer("Maria")
c.add_account(acc1)
c.add_account(acc2)

bank = Bank("OBB")
bank.add_customer(c)

print(bank.total_assets())       # 800
print(bank.richest_customer().name)  # Maria
```

# 🎓 Задача 3: University Grades
**Структура:**

university/
├── student.py
├── course.py
├── university.py
└── main.py

**Описание на класовете:**

**Student**

  - Атрибути: `name`, private `__grades` (dict: course → оценка)
  - Методи:
    - `add_grade(course, grade)` → добавя оценка (2–6)
    - `average()` → връща средната оценка
    - `__str__()` → "{name}, avg: {average}"

**Course**

  - Атрибути: `name`, private `__students` (списък от Student)
  - Методи:
    - `add_student(student)` → добавя студент
    - `average_grade()` → средна оценка на всички
    - `best_student()` → студентът с най-висока средна оценка

**University**

  - Атрибути: `name`, private `__courses`
  - Методи:
    - `add_course(course)` → добавя курс
    - `best_student()` → най-добрият студент във всички курсове
    - `average_university()` → средната оценка за университета

**main.py**
```python
from student import Student
from course import Course
from university import University

s1 = Student("Ivan")
s1.add_grade("Math", 6)
s1.add_grade("CS", 5)

s2 = Student("Maria")
s2.add_grade("Math", 4)
s2.add_grade("CS", 5)

c = Course("Informatics")
c.add_student(s1)
c.add_student(s2)

u = University("SU")
u.add_course(c)

print(c.best_student().name)      # Ivan
print(u.average_university())     # 5.0
```

# 🎬 Задача 4: Movie Ratings
**Структура:**

movie_app/
├── movie.py
├── reviewer.py
├── system.py
└── main.py

**Описание на класовете:**

**Movie**

  - Атрибу  ти: `title`, private `__ratings `(list от числа)
  - Методи:
    - `add_rating(rating)` → добавя оценка (1–10)
    - `average_rating()` → връща средната оценка
    - `__str__()` → "{title}, avg rating: {average}"

**Reviewer**

  - Атрибути: `name`
  - Методи:
    - `rate_movie(movie, rating)` → добавя оценка към филм

**RatingSystem**

  - Атрибути: private `__movies`
  - Методи:
    - `add_movie(movie)` → добавя филм
    - `top_rated()` → филмът с най-висока средна оценка
    - `lowest_rated()` → филмът с най-ниска средна оценка

**main.py**

```python
from movie import Movie
from reviewer import Reviewer
from system import RatingSystem

m1 = Movie("Inception")
m2 = Movie("Titanic")

r = Reviewer("Ivan")
r.rate_movie(m1, 9)
r.rate_movie(m2, 7)

system = RatingSystem()
system.add_movie(m1)
system.add_movie(m2)

print(system.top_rated().title)    # Inception
print(system.lowest_rated().title) # Titanic
```

# 🚗 Задача 5: Transport Network
**Структура:**

transport_network/
├── route.py
├── vehicle.py
├── network.py
└── main.py

**Описание на класовете:**

**Route**

  - Атрибути: `start`, `end`, `distance`
  - Методи:
    - `__str__()` → "Route {start} → {end}, {distance} km"

**Vehicle**

  - Атрибути: `name`, private `__speed`
  - Методи:
    - `travel_time(route)` → време за пътуване = distance / speed
    - `get_speed()` → връща скоростта

**Network**

  - Атрибути: private `__routes`, private `__vehicles`
  - Методи:
    - `add_route(route)` → добавя маршрут
    - `add_vehicle(vehicle)` → добавя превозно средство
    - `fastest_vehicle(route)` → връща най-бързото превозно средство за даден маршрут

**main.py**

```python
from route import Route
from vehicle import Vehicle
from network import Network

r = Route("Sofia", "Plovdiv", 150)

v1 = Vehicle("Car", 100)
v2 = Vehicle("Bus", 75)

n = Network()
n.add_route(r)
n.add_vehicle(v1)
n.add_vehicle(v2)

print(n.fastest_vehicle(r).name)  # Car
```
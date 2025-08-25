
# 🏆 10 ООП Задачи с повече логика и проверки

## 📌 Задача 1: Sports League
**Структура:**
sports_league/  
├── team.py  
├── player.py  
├── league.py  
└── main.py  

**Описание:**

- **Player**
  - Атрибути: `name`, `position`, private `__goals`
  - Методи: `score_goal()`, `get_goals()`, `__str__()`
- **Team**
  - Атрибути: `name`, private `__players`
  - Методи: `add_player()`, `total_goals()`, `best_scorer()`
- **League**
  - Атрибути: private `__teams`
  - Методи: `add_team()`, `top_scorer()`, `total_goals()`

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

## 📌 Задача 2: School System
**Структура:**
school_system/  
├── person.py  
├── student.py  
├── teacher.py  
└── main.py  

**Описание:**

- **Person**: `name`, `age`; метод `__str__()`
- **Student** (наследява Person): private `__grades`; методи `add_grade()`, `average()`
- **Teacher** (наследява Person): `subject`, private `__students`; методи `add_student()`, `class_average()`

**main.py**
```python
from student import Student
from teacher import Teacher

s1 = Student("Anna", 18)
s1.add_grade(5); s1.add_grade(6)

s2 = Student("Boris", 19)
s2.add_grade(4); s2.add_grade(5)

t = Teacher("Mr. Ivanov", "Math")
t.add_student(s1); t.add_student(s2)

print(s1.average())          # 5.5
print(t.class_average())     # 5.0
```

## 📌 Задача 3: Bank Portfolio
**Структура:**
bank_portfolio/  
├── account.py  
├── investment.py  
├── portfolio.py  
└── main.py  

**Описание:**

- **Account**: private `__balance`; методи `deposit()`, `withdraw()`
- **Investment**: private `__amount`, `rate`; метод `calculate_return(years)`
- **Portfolio**: списък от Accounts и Investments; методи `total_value()`, `projected_value(years)`

**main.py**
```python
from account import Account
from investment import Investment
from portfolio import Portfolio

acc1 = Account(1000)
acc2 = Account(2000)
inv = Investment(5000, 0.05)

portfolio = Portfolio()
portfolio.add_account(acc1)
portfolio.add_account(acc2)
portfolio.add_investment(inv)

print(portfolio.total_value())         # 8000
print(portfolio.projected_value(2))   # 1000+2000 + 5000*(1.05^2)
```

## 📌 Задача 4: Election System
**Структура:**
election_system/  
├── candidate.py  
├── party.py  
├── election.py  
└── main.py  

**Описание:**

- **Candidate**: `name`, private `__votes`; методи `add_votes()`, `get_votes()`
- **Party**: `name`, списък от кандидати; метод `total_votes()`
- **Election**: списък от партии; методи `winning_party()`, `top_candidate()`

**main.py**
```python
from candidate import Candidate
from party import Party
from election import Election

c1 = Candidate("Alice"); c1.add_votes(100)
c2 = Candidate("Bob"); c2.add_votes(150)

p = Party("Green"); p.add_candidate(c1); p.add_candidate(c2)

e = Election(); e.add_party(p)

print(e.winning_party().name)    # Green
print(e.top_candidate().name)    # Bob
```

## 📌 Задача 5: Weather Station
**Структура:**
weather_station/  
├── reading.py  
├── station.py  
├── network.py  
└── main.py  

**Описание:**

- **Reading**: private `__temperature`, `__humidity`; методи за достъп
- **Station**: списък от Reading; методи `average_temp()`, `average_humidity()`
- **Network**: списък от станции; метод `overall_average_temp()`

**main.py**
```python
from reading import Reading
from station import Station
from network import Network

r1 = Reading(20, 60)
r2 = Reading(25, 55)
s = Station("Central"); s.add_reading(r1); s.add_reading(r2)

net = Network(); net.add_station(s)

print(s.average_temp())            # 22.5
print(net.overall_average_temp())  # 22.5
```

## 📌 Задача 6: University Grades
**Структура:**
university_grades/  
├── student.py  
├── course.py  
├── university.py  
└── main.py  

**Описание:**

- **Student**: име, private `__grades` (dict: курс → оценка); методи `add_grade()`, `average()`
- **Course**: име, списък от студенти; метод `average_grade()`
- **University**: списък от курсове; метод `best_student()`

**main.py**
```python
from student import Student
from course import Course
from university import University

s1 = Student("Anna"); s1.add_grade("Math", 5); s1.add_grade("Physics", 6)
s2 = Student("Boris"); s2.add_grade("Math", 4); s2.add_grade("Physics", 5)

math = Course("Math"); math.add_student(s1); math.add_student(s2)

uni = University(); uni.add_course(math)

print(s1.average())        # 5.5
print(math.average_grade())# 4.5
print(uni.best_student().name) # Anna
```


# 🏆 ООП Задачи – Част 2 (с повече логика)

---

## 📌 Задача 1: Shopping Cart

**Структура:**
shopping_cart/  
├── product.py  
├── cart.py  
├── discount.py  
└── main.py  

**Описание:**

- **Product**
  - Атрибути: `name`, `price`
  - Метод: `__str__()` → "Product {name}, price {price}"

- **Cart**
  - Атрибути: private `__products`
  - Методи:
    - `add_product(product)`
    - `total_price()`
    - `apply_discount(discount)`

- **Discount**
  - Атрибут: `percent`
  - Метод: `calculate(amount)` → връща сумата след намалението

**main.py**
```python
from product import Product
from cart import Cart
from discount import Discount

p1 = Product("Apple", 2.0)
p2 = Product("Milk", 3.5)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

d = Discount(10)
print(cart.total_price())           # 5.5
print(cart.apply_discount(d))       # 4.95
```

---

## 📌 Задача 2: Library System

**Структура:**
library_system/  
├── book.py  
├── member.py  
├── library.py  
└── main.py  

**Описание:**

- **Book**
  - Атрибути: `title`, `author`, private `__available` (True/False)
  - Методи:
    - `borrow()` → ако е налична, става False
    - `return_book()` → връща я налична

- **Member**
  - Атрибути: `name`, private `__borrowed_books`
  - Методи:
    - `borrow_book(book)`
    - `return_book(book)`
    - `list_books()`

- **Library**
  - Атрибути: private `__books`
  - Методи:
    - `add_book(book)`
    - `available_books()`

**main.py**
```python
from book import Book
from member import Member
from library import Library

b1 = Book("1984", "Orwell")
b2 = Book("Dune", "Herbert")
m = Member("Ivan")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

m.borrow_book(b1)
print(lib.available_books())   # ['Dune']
m.return_book(b1)
print(lib.available_books())   # ['1984', 'Dune']
```

---

## 📌 Задача 3: Bank System

**Структура:**
bank_system/  
├── account.py  
├── customer.py  
├── bank.py  
└── main.py  

**Описание:**

- **Account**
  - Атрибути: private `__balance`
  - Методи:
    - `deposit(amount)`
    - `withdraw(amount)` (с проверка за достатъчна наличност)
    - `get_balance()`

- **Customer**
  - Атрибути: `name`, `account`
  - Методи:
    - `deposit(amount)` → подава към акаунта
    - `withdraw(amount)`
    - `balance()`

- **Bank**
  - Атрибути: private `__customers`
  - Методи:
    - `add_customer(customer)`
    - `total_assets()`

**main.py**
```python
from account import Account
from customer import Customer
from bank import Bank

a1 = Account()
c1 = Customer("Maria", a1)

c1.deposit(500)
c1.withdraw(200)

b = Bank()
b.add_customer(c1)

print(c1.balance())    # 300
print(b.total_assets()) # 300
```

---

## 📌 Задача 4: Online Store

**Структура:**
online_store/  
├── product.py  
├── order.py  
├── store.py  
└── main.py  

**Описание:**

- **Product**
  - Атрибути: `name`, `price`

- **Order**
  - Атрибути: private `__products`
  - Методи:
    - `add_product(product)`
    - `order_total()`

- **Store**
  - Атрибути: private `__orders`
  - Методи:
    - `add_order(order)`
    - `total_revenue()`

**main.py**
```python
from product import Product
from order import Order
from store import Store

p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)

o1 = Order()
o1.add_product(p1)
o1.add_product(p2)

s = Store()
s.add_order(o1)

print(o1.order_total())    # 1225
print(s.total_revenue())   # 1225
```

---

## 📌 Задача 5: Zoo Management

**Структура:**
zoo_management/  
├── animal.py  
├── zookeeper.py  
├── zoo.py  
└── main.py  

**Описание:**

- **Animal**
  - Атрибути: `species`, `age`
  - Метод: `__str__()`

- **Zookeeper**
  - Атрибути: `name`, private `__animals`
  - Методи:
    - `add_animal(animal)`
    - `list_animals()`

- **Zoo**
  - Атрибути: private `__zookeepers`
  - Методи:
    - `add_keeper(keeper)`
    - `all_animals()`

**main.py**
```python
from animal import Animal
from zookeeper import Zookeeper
from zoo import Zoo

a1 = Animal("Lion", 5)
a2 = Animal("Elephant", 12)
zk = Zookeeper("Peter")

zk.add_animal(a1)
zk.add_animal(a2)

z = Zoo()
z.add_keeper(zk)

print(z.all_animals())  # ['Lion', 'Elephant']
```

---

## 📌 Задача 6: Course Management

**Структура:**
course_management/  
├── student.py  
├── course.py  
├── university.py  
└── main.py  

**Описание:**

- **Student**
  - Атрибути: `name`, private `__grades` (dict)
  - Методи:
    - `add_grade(course, grade)`
    - `average()`

- **Course**
  - Атрибути: `name`, private `__students`
  - Методи:
    - `add_student(student)`
    - `average_grade()`

- **University**
  - Атрибути: private `__courses`
  - Методи:
    - `add_course(course)`
    - `best_student()`

**main.py**
```python
from student import Student
from course import Course
from university import University

s1 = Student("Ivan")
s1.add_grade("Math", 5)
s1.add_grade("Math", 6)

c = Course("Math")
c.add_student(s1)

u = University()
u.add_course(c)

print(s1.average())      # 5.5
print(u.best_student())  # Ivan
```

---

## 📌 Задача 7: Tournament

**Структура:**
tournament/  
├── player.py  
├── match.py  
├── tournament.py  
└── main.py  

**Описание:**

- **Player**
  - Атрибути: `name`, private `__score`
  - Методи:
    - `add_score(points)`
    - `get_score()`

- **Match**
  - Атрибути: `player1`, `player2`
  - Метод: `play(winner)` → добавя точки на победителя

- **Tournament**
  - Атрибути: private `__players`
  - Методи:
    - `add_player(player)`
    - `leaderboard()`

**main.py**
```python
from player import Player
from match import Match
from tournament import Tournament

p1 = Player("Alice")
p2 = Player("Bob")

m = Match(p1, p2)
m.play(p1)

t = Tournament()
t.add_player(p1)
t.add_player(p2)

print(t.leaderboard())  # [('Alice', 3), ('Bob', 0)]
```

---

## 📌 Задача 8: Fitness Tracker

**Структура:**
fitness_tracker/  
├── activity.py  
├── user.py  
├── tracker.py  
└── main.py  

**Описание:**

- **Activity**
  - Атрибути: `name`, `calories`

- **User**
  - Атрибути: `name`, private `__activities`
  - Методи:
    - `add_activity(activity)`
    - `total_calories()`

- **Tracker**
  - Атрибути: private `__users`
  - Методи:
    - `add_user(user)`
    - `most_active_user()`

**main.py**
```python
from activity import Activity
from user import User
from tracker import Tracker

a1 = Activity("Running", 300)
a2 = Activity("Cycling", 500)

u = User("Ivan")
u.add_activity(a1)
u.add_activity(a2)

t = Tracker()
t.add_user(u)

print(u.total_calories())      # 800
print(t.most_active_user())    # Ivan
```

---

## 📌 Задача 9: Cinema

**Структура:**
cinema/  
├── movie.py  
├── customer.py  
├── cinema.py  
└── main.py  

**Описание:**

- **Movie**
  - Атрибути: `title`, private `__seats`
  - Методи:
    - `book_seat()` (намалява броя на местата с 1, ако има)

- **Customer**
  - Атрибути: `name`, private `__tickets`
  - Методи:
    - `book_movie(movie)`

- **Cinema**
  - Атрибути: private `__movies`
  - Методи:
    - `add_movie(movie)`
    - `available_movies()`

**main.py**
```python
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
```

---

## 📌 Задача 10: Transport System

**Структура:**
transport_system/  
├── vehicle.py  
├── route.py  
├── system.py  
└── main.py  

**Описание:**

- **Vehicle**
  - Атрибути: `name`, private `__speed`
  - Метод: `travel_time(route)` → разстояние / скорост

- **Route**
  - Атрибути: `start`, `end`, `distance`

- **System**
  - Атрибути: private `__vehicles`
  - Методи:
    - `add_vehicle(vehicle)`
    - `fastest_vehicle(route)`

**main.py**
```python
from vehicle import Vehicle
from route import Route
from system import System

v1 = Vehicle("Car", 100)
v2 = Vehicle("Plane", 800)

r = Route("Sofia", "Varna", 400)

s = System()
s.add_vehicle(v1)
s.add_vehicle(v2)

print(s.fastest_vehicle(r))  # Plane
```

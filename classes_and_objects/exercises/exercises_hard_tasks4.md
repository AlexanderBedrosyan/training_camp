# 🧩 OOP Задачи – Част 3 (по-сложни с повече проверки)

---

## 📌 Задача 1: Online Store

**Структура:**
```
online_store/
├── product.py
├── cart.py
├── order.py
└── main.py
```

**Описание:**
- **Product**
  - Атрибути: `name`, `price`, `stock`
  - Методи:
    - `reduce_stock(qty)` → намалява стоката, ако има наличност
    - `is_available(qty)` → проверява дали продуктът е наличен в нужното количество

- **Cart**
  - Атрибути: private `__items` (dict: продукт → количество)
  - Методи:
    - `add_product(product, qty)` → проверява наличност преди добавяне
    - `total_price()` → сумира общата стойност

- **Order**
  - Атрибути: `cart`, `status`
  - Методи:
    - `confirm_order()` → ако има наличности, намалява стоката и сменя статуса

---

## 📌 Задача 2: University Courses

**Структура:**
```
university_courses/
├── student.py
├── course.py
├── gradebook.py
└── main.py
```

**Описание:**
- **Student**
  - Атрибути: `name`, private `__grades` (dict: course → grade)
  - Методи: `add_grade(course, grade)`, `average()` (проверка дали има оценки)

- **Course**
  - Атрибути: `title`, списък студенти
  - Методи: `add_student(student)`, `course_average()`

- **GradeBook**
  - Атрибути: списък от курсове
  - Методи: `best_student()`, `top_course()`

---

## 📌 Задача 3: Banking System

**Структура:**
```
banking_system/
├── account.py
├── savings.py
├── bank.py
└── main.py
```

**Описание:**
- **Account**
  - Атрибути: `owner`, private `__balance`
  - Методи: `deposit(amount)`, `withdraw(amount)` (с проверки за отрицателни стойности)

- **SavingsAccount (Account)**
  - Атрибути: `interest_rate`
  - Методи: `apply_interest(years)`

- **Bank**
  - Атрибути: списък от акаунти
  - Методи: `total_assets()`, `richest_account()`

---

## 📌 Задача 4: School Management

**Структура:**
```
school_management/
├── person.py
├── teacher.py
├── classroom.py
└── main.py
```

**Описание:**
- **Person**
  - Атрибути: `name`, `age`
  - Метод: `__str__()`

- **Teacher (Person)**
  - Атрибути: `subject`, `salary`
  - Метод: `give_grade(student, grade)`

- **Classroom**
  - Атрибути: списък от ученици, класен ръководител
  - Методи: `average_grade()`, `best_student()`

---

## 📌 Задача 5: Hospital System

**Структура:**
```
hospital_system/
├── patient.py
├── doctor.py
├── hospital.py
└── main.py
```

**Описание:**
- **Patient**
  - Атрибути: `name`, private `__diagnoses`
  - Методи: `add_diagnosis(diagnosis)`, `list_diagnoses()`

- **Doctor**
  - Атрибути: `name`, `specialty`, private `__patients`
  - Методи: `add_patient(patient)`, `num_patients()`

- **Hospital**
  - Атрибути: списък от доктори
  - Методи: `total_patients()`, `most_busy_doctor()`

---

## 📌 Задача 6: Transport Planner

**Структура:**
```
transport_planner/
├── vehicle.py
├── route.py
├── planner.py
└── main.py
```

**Описание:**
- **Vehicle**
  - Атрибути: `name`, `speed`
  - Метод: `travel_time(route)` → проверява скорост > 0

- **Route**
  - Атрибути: `start`, `end`, `distance`
  - Метод: `__str__()`

- **Planner**
  - Атрибути: списък превозни средства и маршрути
  - Методи: `fastest_vehicle(route)`, `shortest_route()`

---

## 📌 Задача 7: Music Platform

**Структура:**
```
music_platform/
├── song.py
├── playlist.py
├── user.py
└── main.py
```

**Описание:**
- **Song**
  - Атрибути: `title`, `duration`
  - Метод: `__str__()`

- **Playlist**
  - Атрибути: списък песни
  - Методи: `add_song(song)`, `total_duration()`

- **User**
  - Атрибути: `name`, списък плейлисти
  - Методи: `add_playlist(pl)`, `favorite_song()` (намира най-дългата песен)

---

## 📌 Задача 8: Tournament

**Структура:**
```
tournament/
├── player.py
├── match.py
├── tournament.py
└── main.py
```

**Описание:**
- **Player**
  - Атрибути: `name`, private `__score`
  - Методи: `add_points(n)`, `get_score()`

- **Match**
  - Атрибути: `p1`, `p2`, `winner`
  - Метод: `play()` → добавя точки на победителя

- **Tournament**
  - Атрибути: списък от мачове
  - Методи: `leaderboard()`, `champion()`

---

## 📌 Задача 9: Airline System

**Структура:**
```
airline_system/
├── passenger.py
├── flight.py
├── airline.py
└── main.py
```

**Описание:**
- **Passenger**
  - Атрибути: `name`, private `__tickets`
  - Методи: `book_ticket(flight)`, `num_tickets()`

- **Flight**
  - Атрибути: `code`, `capacity`, private `__booked`
  - Методи: `book_passenger(p)`, `is_full()`

- **Airline**
  - Атрибути: списък полети
  - Методи: `total_passengers()`, `busiest_flight()`

---

## 📌 Задача 10: Zoo Management

**Структура:**
```
zoo_management/
├── animal.py
├── cage.py
├── zoo.py
└── main.py
```

**Описание:**
- **Animal**
  - Атрибути: `name`, `species`
  - Метод: `__str__()`

- **Cage**
  - Атрибути: номер, списък животни, капацитет
  - Методи: `add_animal(a)` (проверка за капацитет), `count_animals()`

- **Zoo**
  - Атрибути: списък клетки
  - Методи: `total_animals()`, `largest_cage()`

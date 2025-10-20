# 🧠 10 Сложни задачи с речници и класове (Python)

## 📘 Задача 1: Гилдия на приключенците
Създай клас `Guild`, който управлява списък от приключенци и техните точки опит.

### Условия:
- Приключенците се пазят в речник `{име: точки}`.
- Метод `add_adventurer(name, points)` добавя приключенец или увеличава точките му.
- Метод `top_adventurer()` връща името на приключенеца с най-много точки.
- Метод `average_points()` връща средния опит на всички.

### Тест:
```python
g = Guild()
g.add_adventurer("Ivan", 120)
g.add_adventurer("Petar", 80)
g.add_adventurer("Ivan", 30)
print(g.top_adventurer())  # Ivan
print(round(g.average_points(), 2))  # 115.0
```

## 🏦 Задача 2: Банков мениджър
Създай клас Bank, който пази клиенти и баланси.

### Условия:
- Речникът е {име: {"balance": сума, "transactions": []}}
- Метод deposit(name, amount) добавя сума и запис в транзакции.
- Метод withdraw(name, amount) намаля баланса, ако има достатъчно средства.
- Метод richest_client() връща името на най-богатия клиент.

### Тест:
```python
b = Bank()
b.deposit("Maria", 2000)
b.deposit("Ivan", 1000)
b.withdraw("Ivan", 300)
print(b.richest_client())  # Maria
```

## 📚 Задача 3: Онлайн училище
Създай клас School, който управлява ученици и техните оценки.

### Условия:
- Речник {ученик: [оценки]}.
- Метод add_grade(student, grade) добавя оценка.
- Метод best_student() връща ученика с най-висок среден успех.
- Метод class_average() връща средния успех на целия клас.

### Тест:
```python
s = School()
s.add_grade("Anna", 6)
s.add_grade("Anna", 5)
s.add_grade("Boris", 4)
print(s.best_student())  # Anna
print(round(s.class_average(), 2))  # 5.0
```

## 🍴 Задача 4: Ресторантски поръчки
Създай клас Restaurant, който следи клиентски поръчки.

### Условия:
- Речник {клиент: {"orders": [{"item": име, "price": сума}], "total": сума}}
- Метод add_order(client, item, price)
- Метод top_client() – връща клиента с най-голяма сметка.

### Тест:
```python
r = Restaurant()
r.add_order("Nikol", "Pizza", 15)
r.add_order("Ivan", "Pasta", 10)
r.add_order("Nikol", "Juice", 5)
print(r.top_client())  # Nikol
```

## 🚗 Задача 5: Автопарк
Създай клас Garage, който следи коли и ремонти.

### Условия:
- Речник {рег.номер: {"model": име, "repairs": [разходи]}}
- Метод add_repair(reg, cost) – добавя ремонт.
- Метод total_spent(reg) – сума на всички ремонти за колата.
- Метод most_expensive_car() – връща регистрацията на колата с най-много похарчено.

### Тест:
```python
g = Garage()
g.add_repair("CA1234", 400)
g.add_repair("CB5678", 600)
g.add_repair("CA1234", 300)
print(g.most_expensive_car())  # CA1234
```

## 🧾 Задача 6: Пазар за стоки
Създай клас Marketplace, който управлява продукти и наличности.

### Условия:
- Речник {продукт: {"quantity": бр, "price": цена}}
- Метод add_product(name, quantity, price)
- Метод buy_product(name, count) – намаля количеството, ако има.
- Метод total_value() – връща общата стойност на всички стоки.

### Тест:
```python
m = Marketplace()
m.add_product("Apple", 10, 2)
m.add_product("Banana", 5, 3)
m.buy_product("Apple", 3)
print(m.total_value())  # 29
```

## 🎓 Задача 7: Университетска система
Създай клас University, който следи преподаватели и студенти.

### Условия:
- Речник {преподавател: {"students": [списък], "subject": предмет}}
- Метод add_teacher(name, subject)
- Метод add_student(teacher, student)
- Метод teacher_load(teacher) – брой студенти на преподавателя.
- Метод most_loaded_teacher() – връща най-натоварения преподавател.

### Тест:
```python
u = University()
u.add_teacher("Dr. Ivanov", "Math")
u.add_teacher("Dr. Petrov", "Physics")
u.add_student("Dr. Ivanov", "Anna")
u.add_student("Dr. Ivanov", "Boris")
print(u.most_loaded_teacher())  # Dr. Ivanov
```

## 💼 Задача 8: Фирмена йерархия
Създай клас Company, който управлява отдели и служители.

### Условия:
- Речник {отдел: {"employees": [имена], "budget": сума}}
- Метод add_employee(dept, name)
- Метод increase_budget(dept, amount)
- Метод total_budget() – връща общия бюджет на фирмата.

### Тест:
```python
c = Company()
c.add_employee("IT", "Ivan")
c.add_employee("HR", "Maria")
c.increase_budget("IT", 5000)
c.increase_budget("HR", 3000)
print(c.total_budget())  # 8000
```

## 🎮 Задача 9: Видео игрова платформа
Създай клас GamePlatform, който следи игри и оценки.

### Условия:

- Речник {игра: {"ratings": [числа], "genre": жанр}}
- Метод add_rating(game, rating)
- Метод best_game() – връща играта с най-висока средна оценка.
- Метод average_genre(genre) – средна оценка за жанра.

### Тест:
```python
gp = GamePlatform()
gp.add_rating("Zelda", 10)
gp.add_rating("Zelda", 9)
gp.add_rating("Mario", 8)
print(gp.best_game())  # Zelda
```

## 🌍 Задача 10: Туристическа агенция

Създай клас TravelAgency, който следи клиенти и техните пътувания.

### Условия:
- Речник {име: {"trips": [дестинации], "spent": общо_сума}}
- Метод add_trip(name, destination, cost)
- Метод top_traveler() – връща клиента с най-големи разходи.
- Метод unique_destinations() – връща списък с всички различни дестинации.

### Тест:
```python
t = TravelAgency()
t.add_trip("Ivan", "Paris", 1200)
t.add_trip("Maria", "London", 800)
t.add_trip("Ivan", "Rome", 600)
print(t.top_traveler())  # Ivan
print(sorted(t.unique_destinations()))  # ['London', 'Paris', 'Rome']
```
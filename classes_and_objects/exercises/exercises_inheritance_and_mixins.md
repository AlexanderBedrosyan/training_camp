## 🧠 Упражнения с висока трудност – OOP, Наследяване и Миксини

---

### 🗂️ Задача 1: `vehicle_project/`

**Структура:**
```
vehicle_project/
├── vehicle.py
├── car.py
└── main.py
```

**Описание:**
- В `vehicle.py` създай клас `Vehicle` с:
  - protected атрибут `_max_speed`
  - метод `info()`, който връща `"Vehicle with max speed X"`
- В `car.py` създай клас `Car`, който наследява `Vehicle`
  - private атрибут `__brand`
  - метод `info()` да връща `"Brand car with max speed X"`

**main.py:**
```python
from car import Car

c = Car("BMW", 240)
print(c.info())  # BMW car with max speed 240
```

---

### 🗂️ Задача 2: `bank_system/`

**Структура:**
```
bank_system/
├── account.py
├── premium_account.py
└── main.py
```

**Описание:**
- `Account` (в `account.py`) има:
  - private атрибут `__balance`
  - методи `deposit()` и `withdraw()`
- `PremiumAccount` (в `premium_account.py`) наследява `Account`, но има метод `apply_bonus()` – добавя 5% към баланса

**main.py:**
```python
from premium_account import PremiumAccount

acc = PremiumAccount(1000)
acc.deposit(200)
acc.apply_bonus()
print(acc.get_balance())  # ~1260.0
```

---

### 🗂️ Задача 3: `school/`

**Структура:**
```
school/
├── person.py
├── student.py
└── main.py
```

**Описание:**
- `Person` има атрибути: `name`, `age`
- `Student` наследява `Person` и добавя private списък `__grades` и метод `average()`

**main.py:**
```python
from student import Student

s = Student("Eva", 19)
s.add_grade(5)
s.add_grade(6)
print(s.average())  # 5.5
```

---

### 🗂️ Задача 4: `ecommerce/`

**Структура:**
```
ecommerce/
├── item.py
├── cart.py
└── main.py
```

**Описание:**
- `Item` – клас с `name` и `price`
- `Cart` – съдържа списък от `Item` и метод `total()`
- Използвай `@property` за изчисляване на обща сума

**main.py:**
```python
from item import Item
from cart import Cart

cart = Cart()
cart.add_item(Item("Laptop", 1000))
cart.add_item(Item("Mouse", 50))
print(cart.total)  # 1050
```

---

### 🗂️ Задача 5: `employees/`

**Структура:**
```
employees/
├── employee.py
├── manager.py
└── main.py
```

**Описание:**
- `Employee` с атрибути `name`, `salary`
- `Manager` наследява `Employee` и има списък от служители и метод `total_salary()`

**main.py:**
```python
from manager import Manager
from employee import Employee

m = Manager("Laura", 3000)
m.add_employee(Employee("Ivan", 2000))
m.add_employee(Employee("Mira", 2200))
print(m.total_salary())  # 7200
```

---

### 🗂️ Задача 6: `auth_system/`

**Структура:**
```
auth_system/
├── user.py
├── login_mixin.py
└── main.py
```

**Описание:**
- `LoginMixin` с методи `login()` и `logout()`, поддържа флаг `is_logged_in`
- `User` използва миксина, има атрибут `username`

**main.py:**
```python
from user import User

u = User("admin")
u.login()
print(u.is_logged_in)  # True
u.logout()
print(u.is_logged_in)  # False
```

---

### 🗂️ Задача 7: `university/`

**Структура:**
```
university/
├── person.py
├── professor.py
└── main.py
```

**Описание:**
- `Person` с `name`, `id`
- `Professor` – добавя списък от предмети, метод `teach(course)`, и `list_courses()`

**main.py:**
```python
from professor import Professor

p = Professor("Dr. Boris", "P123")
p.teach("Math")
p.teach("Physics")
print(p.list_courses())  # ['Math', 'Physics']
```

---

### 🗂️ Задача 8: `loggable_tools/`

**Структура:**
```
loggable_tools/
├── tool.py
├── loggable_mixin.py
└── main.py
```

**Описание:**
- `LoggableMixin`: записва всяка операция с време в списък
- `Tool` наследява миксина и има метод `use()`

**main.py:**
```python
from tool import Tool

t = Tool("Hammer")
t.use()
t.use()
print(t.logs)  # Логове с време и действие
```

---

### 🗂️ Задача 9: `notifications/`

**Структура:**
```
notifications/
├── message.py
├── email.py
└── main.py
```

**Описание:**
- `Message`: base class
- `EmailMessage`: наследява `Message`, добавя адрес, метод `send()`, който валидира адрес

**main.py:**
```python
from email import EmailMessage

e = EmailMessage("Welcome", "user@example.com")
e.send()  # Message sent to user@example.com
```

---

### 🗂️ Задача 10: `settings/`

**Структура:**
```
settings/
├── config.py
├── editable_mixin.py
└── main.py
```

**Описание:**
- `EditableMixin`: дава възможност за `get`, `set`, `delete` на атрибути чрез `getattr`, `setattr`, `delattr`
- `Config`: клас с private атрибути `__theme`, `__language`

**main.py:**
```python
from config import Config

c = Config("dark", "bg")
c.set_attr("theme", "light")
print(c.get_attr("theme"))  # light
```

---

📝 **Забележка**:  
Във всяка задача:
- използвайте правилно `__private`, `_protected`, класови атрибути  
- стремете се към модулност и добра организация на кода  

Ако желаеш, мога да ти генерирам **готови файлове със скелети**, които просто да качиш в проект.

```python
# Кажи ми "генерирай кодовете по файлове", ако искаш примерен scaffold.
```


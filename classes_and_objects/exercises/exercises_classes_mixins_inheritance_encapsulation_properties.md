## 🧠 Упражнения: Разширени задачи с OOP, Наследяване, Миксини, Свойства

### 🗂️ Задача 1: `smart_home/`

**Структура:**
```
smart_home/
├── device.py
├── light.py
├── thermostat.py
└── main.py
```

**Описание:**
- `Device`: базов клас с protected атрибут `_status` и методи `turn_on()` и `turn_off()`
- `Light` наследява `Device`, има private атрибут `__brightness` с `@property` и `@setter`
- `Thermostat` наследява `Device`, има `@property` `temperature`, който се валидира (10-30 градуса)

**main.py:**
```python
from light import Light
from thermostat import Thermostat

l = Light()
l.turn_on()
l.brightness = 80
print(l.brightness)  # 80

t = Thermostat()
t.temperature = 25
print(t.temperature)  # 25
```

---

### 🗂️ Задача 2: `library_system/`

**Структура:**
```
library_system/
├── item.py
├── book.py
├── dvd.py
└── main.py
```

**Описание:**
- `LibraryItem` с атрибути `title`, `_available` и метод `checkout()`, `return_item()`
- `Book` има допълнителен private атрибут `__author` с `@property`
- `DVD` има `duration` и метод `is_long()` (>120 минути)

**main.py:**
```python
from book import Book
from dvd import DVD

b = Book("1984", "Orwell")
b.checkout()
print(b.is_available())  # False

d = DVD("Inception", 148)
print(d.is_long())  # True
```

---

### 🗂️ Задача 3: `vehicles_extended/`

**Структура:**
```
vehicles_extended/
├── vehicle.py
├── car.py
├── truck.py
└── main.py
```

**Описание:**
- `Vehicle`: базов клас с protected `_max_speed` и метод `describe()`
- `Car` има private атрибут `__brand` и метод `info()`
- `Truck` добавя атрибут `load_capacity` и метод `can_transport(weight)`

**main.py:**
```python
from car import Car
from truck import Truck

c = Car("BMW", 240)
print(c.info())  # BMW car with max speed 240

t = Truck(120, 5000)
print(t.can_transport(3000))  # True
```

---

### 🗂️ Задача 4: `employees_bonus/`

**Структура:**
```
employees_bonus/
├── employee.py
├── developer.py
├── manager.py
└── main.py
```

**Описание:**
- `Employee` с `name`, `_salary`, методи `get_salary()`
- `Developer` добавя `level`, метод `code()`
- `Manager` има екип и метод `total_team_salary()`

**main.py:**
```python
from developer import Developer
from manager import Manager

dev = Developer("Nina", 3000, "senior")
print(dev.code())

mgr = Manager("Max", 5000)
mgr.add_employee(dev)
print(mgr.total_team_salary())  # 8000
```

---

### 🗂️ Задача 5: `university_people/`

**Структура:**
```
university_people/
├── person.py
├── student.py
├── professor.py
└── main.py
```

**Описание:**
- `Person` с `name`, `age`
- `Student`: private `__grades`, метод `average()`
- `Professor`: private `__courses`, метод `list_courses()`

**main.py:**
```python
from student import Student
from professor import Professor

s = Student("Eva", 20)
s.add_grade(5)
s.add_grade(6)
print(s.average())  # 5.5

p = Professor("Dr. John", 50)
p.add_course("Math")
print(p.list_courses())
```

---

### 🗂️ Задача 6: `store_products/`

**Структура:**
```
store_products/
├── product.py
├── perishable.py
├── electronics.py
└── main.py
```

**Описание:**
- `Product` с `name`, `price`
- `Perishable`: добавя `expiration_date`, метод `is_expired(today)`
- `Electronics`: добавя гаранция в месеци, метод `is_under_warranty(months_used)`

**main.py:**
```python
from perishable import Perishable
from electronics import Electronics

milk = Perishable("Milk", 2.5, "2025-08-01")
print(milk.is_expired("2025-08-09"))  # True

tv = Electronics("TV", 500, 24)
print(tv.is_under_warranty(18))  # True
```

---

### 🗂️ Задача 7: `auth_roles/`

**Структура:**
```
auth_roles/
├── user.py
├── admin.py
├── role_mixin.py
└── main.py
```

**Описание:**
- `User`: private `__password`, метод `check_password()`
- `RoleMixin`: методи `add_role()` и `has_role()`
- `Admin` използва миксина, има reset на парола

**main.py:**
```python
from admin import Admin

a = Admin("admin", "1234")
a.add_role("superuser")
print(a.has_role("superuser"))  # True
```

---

### 🗂️ Задача 8: `banking_app/`

**Структура:**
```
banking_app/
├── account.py
├── savings.py
├── logger_mixin.py
└── main.py
```

**Описание:**
- `Account` с `balance`, `deposit()`, `withdraw()`
- `SavingsAccount`: добавя `interest_rate`, метод `apply_interest()`
- `LoggerMixin`: записва всички действия

**main.py:**
```python
from savings import SavingsAccount

acc = SavingsAccount(1000, 0.05)
acc.deposit(500)
acc.apply_interest()
print(acc.balance)
print(acc.get_logs())
```

---

### 🗂️ Задача 9: `shop_discount/`

**Структура:**
```
shop_discount/
├── item.py
├── discount_mixin.py
├── discounted_item.py
└── main.py
```

**Описание:**
- `Item` с `name`, `price`
- `DiscountMixin`: метод `apply_discount(%)`
- `DiscountedItem`: комбинира двете, добавя валидации

**main.py:**
```python
from discounted_item import DiscountedItem

i = DiscountedItem("Chair", 100)
i.apply_discount(10)
print(i.price)  # 90.0
```

---

### 🗂️ Задача 10: `game_characters/`

**Структура:**
```
game_characters/
├── character.py
├── warrior.py
├── mage.py
└── main.py
```

**Описание:**
- `Character` с `name`, `health`, метод `take_damage()`
- `Warrior`: метод `attack()`, защита
- `Mage`: private `__mana`, `cast_spell()` с `@property` и `@setter`

**main.py:**
```python
from warrior import Warrior
from mage import Mage

w = Warrior("Thor", 100)
w.attack()

m = Mage("Gandalf", 80, 100)
m.cast_spell("Fireball")
print(m.mana)
```

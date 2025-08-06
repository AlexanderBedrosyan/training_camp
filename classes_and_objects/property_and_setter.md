## 🧠 Лекция и Упражнения: Свойства в Python (`@property`, `@setter`)

---

### 📚 Теория: Какво е `@property`?

`@property` позволява метод да се използва като атрибут – например за изчисление, валидация или контрол на достъпа.

#### ✅ Предимства:
- Подобрява капсулацията
- Позволява проверка при четене и/или писане
- Позволява скриване на логиката зад интерфейс от типа `obj.attr`

---

### 🧪 Пример: Само четене (read-only)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.5
```

---

### 🔁 Пример с `@property` и `@setter`

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty")
        print("Setting name...")
        self._name = new_name

p = Person("Ivan")
print(p.name)
p.name = "Maria"
print(p.name)
```

---

## 🧩 Задачи: Свойства и Сетъри

---

### 🗂️ Задача 1: `temperature/`

**Структура:**
```
temperature/
├── temperature.py
└── main.py
```

**Описание:**
- Клас `Temperature` с:
  - protected атрибут `_celsius`
  - `@property` `fahrenheit`, който изчислява: `F = C * 1.8 + 32`

**main.py:**
```python
from temperature import Temperature

t = Temperature(25)
print(t.fahrenheit)  # 77.0
```

---

### 🗂️ Задача 2: `person/`

**Структура:**
```
person/
├── person.py
└── main.py
```

**Описание:**
- Клас `Person` с:
  - private атрибут `__height`
  - `@property` и `@setter` за `height`, който не приема отрицателни стойности

**main.py:**
```python
from person import Person

p = Person(180)
p.height = 175
print(p.height)  # 175
```

---

### 🗂️ Задача 3: `rectangle/`

**Структура:**
```
rectangle/
├── rectangle.py
└── main.py
```

**Описание:**
- Клас `Rectangle` с:
  - атрибути `width` и `height`
  - `@property` `area` (само за четене)

**main.py:**
```python
from rectangle import Rectangle

r = Rectangle(10, 5)
print(r.area)  # 50
```

---

### 🗂️ Задача 4: `user/`

**Структура:**
```
user/
├── user.py
└── main.py
```

**Описание:**
- Клас `User` с:
  - protected атрибут `_birth_year`
  - `@property` `age`, която изчислява възраст на база текущата година (2025)

**main.py:**
```python
from user import User

u = User("Mira", 2000)
print(u.age)  # 25
```

---

### 🗂️ Задача 5: `account/`

**Структура:**
```
account/
├── bank_account.py
└── main.py
```

**Описание:**
- Клас `BankAccount` с:
  - private атрибут `__balance`
  - `@property` и `@setter` за `balance`:
    - не позволява отрицателна стойност

**main.py:**
```python
from bank_account import BankAccount

acc = BankAccount(100)
acc.balance = 200
print(acc.balance)  # 200
```

---

### 🗂️ Задача 6: `circle/`

**Структура:**
```
circle/
├── circle.py
└── main.py
```

**Описание:**
- Клас `Circle` с:
  - атрибут `radius`
  - `@property` `diameter`
  - `@setter` за `diameter`, който променя радиуса

**main.py:**
```python
from circle import Circle

c = Circle(5)
print(c.diameter)  # 10
c.diameter = 14
print(c.radius)    # 7.0
```

---

### 🗂️ Задача 7: `email_user/`

**Структура:**
```
email_user/
├── user.py
└── main.py
```

**Описание:**
- Клас `User` с:
  - атрибут `email`
  - `@setter` за валидация – съдържа ли '@', иначе грешка

**main.py:**
```python
from user import User

u = User("a@b.com")
u.email = "b@c.com"
print(u.email)  # b@c.com
```

---

💡 **Бележка**:  
Във всички задачи използвай:

- `_protected` – когато достъпът е ограничен в класа и наследниците  
- `__private` – когато достъпът е само в класа (name mangling)  
- `@property` – когато атрибутът трябва да има контрол при четене  
- `@setter` – когато искаме да имаме логика/валидация при промяна

---

🔧 Ако желаеш, мога да генерирам и директно `.py` файловете по тези задачи, под формата на scaffold. Кажи **„създай файловете“**, ако искаш!

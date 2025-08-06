## 🏠 Домашна работа: Класове, Атрибути, Капсулация и Свойства

### 1. 📦 `Product`

Създай клас `Product` със следните елементи:
- **private атрибут** `__price`
- **обикновен атрибут** `name`
- метод `set_discount(percentage)` – намалява цената с определен процент
- метод `get_price()` – връща текущата цена, минимална цена е 0

**Примерен вход:**
```python
p = Product("Shoes", 120)
p.set_discount(20)
print(p.get_price())  # 96.0
```

---

### 2. 🔐 `Safe`

Създай клас `Safe`, който съдържа:
- **private атрибут** `__code` – задава се при създаване
- метод `unlock(code)` – отпечатва "Unlocked" само ако кодът е верен

**Примерен вход:**
```python
s = Safe("9876")
s.unlock("1234")  # Nothing
s.unlock("9876")  # Unlocked
```

---

### 3. 🏷️ `User`

Създай клас `User` със:
- **инстанс атрибут** `username`
- **класов атрибут** `user_count`, който се увеличава с всяко ново създаване на обект
- класов метод `get_user_count()`

**Примерен вход:**
```python
u1 = User("ivan")
u2 = User("maria")
print(User.get_user_count())  # 2
```

---

### 4. 🛠️ `Tool`

Създай клас `Tool`. След създаване:
- добави нов **обикновен атрибут** `weight` чрез `setattr()`
- използвай `getattr()` и `hasattr()` за извличане и проверка

**Примерен вход:**
```python
t = Tool()
setattr(t, "weight", 3.5)
if hasattr(t, "weight"):
    print(getattr(t, "weight"))  # 3.5
```

---

### 5. 🧪 `TestCase`

Създай клас с:
- **protected атрибут** `_name`
- **private атрибут** `__status` (по подразбиране "Not Run")
- метод `run()` – променя `__status` на "Passed"
- `@property` за `status`

**Примерен вход:**
```python
t = TestCase("Check sum")
print(t.status)  # Not Run
t.run()
print(t.status)  # Passed
```

---

### 6. 🎓 `Student`

Създай клас `Student` с:
- **обикновен атрибут** `name`
- **private атрибут** `__grades` (списък)
- метод `add_grade(grade)`
- `@property` за `average`, който връща средната стойност

**Примерен вход:**
```python
s = Student("Toni")
s.add_grade(5)
s.add_grade(6)
print(s.average)  # 5.5
```

---

### 7. 🧑‍💼 `Employee`

Създай клас с:
- **обикновен атрибут** `name`
- **private атрибут** `__salary`
- метод `increase_salary(amount)`
- `@property` за `salary` (само за четене)

**Примерен вход:**
```python
e = Employee("Anna", 3000)
e.increase_salary(500)
print(e.salary)  # 3500
```

---

### 8. 🧍 `Person`

Създай клас `Person` с:
- **обикновен атрибут** `name`
- **класов атрибут** `species = "Human"`
- метод `info()` – връща `"{name} is a {species}"`
- метод `change_species(new_species)` – създава **инстанс атрибут**, който засенчва класовия

**Примерен вход:**
```python
p1 = Person("Mira")
p2 = Person("Alex")
p2.change_species("Alien")
print(p1.info())  # Mira is a Human
print(p2.info())  # Alex is a Alien
```

---

### 9. ⏱️ `Timer`

Създай клас с:
- **private атрибут** `__seconds`
- `@property` `minutes` – връща времето в минути
- `@minutes.setter` – приема минути и преизчислява `__seconds`

**Примерен вход:**
```python
t = Timer()
t.minutes = 2
print(t.minutes)  # 2
print(t._Timer__seconds)  # 120
```

---

### 10. 📚 `Book`

Създай клас `Book` със:
- **обикновени атрибути** `title`, `author`, `pages`
- метод `__str__()` – връща `"Title by Author"`
- метод `__len__()` – връща `pages`
- използвай `getattr()` и `setattr()` за промяна на заглавието

**Примерен вход:**
```python
b = Book("Clean Code", "Robert C. Martin", 464)
print(str(b))      # Clean Code by Robert C. Martin
print(len(b))      # 464
setattr(b, "title", "Clean Architecture")
print(getattr(b, "title"))  # Clean Architecture
```

---

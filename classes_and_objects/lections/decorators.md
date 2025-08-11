# 🐍 Урок: Декоратори в Python

## 📌 Какво е декоратор?
В Python **декоратор** е функция, която приема **друга функция** като аргумент, добавя ѝ допълнителна функционалност и връща нова функция.

Може да мислиш за декоратор като за **"обвивка"** около функция — без да променяме оригиналния ѝ код.

---

## ✨ Защо да използваме декоратори?
- ✅ Повторно използване на код  
- ✅ Разделяне на логиката от допълнителните проверки/логове  
- ✅ По-чист и поддържан код  

---

## 🏗️ Пример: Декоратор за логване
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Викане на функция: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Резултат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```
**Какво става тук?**
1. `@logger` казва: "Обвий функцията `add` с `logger`"
2. Всеки път, когато извикаме `add`, ще имаме логове преди и след изпълнението.

---

## ⚙️ Как работят декораторите стъпка по стъпка
1. Декораторът е функция, която връща нова функция (wrapper).
2. `@decorator_name` е съкратен запис на:
```python
add = logger(add)
```
3. `*args` и `**kwargs` гарантират, че wrapper може да приема всякакви аргументи.

---

## 🏷️ Декоратори с аргументи
Ако искаме декораторът да приема **собствени параметри**:
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```
Тук `repeat(3)` връща декоратор, който изпълнява функцията 3 пъти.

---

## 🔍 Запазване на информацията за оригиналната функция
За да не се губи името и документацията:
```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```
`@wraps(func)` пази метаданните (име, docstring и т.н.).

---

# 🧠 Задачи за упражнение

---

## 🗂️ Задача 1: `execution_time.py`
**Описание:**
Напиши декоратор `measure_time`, който измерва и отпечатва колко време е отнело изпълнението на функцията.

**Пример:**
```python
@measure_time
def slow_function():
    import time
    time.sleep(2)
    return "Done"

slow_function()
# Изход:
# Executed slow_function in 2.00 seconds
```

---

## 🗂️ Задача 2: `authorize.py`
**Описание:**
Създай декоратор `requires_login`, който приема параметър `user_logged_in` (булев).  
Ако потребителят не е логнат, функцията да не се изпълнява.

**Пример:**
```python
@requires_login(user_logged_in=True)
def view_profile():
    print("Profile page")

view_profile()
```

---

## 🗂️ Задача 3: `cache.py`
**Описание:**
Напиши декоратор `cache_results`, който кешира резултатите от функцията (по аргументи), така че при повторно извикване със същите аргументи да не изчислява отново.

**Пример:**
```python
@cache_results
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 🗂️ Задача 4: `validate_args.py`
**Описание:**
Напиши декоратор `validate_positive`, който проверява дали всички числови аргументи са положителни.  
Ако някой е отрицателен — вдигни `ValueError`.

**Пример:**
```python
@validate_positive
def multiply(a, b):
    return a * b

multiply(3, 4)   # ОК
multiply(-2, 5)  # Грешка
```

---

## 🗂️ Задача 5: `retry.py`
**Описание:**
Създай декоратор `retry(times)`, който при грешка автоматично опитва да изпълни функцията още `times` пъти.

**Пример:**
```python
@retry(3)
def unstable():
    import random
    if random.random() < 0.7:
        raise Exception("Random fail!")
    print("Success!")

unstable()
```

---

📝 **Съвети:**
- Ползвай `functools.wraps` за да пазиш информация за оригиналната функция  
- Ползвай `*args, **kwargs` за гъвкавост  
- Можеш да комбинираш декоратори, като ги подредиш един над друг

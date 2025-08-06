# 🧠 Урок: Encapsulation, Name Mangling, Атрибути и Вградени функции

## 🔹 1. Какво е Encapsulation (Капсулация)

**Капсулацията** е OOP принцип, който скрива вътрешната реализация на обектите.  
Целта ѝ е да защити вътрешните данни, така че да не могат да бъдат достъпвани директно отвън.

В Python няма строга капсулация (както в Java/C#), но се използват **конвенции и техники**:

| Тип достъп | Синтаксис | Описание |
|------------|-----------|----------|
| Public     | `self.name`  | Достъпно отвсякъде |
| Protected  | `self._name` | По конвенция: "вътрешно" използване |
| Private    | `self.__name`| Скриване чрез *name mangling* |

---

## 🔹 2. Name Mangling на променлива

При използване на **__име (две долни черти)**, Python променя името, за да не може да се достъпи директно отвън. Това е **name mangling**.

```python
class SecretBox:
    def __init__(self):
        self.__code = "1234"  # private

box = SecretBox()

# print(box.__code)  ❌ Грешка: няма такъв атрибут
print(box._SecretBox__code)  # ✅ Name mangling
```

## 🔹 3. Name Mangling на метод

Същото важи и за методи:

```python
class Safe:
    def __init__(self):
        self.__lock_code = "0000"
    
    def __unlock(self):
        print("Unlocked!")

safe = Safe()

# safe.__unlock() ❌ AttributeError
safe._Safe__unlock()  # ✅ Работи
```

➡️ Полезно е, когато не искаш методи или данни да бъдат лесно достъпни от потребителя.

## 🔹 4. Built-in функции за атрибути

Python предоставя вградени функции за работа с атрибути:

| Функция                     | Описание                        |
|-----------------------------|----------------------------------|
| `getattr(obj, name)`        | Връща стойност на атрибут       |
| `setattr(obj, name, value)` | Присвоява стойност             |
| `hasattr(obj, name)`        | Проверява дали съществува       |
| `delattr(obj, name)`        | Изтрива атрибут                  |


```python
class User:
    def __init__(self):
        self.username = "admin"

u = User()
print(getattr(u, "username"))     # admin
setattr(u, "username", "guest")   # променя стойността
print(hasattr(u, "username"))     # True
delattr(u, "username")
```

## 🔹 5. Class Attributes vs Instance Attributes

Инстанс атрибути се дефинират чрез self – те са индивидуални за всеки обект.
Клас атрибути са споделени от всички обекти.

```python
class Dog:
    species = "Canine"  # Клас атрибут

    def __init__(self, name):
        self.name = name  # Инстанс атрибут

d1 = Dog("Rex")
d2 = Dog("Bella")

print(d1.species)  # Canine
print(d2.species)  # Canine

Dog.species = "Wolf"
print(d1.species)  # Wolf (защото species e променен за класа)
```

| Атрибут       | Ниво    | Споделен? | Пример                    |
| ------------- | ------- | --------- | ------------------------- |
| `self.name`   | инстанс | ❌ Не      | Име на конкретно куче     |
| `Dog.species` | класов  | ✅ Да      | Всички кучета са "Canine" |


## ✍️ Задачи за упражнения
# ✅ Основни задачи
# 🔸 Задача 1

Създай клас Account, който има private атрибут __balance. Добави методи deposit(amount) и get_balance().

# 🔸 Задача 2

Създай клас User с private метод __display(), който принтира "Hello". Извикай метода чрез name mangling.

# 🔸 Задача 3

Създай клас Car с protected атрибут _engine. Добави метод start() и принтирай "Engine started".

# 🔸 Задача 4

Създай клас Settings с атрибут theme. Използвай getattr, setattr и hasattr, за да достъпиш, промениш и провериш theme.

# 🔸 Задача 5

Създай клас Person с инстанс атрибут name и клас атрибут species = "Human". Създай няколко обекта и покажи как species е споделен.

## 🔥 По-трудни задачи
# 🔸 Задача 6

Създай клас Vault със secret code, който е private. Напиши метод __verify(code), който връща True ако кодът е верен. Извикай метода чрез name mangling.

# 🔸 Задача 7

Създай клас Robot с метод __compute() и атрибут __power_level. Достъпи и двете от външен код чрез name mangling.

# 🔸 Задача 8

Създай клас Logger, който има метод log() и използва setattr() за да добавя нови динамични атрибути (напр. log level, timestamp и т.н.).

# 🔸 Задача 9

Създай клас Student, в който се пази списък от всички студенти като клас атрибут. При създаване на обект, студентът се добавя в този списък. Напиши метод, който връща броя на студентите.

# 🔸 Задача 10

Създай клас Session с __token (private), и методи get_token() и __refresh_token(). Извикай метода чрез name mangling и демонстрирай капсулация.

## 📌 Обобщение

Encapsulation = контрол върху достъпа до вътрешни данни.

Name mangling = Python механизъм за "преименуване" на private методи/атрибути.

Клас атрибути = споделени между обектите.

Инстанс атрибути = уникални за всеки обект.

Вградени функции като getattr() и setattr() дават гъвкавост при работа с обекти.
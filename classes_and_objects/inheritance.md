# 📝 Python OOP – Наследяване (Inheritance)

## 🔹 Какво е наследяване?

**Наследяване (Inheritance)** позволява на един клас (child/subclass) да използва атрибутите и методите на друг клас (parent/superclass).

Например:  
- **Клас Parent (Родител)** = обща логика (напр. човек)  
- **Клас Child (Дете)** = специализация (напр. студент) с допълнителни функционалности

---

## ✅ Защо е важно?

- Премахва дублирането на код  
- Позволява повторно използване на вече създадената логика  
- Прави кода по-четим, модулен и разширяем

---

## 🔹 Пример за наследяване

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

# Тестване
student = Student("Anna")
student.greet()   # Hello, I am Anna
student.study()   # Anna is studying.
```

## 🔹 super() метод

- Използва се за извикване на методите на родителския клас, най-често в __init__ за инициализация.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Тестване
manager = Manager("George", 5000, "IT")
print(manager.name)        # George
print(manager.department)  # IT
```

## 🔹 Видове наследяване в Python

**Single Inheritance (Единично)** – една йерархия

**Multilevel Inheritance (Многостепенно)** – дете -> родител -> прародител

**Multiple Inheritance (Множествено)** – дете с много родители

**Hierarchical Inheritance (Йерархично)** – много деца от един родител

**Hybrid Inheritance (Хибридно)** – комбинация от горните


## Задачи за упражнения

- ✅ Задача 1 – Single Inheritance
Създай клас Animal с метод eat(), който принтира "eating...".
Създай клас Dog, който наследява Animal и има метод bark(), който принтира "barking...".
Създай обект на Dog и извикай двата метода.

- ✅ Задача 2 – Multilevel Inheritance
Създай клас Vehicle с метод move(), който принтира "moving...".
Създай клас Car, който наследява Vehicle и има метод drive(), който принтира "driving...".
Създай клас SportsCar, който наследява Car и има метод race(), който принтира "racing...".
Създай обект на SportsCar и извикай трите метода.

- ✅ Задача 3 – Multiple Inheritance
Създай клас Mother с метод cook(), който принтира "cooking...".
Създай клас Father с метод work(), който принтира "working...".
Създай клас Child, който наследява и двата класа и има метод play(), който принтира "playing...".
Създай обект на Child и извикай трите метода.

- ✅ Задача 4 – Hierarchical Inheritance
Създай клас Shape с метод draw(), който принтира "drawing shape...".
Създай два класа Circle и Square, които наследяват Shape.
Circle има метод draw_circle(), който принтира "drawing circle...", а Square има метод draw_square(), който принтира "drawing square...".
Създай обект на Circle и на Square и извикай всички подходящи методи.

- ✅ Задача 5 – super() използване
Създай клас Person с атрибут name.
Създай клас Student, който наследява Person и има допълнителен атрибут student_id.
Използвай super() за инициализация. Добави метод, който принтира "{name}'s ID is {student_id}".

- ✅ Задача 6 – Bank Example
Създай клас BankAccount с атрибут balance и метод check_balance(), който връща текущия баланс.
Създай клас SavingsAccount, който наследява BankAccount и има метод add_interest(rate), който увеличава баланса с процентното оскъпяване.

- ✅ Задача 7 – Employees
Създай клас Employee с атрибути name и salary.
Създай клас Developer, който наследява Employee и има допълнителен атрибут programming_language.
Добави метод code(), който принтира "{name} is coding in {programming_language}."

- ✅ Задача 8 – Mixins (за по-напреднали)
Създай клас Vehicle с атрибут position.
Създай миксин клас RadioMixin с метод play_radio(station), който принтира "Playing {station}".
Създай клас Car, който наследява Vehicle и използва RadioMixin.
Създай обект и извикай метода за радио.

## 📌 Обобщение

Наследяването е основна концепция в ООП, която позволява структуриране, повторно използване на код и разширяване на функционалност без промяна на вече съществуващи класове. Тренирай всички видове, за да преминеш към интерфейси, абстрактни класове и дизайн модели.

## 🔹 Mixins

## ✅ Какво е Mixin?

🔹 **Mixin** е специален вид клас, който се използва за добавяне на **допълнителна функционалност** към други класове.

- Не е предназначен да се използва самостоятелно.  
- **"Mix in"** означава *смесване на свойства и методи* в други класове.

### 📌 Характеристики на Mixin класовете:

✔️ Имат **методи**, но обикновено **нямат свои собствени данни (атрибути)**  
✔️ **Не могат да бъдат инстанцирани директно**  
✔️ Използват се чрез **множествено наследяване**, за да добавят функционалност към основния клас  
✔️ Осигуряват **по-добра повторна употреба на кода**

---

## 🔹 Пример: Mixin

```python
class RadioMixin:
    def play_song_on_station(self, station_frequency):
        return f"Playing song on radio frequency {station_frequency}"

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle, RadioMixin):
    pass

class Clock(RadioMixin):
    pass

car = Car("Toyota")
print(car.play_song_on_station(95.0))   # Playing song on radio frequency 95.0

clock = Clock()
print(clock.play_song_on_station(101.1)) # Playing song on radio frequency 101.1
```

## 🔍 Какво става тук?
RadioMixin съдържа метод, но няма собствени атрибути.

Класът Car наследява както от Vehicle, така и от RadioMixin, за да получи радио функционалност.

Класът Clock също наследява RadioMixin, за да ползва метода play_song_on_station.

## ✅ Защо да използваме Mixins?
🔹 За да добавим специфична функционалност към много класове, без да дублираме код
🔹 За да поддържаме кода чист и модулен
🔹 За да избегнем сложността на дълбоките йерархии при множествено наследяване

🔹 Пример с пояснение
Ако имаш много различни класове (Car, Clock, Phone), но всички трябва да имат възможност за пускане на радио, не е нужно да пишеш отделен метод във всеки клас. Създаваш RadioMixin и просто го наследяваш там, където е нужно.

## 📝 Задачи за упражнения (Mixins)
## ✅ Задача 1
Създай клас LoggerMixin, който има метод log(message), който принтира:
[LOG]: {message}

Създай клас User с атрибут name. Направи User да наследява и от LoggerMixin. Създай обект и извикай log.

## ✅ Задача 2
Създай Mixin клас FlyMixin, който има метод fly() връщащ "Flying...". Създай клас Bird, който наследява FlyMixin, и тествай метода.

## ✅ Задача 3
Създай Mixin клас SwimMixin с метод swim() връщащ "Swimming...".
Създай клас Duck, който наследява и от SwimMixin, и от FlyMixin (от предходната задача), и извикай и двата метода.

## ✅ Задача 4
Създай TalkMixin с метод talk() връщащ "Talking...". Направи клас Robot, който наследява от него, и тествай.

## ✅ Задача 5
Създай MoveMixin с метод move() връщащ "Moving...". Направи клас Vehicle с атрибут brand и клас Bike, който наследява от Vehicle и MoveMixin. Създай Bike и извикай move.

## ✅ Задача 6
Създай Mixin клас ChargeMixin с метод charge() връщащ "Charging battery...". Създай клас Phone, който наследява от ChargeMixin, и извикай метода.

## ✅ Задача 7
Създай клас Person с атрибут name и клас SpeakerMixin с метод speak() връщащ "Speaking...". Направи клас Teacher, който наследява и от двата, и тествай speak().

## ✅ Задача 8
Създай Mixin WriteMixin с метод write() връщащ "Writing...". Създай клас Author, който използва този миксин и има атрибут books. Тествай метода write() за Author.

## 📌 Обобщение
Mixins са мощен инструмент за разширяване на функционалността без сложни йерархии. Използвай ги, когато много класове трябва да споделят едни и същи действия, без да се дублира код.
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
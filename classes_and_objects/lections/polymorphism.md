
# Урок: Полиморфизъм в обектно-ориентираното програмиране (Python)

## Въведение

Полиморфизмът е един от основните принципи на обектно-ориентираното програмиране (ООП). 
Думата идва от гръцки: *poly* – „много“ и *morph* – „форма“. В програмирането това означава, 
че един и същи метод или операция може да има различно поведение в зависимост от обекта, върху който се прилага.

Пример: операторът `+` в Python може да събира както числа, така и да конкатенира стрингове.  
Това е форма на полиморфизъм.


## Видове полиморфизъм

1. **Полиморфизъм чрез наследяване (override)**  
   Когато клас наследи друг клас и презапише (override-не) негов метод, но запази същото име и интерфейс.

2. **Полиморфизъм чрез интерфейси/абстрактни класове**  
   Различни класове могат да имплементират един и същ метод по различен начин.

3. **Duck Typing (динамичен полиморфизъм)**  
   В Python често говорим за *duck typing*: „Ако изглежда като патица и квака като патица – то е патица.“  
   Тоест не е важно от кой клас е даден обект, а дали притежава необходимия метод/атрибут.


## Пример 1: Полиморфизъм чрез наследяване

```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.make_sound())
```

---

## Пример 2: Duck Typing

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I can imitate a duck!"

def make_it_quack(obj):
    print(obj.quack())

make_it_quack(Duck())
make_it_quack(Person())
```

---

## Пример 3: Полиморфизъм чрез абстрактни класове

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.area())
```

---

## Задачи за упражнение

### Задача 1
Създайте клас `Vehicle` с метод `move()`. Създайте класове `Car` и `Plane`, които наследяват `Vehicle` и реализират собствени версии на `move()`.

### Задача 2
Направете функция `animal_sound(animal)`, която приема обект и извиква неговия метод `make_sound()`. Тествайте я с класове `Dog`, `Cat`, `Cow`.

### Задача 3
Използвайки `abc.ABC`, създайте абстрактен клас `Shape` с метод `perimeter()`. Имплементирайте го в класове `Square` и `Triangle`.

### Задача 4
Направете клас `Employee` с метод `calculate_salary()`. Наследете го в `Manager` и `Developer`, като всеки има различна формула за изчисление на заплатата.

### Задача 5
Направете клас `Printer`, който има метод `print_document()`. Създайте два различни типа принтери (`LaserPrinter` и `InkjetPrinter`), които отпечатват по различен начин.

### Задача 6
Създайте функция `start_engine(vehicle)`, която може да стартира двигател на всяко превозно средство (`Car`, `Motorcycle`, `Boat`), без да се интересува от класа.

### Задача 7
Създайте програма, която приема списък от обекти (`Dog`, `Cat`, `Bird`) и за всеки извиква метод `make_sound()`. Добавете нов клас `Fish`, който няма `make_sound()`, и се уверете, че програмата може да обработи това чрез проверка с `hasattr()`.

---

## Заключение

Полиморфизмът е мощна концепция, която прави кода:
- По-гъвкав;
- По-разширяем;
- По-четим.

Той позволява писането на общи функции, които работят с различни типове обекти.  
В Python особено силно се проявява чрез *duck typing* и наследяване.

# 🏆 10 Задачи за Полиморфизъм (Над средно ниво)

---

## 📌 Задача 1: Payment System

**Структура:**
```
payment_system/
├── payment.py
├── credit_card.py
├── paypal.py
├── bank_transfer.py
└── main.py
```

**Описание:**
- `Payment`: базов клас с метод `process(amount)`
- `CreditCardPayment`: наследява `Payment`, метод `process()` → "Processing credit card payment of {amount}"
- `PayPalPayment`: наследява `Payment`, метод `process()` → "Processing PayPal payment of {amount}"
- `BankTransferPayment`: наследява `Payment`, метод `process()` → "Processing bank transfer of {amount}"

**main.py**
```python
from credit_card import CreditCardPayment
from paypal import PayPalPayment
from bank_transfer import BankTransferPayment

payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for p in payments:
    print(p.process(100))
```
---

## 📌 Задача 2: Animal Sounds

**Структура:**
```
animal_sounds/
├── animal.py
├── dog.py
├── cat.py
├── cow.py
└── main.py
```

**Описание:**
- `Animal`: базов клас с метод `make_sound()`
- `Dog`: връща "Woof!"
- `Cat`: връща "Meow!"
- `Cow`: връща "Moo!"

**main.py**
```python
from dog import Dog
from cat import Cat
from cow import Cow

animals = [Dog(), Cat(), Cow()]
for a in animals:
    print(a.make_sound())
```
---

## 📌 Задача 3: Document Export

**Структура:**
```
document_export/
├── document.py
├── pdf_exporter.py
├── word_exporter.py
├── text_exporter.py
└── main.py
```

**Описание:**
- `DocumentExporter`: базов клас с метод `export(content)`
- `PDFExporter`: връща "Exporting {content} to PDF"
- `WordExporter`: връща "Exporting {content} to Word"
- `TextExporter`: връща "Exporting {content} to TXT"

**main.py**
```python
from pdf_exporter import PDFExporter
from word_exporter import WordExporter
from text_exporter import TextExporter

exporters = [PDFExporter(), WordExporter(), TextExporter()]
for e in exporters:
    print(e.export("Hello World"))
```
---

## 📌 Задача 4: Shape Areas

**Структура:**
```
shapes/
├── shape.py
├── circle.py
├── rectangle.py
├── triangle.py
└── main.py
```

**Описание:**
- `Shape`: базов клас с метод `area()`
- `Circle`: изчислява площ: π * r^2
- `Rectangle`: изчислява площ: width * height
- `Triangle`: изчислява площ: 0.5 * base * height

**main.py**
```python
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
for s in shapes:
    print(s.area())
```
---

## 📌 Задача 5: Messaging System

**Структура:**
```
messaging/
├── message.py
├── email.py
├── sms.py
├── push_notification.py
└── main.py
```

**Описание:**
- `Message`: базов клас с метод `send(msg)`
- `Email`: връща "Sending email: {msg}"
- `SMS`: връща "Sending SMS: {msg}"
- `PushNotification`: връща "Sending push notification: {msg}"

**main.py**
```python
from email import Email
from sms import SMS
from push_notification import PushNotification

messages = [Email(), SMS(), PushNotification()]
for m in messages:
    print(m.send("Hello!"))
```
---

## 📌 Задача 6: Employee Payroll

**Структура:**
```
payroll/
├── employee.py
├── developer.py
├── manager.py
├── intern.py
└── main.py
```

**Описание:**
- `Employee`: базов клас с метод `calculate_salary()`
- `Developer`: базова заплата + бонус за проект
- `Manager`: базова заплата + бонус за екип
- `Intern`: фиксирана малка заплата

**main.py**
```python
from developer import Developer
from manager import Manager
from intern import Intern

employees = [Developer(2000, 500), Manager(3000, 1000), Intern(800)]
for e in employees:
    print(e.calculate_salary())
```
---

## 📌 Задача 7: Transport Vehicles

**Структура:**
```
transport/
├── vehicle.py
├── car.py
├── bike.py
├── bus.py
└── main.py
```

**Описание:**
- `Vehicle`: базов клас с метод `travel_time(distance)`
- `Car`: връща `distance / speed`
- `Bike`: връща `distance / speed`
- `Bus`: връща `distance / speed`

**main.py**
```python
from car import Car
from bike import Bike
from bus import Bus

vehicles = [Car(100), Bike(20), Bus(60)]
for v in vehicles:
    print(v.travel_time(120))
```
---

## 📌 Задача 8: Online Store Discounts

**Структура:**
```
store/
├── discount.py
├── percentage_discount.py
├── fixed_discount.py
├── no_discount.py
└── main.py
```

**Описание:**
- `Discount`: базов клас с метод `apply(price)`
- `PercentageDiscount`: прилага % намаление
- `FixedDiscount`: прилага фиксирано намаление
- `NoDiscount`: връща оригиналната цена

**main.py**
```python
from percentage_discount import PercentageDiscount
from fixed_discount import FixedDiscount
from no_discount import NoDiscount

discounts = [PercentageDiscount(10), FixedDiscount(5), NoDiscount()]
for d in discounts:
    print(d.apply(100))
```
---

## 📌 Задача 9: Game Characters

**Структура:**
```
game/
├── character.py
├── warrior.py
├── mage.py
├── archer.py
└── main.py
```

**Описание:**
- `Character`: базов клас с метод `attack()`
- `Warrior`: връща "Swing sword"
- `Mage`: връща "Cast spell"
- `Archer`: връща "Shoot arrow"

**main.py**
```python
from warrior import Warrior
from mage import Mage
from archer import Archer

chars = [Warrior(), Mage(), Archer()]
for c in chars:
    print(c.attack())
```
---

## 📌 Задача 10: File Readers

**Структура:**
```
file_readers/
├── reader.py
├── csv_reader.py
├── json_reader.py
├── xml_reader.py
└── main.py
```

**Описание:**
- `Reader`: базов клас с метод `read(file)`
- `CSVReader`: връща "Reading CSV file {file}"
- `JSONReader`: връща "Reading JSON file {file}"
- `XMLReader`: връща "Reading XML file {file}"

**main.py**
```python
from csv_reader import CSVReader
from json_reader import JSONReader
from xml_reader import XMLReader

files = [CSVReader(), JSONReader(), XMLReader()]
for f in files:
    print(f.read("data"))
```
---

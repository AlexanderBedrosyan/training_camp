# 📝 Задачи – Класове, Обекти, Наследяване, Mixins


### 🔹 Задача 1
Създай клас `Book` с атрибути `title` и `author`. Добави метод `get_info()`, който връща:  
`"{title} by {author}"`. Създай обект и извикай метода.

---

### 🔹 Задача 2
Създай клас `Animal` с метод `make_sound()`, връщащ "Some sound".  
Създай клас `Cat`, който наследява `Animal` и override-ва `make_sound()` да връща "Meow".

---

### 🔹 Задача 3
Създай клас `Employee` с атрибут `name` и метод `work()`, връщащ "{name} is working".  
Създай клас `Manager`, наследяващ `Employee`, и добави метод `manage()` връщащ "{name} is managing".

---

### 🔹 Задача 4
Създай Mixin клас `LogMixin` с метод `log(message)`, който принтира:  
`[LOG]: {message}`.  
Създай клас `App` с атрибут `name`, наследяващ `LogMixin`, и извикай log с името.

---

### 🔹 Задача 5
Създай клас `Vehicle` с атрибут `speed` и метод `move()` връщащ "Moving at {speed} km/h".  
Създай клас `Plane`, наследяващ `Vehicle`, и добави метод `fly()` връщащ "Flying".

---

### 🔹 Задача 6
Създай Mixin `DriveMixin` с метод `drive()` връщащ "Driving...".  
Създай клас `Truck` с атрибут `weight`, наследяващ `DriveMixin`, и тествай drive().

---

### 🔹 Задача 7
Създай клас `Person` с атрибути `name` и `age`. Добави метод `birthday()`, който увеличава възрастта с 1 и връща новата възраст.

---

### 🔹 Задача 8
Създай клас `Shape` с метод `area()` връщащ 0.  
Създай клас `Rectangle`, наследяващ `Shape`, с атрибути `width` и `height`, и override-вай `area()` да връща `width * height`.

---

## 🔥 Висока трудност (по-заплетени, с множествено наследяване и mixins)

### 🔹 Задача 9
Създай клас `Course` с атрибути `name` и `students` (списък). Добави метод `add_student(student_name)`, който добавя студент, и метод `get_students_count()`, който връща броя на студентите.  
Създай клас `ProgrammingCourse`, наследяващ `Course`, и добави метод `add_language(language)`, който добавя език за курса в нов атрибут `languages` (списък).

---

### 🔹 Задача 10
Създай клас `Device` с атрибут `status="off"`. Добави метод `toggle()` сменящ между "on" и "off".  
Създай клас `Smartphone`, наследяващ `Device`, и добави метод `call(number)` връщащ "Calling {number}".  
Създай клас `SmartWatch`, наследяващ `Device`, с метод `measure_heart_rate()` връщащ "Heart rate measured".

---

### 🔹 Задача 11
Създай два Mixin класа:
- `PaymentMixin` с метод `pay(amount)` връщащ "Paid {amount} USD"
- `DiscountMixin` с метод `apply_discount(price, discount)`, връщащ цената след намаление

Създай клас `OnlineOrder`, който използва и двата mixin-а и има атрибут `order_id`. Тествай pay и apply_discount.

---

### 🔹 Задача 12
Създай клас `User` с атрибути `username` и `email`. Добави метод `change_email(new_email)`, който сменя имейла само ако съдържа "@".  
Създай клас `Admin`, наследяващ `User`, който добавя метод `reset_password()` връщащ "Password reset for {username}".

---

### 🔹 Задача 13
Създай клас `LibraryItem` с атрибути `title` и `year`.  
Създай класове `Book` и `Magazine`, които наследяват `LibraryItem`.  
`Book` има атрибут `author`, а `Magazine` – `issue_number`.  
Създай клас `DigitalMagazine`, наследяващ `Magazine`, с метод `download()` връщащ "Downloading {title} issue {issue_number}".

---

### 🔹 Задача 14
Създай Mixin `EncryptMixin` с метод `encrypt(data)`, връщащ "Encrypted {data}".  
Създай клас `File`, който има `filename`, и клас `SecureFile`, който наследява `File` и използва `EncryptMixin`.  
Добави метод `secure_save()` в `SecureFile`, който връща "Saving {encrypted filename}".

---

### 🔹 Задача 15
Създай клас `Account` с атрибут `balance`. Добави метод `deposit(amount)` и метод `withdraw(amount)` (ако няма достатъчно средства, връща "Insufficient funds").  
Създай клас `PremiumAccount`, наследяващ `Account`, който override-ва `withdraw(amount)`, за да позволява овърдрафт до -500.

---

### 🔹 Задача 16
Създай клас `Instrument` с метод `play()` връщащ "Playing music".  
Създай клас `Guitar`, наследяващ `Instrument`, с метод `tune()` връщащ "Tuning guitar".  
Създай клас `ElectricMixin` с метод `plug_in()` връщащ "Plugged in electric instrument".  
Създай клас `ElectricGuitar`, който наследява `Guitar` и използва `ElectricMixin`, добави метод `distortion()` връщащ "Distortion effect ON".

---

## 📌 Инструкции

- Реши задачите в отделни Python файлове или един общ Jupyter notebook.  
- Тествай всеки клас, метод, наследяване и mixin с реални примери.  
- Обърни внимание на използването на **super()**, множествено наследяване и миксини.

---


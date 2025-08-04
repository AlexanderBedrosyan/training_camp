## 🧠 Задачи: Напреднало ниво с Класове, Атрибути и OOP концепции

> 🔁 Всяка задача изисква **няколко Python файла**, които да си комуникират помежду си.
> Използвай **encapsulation**, **mixins**, `getattr()`, `setattr()` и класови атрибути, когато е приложимо.

---

### 🧩 Задача 1: `vehicle.py` + `engine.py`

Създай два файла:

#### `vehicle.py`:
- Клас `Vehicle` със:
  - **protected атрибут** `_type`
  - метод `start()`, който отпечатва `"Starting {type}"`

#### `engine.py`:
- Клас `Engine` с:
  - **private атрибут** `__power`
  - `@property` за достъп до него

Свържи двата чрез нов клас `Car(Vehicle, Engine)`, който стартира двигателя.

**Примерен вход:**
```python
from vehicle import Car

car = Car("sedan", 180)
car.start()          # Starting sedan
print(car.power)     # 180
```

---

### 🔐 Задача 2: `user.py` + `access.py`

#### `user.py`:
- Клас `User` с:
  - **private атрибут** `__password`
  - метод `check_password(pw)`

#### `access.py`:
- Клас `AdminMixin` с метод `reset_password(obj, new_pw)`, който използва name mangling за достъп

Създай клас `Admin(User, AdminMixin)`

**Примерен вход:**
```python
admin = Admin("ivan", "1234")
print(admin.check_password("1234"))  # True
admin.reset_password(admin, "5678")
print(admin.check_password("5678"))  # True
```

---

### 🧬 Задача 3: `base.py` + `bio.py`

#### `base.py`:
- Клас `Person` с атрибути `name`, `age`

#### `bio.py`:
- Клас `BioMixin` с метод `bio()` → `"{name}, age {age}"`

Създай `Student(Person, BioMixin)`

**Примерен вход:**
```python
s = Student("Maria", 20)
print(s.bio())  # Maria, age 20
```

---

### ⚙️ Задача 4: `machine.py` + `tracker.py`

#### `machine.py`:
- Клас `Machine` с класов атрибут `machines_created`, който се увеличава при всяка нова машина

#### `tracker.py`:
- Клас `UsageTracker` с protected атрибут `_hours_used`

Създай клас `TrackedMachine(Machine, UsageTracker)`

**Примерен вход:**
```python
m1 = TrackedMachine(10)
m2 = TrackedMachine(25)
print(TrackedMachine.machines_created)  # 2
```

---

### 📁 Задача 5: `data.py` + `json_helper.py`

#### `data.py`:
- Клас `DataObject` със:
  - **private атрибут** `__data`
  - метод `get(key)`

#### `json_helper.py`:
- Mixin `JsonMixin` с метод `to_json()`, използвайки `getattr()` за динамично извличане на данни

**Примерен вход:**
```python
d = DataObject({"name": "Anna"})
print(d.get("name"))     # Anna
print(d.to_json())       # {"name": "Anna"}
```

---

### 🧑‍🔧 Задача 6: `employee.py` + `payment.py` + `log.py`

#### `employee.py`:
- Клас `Employee` с:
  - **protected атрибут** `_hours`
  - метод `work(hours)`

#### `payment.py`:
- Mixin `PaymentMixin` с метод `calculate_payment(rate)`

#### `log.py`:
- Mixin `LoggerMixin` с метод `log(msg)`

Създай `PayrollEmployee(Employee, PaymentMixin, LoggerMixin)`

**Примерен вход:**
```python
e = PayrollEmployee("Ivan")
e.work(10)
print(e.calculate_payment(20))  # 200
e.log("Payment calculated.")    # LOG: Payment calculated.
```

---

### 📡 Задача 7: `device.py` + `mixin_power.py`

#### `device.py`:
- Клас `Device` с:
  - **class атрибут** `devices_on = 0`
  - методи `power_on()` / `power_off()`

#### `mixin_power.py`:
- Mixin `PowerStatusMixin` с метод `status()`

Създай `SmartDevice(Device, PowerStatusMixin)`

**Примерен вход:**
```python
d1 = SmartDevice()
d1.power_on()
print(SmartDevice.devices_on)  # 1
print(d1.status())             # Powered ON
```

---

### 🧾 Задача 8: `order.py` + `discount.py`

#### `order.py`:
- Клас `Order` с:
  - **protected атрибут** `_total`
  - метод `add_item(price)`

#### `discount.py`:
- Mixin `DiscountMixin` с:
  - **class атрибут** `discount_rate = 0.1`
  - метод `apply_discount()`

Създай `DiscountOrder(Order, DiscountMixin)`

**Примерен вход:**
```python
o = DiscountOrder()
o.add_item(100)
print(o.apply_discount())  # 90.0
```

---

### 🔁 Задача 9: `storage.py` + `manager.py`

#### `storage.py`:
- Клас `Storage` със:
  - **private атрибут** `__items` (списък)
  - метод `add_item(item)`
  - `@property` `items` (само за четене)

#### `manager.py`:
- Mixin `RemoveMixin` с метод `remove_item(item)`

Създай `Inventory(Storage, RemoveMixin)`

**Примерен вход:**
```python
inv = Inventory()
inv.add_item("apple")
inv.add_item("banana")
inv.remove_item("apple")
print(inv.items)  # ['banana']
```

---

### 🛑 Задача 10: `secure_data.py` + `tools.py`

#### `secure_data.py`:
- Клас `SecureData` с:
  - **private атрибут** `__value`
  - метод `access(password)` – ако е вярна, връща стойността

#### `tools.py`:
- Mixin `AdminAccessMixin` с метод `force_access(obj)`, който използва name mangling, за да върне `__value` без парола

Създай `AdminData(SecureData, AdminAccessMixin)`

**Примерен вход:**
```python
data = AdminData("SECRET", "abc123")
print(data.access("wrong"))        # None
print(data.force_access(data))     # SECRET
```

---


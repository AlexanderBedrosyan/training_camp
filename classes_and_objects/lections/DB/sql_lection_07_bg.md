# SQL Лекция 7: Индекси — Пълно Ръководство за Ускоряване на Бази Данни

Добре дошли в седмата лекция по SQL!

В **Лекция 6** разгледахме индексите като трета тема заедно с JOIN и подзаявки. В тази лекция ще се фокусираме **само върху индексите** — ще ги разгледаме много по-задълбочено, с повече примери и аналогии, за да ги разберете напълно.

> **Защо е важна тази тема?**
> Индексите са едно от най-мощните инструменти за оптимизиране на бази данни. Правилно поставен индекс може да превърне заявка, която е работела **30 секунди**, в такава, която работи за **0.001 секунди**. Без индекси — реалните приложения просто не могат да работят при хиляди и милиони записи.

---

## Съдържание

| # | Тема |
|---|------|
| 1 | Аналогии от реалния живот — разбираме концепцията |
| 2 | Как работи индексът вътрешно (B-Tree) |
| 3 | Пълен скан (Full Table Scan) — проблемът |
| 4 | Clustered Index (Клъстеризиран) |
| 5 | Non-Clustered Index (Некклъстеризиран) |
| 6 | Видове индекси: Уникален, Съставен, Частичен, Покриващ |
| 7 | EXPLAIN QUERY PLAN — виждаме какво прави SQL |
| 8 | Цената на индексите — кога помагат и кога пречат |
| 9 | Задачи за упражнение |

---

## Подготовка: Тестова Схема

Ползваме същата схема като в Лекция 6. Изпълнете целия блок преди да продължите:

```sql
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS warehouses;

CREATE TABLE categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    NOT NULL UNIQUE
);

CREATE TABLE products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    price       REAL    NOT NULL CHECK (price >= 0),
    stock       INTEGER NOT NULL DEFAULT 0,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

CREATE TABLE warehouses (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    city     TEXT    NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE customers (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL,
    email      TEXT    UNIQUE NOT NULL,
    city       TEXT    NOT NULL,
    registered TEXT    NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    ordered_on  TEXT    NOT NULL,
    status      TEXT    NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending','shipped','delivered','cancelled')),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

CREATE TABLE order_items (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id   INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity   INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL    NOT NULL,
    FOREIGN KEY (order_id)   REFERENCES orders(id)   ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

INSERT INTO categories (name) VALUES
    ('Електроника'), ('Книги'), ('Дрехи'), ('Спорт'), ('Дом и Градина');

INSERT INTO products (name, price, stock, category_id) VALUES
    ('Лаптоп Dell XPS',         2199.99, 15,  1),
    ('Слушалки Sony WH-1000',    349.99, 42,  1),
    ('Безжична мишка Logitech',   59.99, 80,  1),
    ('Клавиатура Mechanical',    129.99, 35,  1),
    ('Монитор LG 27"',           699.99, 10,  1),
    ('SQL за начинаещи',          39.99, 55,  2),
    ('Python Crash Course',       44.99, 30,  2),
    ('Чист Код - Р. Мартин',      49.99, 20,  2),
    ('Тениска Памучна XL',        29.99, 100, 3),
    ('Яке Зимно',                149.99, 25,  3),
    ('Маратонки Nike Air',        189.99, 60,  4),
    ('Yoga Mat 6мм',              49.99, 45,  4),
    ('Гири 10кг Комплект',        89.99, 18,  4),
    ('Градинска Ножица',          24.99, 70,  5),
    ('Саксия Керамична',          19.99, 90,  5),
    ('Разширител USB-C',          34.99, 55,  NULL);

INSERT INTO warehouses (city, capacity) VALUES
    ('София', 5000), ('Пловдив', 3000), ('Варна', 2500);

INSERT INTO customers (first_name, last_name, email, city, registered) VALUES
    ('Мартина',   'Колева',    'martina@mail.bg',   'София',   '2022-03-15'),
    ('Стефан',    'Димов',     'stefan@mail.bg',    'Пловдив', '2021-07-20'),
    ('Галина',    'Пенева',    'galina@mail.bg',    'Варна',   '2023-01-10'),
    ('Борислав',  'Неделчев',  'borislav@mail.bg',  'София',   '2020-11-05'),
    ('Цветелина', 'Атанасова', 'cveta@mail.bg',     'Бургас',  '2023-09-22'),
    ('Радослав',  'Иванов',    'radoslav@mail.bg',  'София',   '2024-01-30'),
    ('Деница',    'Георгиева', 'denica@mail.bg',    'Пловдив', '2022-06-18'),
    ('Калоян',    'Тодоров',   'kaloyan@mail.bg',   'Варна',   '2021-12-01'),
    ('Ивета',     'Стоянова',  'iveta@mail.bg',     'София',   '2023-04-14'),
    ('Никола',    'Петров',    'nikola@mail.bg',    'Русе',    '2024-02-28');

INSERT INTO orders (customer_id, ordered_on, status) VALUES
    (1, '2024-01-10', 'delivered'),
    (1, '2024-03-05', 'shipped'),
    (2, '2024-01-15', 'delivered'),
    (3, '2024-02-20', 'pending'),
    (4, '2024-01-22', 'delivered'),
    (4, '2024-04-01', 'cancelled'),
    (6, '2024-03-18', 'shipped'),
    (7, '2024-02-14', 'delivered'),
    (8, '2024-04-10', 'pending'),
    (9, '2024-01-05', 'delivered'),
    (10,'2024-03-25', 'shipped');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1,  1,  1, 2199.99), (1,  3,  1,   59.99),
    (2,  2,  1,  349.99),
    (3,  6,  2,   39.99), (3,  7,  1,   44.99),
    (4,  12, 1,   49.99), (4,  13, 1,   89.99),
    (5,  1,  1, 2199.99), (5,  4,  1,  129.99), (5,  5,  1, 699.99),
    (6,  9,  3,   29.99),
    (7,  11, 1,  189.99),
    (8,  8,  1,   49.99), (8,  6,  1,   39.99),
    (9,  15, 2,   19.99),
    (10, 2,  1,  349.99), (10, 3,  2,   59.99),
    (11, 16, 1,   34.99);
```

---

---

# ЧАСТ 1: Аналогии от Реалния Живот

---

## 1.1 Проблемът без индекс — аналогия с библиотека

Представете си огромна библиотека с **1 000 000 книги**, но **без каталог** и без никакъв ред. Всички книги са наредени произволно на рафтовете.

Вие търсите книгата "SQL за начинаещи".

**Какво трябва да направите?**

```
Без каталог:
┌─────────────────────────────────────────────────────────────┐
│ Рафт 1:  Математика, История, Готварство, Романи, Ботаника  │
│ Рафт 2:  Физика, Детски книги, SQL, Бизнес, Музика          │ ← може тук
│ Рафт 3:  Поезия, Програмиране, Биология, Химия, Философия  │
│ ...      (999 994 повече книги)                              │
└─────────────────────────────────────────────────────────────┘
→ Трябва да проверите ВСЯКА книга докато намерите правилната!
→ Средно: 500 000 проверки
```

Точно това прави SQL без индекс — проверява **всеки ред** в таблицата. Това се нарича **Full Table Scan**.

---

**Сега си представете, че библиотеката има каталог** — азбучен указател, в който за всяка книга пише на кой рафт и кое място се намира:

```
Каталог по заглавие (индекс):
...
С: Системи за управление → Рафт 45, Място 3
   Сметаналарски речник  → Рафт 12, Място 7
   SQL за начинаещи      → Рафт 2,  Място 3  ← директно!
Т: Тригонометрия         → Рафт 78, Място 1
...
```

С каталога отивате **директно** на правилното място. Само 2-3 стъпки вместо 500 000!

> **Индексът в SQL = Каталогът в библиотеката**
> Той не съдържа самите данни, а **указател** към тях.

---

## 1.2 Втора аналогия — телефонен указател

Телефонният указател е сортиран **по фамилия**. Ако търсите "Петров" — отваряте на буква "П" и намирате за секунди.

Ако обаче търсите по **телефонен номер** (няма индекс по номер) — трябва да прегледате **всicial** записи.

```
Търсене по фамилия "Петров":  ← ИМА ИНДЕКС (телефонникът е сортиран)
→ О(log n) операции: директно на П-страницата

Търсене по номер "0888-123456": ← НЯМА ИНДЕКС по номер
→ О(n) операции: четете от страница 1 до края
```

**Урокът:** Индексът ускорява търсенето по **конкретни колони**. Таблица може да има много индекси — по различни колони, за различни типове търсения.

---

---

# ЧАСТ 2: Как Работи Индексът Вътрешно (B-Tree)

---

## 2.1 Структурата B-Tree (Балансирано Дърво)

Повечето индекси в SQL базите данни използват структура, наречена **B-Tree** (Balanced Tree — Балансирано Дърво).

> Не е нужно да помните детайлите на B-Tree наизуст. Важното е да разберете **защо е бързо**.

### Как изглежда B-Tree?

Представете си, че имаме индекс по колоната `price` в таблицата `products`:

```
                        B-Tree Индекс по PRICE
                        ═══════════════════════

                          ┌─────────┐
                          │  129.99 │    ← Корен (Root)
                          └────┬────┘
                    ┌──────────┴──────────┐
               ┌────┴────┐           ┌────┴────┐
               │  49.99  │           │  349.99 │    ← Вътрешни Възли
               └────┬────┘           └────┬────┘
          ┌─────────┴─────┐      ┌────────┴────────┐
     ┌────┴───┐       ┌───┴──┐  ┌┴──────┐     ┌────┴────┐
     │ 19.99  │       │ 59.99│  │189.99 │     │2199.99  │  ← Листа (Leaves)
     │ 24.99  │       │ 89.99│  │349.99 │     │ 699.99  │
     │ 29.99  │       │129.99│  │       │     │         │
     │ 34.99  │       │      │  │       │     │         │
     └────┬───┘       └───┬──┘  └┬──────┘     └────┬────┘
          │               │      │                  │
       Указатели към реалните редове в таблицата
       (row_id / page_number)
```

### Как се търси в B-Tree?

Нека да потърсим `price = 59.99`:

```
Стъпка 1: Коренът е 129.99
          59.99 < 129.99 → отиди ЛЯВО

Стъпка 2: Намираме 49.99
          59.99 > 49.99 → отиди ДЯСНО

Стъпка 3: Намираме листата: 59.99 → Ред #3 в таблицата!
          Само 3 стъпки вместо 16!
```

### Математиката зад скоростта

```
Таблица с N реда:

БЕЗ индекс (Full Scan):  N проверки
С B-Tree индекс:          log₂(N) проверки

Примери:
N = 1 000:       Full Scan = 1 000 стъпки     │  B-Tree =  10 стъпки
N = 1 000 000:   Full Scan = 1 000 000 стъпки │  B-Tree =  20 стъпки
N = 1 000 000 000: Full Scan = 1 млрд стъпки  │  B-Tree =  30 стъпки

Разликата: от МИЛИАРДИ стъпки до само 30!
```

> **Ключова поука:** При 1 милиард реда, B-Tree индексът е **33 000 000 пъти** по-бърз от Full Scan!

---

## 2.2 B-Tree и диапазонни заявки

B-Tree е особено ефективен при **диапазонни** заявки (`>`, `<`, `BETWEEN`, `LIKE 'abc%'`), защото листата са **свързани** помежду си:

```
Листа на B-Tree (свързан списък):

[19.99] ↔ [24.99] ↔ [29.99] ↔ [34.99] ↔ [39.99] ↔ [44.99] ↔ [49.99] ↔ [59.99] ↔ ...

Заявка: WHERE price BETWEEN 29.99 AND 59.99

Стъпка 1: Намери 29.99 с B-Tree (бързо: log n)
Стъпка 2: Следвай свързания списък надясно до 59.99
→ Резултат: [29.99, 34.99, 39.99, 44.99, 49.99, 59.99]
→ Само 6 стъпки + log(n) за намиране на старта!
```

---

---

# ЧАСТ 3: Full Table Scan — Проблемът

---

## 3.1 Какво е Full Table Scan?

**Full Table Scan** (пълен скан на таблицата) означава, че SQL двигателят чете **всеки ред** от таблицата, за да намери съвпадения с условието в `WHERE`.

```sql
-- Тази заявка БЕЗ индекс прави Full Table Scan
SELECT * FROM customers WHERE email = 'stefan@mail.bg';
```

```
Full Table Scan на customers (10 реда в нашия пример):

Ред 1: id=1, email='martina@mail.bg'   → 'martina' = 'stefan'? НЕ
Ред 2: id=2, email='stefan@mail.bg'    → 'stefan' = 'stefan'? ДА! → добавяме в резултата
Ред 3: id=3, email='galina@mail.bg'    → 'galina' = 'stefan'? НЕ
Ред 4: id=4, email='borislav@mail.bg'  → НЕ
Ред 5: id=5, email='cveta@mail.bg'     → НЕ
Ред 6: id=6, email='radoslav@mail.bg'  → НЕ
Ред 7: id=7, email='denica@mail.bg'    → НЕ
Ред 8: id=8, email='kaloyan@mail.bg'   → НЕ
Ред 9: id=9, email='iveta@mail.bg'     → НЕ
Ред 10: id=10, email='nikola@mail.bg'  → НЕ

→ Проверени редове: 10 (всички!)
```

При 10 реда е бързо. При **10 милиона реда** — е катастрофа.

---

## 3.2 Виждаме Full Table Scan с EXPLAIN

```sql
-- Проверяваме дали има индекс по email:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'stefan@mail.bg';
```

**Резултат (без индекс):**
```
QUERY PLAN
└── SCAN customers
```

`SCAN` = Full Table Scan = БАВНО при много данни.

```sql
-- Сега създаваме индекс:
CREATE INDEX idx_customers_email ON customers (email);

-- И проверяваме отново:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'stefan@mail.bg';
```

**Резултат (с индекс):**
```
QUERY PLAN
└── SEARCH customers USING INDEX idx_customers_email (email=?)
```

`SEARCH USING INDEX` = Търсене с индекс = БЪРЗО!

> **Правило:** `SCAN` е лошо при голяма таблица. `SEARCH USING INDEX` е добро.

---

---

# ЧАСТ 4: Clustered Index (Клъстеризиран Индекс)

---

## 4.1 Основна идея

**Clustered Index** е специален вид индекс, при който данните в таблицата са **физически наредени** по ключа на индекса. Това означава, че **индексът и данните са едно и също нещо** — не са разделени.

### Аналогия

Представете си речник (например речник на чуждите думи). Страниците на речника са наредени **по азбучен ред**. Самото подреждане **е** индексът — не е нужен отделен каталог. Просто отваряш на буква "С" и си вече близо до търсената дума.

```
Clustered Index (данните СА наредени по ключа):

Физически файл на диска:
┌──────────────────────────────────────────────────────────┐
│ Страница 1:  [id=1, Лаптоп, 2199.99]                    │
│              [id=2, Слушалки, 349.99]                    │
│              [id=3, Безжична мишка, 59.99]               │
│ Страница 2:  [id=4, Клавиатура, 129.99]                  │
│              [id=5, Монитор, 699.99]                     │
│              [id=6, SQL книга, 39.99]                    │
│ ...                                                       │
└──────────────────────────────────────────────────────────┘
Данните са наредени по id — индексът ОПРЕДЕЛЯ физическия ред!
```

---

## 4.2 PRIMARY KEY = Clustered Index

В SQLite (и в повечето СУБД) **PRIMARY KEY автоматично създава Clustered Index**.

```sql
CREATE TABLE products (
    id    INTEGER PRIMARY KEY,   -- ← автоматично CLUSTERED INDEX по id!
    name  TEXT,
    price REAL
);
```

Затова заявки по `id` са **изключително бързи**:

```sql
-- Тези заявки ползват Clustered Index (много бързи):
SELECT * FROM products WHERE id = 5;
SELECT * FROM products WHERE id BETWEEN 3 AND 8;
SELECT * FROM products ORDER BY id;

-- EXPLAIN QUERY PLAN показва:
-- SEARCH products USING INTEGER PRIMARY KEY (rowid=?)
```

---

## 4.3 Ограничения на Clustered Index

```
Clustered Index ПО ПРАВИЛО:

✓ Само ЕДИН на таблица
  (данните имат само един физически ред — не може да са наредени по два критерия едновременно)

✓ Обикновено е PRIMARY KEY

✓ Много ефективен за:
  - WHERE id = X           (точно търсене)
  - WHERE id BETWEEN 5 AND 10  (диапазон)
  - ORDER BY id            (вече наредено!)

✗ Не помага при:
  - WHERE email = '...'    (данните не са наредени по email)
  - WHERE price > 100      (данните не са наредени по price)
```

**Пример — кога clustered index помага и кога не:**

```sql
-- БЪРЗО — ползва Clustered Index (PRIMARY KEY по id):
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE id = 3;
-- Output: SEARCH products USING INTEGER PRIMARY KEY (rowid=?)

-- БАВНО — не ползва никакъв индекс (full scan):
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price > 100;
-- Output: SCAN products

-- Решение: добавяме Non-Clustered Index по price
CREATE INDEX idx_products_price ON products (price);

-- БЪРЗО отново:
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price > 100;
-- Output: SEARCH products USING INDEX idx_products_price (price>?)
```

---

---

# ЧАСТ 5: Non-Clustered Index (Некклъстеризиран Индекс)

---

## 5.1 Основна идея

**Non-Clustered Index** е **отделна структура** (B-Tree), която живее извън основната таблица. Тя съдържа:
1. Копие на стойностите от индексираната колона (сортирани)
2. Указател към реалния ред в таблицата (row pointer)

### Аналогия

Представете си, че имате книга с **азбучен указател в края** (index page). Указателят не съдържа самия текст — само ключова дума и номер на страница. Когато намерите думата в указателя, **скачате** на посочената страница.

```
Non-Clustered Index по price (отделна структура):

  ИНДЕКСНА B-TREE               РЕАЛНА ТАБЛИЦА
  ════════════════════          ════════════════════════════════
  price   │ → row_ptr           id │ name              │ price
  ──────────────────           ────┼───────────────────┼───────
  19.99   │ ──────────────────► 15 │ Саксия Керамична  │ 19.99
  24.99   │ ──────────────────► 14 │ Градинска Ножица  │ 24.99
  29.99   │ ──────────────────►  9 │ Тениска Памучна   │ 29.99
  34.99   │ ──────────────────► 16 │ Разширител USB-C  │ 34.99
  39.99   │ ──────────────────►  6 │ SQL за начинаещи  │ 39.99
  44.99   │ ──────────────────►  7 │ Python Crash Crs. │ 44.99
  49.99   │ ──────────────────►  8 │ Чист Код          │ 49.99
  49.99   │ ──────────────────► 12 │ Yoga Mat          │ 49.99
  59.99   │ ──────────────────►  3 │ Безжична мишка    │ 59.99
  89.99   │ ──────────────────► 13 │ Гири 10кг         │ 89.99
  129.99  │ ──────────────────►  4 │ Клавиатура Mech.  │ 129.99
  149.99  │ ──────────────────► 10 │ Яке Зимно         │ 149.99
  189.99  │ ──────────────────► 11 │ Маратонки Nike    │ 189.99
  349.99  │ ──────────────────►  2 │ Слушалки Sony     │ 349.99
  699.99  │ ──────────────────►  5 │ Монитор LG 27"    │ 699.99
  2199.99 │ ──────────────────►  1 │ Лаптоп Dell XPS   │2199.99

  Стъпка 1: Търси в индекса (бързо, B-tree)
  Стъпка 2: Скочи до реда в таблицата (row pointer)
  Общо: 2 скока вместо full scan!
```

---

## 5.2 Процесът на търсене стъпка по стъпка

```sql
SELECT name, price, stock
FROM products
WHERE price = 49.99;
```

**Без индекс:**
```
Стъпка 1: Прочети ред 1 → price=2199.99 → не е 49.99
Стъпка 2: Прочети ред 2 → price=349.99  → не е 49.99
Стъпка 3: Прочети ред 3 → price=59.99   → не е 49.99
...
Стъпка 8: Прочети ред 8 → price=49.99   → намери! → но продължи...
...
Стъпка 12: Прочети ред 12 → price=49.99 → намери!
...
Стъпка 16: Край
→ Прочетени редове: 16 (всичките)
```

**С Non-Clustered Index по price:**
```
Стъпка 1: Влез в B-Tree на индекса, търси 49.99
          → B-Tree намери: 49.99 сочи към редове #8 и #12
Стъпка 2: Скочи директно до ред #8 → name="Чист Код",   stock=20
Стъпка 3: Скочи директно до ред #12 → name="Yoga Mat",  stock=45
→ Прочетени редове: само 2 (плюс ~3 стъпки в индекса)
```

---

## 5.3 Разлика между Clustered и Non-Clustered

```
┌─────────────────────┬────────────────────────┬──────────────────────────┐
│ Характеристика      │    CLUSTERED           │    NON-CLUSTERED         │
├─────────────────────┼────────────────────────┼──────────────────────────┤
│ Структура           │ Данни = Индекс         │ Индекс е ОТДЕЛЕН         │
│ Брой на таблица     │ Само 1                 │ Много (практически ~10)  │
│ Брой скокове        │ 1 скок                 │ 2 скока                  │
│ Скорост             │ По-бърз                │ По-бавен, но пак бърз    │
│ Дисково място       │ Включено в таблицата   │ Допълнително             │
│ Кога се ползва      │ PK, основен orderby    │ FK, WHERE, JOIN колони   │
│ Пример              │ id, order_number       │ email, city, price       │
└─────────────────────┴────────────────────────┴──────────────────────────┘
```

**Визуално сравнение:**

```
CLUSTERED (един скок):              NON-CLUSTERED (два скока):
═══════════════════════             ══════════════════════════════

  WHERE id = 5                        WHERE price = 59.99
      │                                   │
      ▼                                   ▼
  [B-Tree по id]                     [B-Tree по price — ОТДЕЛЕН]
      │                                   │
      ▼                                   ▼ (указател)
  [ДАННИТЕ ВЪВ ФАЙЛА]                [ДАННИТЕ ВЪВ ФАЙЛА]
  ← данните СА B-Tree                ← 2 структури, 2 скока
```

---

---

# ЧАСТ 6: Видове Индекси

---

## 6.1 Обикновен Индекс (Regular Index)

Най-простият вид — ускорява търсене, позволява дублиращи стойности.

```sql
-- Синтаксис:
CREATE INDEX <ime_na_indeks> ON <tablitsa> (<kolona>);

-- Примери:
CREATE INDEX idx_products_price
    ON products (price);

CREATE INDEX idx_orders_ordered_on
    ON orders (ordered_on);

CREATE INDEX idx_products_category_id
    ON products (category_id);
```

**Конвенция за именуване:** `idx_<таблица>_<колона>` — описателно и лесно за разчитане.

```sql
-- Тестваме:
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price < 50;
-- Преди индекс: SCAN products
-- След индекс:  SEARCH products USING INDEX idx_products_price (price<?)
```

---

## 6.2 Уникален Индекс (UNIQUE INDEX)

**Уникалният индекс** освен ускоряване на търсенето, **забранява дублиращи стойности** в колоната.

```sql
-- Синтаксис:
CREATE UNIQUE INDEX <ime> ON <tablitsa> (<kolona>);

-- Пример: уникален email на клиент
CREATE UNIQUE INDEX idx_customers_email_unique
    ON customers (email);
```

**Тест — опит за дублиране:**

```sql
-- Опитваме да вкараме два клиента с един и същи email:
INSERT INTO customers (first_name, last_name, email, city, registered)
VALUES ('Тест', 'Тестов', 'stefan@mail.bg', 'София', '2024-01-01');

-- ГРЕШКА: UNIQUE constraint failed: customers.email
-- Индексът защитава данните!
```

> **Важно:** `UNIQUE` в `CREATE TABLE` автоматично създава уникален индекс! Не е нужно отделно `CREATE UNIQUE INDEX`:
> ```sql
> email TEXT UNIQUE NOT NULL  -- ← автоматично уникален индекс!
> ```

---

## 6.3 Съставен Индекс (Composite Index)

**Съставният индекс** покрива **две или повече колони**. Полезен е, когато заявките редовно филтрират по **комбинация от колони**.

```sql
-- Индекс по (customer_id, status) — за заявки като:
-- WHERE customer_id = 1 AND status = 'shipped'
CREATE INDEX idx_orders_customer_status
    ON orders (customer_id, status);
```

### Важно: Редът на колоните има значение!

Съставният индекс работи **от ляво на дясно**. Той помага на заявки, които ползват:
- Само **първата** колона
- **Двете** колони заедно

Но **НЕ** помага, ако ползвате само **втората** колона:

```sql
-- Индекс: (customer_id, status)

-- ✓ РАБОТИ — ползва индекса (първата колона):
SELECT * FROM orders WHERE customer_id = 1;

-- ✓ РАБОТИ — ползва индекса (двете колони):
SELECT * FROM orders WHERE customer_id = 1 AND status = 'shipped';

-- ✗ НЕ РАБОТИ добре — не ползва индекса (само втората колона):
SELECT * FROM orders WHERE status = 'shipped';
-- За тази заявка трябва отделен индекс по status!
```

**Визуален пример:**

```
Индекс: (customer_id, status)  — B-Tree наредено ПЪРВО по customer_id, ПОСЛЕ по status

┌─────────────┬─────────────┬──────────┐
│ customer_id │   status    │ row_ptr  │
├─────────────┼─────────────┼──────────┤
│      1      │ delivered   │ → ред #1 │
│      1      │ shipped     │ → ред #2 │
│      2      │ delivered   │ → ред #3 │
│      3      │ pending     │ → ред #4 │
│      4      │ cancelled   │ → ред #6 │
│      4      │ delivered   │ → ред #5 │
│      6      │ shipped     │ → ред #7 │
│      7      │ delivered   │ → ред #8 │
│      8      │ pending     │ → ред #9 │
│      9      │ delivered   │ → ред #10│
│     10      │ shipped     │ → ред #11│
└─────────────┴─────────────┴──────────┘

WHERE customer_id = 4           → директно сканира редовете с 4 → бързо!
WHERE customer_id = 4 AND status='delivered' → директно до реда → бързо!
WHERE status = 'shipped'        → трябва да сканира ВСИЧКО → бавно!
```

### Практически пример

```sql
-- Заявка: всички shipped поръчки на конкретен клиент
SELECT o.id, o.ordered_on
FROM orders o
WHERE o.customer_id = 1 AND o.status = 'shipped';

-- EXPLAIN преди индекс:
-- SCAN orders

-- Създаваме съставен индекс:
CREATE INDEX idx_orders_customer_status ON orders (customer_id, status);

-- EXPLAIN след индекс:
-- SEARCH orders USING INDEX idx_orders_customer_status (customer_id=? AND status=?)
```

---

## 6.4 Частичен Индекс (Partial Index)

**Частичният индекс** индексира само **подмножество от редовете** — тези, отговарящи на `WHERE` условие. По-малък, по-бърз, заема по-малко място.

```sql
-- Синтаксис:
CREATE INDEX <ime> ON <tablitsa> (<kolona>) WHERE <uslovie>;

-- Пример: Индексираме само активни (неизпълнени) поръчки
-- 'delivered' поръчки са исторически данни — рядко ги търсим
CREATE INDEX idx_orders_active_by_date
    ON orders (ordered_on)
    WHERE status IN ('pending', 'shipped');
```

### Защо е полезен?

```
Таблица orders — 1 000 000 реда:

┌─────────────────────────────────────────┐
│ status      │  Брой редове              │
├─────────────┼───────────────────────────┤
│ delivered   │ 850 000 (85%)  ← стари    │
│ shipped     │  80 000 ( 8%)  ← активни  │
│ pending     │  60 000 ( 6%)  ← активни  │
│ cancelled   │  10 000 ( 1%)  ← стари    │
└─────────────┴───────────────────────────┘

Пълен индекс по ordered_on: 1 000 000 записа в индекса
Частичен индекс (само активни): само 140 000 записа — 7 пъти по-малък!
```

```sql
-- Тази заявка ще ползва частичния индекс:
SELECT * FROM orders
WHERE status = 'pending' AND ordered_on > '2024-01-01';

-- EXPLAIN: SEARCH orders USING INDEX idx_orders_active_by_date
```

---

## 6.5 Покриващ Индекс (Covering Index)

**Покриващият индекс** е Non-Clustered индекс, който съдържа **всички колони**, нужни на заявката. SQL не трябва да скача до реалната таблица изобщо — **всичко е в индекса**.

### Нормален индекс (2 скока)

```
Заявка: SELECT email, city FROM customers WHERE city = 'София';
Индекс само по city:

Стъпка 1: B-Tree по city → намери "София" → указатели към редове #1, #4, #6, #9
Стъпка 2: Скочи до всеки ред в таблицата → вземи email и city
                                            ↑
                                   2 скока за всеки ред
```

### Покриващ индекс (1 скок — без таблицата)

```sql
-- Индексираме И city, И email — всичко нужно е в индекса:
CREATE INDEX idx_customers_city_email ON customers (city, email);
```

```
Стъпка 1: B-Tree по city → намери "София" → в листата намираме И city И email!
Стъпка 2: [НЯМА] — не е нужен скок до таблицата!

→ EXPLAIN ще покаже: USING COVERING INDEX
```

**Тест:**

```sql
-- Тест с EXPLAIN:
EXPLAIN QUERY PLAN
SELECT email, city
FROM customers
WHERE city = 'София';

-- С нормален индекс само по city:
-- SEARCH customers USING INDEX idx_customers_city (city=?)

-- С покриващ индекс (city, email):
-- SEARCH customers USING COVERING INDEX idx_customers_city_email (city=?)
--                                                ↑
--                          "COVERING" = не влиза в таблицата!
```

### Кога да ползвате Covering Index?

```sql
-- Добър кандидат: заявка, която чете САМО определени колони:
SELECT first_name, last_name, email
FROM customers
WHERE city = 'София'
ORDER BY last_name;

-- Покриващ индекс:
CREATE INDEX idx_customers_city_name_email
    ON customers (city, last_name, first_name, email);
-- Индексът съдържа всичко необходимо — таблицата не се чете!
```

> **Внимание:** Не прекалявайте! Покриващите индекси са по-големи и по-бавни за UPDATE/INSERT. Ползвайте ги само за **критично важни** заявки.

---

---

# ЧАСТ 7: EXPLAIN QUERY PLAN — Виждаме Какво Прави SQL

---

## 7.1 Основи на EXPLAIN QUERY PLAN

`EXPLAIN QUERY PLAN` е инструментът, с който **виждате как SQL изпълнява заявката** — дали ползва индекс или прави Full Scan.

```sql
EXPLAIN QUERY PLAN
<вашата заявка тук>;
```

### Речник на изходните съобщения

```
SCAN <таблица>
    → Full Table Scan — чете ВСЕКИ ред
    → Лошо при голяма таблица
    → Трябва индекс!

SEARCH <таблица> USING INDEX <индекс> (<колона>=?)
    → Използва Non-Clustered индекс
    → Добро!

SEARCH <таблица> USING INTEGER PRIMARY KEY (rowid=?)
    → Използва Clustered Index (PRIMARY KEY)
    → Най-добро!

SEARCH <таблица> USING COVERING INDEX <индекс> (<колона>=?)
    → Покриващ индекс — дори не чете таблицата
    → Отлично!

USE TEMP B-TREE FOR ORDER BY
    → SQL сортира в паметта защото няма подходящ индекс
    → Помага: CREATE INDEX по ORDER BY колоната
```

---

## 7.2 Примери — Преди и След Индекс

### Пример A: Търсене по email

```sql
-- БЕЗ ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'stefan@mail.bg';
-- Output: SCAN customers  ← Full Scan!

-- Създаваме индекс:
CREATE INDEX idx_customers_email ON customers (email);

-- С ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'stefan@mail.bg';
-- Output: SEARCH customers USING INDEX idx_customers_email (email=?)  ← Бързо!
```

---

### Пример B: Диапазонно търсене по цена

```sql
-- БЕЗ ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price BETWEEN 50 AND 200;
-- Output: SCAN products

-- Създаваме индекс:
CREATE INDEX idx_products_price ON products (price);

-- С ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price BETWEEN 50 AND 200;
-- Output: SEARCH products USING INDEX idx_products_price (price>? AND price<?)
```

---

### Пример C: JOIN по Foreign Key

```sql
-- БЕЗ ИНДЕКС по customer_id:
EXPLAIN QUERY PLAN
SELECT c.first_name, o.id, o.status
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id;
-- Output:
-- SCAN c                        ← чете всички клиенти
-- SCAN o                        ← за всеки клиент чете ВСИЧКИ поръчки!

-- Създаваме индекс по FK:
CREATE INDEX idx_orders_customer_id ON orders (customer_id);

-- С ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT c.first_name, o.id, o.status
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id;
-- Output:
-- SCAN c
-- SEARCH o USING INDEX idx_orders_customer_id (customer_id=?)  ← Бързо!
```

---

### Пример D: ORDER BY с и без индекс

```sql
-- БЕЗ ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT name, price FROM products ORDER BY price ASC;
-- Output:
-- SCAN products
-- USE TEMP B-TREE FOR ORDER BY  ← сортира в паметта — бавно!

-- С индекс по price:
-- (вече съществува idx_products_price)
EXPLAIN QUERY PLAN
SELECT name, price FROM products ORDER BY price ASC;
-- Output:
-- SCAN products USING INDEX idx_products_price  ← вече е наредено!
```

---

### Пример E: JOIN с четири таблици — пълен анализ

```sql
-- Голяма заявка: клиент → поръчка → артикул → продукт
EXPLAIN QUERY PLAN
SELECT c.first_name, o.ordered_on, p.name, oi.quantity
FROM customers      AS c
    JOIN orders      AS o  ON c.id          = o.customer_id
    JOIN order_items AS oi ON o.id          = oi.order_id
    JOIN products    AS p  ON oi.product_id = p.id
WHERE c.city = 'София';

-- БЕЗ никакви индекси:
-- SCAN c         ← Full scan customers
-- SCAN o         ← Full scan orders за всеки клиент
-- SCAN oi        ← Full scan order_items за всяка поръчка
-- SEARCH p USING INTEGER PRIMARY KEY  ← тук id е PK, добре

-- Добавяме индекси по FK-тата:
CREATE INDEX idx_orders_customer_id      ON orders      (customer_id);
CREATE INDEX idx_order_items_order_id    ON order_items (order_id);
CREATE INDEX idx_order_items_product_id  ON order_items (product_id);
CREATE INDEX idx_customers_city          ON customers   (city);

-- С ИНДЕКСИ:
-- SEARCH c USING INDEX idx_customers_city (city=?)  ← само Софийски клиенти
-- SEARCH o USING INDEX idx_orders_customer_id (customer_id=?)
-- SEARCH oi USING INDEX idx_order_items_order_id (order_id=?)
-- SEARCH p USING INTEGER PRIMARY KEY (rowid=?)
-- БЪРЗО!
```

---

---

# ЧАСТ 8: Цената на Индексите — Кога Помагат и Кога Пречат

---

## 8.1 Индексите не са безплатни

Индексите **ускоряват четенето**, но **забавят писането**. Всеки `INSERT`, `UPDATE` или `DELETE` трябва да обнови **всички индекси** на таблицата.

```
Операция INSERT без индекси:
→ Пиши нов ред в таблицата = 1 операция

Операция INSERT с 5 индекса:
→ Пиши нов ред в таблицата
→ Обнови индекс 1
→ Обнови индекс 2
→ Обнови индекс 3
→ Обнови индекс 4
→ Обнови индекс 5
= 6 операции — 6 пъти по-бавен INSERT!
```

```
                  | READ  | INSERT | UPDATE | DELETE
──────────────────+───────+────────+────────+─────────
Без индекс        | Бавно │ Бързо  │ Бързо  │ Бързо
С 1 индекс        | Бързо │ Малко  │ Малко  │ Малко
                  |       │ по-бав.│ по-бав.│ по-бав.
С много индекси   | Бързо │ Бавно  │ Бавно  │ Бавно
```

> **Балансът:** Добавяйте индекси само там, където **четенето е по-важно от писането**. В повечето приложения четем **много повече** отколкото пишем — индексите си заслужават.

---

## 8.2 Индексите заемат място на диска

```sql
-- Вижте размера на индексите (SQLite):
SELECT name, tbl_name
FROM sqlite_master
WHERE type = 'index'
ORDER BY tbl_name, name;
```

Всеки индекс е копие на данните в сортиран вид — заема **допълнително дисково пространство**. Обикновено индексите увеличават размера на базата данни с **20-50%**.

---

## 8.3 Кога ДА създаваме индекс

```sql
-- ✓ 1. Foreign Key колони — ЗАДЪЛЖИТЕЛНО!
--    (всеки JOIN по FK без индекс = Full Scan)
CREATE INDEX idx_orders_customer_id      ON orders      (customer_id);
CREATE INDEX idx_order_items_order_id    ON order_items (order_id);
CREATE INDEX idx_order_items_product_id  ON order_items (product_id);
CREATE INDEX idx_products_category_id   ON products    (category_id);

-- ✓ 2. Колони с висока селективност в WHERE
--    (много различни стойности → индексът е ефективен)
CREATE INDEX idx_customers_email     ON customers (email);
CREATE INDEX idx_products_price      ON products  (price);

-- ✓ 3. Колони в ORDER BY при бавни заявки
CREATE INDEX idx_orders_ordered_on   ON orders (ordered_on);

-- ✓ 4. Комбинации от колони, ако WHERE ги ползва заедно
CREATE INDEX idx_orders_customer_status ON orders (customer_id, status);
```

---

## 8.4 Кога НЕ създаваме индекс

```sql
-- ✗ 1. Колони с малко различни стойности (нисък кардиналитет)
--    status има само 4 стойности — индексът почти не помага
CREATE INDEX idx_orders_status ON orders (status);  -- ЛОШО

-- Защо? При 1 000 000 реда с 4 статуса, всеки статус се среща ~250 000 пъти.
-- Индексът ще ни върне 250 000 row pointers — SQL ще чете таблицата пак!

-- ✗ 2. Малки таблици (под ~1000 реда)
CREATE INDEX idx_warehouses_city ON warehouses (city);  -- БЕЗСМИСЛЕНО
-- 3 реда сe сканират за микросекунди и без индекс

-- ✗ 3. Колони, по които НИКОГА не се търси
CREATE INDEX idx_products_stock ON products (stock);  -- само ако имате WHERE stock = X

-- ✗ 4. Таблици с изключително много INSERT/UPDATE
-- Logging таблици, event tables — там индексите забавят записа твърде много
```

---

## 8.5 Правилото за Кардиналитет

**Кардиналитетът** е броят на **уникалните стойности** в колона. Колкото по-висок е кардиналитетът, толкова по-ефективен е индексът.

```
Колона       │ Уникални стойности │ Кардиналитет │ Индекс полезен?
─────────────┼────────────────────┼──────────────┼─────────────────
email        │ =N (всеки уникален)│ Много висок  │ ДА (задължително)
id           │ =N                 │ Много висок  │ ДА (PK автом.)
price        │ ~N/2 (много разл.) │ Висок        │ ДА
city         │ ~20-100            │ Среден       │ МОЖЕ БИ
category_id  │ 5                  │ Нисък        │ Само за JOIN (FK)
status       │ 4                  │ Много нисък  │ НЕ (без JOIN)
```

---

## 8.6 Преглед и управление на индекси

```sql
-- Всички индекси в базата данни:
SELECT name, tbl_name, sql
FROM sqlite_master
WHERE type = 'index'
ORDER BY tbl_name, name;

-- Индекси само за конкретна таблица:
PRAGMA index_list('orders');

-- Детайли за конкретен индекс:
PRAGMA index_info('idx_orders_customer_id');

-- Изтриване на индекс:
DROP INDEX IF EXISTS idx_orders_customer_id;
```

---

## 8.7 Практически набор от индекси за нашата схема

```sql
-- ================================================
-- ПРЕПОРЪЧИТЕЛНИ ИНДЕКСИ ЗА ОНЛАЙН МАГАЗИН
-- ================================================

-- Foreign Keys (задължителни за JOIN):
CREATE INDEX idx_products_category_id   ON products    (category_id);
CREATE INDEX idx_orders_customer_id     ON orders      (customer_id);
CREATE INDEX idx_order_items_order_id   ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);

-- Търсене по email (уникален + бърз):
-- (вече е UNIQUE в таблицата — автоматичен индекс)

-- Търсене по цена:
CREATE INDEX idx_products_price         ON products    (price);

-- Търсене/сортиране по дата на поръчка:
CREATE INDEX idx_orders_ordered_on      ON orders      (ordered_on);

-- Търсене по град на клиент:
CREATE INDEX idx_customers_city         ON customers   (city);

-- Съставен: клиент + статус (чести комбинирани заявки):
CREATE INDEX idx_orders_customer_status ON orders      (customer_id, status);
```

---

---

# Задачи за Упражнение

> **Преди да започнете:** Изпълнете блока за подготовка от началото на лекцията и **изтрийте всички индекси**, за да започнете чисто:
> ```sql
> DROP INDEX IF EXISTS idx_customers_email;
> DROP INDEX IF EXISTS idx_products_price;
> DROP INDEX IF EXISTS idx_orders_customer_id;
> DROP INDEX IF EXISTS idx_order_items_order_id;
> DROP INDEX IF EXISTS idx_order_items_product_id;
> DROP INDEX IF EXISTS idx_products_category_id;
> DROP INDEX IF EXISTS idx_orders_ordered_on;
> DROP INDEX IF EXISTS idx_customers_city;
> DROP INDEX IF EXISTS idx_orders_customer_status;
> DROP INDEX IF EXISTS idx_customers_city_email;
> ```

---

### Задача 1: EXPLAIN преди и след

За всяка от следните заявки:
1. Изпълнете `EXPLAIN QUERY PLAN` **без** индекс — запишете изхода
2. Създайте подходящ индекс
3. Изпълнете `EXPLAIN QUERY PLAN` **с** индекс — запишете разликата

```sql
-- A: Търсене по email
SELECT * FROM customers WHERE email = 'borislav@mail.bg';

-- B: Диапазон по цена
SELECT name, price FROM products WHERE price BETWEEN 30 AND 150;

-- C: Сортиране по дата
SELECT id, ordered_on, status FROM orders ORDER BY ordered_on DESC;

-- D: Търсене по град
SELECT first_name, last_name FROM customers WHERE city = 'Пловдив';
```

---

### Задача 2: Кардиналитет — оценете колоните

Напишете заявки, които преброяват **броя уникални стойности** в следните колони:
- `customers.city`
- `orders.status`
- `products.price`
- `products.category_id`
- `customers.email`

На база резултатите — за кои колони **бихте създали** индекс и защо?

*(Подсказка: `SELECT COUNT(DISTINCT kolona) FROM tablitsa`)*

---

### Задача 3: Оптимизиране на JOIN заявка

Дадена е следната заявка:

```sql
SELECT c.first_name || ' ' || c.last_name AS klient,
       o.ordered_on,
       p.name AS produkt,
       oi.quantity,
       oi.unit_price
FROM customers      AS c
    JOIN orders      AS o  ON c.id          = o.customer_id
    JOIN order_items AS oi ON o.id          = oi.order_id
    JOIN products    AS p  ON oi.product_id = p.id
WHERE c.city = 'София'
  AND o.status = 'delivered'
ORDER BY o.ordered_on DESC;
```

1. Изпълнете `EXPLAIN QUERY PLAN` **без** никакви допълнителни индекси
2. Анализирайте изхода — кои таблици правят SCAN?
3. Създайте всички необходими индекси
4. Изпълнете `EXPLAIN QUERY PLAN` отново — всичко ли е SEARCH вместо SCAN?

---

### Задача 4: Съставен индекс — ред на колоните

Разгледайте следните две заявки:

```sql
-- Заявка 1:
SELECT * FROM orders WHERE customer_id = 4 AND status = 'delivered';

-- Заявка 2:
SELECT * FROM orders WHERE status = 'delivered';
```

1. Създайте индекс `(customer_id, status)`.
2. Проверете с `EXPLAIN QUERY PLAN` дали **и двете** заявки го ползват.
3. Какво наблюдавате за Заявка 2?
4. Какъв отделен индекс трябва да добавите, за да оптимизирате Заявка 2?

---

### Задача 5: Частичен индекс

В реална система, `delivered` поръчките са вече завършени и **рядко се търсят**. Активните поръчки (`pending`, `shipped`) са важни.

1. Създайте **частичен индекс** по `ordered_on`, само за активни поръчки.
2. Тествайте следната заявка с `EXPLAIN QUERY PLAN`:
   ```sql
   SELECT * FROM orders
   WHERE status = 'pending'
     AND ordered_on > '2024-01-01';
   ```
3. Ползва ли се частичният индекс?

---

### Задача 6: Покриващ индекс

Следната заявка се изпълнява много често:

```sql
SELECT first_name, last_name, email
FROM customers
WHERE city = 'София'
ORDER BY last_name;
```

1. Изпълнете `EXPLAIN QUERY PLAN` без индекс.
2. Създайте обикновен индекс само по `city` и тествайте отново.
3. Създайте **покриващ индекс** по `(city, last_name, first_name, email)`.
4. Тествайте отново — вижда ли се `COVERING INDEX` в изхода?
5. Каква е разликата между стъпките 2 и 4?

---

### Задача 7: Кога индексът вреди

Изпълнете следните `INSERT` команди и обяснете защо **при таблица с много индекси** те биха били по-бавни от таблица без индекси:

```sql
-- Добавете 3 нови клиента:
INSERT INTO customers (first_name, last_name, email, city, registered)
VALUES
    ('Петър',  'Стоев',   'petar@mail.bg',   'Варна',    '2024-05-01'),
    ('Мария',  'Тонева',  'maria@mail.bg',   'София',    '2024-05-02'),
    ('Виктор', 'Железов', 'viktor@mail.bg',  'Пловдив',  '2024-05-03');
```

Опишете кои индекси (от Задача 3) трябва да се обновят при всеки `INSERT`.

---

### Задача 8: Пълен набор — онлайн магазин

Разгледайте следните **3 сценария** за реален онлайн магазин и за всеки:
- Напишете заявката
- Добавете подходящия индекс
- Проверете с `EXPLAIN QUERY PLAN`

**Сценарий A:** Клиент влиза в профила си. Системата трябва **бързо** да намери клиента по имейл адрес.

**Сценарий Б:** Страница с продукти — показва всички продукти от категория "Електроника", наредени по цена.

**Сценарий В:** Административен панел — показва всички `shipped` поръчки, наредени по дата (от най-нова), с имената на клиентите.

---

*Следваща лекция: **VIEW (Изгледи)**, **Транзакции (COMMIT / ROLLBACK)**, **Тригери (Triggers)** и **Агрегатни прозорни функции (Window Functions)**.*

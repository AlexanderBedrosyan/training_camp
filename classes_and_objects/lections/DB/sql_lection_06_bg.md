# SQL Лекция 6: JOIN — Данни от Множество Таблици, Подзаявки и Индекси

Добре дошли в шестата лекция по SQL!

В **Лекция 5** научихме как да проектираме бази данни с релации. Сега ще задълбочим уменията си и ще научим как **майсторски** да извличаме данни от тях. Тази лекция покрива три от най-важните теми в SQL:

| # | Тема | Какво ще научим |
|---|------|-----------------|
| 1 | **JOIN — Данни от множество таблици** | Всички видове JOIN, aliases, multi-table joins |
| 2 | **Подзаявки (Subqueries)** | Вложени заявки, корелирани подзаявки, EXISTS, IN |
| 3 | **Индекси (Indices)** | Clustered vs Non-Clustered, кога и как да ги ползваме |

---

## Подготовка: Тестова Схема — Онлайн Магазин

За цялата лекция ще използваме схема на **онлайн магазин** с клиенти, продукти, поръчки и категории.

```sql
-- ============================================================
-- ИЗЧИСТВАНЕ НА ПРЕДИШНИ ТАБЛИЦИ
-- ============================================================
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS warehouses;

-- ============================================================
-- СТРУКТУРА НА ТАБЛИЦИТЕ
-- ============================================================

CREATE TABLE categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    NOT NULL UNIQUE
);

CREATE TABLE products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    price       REAL    NOT NULL CHECK (price >= 0),
    stock       INTEGER NOT NULL DEFAULT 0,
    category_id INTEGER,                              -- може да е NULL (без категория)
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
    registered TEXT    NOT NULL   -- дата на регистрация
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
    unit_price REAL    NOT NULL,                     -- цена към момента на поръчката
    FOREIGN KEY (order_id)   REFERENCES orders(id)   ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- ============================================================
-- ДАННИ
-- ============================================================

INSERT INTO categories (name) VALUES
    ('Електроника'),
    ('Книги'),
    ('Дрехи'),
    ('Спорт'),
    ('Дом и Градина');

INSERT INTO products (name, price, stock, category_id) VALUES
    ('Лаптоп Dell XPS',        2199.99, 15,  1),
    ('Слушалки Sony WH-1000',   349.99, 42,  1),
    ('Безжична мишка Logitech',  59.99, 80,  1),
    ('Клавиатура Mechanical',   129.99, 35,  1),
    ('Монитор LG 27"',          699.99, 10,  1),
    ('SQL за начинаещи',         39.99, 55,  2),
    ('Python Crash Course',      44.99, 30,  2),
    ('Чист Код - Р. Мартин',     49.99, 20,  2),
    ('Тениска Памучна XL',       29.99, 100, 3),
    ('Яке Зимно',               149.99, 25,  3),
    ('Маратонки Nike Air',       189.99, 60,  4),
    ('Yoga Mat 6мм',             49.99, 45,  4),
    ('Гири 10кг Комплект',       89.99, 18,  4),
    ('Градинска Ножица',         24.99, 70,  5),
    ('Саксия Керамична',         19.99, 90,  5),
    ('Разширител USB-C',         34.99, 55,  NULL);  -- без категория!

INSERT INTO warehouses (city, capacity) VALUES
    ('София',   5000),
    ('Пловдив', 3000),
    ('Варна',   2500);

INSERT INTO customers (first_name, last_name, email, city, registered) VALUES
    ('Мартина',  'Колева',    'martina@mail.bg',   'София',    '2022-03-15'),
    ('Стефан',   'Димов',     'stefan@mail.bg',    'Пловдив',  '2021-07-20'),
    ('Галина',   'Пенева',    'galina@mail.bg',    'Варна',    '2023-01-10'),
    ('Борислав', 'Неделчев',  'borislav@mail.bg',  'София',    '2020-11-05'),
    ('Цветелина','Атанасова', 'cveta@mail.bg',     'Бургас',   '2023-09-22'),
    ('Радослав', 'Иванов',    'radoslav@mail.bg',  'София',    '2024-01-30'),
    ('Деница',   'Георгиева', 'denica@mail.bg',    'Пловдив',  '2022-06-18'),
    ('Калоян',   'Тодоров',   'kaloyan@mail.bg',   'Варна',    '2021-12-01'),
    ('Ивета',    'Стоянова',  'iveta@mail.bg',     'София',    '2023-04-14'),
    ('Никола',   'Петров',    'nikola@mail.bg',    'Русе',     '2024-02-28');

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
    (1,  1,  1,  2199.99),   -- Лаптоп
    (1,  3,  1,    59.99),   -- Мишка
    (2,  2,  1,   349.99),   -- Слушалки
    (3,  6,  2,    39.99),   -- SQL книга x2
    (3,  7,  1,    44.99),   -- Python книга
    (4,  12, 1,    49.99),   -- Yoga Mat
    (4,  13, 1,    89.99),   -- Гири
    (5,  1,  1,  2199.99),   -- Лаптоп
    (5,  4,  1,   129.99),   -- Клавиатура
    (5,  5,  1,   699.99),   -- Монитор
    (6,  9,  3,    29.99),   -- Тениска x3
    (7,  11, 1,   189.99),   -- Маратонки
    (8,  8,  1,    49.99),   -- Чист Код
    (8,  6,  1,    39.99),   -- SQL книга
    (9,  15, 2,    19.99),   -- Саксия x2
    (10, 2,  1,   349.99),   -- Слушалки
    (10, 3,  2,    59.99),   -- Мишка x2
    (11, 16, 1,    34.99);   -- USB-C разширител
```

### Визуална схема на базата данни

```
┌───────────────┐         ┌──────────────────────┐
│   CATEGORIES  │         │       PRODUCTS        │
├───────────────┤         ├──────────────────────┤
│ PK id         │◄───1:N──│ PK id                │
│    name       │         │ FK category_id (NULL)│
└───────────────┘         │    name              │
                          │    price             │
                          │    stock             │
                          └──────────┬───────────┘
                                     │ 1
                                     │
                                     │ N
┌───────────────┐         ┌──────────┴───────────┐
│   CUSTOMERS   │         │     ORDER_ITEMS       │
├───────────────┤         ├──────────────────────┤
│ PK id         │         │ PK id                │
│    first_name │         │ FK order_id          │
│    last_name  │         │ FK product_id        │
│    email      │         │    quantity          │
│    city       │         │    unit_price        │
│    registered │         └──────────┬───────────┘
└───────┬───────┘                    │ N
        │ 1                          │
        │                            │ 1
        │ N                 ┌────────┴───────────┐
        └──────────────────►│       ORDERS       │
                            ├────────────────────┤
                            │ PK id              │
                            │ FK customer_id     │
                            │    ordered_on      │
                            │    status          │
                            └────────────────────┘
```

---

---

# ЧАСТ 1: JOIN — Събиране на Данни от Множество Таблици

---

## 1.1 Какво е JOIN и защо го използваме?

В нормализирана база данни информацията е **разпределена** в много таблици. `JOIN` е механизмът, чрез който SQL **обединява** редове от различни таблици въз основа на логическа **съвпадаща стойност** (обикновено връзка PK → FK).

### Принципна схема

```
customers             orders
─────────────────     ──────────────────────
id │ first_name       id │ customer_id │ status
1  │ Мартина          1  │     1       │ delivered   ← customer_id = 1 съвпада с id = 1
2  │ Стефан           2  │     1       │ shipped     ← също
3  │ Галина           3  │     2       │ delivered   ← customer_id = 2 съвпада с id = 2
                      4  │     3       │ pending

                     JOIN ON orders.customer_id = customers.id

Резултат:
first_name │ status
───────────│──────────
Мартина    │ delivered
Мартина    │ shipped
Стефан     │ delivered
Галина     │ pending
```

### Основен синтаксис

```sql
SELECT    таблица1.колона, таблица2.колона, ...
FROM      таблица1
    [TIP_JOIN] таблица2 ON таблица1.ключ = таблица2.ключ
WHERE     условие
ORDER BY  колона;
```

---

## 1.2 Table Aliases — Съкратени Имена

При работа с много таблици е неудобно да пишем пълното им наименование. `AS` ни дава кратък **псевдоним**:

```sql
-- Без alias — тромаво
SELECT customers.first_name, orders.status
FROM customers
    JOIN orders ON customers.id = orders.customer_id;

-- С alias — чисто и ясно
SELECT c.first_name, o.status
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id;

-- AS е по избор — може и без него
SELECT c.first_name, o.status
FROM customers c
    JOIN orders o ON c.id = o.customer_id;
```

> **Правило:** Щом имате повече от 2 таблици, **винаги** използвайте aliases!

---

## 1.3 INNER JOIN

**INNER JOIN** (или просто `JOIN`) връща само редовете, при които има **съвпадение в ДВЕТЕ таблици**.

```
   customers          orders              INNER JOIN
   ──────────         ──────────          ──────────────────────
   1 Мартина     ◄──► 1  (c=1)           1 Мартина  | delivered
   2 Стефан      ◄──► 2  (c=1)           1 Мартина  | shipped
   3 Галина      ◄──► 3  (c=2)           2 Стефан   | delivered
   4 Борислав    ◄──► 4  (c=3)           3 Галина   | pending
   5 Цветелина        5  (c=4)           4 Борислав | delivered
   ...           ◄──► ...               ...
                                    ↑ клиенти БЕЗ поръчки НЕ се включват!
```

### Пример 1: Продукти с техните категории

```sql
SELECT p.name          AS produkt,
       p.price         AS tsena,
       c.name          AS kategoriya
FROM products AS p
    INNER JOIN categories AS c ON p.category_id = c.id
ORDER BY c.name, p.price;
```

**Резултат (извадка):**
```
produkt                    | tsena   | kategoriya
---------------------------|---------|------------
Безжична мишка Logitech    |  59.99  | Електроника
Клавиатура Mechanical      | 129.99  | Електроника
Слушалки Sony WH-1000      | 349.99  | Електроника
Монитор LG 27"             | 699.99  | Електроника
Лаптоп Dell XPS            |2199.99  | Електроника
SQL за начинаещи           |  39.99  | Книги
...
```

> **Забележи:** Продуктът "Разширител USB-C" (`category_id = NULL`) **не се появява** — INNER JOIN изхвърля редове без съвпадение!

### Пример 2: Поръчки с имена на клиенти

```sql
SELECT o.id             AS order_id,
       o.ordered_on     AS data,
       o.status,
       c.first_name || ' ' || c.last_name AS klient,
       c.city
FROM orders AS o
    INNER JOIN customers AS c ON o.customer_id = c.id
ORDER BY o.ordered_on DESC;
```

---

## 1.4 LEFT JOIN (LEFT OUTER JOIN)

**LEFT JOIN** връща **ВСИЧКИ** редове от **лявата** таблица. Ако за ред от лявата таблица **няма** съответстващ ред в дясната — дясната страна е `NULL`.

```
   products (лява)      categories (дясна)    LEFT JOIN резултат
   ──────────────────   ──────────────────    ────────────────────────────
   id │ name  │ cat_id  id │ name             name            │ kategoriya
   1  │ Laptop│  1       1  │ Електроника      Laptop          │ Електроника
   2  │ Sony  │  1       2  │ Книги            Sony            │ Електроника
   ...│       │  ...     ...│                  ...             │ ...
   16 │ USB-C │  NULL   ← НЯМА съвпадение     USB-C Разшир.   │ NULL  ← включен!
```

### Пример 3: Всички продукти — дори без категория

```sql
SELECT p.name          AS produkt,
       p.price         AS tsena,
       COALESCE(c.name, '— без категория —') AS kategoriya
FROM products AS p
    LEFT JOIN categories AS c ON p.category_id = c.id
ORDER BY kategoriya, tsena;
```

**Резултат (извадка на дъното):**
```
produkt              | tsena | kategoriya
---------------------|-------|--------------------
Разширител USB-C     | 34.99 | — без категория —
```

### Пример 4: Клиенти без поръчки

Класическата употреба на LEFT JOIN — намиране на редове **без** съответствие:

```sql
-- Клиенти, които НИКОГА не са поръчвали
SELECT c.first_name || ' ' || c.last_name AS klient,
       c.email,
       c.city
FROM customers AS c
    LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.id IS NULL    -- ← ключовото: дясната страна е NULL = няма поръчка
ORDER BY c.last_name;
```

> **Модел:**
> ```
> LEFT JOIN + WHERE дяснаТаблица.id IS NULL
> ```
> = "Намери всичко от лявата таблица, за което НЯМА запис в дясната"

---

## 1.5 RIGHT JOIN и FULL OUTER JOIN

### RIGHT JOIN

**RIGHT JOIN** е огледалото на LEFT JOIN — връща всички редове от **дясната** таблица + съвпадащите от лявата.

```sql
-- Всички категории, дори тези без продукти
SELECT c.name           AS kategoriya,
       p.name           AS produkt,
       p.price
FROM products AS p
    RIGHT JOIN categories AS c ON p.category_id = c.id
ORDER BY c.name;
```

> **Практически съвет:** В SQLite `RIGHT JOIN` и `FULL OUTER JOIN` не се поддържат директно. Можем да симулираме `RIGHT JOIN` като разменим таблиците и ползваме `LEFT JOIN`:
>
> ```sql
> -- Еквивалентно на: products RIGHT JOIN categories
> SELECT c.name, p.name, p.price
> FROM categories AS c
>     LEFT JOIN products AS p ON p.category_id = c.id
> ORDER BY c.name;
> ```

### FULL OUTER JOIN

Връща **ВСИЧКИ** редове и от двете таблици. Липсващите стойности и от двете страни са `NULL`.

```
LEFT JOIN + UNION + RIGHT JOIN = FULL OUTER JOIN
```

```sql
-- Симулация на FULL OUTER JOIN в SQLite
SELECT c.first_name || ' ' || c.last_name AS klient,
       o.id AS order_id,
       o.status
FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id

UNION

SELECT c.first_name || ' ' || c.last_name,
       o.id,
       o.status
FROM customers c
    RIGHT JOIN orders o ON c.id = o.customer_id
WHERE c.id IS NULL;
```

---

## 1.6 Визуално сравнение на всички JOIN видове

```
                   ┌───────┐   ┌───────┐
                   │   A   │   │   B   │
                   └───────┘   └───────┘

INNER JOIN            ∩              Само съвпадащите
  [    A ●●│●● B   ]

LEFT JOIN             ←              Всички от A + съвпадащите от B
  [ ●●●A ●●│●● B   ]

RIGHT JOIN            →              Всички от B + съвпадащите от A
  [    A ●●│●● B●●● ]

FULL OUTER JOIN       ↔              Всички от A и всички от B
  [ ●●●A ●●│●● B●●● ]

CROSS JOIN            ×              Декартово произведение (всяко с всяко)
  [ A×B = |A|×|B| реда              ]
```

---

## 1.7 CROSS JOIN — Декартово Произведение

`CROSS JOIN` свързва **всеки ред** от лявата таблица с **всеки ред** от дясната. Резултатът е `|A| × |B|` реда. Рядко се ползва в практиката, но е полезен за генериране на комбинации.

```sql
-- Всички комбинации от продукти и градове (за хипотетично доставяне)
SELECT p.name AS produkt, w.city AS skladov_grad
FROM products AS p
    CROSS JOIN warehouses AS w
ORDER BY p.name, w.city;
-- Резултат: 16 продукта × 3 складa = 48 реда
```

---

## 1.8 SELF JOIN — Таблица, свързана сама със себе си

`SELF JOIN` позволява на таблица да се свърже **сама със себе си**. Задължително използваме **различни aliases**.

### Пример: Клиенти от един и същи град

```sql
-- Намерете двойки клиенти, живеещи в един и същи град
SELECT a.first_name || ' ' || a.last_name AS klient_1,
       b.first_name || ' ' || b.last_name AS klient_2,
       a.city
FROM customers AS a
    JOIN customers AS b ON a.city = b.city
                       AND a.id < b.id   -- предотвратяваме дублирания (A-B и B-A)
ORDER BY a.city, klient_1;
```

**Резултат:**
```
klient_1              | klient_2              | city
----------------------|-----------------------|-------
Борислав Неделчев     | Мартина Колева        | София
Борислав Неделчев     | Радослав Иванов        | София
Борислав Неделчев     | Ивета Стоянова        | София
Мартина Колева        | Радослав Иванов        | София
Мартина Колева        | Ивета Стоянова        | София
Радослав Иванов       | Ивета Стоянова        | София
Галина Пенева         | Калоян Тодоров        | Варна
Деница Георгиева      | Стефан Димов          | Пловдив
```

---

## 1.9 Multi-Table JOIN — Свързване на 3+ Таблици

В реалните запитвания рядко свързваме само 2 таблици. SQL позволява верига от JOIN-ове:

```sql
-- Пълна история на поръчките: клиент → поръчка → артикул → продукт → категория
SELECT c.first_name || ' ' || c.last_name AS klient,
       o.ordered_on,
       o.status,
       p.name        AS produkt,
       cat.name      AS kategoriya,
       oi.quantity   AS kolichestvo,
       oi.unit_price AS tsena,
       oi.quantity * oi.unit_price AS suma
FROM customers      AS c
    JOIN orders      AS o   ON c.id          = o.customer_id
    JOIN order_items AS oi  ON o.id          = oi.order_id
    JOIN products    AS p   ON oi.product_id = p.id
    LEFT JOIN categories AS cat ON p.category_id = cat.id
ORDER BY o.ordered_on DESC, c.last_name;
```

> **Стъпка по стъпка:**
> ```
> customers  →(1:N)→  orders  →(1:N)→  order_items  →(N:1)→  products  →(N:1)→  categories
>     c                 o                   oi                    p                  cat
> ```

### Агрегиране при Multi-Table JOIN

```sql
-- Обща стойност на всяка поръчка
SELECT o.id                                        AS order_id,
       o.ordered_on,
       c.first_name || ' ' || c.last_name          AS klient,
       o.status,
       SUM(oi.quantity * oi.unit_price)             AS obstha_suma,
       COUNT(oi.id)                                 AS broi_artikuli
FROM orders      AS o
    JOIN customers   AS c  ON o.customer_id = c.id
    JOIN order_items AS oi ON o.id           = oi.order_id
GROUP BY o.id, o.ordered_on, klient, o.status
ORDER BY obstha_suma DESC;
```

**Резултат:**
```
order_id | ordered_on | klient             | status    | obstha_suma | broi_artikuli
---------|------------|--------------------|-----------|-------------|---------------
5        | 2024-01-22 | Борислав Неделчев  | delivered | 3029.97     | 3
1        | 2024-01-10 | Мартина Колева     | delivered | 2259.98     | 2
10       | 2024-01-05 | Ивета Стоянова     | delivered |  469.97     | 2
...
```

---

---

# ЧАСТ 2: Подзаявки (Subqueries)

---

## 2.1 Какво е Подзаявка?

**Подзаявката** (subquery) е `SELECT` заявка, вложена **вътре в друга** заявка. Тя се изпълнява **преди** основната заявка и резултатът й се използва като стойност, списък или виртуална таблица.

```
┌─────────────────────────────────────────────────────────┐
│  SELECT ...                                             │
│  FROM ...                                               │
│  WHERE колона = (                                       │
│                  ┌────────────────────────────────────┐ │
│                  │  SELECT ...   ← ПОДЗАЯВКА          │ │
│                  │  FROM ...                          │ │
│                  │  WHERE ...                         │ │
│                  └────────────────────────────────────┘ │
│                 )                                       │
└─────────────────────────────────────────────────────────┘
```

### Три места, където може да стои подзаявка

| Позиция | Синтаксис | Описание |
|---------|-----------|----------|
| `WHERE` | `WHERE col = (SELECT ...)` | Филтриране по резултат |
| `FROM` | `FROM (SELECT ...) AS alias` | Виртуална таблица |
| `SELECT` | `SELECT (SELECT ...) AS col` | Изчислена колона |

---

## 2.2 Скаларна Подзаявка (Scalar Subquery)

Връща **точно една стойност** (един ред, една колона). Използва се навсякъде, където може да стои единична стойност.

### В WHERE клаузата

```sql
-- Намерете продукти, по-скъпи от средната цена
SELECT name, price
FROM products
WHERE price > (
    SELECT AVG(price)        -- ← скаларна подзаявка, връща едно число
    FROM products
)
ORDER BY price DESC;
```

**Как работи:**
```
Стъпка 1: SELECT AVG(price) FROM products  →  288.11 (средна цена)
Стъпка 2: SELECT name, price FROM products WHERE price > 288.11
```

**Резултат:**
```
name                   | price
-----------------------|-------
Лаптоп Dell XPS        | 2199.99
Монитор LG 27"         |  699.99
Слушалки Sony WH-1000  |  349.99
Маратонки Nike Air     |  189.99
```

### В SELECT клаузата

```sql
-- Всяка поръчка + разлика от максималната поръчка
SELECT o.id,
       c.first_name || ' ' || c.last_name           AS klient,
       SUM(oi.quantity * oi.unit_price)              AS suma,
       (
           SELECT MAX(sub_oi.quantity * sub_oi.unit_price)
           FROM order_items sub_oi
       )                                             AS max_suma,
       (SELECT MAX(sub_oi.quantity * sub_oi.unit_price)
        FROM order_items sub_oi)
       - SUM(oi.quantity * oi.unit_price)            AS razlika
FROM orders o
    JOIN customers   c  ON o.customer_id = c.id
    JOIN order_items oi ON o.id          = oi.order_id
GROUP BY o.id, klient
ORDER BY suma DESC;
```

---

## 2.3 Подзаявка с IN

`IN` проверява дали стойността **присъства в списък**, върнат от подзаявката.

```sql
-- Намерете клиентите, поръчали поне веднъж продукт от категория "Електроника"
SELECT DISTINCT c.first_name || ' ' || c.last_name AS klient,
                c.email
FROM customers AS c
WHERE c.id IN (
    SELECT DISTINCT o.customer_id
    FROM orders      AS o
        JOIN order_items AS oi  ON o.id          = oi.order_id
        JOIN products    AS p   ON oi.product_id = p.id
        JOIN categories  AS cat ON p.category_id = cat.id
    WHERE cat.name = 'Електроника'
)
ORDER BY klient;
```

**Как работи:**
```
Подзаявката връща списък:  {1, 4, 9}   (id-та на клиентите с електроника)
Главната WHERE проверява:  c.id IN {1, 4, 9}
```

### NOT IN — Обратна проверка

```sql
-- Клиенти, които НЕ са поръчвали книги
SELECT c.first_name || ' ' || c.last_name AS klient
FROM customers AS c
WHERE c.id NOT IN (
    SELECT DISTINCT o.customer_id
    FROM orders      AS o
        JOIN order_items AS oi  ON o.id          = oi.order_id
        JOIN products    AS p   ON oi.product_id = p.id
        JOIN categories  AS cat ON p.category_id = cat.id
    WHERE cat.name = 'Книги'
)
ORDER BY klient;
```

> **Внимание с NOT IN и NULL!** Ако подзаявката може да върне `NULL`, `NOT IN` дава неочаквани резултати. Използвайте `NOT EXISTS` вместо това.

---

## 2.4 Подзаявка с EXISTS / NOT EXISTS

`EXISTS` проверява дали подзаявката **въобще връща редове** (без значение какви). Спира при намиране на първия ред — по-бързо от `IN` при големи данни.

```sql
-- EXISTS: Клиенти с поне 2 поръчки
SELECT c.first_name || ' ' || c.last_name AS klient,
       c.city
FROM customers AS c
WHERE EXISTS (
    SELECT 1                         -- "SELECT 1" е конвенция — стойността няма значение
    FROM orders AS o
    WHERE o.customer_id = c.id       -- ← свързва се с外 клиент
    HAVING COUNT(*) >= 2
)
ORDER BY klient;
```

### NOT EXISTS — "Намери неналичното"

```sql
-- Продукти, които НИКОГА не са поръчвани
SELECT p.name, p.price, p.stock
FROM products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_items AS oi
    WHERE oi.product_id = p.id
)
ORDER BY p.price DESC;
```

**Резултат:**
```
name                | price  | stock
--------------------|--------|------
Яке Зимно           | 149.99 | 25
Безжична мишка...   |  59.99 | 80  ← Внимание: тази е поръчвана — само пример!
...
```

---

## 2.5 Корелирана Подзаявка (Correlated Subquery)

**Корелираната подзаявка** се различава от обикновената по това, че **зависи от стойност на външната заявка** и се изпълнява **по веднъж за всеки ред** от нея.

```
За всеки ред на [ВЪНШНА ЗАЯВКА]:
    → изпълни [ВЪТРЕШНА ПОДЗАЯВКА] с текущата стойност от外
    → използвай резултата за филтриране/изчисление
```

```sql
-- За всеки продукт: покажи го само ако цената му е над средната за категорията му
SELECT p.name,
       p.price,
       cat.name AS kategoriya
FROM products AS p
    JOIN categories AS cat ON p.category_id = cat.id
WHERE p.price > (
    SELECT AVG(p2.price)
    FROM products AS p2
    WHERE p2.category_id = p.category_id   -- ← КОРЕЛАЦИЯ: зависи от外 p.category_id
)
ORDER BY cat.name, p.price DESC;
```

**Как работи:**
```
За Лаптоп (cat_id=1):   AVG(Електроника) = (2199.99+349.99+59.99+129.99+699.99)/5 = 688.0
                         2199.99 > 688.0? ДА → включи
За Мишка (cat_id=1):    59.99 > 688.0?  НЕ → не включи
За SQL книга (cat_id=2): AVG(Книги) = (39.99+44.99+49.99)/3 = 44.99
                         39.99 > 44.99? НЕ → не включи
```

---

## 2.6 Подзаявка в FROM (Derived Table / Inline View)

Подзаявката в `FROM` действа като **временна (виртуална) таблица**. Задължително се дава alias.

```sql
-- Топ 3 категории по приход от поръчки
SELECT  kategoriya,
        ROUND(obsth_prihod, 2) AS prihod,
        broi_prodadeni
FROM (
    -- Вътрешна заявка: пресмята прихода по категория
    SELECT  cat.name                              AS kategoriya,
            SUM(oi.quantity * oi.unit_price)      AS obsth_prihod,
            SUM(oi.quantity)                      AS broi_prodadeni
    FROM order_items AS oi
        JOIN products    AS p   ON oi.product_id = p.id
        JOIN categories  AS cat ON p.category_id = cat.id
    GROUP BY cat.id, cat.name
) AS prihod_po_kat           -- ← задължителен alias!
ORDER BY prihod DESC
LIMIT 3;
```

**Резултат:**
```
kategoriya    | prihod  | broi_prodadeni
--------------|---------|---------------
Електроника   | 6869.92 | 9
Книги         |  214.94 | 6
Спорт         |  329.96 | 3
```

---

## 2.7 Подзаявки с ALL и ANY

### ANY (SOME) — Вярно за поне един елемент

```sql
-- Продукти, по-скъпи от поне ЕДИН продукт в категория "Книги"
SELECT name, price
FROM products
WHERE price > ANY (
    SELECT price
    FROM products
        JOIN categories c ON products.category_id = c.id
    WHERE c.name = 'Книги'
)
  AND products.category_id != (SELECT id FROM categories WHERE name = 'Книги')
ORDER BY price;
```

### ALL — Вярно за ВСИЧКИ елементи

```sql
-- Продуктите, по-скъпи от ВСИЧКИ продукти в категория "Книги"
SELECT name, price
FROM products
WHERE price > ALL (
    SELECT price
    FROM products AS p2
        JOIN categories c ON p2.category_id = c.id
    WHERE c.name = 'Книги'
)
ORDER BY price;
```

---

## 2.8 WITH (Common Table Expression — CTE)

`WITH` дефинира **именувана временна таблица** (CTE), която може да се референцира многократно. По-четимо от вложени подзаявки.

```sql
-- CTE: Пресмятаме сумата на всяка поръчка, след което филтрираме
WITH order_totals AS (
    SELECT o.id          AS order_id,
           o.customer_id,
           o.status,
           SUM(oi.quantity * oi.unit_price) AS suma
    FROM orders      AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    GROUP BY o.id, o.customer_id, o.status
)
SELECT  c.first_name || ' ' || c.last_name AS klient,
        ot.order_id,
        ot.status,
        ROUND(ot.suma, 2) AS suma
FROM order_totals AS ot
    JOIN customers AS c ON ot.customer_id = c.id
WHERE ot.suma > 500
ORDER BY ot.suma DESC;
```

### Множество CTE

```sql
WITH
    -- CTE 1: Топ продукти по продадени бройки
    top_products AS (
        SELECT product_id,
               SUM(quantity)               AS total_qty,
               SUM(quantity * unit_price)  AS total_revenue
        FROM order_items
        GROUP BY product_id
    ),
    -- CTE 2: Обогатяваме с имена
    enriched AS (
        SELECT p.name           AS produkt,
               p.price          AS tekushta_tsena,
               tp.total_qty,
               tp.total_revenue
        FROM top_products tp
            JOIN products p ON tp.product_id = p.id
    )
-- Финална заявка върху CTE-тата
SELECT produkt,
       tekushta_tsena,
       total_qty,
       ROUND(total_revenue, 2) AS prihod
FROM enriched
ORDER BY total_qty DESC
LIMIT 5;
```

---

---

# ЧАСТ 3: Индекси (Indices)

---

## 3.1 Какво е Индекс?

**Индексът** е допълнителна структура от данни, създадена от базата данни, която ускорява **търсенето** на записи. Аналогът в реалния живот — **азбучният индекс** в края на книга: вместо да четете всичко от начало, отивате директно на правилната страница.

```
БЕЗ ИНДЕКС (Full Table Scan):
┌────┬─────────────────┬────────┐
│ id │      name       │ price  │
├────┼─────────────────┼────────┤
│  1 │ Лаптоп Dell XPS │2199.99 │ ← проверяваме...
│  2 │ Слушалки Sony   │ 349.99 │ ← проверяваме...
│  3 │ Безжична мишка  │  59.99 │ ← намерихме!
│  4 │ Клавиатура      │ 129.99 │ ← но продължаваме до края!
│ .. │      ...        │  ...   │
└────┴─────────────────┴────────┘
WHERE name = 'Безжична мишка Logitech'  →  O(n) — сканира ВСИЧКИ редове

С ИНДЕКС (Index Lookup):
Индекс по name (B-Tree):
   Б → [Безжична мишка: ред #3]  ← директно!
   В → [...]
   Г → [...]

WHERE name = 'Безжична мишка Logitech'  →  O(log n) — директен скок!
```

### Кога индексите помагат?

| Операция | Помагат? | Пример |
|----------|----------|--------|
| `WHERE col = 'x'` | ДА | `WHERE email = 'a@b.com'` |
| `WHERE col > 100` | ДА | `WHERE price > 100` |
| `JOIN` по FK | ДА (много!) | `ON o.customer_id = c.id` |
| `ORDER BY col` | ДА | `ORDER BY price` |
| `GROUP BY col` | ЧАСТИЧНО | `GROUP BY category_id` |
| `SELECT *` без WHERE | НЕ | пълен скан така или иначе |
| Много `INSERT/UPDATE` | БАВЯТ | всяка промяна обновява индекса |

---

## 3.2 Видове Индекси

### Clustered Index (Клъстеризиран Индекс)

**Клъстеризираният индекс** определя **физическия ред на съхранение** на данните в таблицата. Данните са наредени по ключа на индекса.

```
Clustered Index по id (PRIMARY KEY):
Физически ред на дисков файл:

┌────────────────────────────────────────────────────────────┐
│ [id=1|Лаптоп|2199.99] → [id=2|Слушалки|349.99] → [id=3|..│
└────────────────────────────────────────────────────────────┘
  Данните СА наредени по id на диска — индексът и данните са ЕДНО!
```

**Ключови характеристики:**
- Може да има **само ЕДИН** clustered index на таблица (данните имат само един физически ред)
- В повечето СУБД **PRIMARY KEY автоматично** създава clustered index
- Много бърз за `WHERE id = X` и `ORDER BY id`
- Диапазонни заявки (`BETWEEN`, `>`, `<`) са ефективни

```sql
-- В SQLite PRIMARY KEY e clustered по подразбиране
CREATE TABLE products (
    id    INTEGER PRIMARY KEY,   -- ← автоматично CLUSTERED INDEX!
    name  TEXT,
    price REAL
);
```

### Non-Clustered Index (Некклъстеризиран Индекс)

**Некклъстеризираният индекс** е **отделна структура**, която съдържа копие на индексираните колони + указател (pointer) към реалния ред в таблицата.

```
Non-Clustered Index по price:

Индексна структура (B-Tree):         Реална таблица (наредена по id):
┌────────────────────────┐           ┌────┬────────────────┬────────┐
│ price  │ row_pointer   │           │ id │    name        │ price  │
├────────┼───────────────┤           ├────┼────────────────┼────────┤
│  19.99 │ → ред #15     │────────►  │  1 │ Лаптоп         │2199.99 │
│  24.99 │ → ред #14     │           │  2 │ Слушалки       │ 349.99 │
│  29.99 │ → ред #9      │           │ ...│                │        │
│  34.99 │ → ред #16     │           │ 14 │ Градинска нож. │  24.99 │
│  39.99 │ → ред #6      │           │ 15 │ Саксия         │  19.99 │
│ ...    │ ...           │           └────┴────────────────┴────────┘
└────────┴───────────────┘
  Индексът е ОТДЕЛЕН от данните — два скока: индекс → таблица
```

**Ключови характеристики:**
- Може да има **много** non-clustered индекси на таблица
- Всеки индекс заема **допълнително дисково пространство**
- Малко по-бавен от clustered (два скока вместо един), но пак много по-бърз от full scan
- Подходящ за колони, по които **често се търси, но не е PK**

---

## 3.3 Сравнение: Clustered vs Non-Clustered

```
                 CLUSTERED                    NON-CLUSTERED
                 ──────────────────────        ──────────────────────
Структура:       Данни = Индекс               Индекс е ОТДЕЛЕН
Брой:            1 на таблица                 Много на таблица
Скорост:         По-бърз (1 скок)             По-бавен (2 скока)
Място:           Включено в таблицата         Допълнително място
Кога:            PK, най-честия orderby       FK колони, WHERE колони
Пример:          id, order_number             email, city, category_id
```

---

## 3.4 Създаване на Индекси в SQL

### Основен синтаксис

```sql
-- Основен Non-Clustered индекс
CREATE INDEX idx_products_price
    ON products (price);

-- Уникален индекс (заедно предотвратява дублирани стойности)
CREATE UNIQUE INDEX idx_customers_email
    ON customers (email);

-- Съставен индекс (Composite Index) — по две и повече колони
CREATE INDEX idx_orders_customer_status
    ON orders (customer_id, status);

-- Частичен индекс (Partial Index) — само за определени редове
CREATE INDEX idx_orders_pending
    ON orders (ordered_on)
    WHERE status = 'pending';
```

### Изтриване на индекс

```sql
DROP INDEX IF EXISTS idx_products_price;
```

### Преглед на съществуващи индекси (SQLite)

```sql
-- Всички индекси в базата данни
SELECT name, tbl_name, sql
FROM sqlite_master
WHERE type = 'index'
ORDER BY tbl_name, name;

-- Индекси само на конкретна таблица
PRAGMA index_list('products');
PRAGMA index_info('idx_products_price');
```

---

## 3.5 EXPLAIN QUERY PLAN — Как SQL Изпълнява Заявката

`EXPLAIN QUERY PLAN` показва **плана за изпълнение** — дали SQL ще използва индекс или ще сканира цялата таблица.

```sql
-- БЕЗ ИНДЕКС по email:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'martina@mail.bg';
-- Output: SCAN customers  ← ЛОШ (full scan)

-- Създаваме индекс:
CREATE INDEX idx_customers_email ON customers (email);

-- С ИНДЕКС:
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'martina@mail.bg';
-- Output: SEARCH customers USING INDEX idx_customers_email (email=?)  ← ДОБЪР!
```

### Пример: Индекс за JOIN

```sql
-- Без индекс по FK:
EXPLAIN QUERY PLAN
SELECT c.first_name, o.status
FROM customers c
    JOIN orders o ON c.id = o.customer_id;
-- Output: SCAN orders  ← сканира цялата таблица при всеки JOIN

-- Създаваме индекс по FK:
CREATE INDEX idx_orders_customer_id ON orders (customer_id);

-- С индекс:
EXPLAIN QUERY PLAN
SELECT c.first_name, o.status
FROM customers c
    JOIN orders o ON c.id = o.customer_id;
-- Output: SEARCH orders USING INDEX idx_orders_customer_id (customer_id=?)  ← ДОБЪР!
```

---

## 3.6 Кога да Създаваме Индекси (и кога НЕ)

### ДА — Добри кандидати за индекс

```sql
-- 1. Foreign Key колони (много JOIN операции)
CREATE INDEX idx_orders_customer_id     ON orders      (customer_id);
CREATE INDEX idx_order_items_order_id   ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
CREATE INDEX idx_products_category_id   ON products    (category_id);

-- 2. Колони в WHERE с висока селективност (много различни стойности)
CREATE INDEX idx_customers_email ON customers (email);
CREATE INDEX idx_products_price  ON products  (price);

-- 3. Колони в ORDER BY при бавни заявки
CREATE INDEX idx_orders_ordered_on ON orders (ordered_on);

-- 4. Уникалност + бързо търсене
CREATE UNIQUE INDEX idx_customers_email ON customers (email);
```

### НЕ — Лоши кандидати за индекс

```sql
-- 1. Малко различни стойности (нисък кардиналитет)
--    status има само: 'pending','shipped','delivered','cancelled'
--    Индексът почти не помага, а заема място
CREATE INDEX idx_orders_status ON orders (status);  -- ЛОШО

-- 2. Малки таблици (< 1000 реда) — full scan е също бърз
CREATE INDEX idx_warehouses_city ON warehouses (city);  -- БЕЗСМИСЛЕНО

-- 3. Колони, по които НИКОГА не се търси или JOIN-ва
CREATE INDEX idx_customers_registered ON customers (registered);  -- вероятно излишно
```

---

## 3.7 Покриващ Индекс (Covering Index)

**Покриващият индекс** съдържа **всички колони**, нужни за заявката — SQL не трябва да отива до реалната таблица изобщо!

```sql
-- Заявката търси само email и city: 
SELECT email, city FROM customers WHERE city = 'София';

-- Нормален индекс по city:
CREATE INDEX idx_customers_city ON customers (city);
-- → Намери редовете по city, после скочи в таблицата за email

-- Покриващ индекс (включва и email):
CREATE INDEX idx_customers_city_email ON customers (city, email);
-- → Намери редовете и вземи email директно от индекса — БЕЗ таблицата!
-- EXPLAIN QUERY PLAN ще покаже: "USING COVERING INDEX"
```

---

---

# Задачи за Упражнение

> **Преди да започнете:** Изпълнете цялата SQL подготовка от началото на лекцията (DROP, CREATE, INSERT).

---

### Задача 1: Пълен каталог с категории

Напишете заявка, която показва **всички продукти** (включително тези без категория) с колоните:
- `produkt` — името на продукта
- `tsena` — цената
- `nalichnost` — брой в наличност
- `kategoriya` — името на категорията, или `'Некатегоризиран'` ако няма

Наредете резултата по `kategoriya` **възходящо**, след това по `tsena` **низходящо**.

*(Подсказка: LEFT JOIN + COALESCE или IFNULL)*

---

### Задача 2: Поръчки с детайли от 4 таблици

Напишете заявка, която свързва **customers → orders → order_items → products** и показва:
- `klient` — пълното имe на клиента
- `order_id`
- `data` — датата на поръчката
- `produkt` — имeто на продукта
- `kolichestvo`
- `unit_price` — цената при поръчката
- `red_suma` — `quantity × unit_price`

Наредете по `data` **низходящо**, после по `klient`.

---

### Задача 3: Клиенти без нито една поръчка

Намерете всички клиенти, които **никога не са поръчвали**. Покажете пълното им имe, email и град.  
Решете задачата по **два начина**:
1. С `LEFT JOIN + WHERE ... IS NULL`
2. С `NOT EXISTS`

Проверете дали двата подхода дават еднакъв резултат.

---

### Задача 4: Продукти над средната цена за категорията им

Използвайки **корелирана подзаявка**, намерете всички продукти, чиято цена е **по-висока от средната цена** за тяхната категория. Покажете:
- `produkt`
- `tsena`
- `kategoriya`
- `sredna_za_kat` — средната цена за категорията (закръглена до 2 десетични)

Наредете по `kategoriya`, след това по `tsena` низходящо.

*(Подсказка: корелирана подзаявка в WHERE или в SELECT)*

---

### Задача 5: Топ 3 клиента по обща стойност на поръчките им

Напишете заявка (с подзаявка в `FROM` или с `WITH`), която показва **трите клиента с най-голяма обща стойност** на всичките им поръчки. Покажете:
- `klient`
- `broi_poruchki`
- `obstha_suma` (закръглена до 2 десетични)

*(Подсказка: JOIN 3 таблици → GROUP BY → ORDER BY → LIMIT 3)*

---

### Задача 6: Продукти, наредени по продажби

Използвайки **`WITH` (CTE)**, намерете колко пъти е поръчван всеки продукт и каква е общата сума от продажбите му. Покажете:
- `produkt`
- `kategoriya` (или `'Некатегоризиран'`)
- `broi_poruchki` — в колко различни поръчки е участвал
- `total_kolichestvo` — общо продадени бройки
- `total_prihod` (закръглен до 2 десетични)

Включете и продукти, **които никога не са поръчвани** (с нули). Наредете по `total_prihod` низходящо.

*(Подсказка: CTE с LEFT JOIN от products → order_items)*

---

### Задача 7: Клиенти от един и същи град (SELF JOIN)

Напишете заявка с `SELF JOIN`, която показва всички **двойки клиенти** от един и същи **град** (с поне 2 клиента). Покажете:
- `klient_1`
- `klient_2`
- `grad`

Избегнете дублиращи двойки (А-Б и Б-А да не се появяват и двете).

---

### Задача 8: Създаване на Индекси

Анализирайте следните заявки и за всяка от тях:
1. Напишете `EXPLAIN QUERY PLAN` и запишете наблюдението си (scan vs search)
2. Създайте подходящ индекс
3. Пуснете `EXPLAIN QUERY PLAN` отново и отбележете разликата

**Заявки за анализ:**

```sql
-- A: Търсене по email
SELECT * FROM customers WHERE email = 'stefan@mail.bg';

-- B: Филтриране на поръчки по статус и дата
SELECT * FROM orders WHERE status = 'shipped' AND ordered_on > '2024-02-01';

-- C: JOIN по foreign key
SELECT c.first_name, o.id, o.status
FROM customers c
    JOIN orders o ON c.id = o.customer_id
WHERE c.city = 'София';
```

Напишете `CREATE INDEX` командите с описателни имена.

---

### Задача 9: Подзаявка с EXISTS — Категории с продукти над 100 лв.

Напишете заявка, която извежда само **категориите**, в които **съществува поне един продукт** с цена над `100.00` лева. Използвайте `EXISTS`.

Покажете: `kategoriya_id`, `kategoriya_ime`, и `max_tsena` в категорията.

---

### Задача 10: Комплексен Анализ — Приход по Град и Категория

Напишете **комплексна заявка** с `WITH`, която показва приходите, разбити по **град на клиента** и **категория продукт**. Включете само доставени поръчки (`status = 'delivered'`). Покажете:
- `grad`
- `kategoriya`
- `broi_poruchki` — брой поръчки
- `prihod` — сумарен приход (закръглен до 2 десетични)

Наредете по `grad`, след това по `prihod` низходящо.

*(Подсказка: CTE → JOIN customers, orders, order_items, products, categories → GROUP BY grad, kategoriya)*

---

*Следваща лекция: **VIEW**, **Транзакции (COMMIT / ROLLBACK)**, **Тригери (Triggers)** и **Агрегатни прозорни функции (Window Functions)**.*

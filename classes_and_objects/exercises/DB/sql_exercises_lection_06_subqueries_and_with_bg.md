# SQL Упражнения — Лекция 6, Част 1: Подзаявки и WITH (CTE)

Използвайте таблиците от **Лекция 6**. Ако не сте ги създали, изпълнете следното:

```sql
PRAGMA foreign_keys = ON;

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
    ('Разширител USB-C',         34.99, 55,  NULL);

INSERT INTO warehouses (city, capacity) VALUES
    ('София',   5000),
    ('Пловдив', 3000),
    ('Варна',   2500);

INSERT INTO customers (first_name, last_name, email, city, registered) VALUES
    ('Мартина',   'Колева',    'martina@mail.bg',   'София',    '2022-03-15'),
    ('Стефан',    'Димов',     'stefan@mail.bg',    'Пловдив',  '2021-07-20'),
    ('Галина',    'Пенева',    'galina@mail.bg',    'Варна',    '2023-01-10'),
    ('Борислав',  'Неделчев',  'borislav@mail.bg',  'София',    '2020-11-05'),
    ('Цветелина', 'Атанасова', 'cveta@mail.bg',     'Бургас',   '2023-09-22'),
    ('Радослав',  'Иванов',    'radoslav@mail.bg',  'София',    '2024-01-30'),
    ('Деница',    'Георгиева', 'denica@mail.bg',    'Пловдив',  '2022-06-18'),
    ('Калоян',    'Тодоров',   'kaloyan@mail.bg',   'Варна',    '2021-12-01'),
    ('Ивета',     'Стоянова',  'iveta@mail.bg',     'София',    '2023-04-14'),
    ('Никола',    'Петров',    'nikola@mail.bg',    'Русе',     '2024-02-28');

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
    (1,  1,  1, 2199.99),
    (1,  3,  1,   59.99),
    (2,  2,  1,  349.99),
    (3,  6,  2,   39.99),
    (3,  7,  1,   44.99),
    (4,  12, 1,   49.99),
    (4,  13, 1,   89.99),
    (5,  1,  1, 2199.99),
    (5,  4,  1,  129.99),
    (5,  5,  1,  699.99),
    (6,  9,  3,   29.99),
    (7,  11, 1,  189.99),
    (8,  8,  1,   49.99),
    (8,  6,  1,   39.99),
    (9,  15, 2,   19.99),
    (10, 2,  1,  349.99),
    (10, 3,  2,   59.99),
    (11, 16, 1,   34.99);
```

---

## Упражнения 1–5: Подзаявки (Subqueries)

---

### Упражнение 1: Продукти над средната цена *(лесно)*

Напишете заявка, която извежда `name` и `price` на всички продукти, чиято цена е **над средната цена** на всички продукти в базата данни.  
Наредете по `price` **низходящо**.

**Очакван резултат (извадка):**
```
name                    | price
------------------------|--------
Лаптоп Dell XPS         | 2199.99
Монитор LG 27"          |  699.99
Слушалки Sony WH-1000   |  349.99
Маратонки Nike Air      |  189.99
Яке Зимно               |  149.99
...
```

*(Подсказка: скаларна подзаявка в `WHERE` с `AVG(price)`)*

---

### Упражнение 2: Клиенти, поръчали поне веднъж *(лесно)*

Напишете заявка с `IN`, която извежда пълното име (`klient`) и `email` на всички клиенти, които имат **поне една поръчка** в системата.  
Наредете по пълното им име **възходящо**.

**Очакван резултат (извадка):**
```
klient                  | email
------------------------|--------------------
Борислав Неделчев       | borislav@mail.bg
Галина Пенева           | galina@mail.bg
Деница Георгиева        | denica@mail.bg
...
```

*(Подсказка: `WHERE c.id IN (SELECT DISTINCT customer_id FROM orders)`)*

---

### Упражнение 3: Клиенти без нито една поръчка *(лесно–средно)*

Напишете заявка с `NOT EXISTS`, която извежда пълното име и `city` на клиентите, **нямащи нито една поръчка** в системата.  
Наредете по `city`, след това по пълното им имe **възходящо**.

**Очакван резултат:**
```
klient              | city
--------------------|--------
Цветелина Атанасова | Бургас
Калоян Тодоров      | Варна
```

*(Подсказка: `WHERE NOT EXISTS (SELECT 1 FROM orders WHERE orders.customer_id = c.id)`)*

---

### Упражнение 4: Продукти, никога не поръчвани *(средно)*

Напишете заявка с `NOT IN`, която показва `name`, `price` и `stock` на продуктите, **за които няма нито един ред в `order_items`**.  
Наредете по `price` **низходящо**.

**Очакван резултат:**
```
name            | price  | stock
----------------|--------|------
Яке Зимно       | 149.99 | 25
Гири 10кг Комплект|  89.99| 18
Yoga Mat 6мм    |  49.99 | 45
Тениска Памучна XL| 29.99|100
Градинска Ножица|  24.99 | 70
```

*(Подсказка: `WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items)`)*

---

### Упражнение 5: Продукт с най-висока продажна единична цена *(средно)*

Намерете **продукта** (по `name`) и **поръчката** (по `order_id`), в която е фигурирал с **най-висока `unit_price`** от цялата таблица `order_items`.  
Изведете `name` на продукта, `order_id` и `unit_price`.

*(Подсказка: скаларна подзаявка `WHERE oi.unit_price = (SELECT MAX(unit_price) FROM order_items)`; направете JOIN с `products`)*

---

### Упражнение 6: Корелирана подзаявка — продукти над средната за категорията *(средно–трудно)*

Напишете заявка с **корелирана подзаявка**, която извежда `name`, `price` и `category_id` на продуктите, чиято цена е **над средната цена в тяхната собствена категория**.  
Включете само продукти с непразна категория (`category_id IS NOT NULL`).  
Наредете по `category_id` **възходящо**, след това по `price` **низходящо**.

**Очакван резултат (извадка):**
```
name                    | price   | category_id
------------------------|---------|------------
Лаптоп Dell XPS         | 2199.99 | 1
Монитор LG 27"          |  699.99 | 1
Слушалки Sony WH-1000   |  349.99 | 1
Чист Код - Р. Мартин    |   49.99 | 2
Яке Зимно               |  149.99 | 3
Маратонки Nike Air      |  189.99 | 4
...
```

*(Подсказка: `WHERE p.price > (SELECT AVG(p2.price) FROM products p2 WHERE p2.category_id = p.category_id)`)*

---

### Упражнение 7: Derived table — топ 3 клиента по обща сума *(средно–трудно)*

Напишете заявка, в която **подзаявката в `FROM`** пресмята общата сума на поръчките за всеки клиент, а външната заявка взема **топ 3** с най-висока обща сума.  
Изведете пълното им имe (`klient`) и `ROUND(obshta_suma, 2)` като `obshta_suma`.  
Наредете по `obshta_suma` **низходящо**.

**Очакван резултат:**
```
klient              | obshta_suma
--------------------|------------
Борислав Неделчев   | 3029.97
Мартина Колева      | 2609.97
Ивета Стоянова      |  349.99
```

*(Подсказка: `FROM (SELECT o.customer_id, SUM(...) AS obshta_suma FROM orders o JOIN order_items oi ... GROUP BY o.customer_id) AS totals JOIN customers ...`)*

---

## Упражнения 8–10: WITH (CTE)

---

### Упражнение 8: CTE — поръчки над 500 лв. *(лесно CTE)*

С помощта на **WITH** дефинирайте CTE на име `order_totals`, което пресмята общата сума на всяка поръчка (`order_id`, `customer_id`, `suma`).  
След това изведете от CTE-то пълното имe на клиента (`klient`), `order_id` и `ROUND(suma, 2)` само за поръчките с `suma > 500`.  
Наредете по `suma` **низходящо**.

**Очакван резултат:**
```
klient              | order_id | suma
--------------------|----------|--------
Борислав Неделчев   | 5        | 3029.97
Мартина Колева      | 1        | 2259.98
Ивета Стоянова      | 10       |  469.97
...
```

*(Подсказка: `WITH order_totals AS (SELECT o.id AS order_id, o.customer_id, SUM(oi.quantity * oi.unit_price) AS suma FROM orders o JOIN order_items oi ON o.id = oi.order_id GROUP BY o.id, o.customer_id)`)*

---

### Упражнение 9: Множество CTE — топ продукт по приход за всяка категория *(трудно)*

Напишете заявка с **две CTE**:

1. **`product_revenue`** — пресмята общия приход (`total_revenue`) за всеки `product_id` от `order_items`.
2. **`ranked`** — обединява с `products` и `categories`, и за всяка категория определя продукта с **най-висок приход** (`RANK()` или подзаявка по ваш избор).

Финалната заявка извежда `kategoriya`, `produkt` и `ROUND(total_revenue, 2)` само за **ранк 1** (най-добрият продукт) от всяка категория.  
Наредете по `total_revenue` **низходящо**.

**Очакван резултат:**
```
kategoriya      | produkt              | total_revenue
----------------|----------------------|-------------
Електроника     | Лаптоп Dell XPS      | 4399.98
Книги           | SQL за начинаещи     |  119.97
Спорт           | Маратонки Nike Air   |  189.99
Дом и Градина   | Саксия Керамична     |   39.98
```

*(Подсказка: в третото CTE или директно в `WHERE` използвайте `total_revenue = (SELECT MAX(...) FROM product_revenue pr2 JOIN products p2 ON ... WHERE p2.category_id = p.category_id)`)*

---

### Упражнение 10: CTE с EXISTS — активни клиенти от София с повече от 1 поръчка *(трудно)*

Напишете заявка, която комбинира **WITH** и **EXISTS**:

1. Дефинирайте CTE на ime `sofia_customers`, което извежда всички клиенти от **`'София'`**.
2. От CTE-то изберете само тези клиенти, за които `EXISTS` поне **2 поръчки** в таблицата `orders`.

Изведете `first_name`, `last_name`, `email` и `registered` на тези клиенти.  
Наредете по `registered` **възходящо**.

**Очакван резултат:**
```
first_name | last_name | email             | registered
-----------|-----------|-------------------|------------
Борислав   | Неделчев  | borislav@mail.bg  | 2020-11-05
Мартина    | Колева    | martina@mail.bg   | 2022-03-15
```

*(Подсказка: `WITH sofia_customers AS (SELECT * FROM customers WHERE city = 'София')` → `WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = sc.id HAVING COUNT(*) >= 2)`)*

# SQL Упражнения — Лекция 6, Част 2: Индекси (Indexes)

Използвайте таблиците от **Лекция 6**. Ако не сте ги създали, изпълнете схемата от файла с упражнения за подзаявки или директно от лекцията.

> **Важно:** Упражненията за индекси изискват `EXPLAIN QUERY PLAN` и `PRAGMA` команди, достъпни в **SQLite**. Изпълнявайте ги в DB Browser for SQLite или SQLite CLI.

---

## Упражнения 1–4: Създаване и проверка на индекси

---

### Упражнение 1: Първи поглед — full scan без индекс *(лесно)*

Изпълнете следната заявка с `EXPLAIN QUERY PLAN` **преди** да създадете какъвто и да е индекс:

```sql
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE city = 'София';
```

**Въпроси:**
1. Какво пише в колона `detail` на резултата? Виждате ли думата `SCAN` или `SEARCH`?
2. Какво означава `SCAN`? Ефективна ли е тази операция, ако таблицата има 1 000 000 реда?
3. Каква е сложността на операцията — O(1), O(log n) или O(n)?

*(Подсказка: очаквайте нещо от рода на `SCAN customers`)*

---

### Упражнение 2: Създайте индекс по `city` и проверете разликата *(лесно)*

1. Създайте **non-clustered индекс** с ime `idx_customers_city` върху колона `city` в таблица `customers`.
2. Изпълнете отново `EXPLAIN QUERY PLAN` за същата заявка от Упражнение 1.
3. Сравнете резултата — видите ли `SEARCH` вместо `SCAN`?

```sql
-- Стъпка 1: Създайте индекса
CREATE INDEX idx_customers_city ON customers (city);

-- Стъпка 2: Проверете плана
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE city = 'София';
```

**Въпроси:**
1. Какво пише сега в `detail`? Споменава ли се `idx_customers_city`?
2. С какво е по-бързо търсенето с B-Tree индекс в сравнение с full scan?
3. Подходящ ли е индекс по `city`, ако стойностите са само 5–6 различни града? Защо или защо не?

---

### Упражнение 3: Уникален индекс и проверка на ограничения *(лесно–средно)*

Колоната `email` в `customers` вече има `UNIQUE` ограничение, което SQLite поддържа с вграден индекс.

1. Изпълнете `PRAGMA index_list('customers');` — колко индекса виждате и какви са имената им?
2. Напишете заявка с `EXPLAIN QUERY PLAN`, която търси клиент по `email`. Използва ли се индексът?
3. Опитайте да вмъкнете втори ред с вече съществуващ имейл:

```sql
INSERT INTO customers (first_name, last_name, email, city, registered)
VALUES ('Тест', 'Тестов', 'martina@mail.bg', 'Варна', '2024-06-01');
```

**Въпроси:**
1. Каква грешка получавате и защо?
2. Каква е разликата между `CREATE UNIQUE INDEX` и обикновен `CREATE INDEX`?

---

### Упражнение 4: Съставен индекс (Composite Index) *(средно)*

Честа заявка в приложението е: „намери всички поръчки на даден клиент с определен статус".

1. Създайте **съставен индекс** `idx_orders_customer_status` по колоните `customer_id` и `status` в таблица `orders`.
2. Проверете с `EXPLAIN QUERY PLAN` дали следната заявка го използва:

```sql
EXPLAIN QUERY PLAN
SELECT id, ordered_on, status
FROM orders
WHERE customer_id = 4 AND status = 'delivered';
```

3. Проверете и тази заявка — използва ли се пак индексът, когато търсим само по `customer_id`?

```sql
EXPLAIN QUERY PLAN
SELECT id, ordered_on, status
FROM orders
WHERE customer_id = 4;
```

**Въпроси:**
1. Защо редът на колоните в съставния индекс (`customer_id, status`) е важен?
2. Ако беше `(status, customer_id)`, щеше ли заявката `WHERE customer_id = 4` да използва индекса?

---

## Упражнения 5–7: Частичен индекс и индекс за JOIN

---

### Упражнение 5: Частичен индекс за активни поръчки *(средно)*

Приложението много по-често работи с поръчки в статус `'pending'` и `'shipped'`, отколкото с приключени.

1. Създайте **частичен (partial) индекс** `idx_orders_active` върху колона `ordered_on` в `orders`, но само за редовете, при които `status IN ('pending', 'shipped')`.
2. Изпълнете `EXPLAIN QUERY PLAN` за:

```sql
EXPLAIN QUERY PLAN
SELECT id, customer_id, ordered_on
FROM orders
WHERE status = 'pending'
ORDER BY ordered_on;
```

3. Изпълнете `EXPLAIN QUERY PLAN` за поръчки с `status = 'delivered'` — използва ли се индексът?

**Въпроси:**
1. Какво е предимството на частичния индекс пред пълния индекс по `ordered_on`?
2. В кои реални сценарии е полезен частичен индекс?

---

### Упражнение 6: Индекс за ускоряване на JOIN *(средно–трудно)*

Без индекс по FK колоните, JOIN операциите правят full scan.

1. Проверете **преди** добавяне на индекс:

```sql
EXPLAIN QUERY PLAN
SELECT c.first_name, c.last_name, o.status, o.ordered_on
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id
WHERE c.city = 'София';
```

2. Ако нямате `idx_customers_city` и `idx_orders_customer_status` от предишните задачи, създайте ги сега. Изпълнете плана отново.
3. Обяснете стъпка по стъпка как SQL Engine ще изпълни заявката **с** индексите.

**Въпроси:**
1. Защо FK колоните (като `orders.customer_id`) са особено добри кандидати за индексиране?
2. Колко full scan операции се правят без индекси при тази заявка? А с индекси?

---

### Упражнение 7: Преглед на всички индекси в базата данни *(средно)*

1. Напишете заявка, която показва **всички индекси** в текущата SQLite база данни — техните имена, таблиците, към които принадлежат, и SQL командата за създаването им:

```sql
SELECT name, tbl_name, sql
FROM sqlite_master
WHERE type = 'index'
ORDER BY tbl_name, name;
```

2. Разгледайте резултата. Кои индекси са **автоматично създадени** от SQLite (за PK и UNIQUE) и кои сте създали вие?
3. Изтрийте индекса `idx_customers_city` и проверете дали изчезва от списъка.

```sql
DROP INDEX IF EXISTS idx_customers_city;
```

---

## Упражнения 8–10: Напреднало — производителност и дизайн

---

### Упражнение 8: Кога индексите вредят? *(средно–трудно)*

Индексите ускоряват четенето, но **забавят писането**.

1. Изпълнете следната заявка, за да симулирате масово вмъкване на 500 броя поръчки в таблица `orders` — **преди** и **след** като добавите индекс по `ordered_on`:

```sql
-- Масово вмъкване (изпълнете с различни параметри преди/след индекс)
WITH RECURSIVE gen(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM gen WHERE n < 500
)
INSERT INTO orders (customer_id, ordered_on, status)
SELECT (n % 10) + 1,
       DATE('2024-01-01', '+' || n || ' days'),
       CASE (n % 4)
           WHEN 0 THEN 'pending'
           WHEN 1 THEN 'shipped'
           WHEN 2 THEN 'delivered'
           ELSE 'cancelled'
       END
FROM gen;
```

**Въпроси:**
1. Ако имате 10 индекса на таблица с 10 млн. реда — всеки `INSERT` трябва да обнови колко структури?
2. В кои сценарии е по-добре да **нямате** индекс на дадена колона?
3. Как се справят СУБД-и с масово зареждане на данни (bulk insert) при наличие на много индекси?

---

### Упражнение 9: Анализ — кои колони заслужават индекс? *(трудно)*

Разгледайте следните 5 заявки и за **всяка** решете: трябва ли нов индекс и защо?

**Заявка А:**
```sql
SELECT * FROM products WHERE stock < 20;
```

**Заявка Б:**
```sql
SELECT * FROM products WHERE category_id = 1 ORDER BY price DESC;
```

**Заявка В:**
```sql
SELECT COUNT(*) FROM order_items;
```

**Заявка Г:**
```sql
SELECT * FROM order_items WHERE order_id = 5;
```

**Заявка Д:**
```sql
SELECT first_name, last_name FROM customers ORDER BY last_name, first_name;
```

За всяка заявка:
1. Предложете конкретна `CREATE INDEX` команда (ако е нужна).
2. Обяснете избора си — коя колона, защо точно тя.
3. Посочете дали е прост, съставен или частичен индекс.

---

### Упражнение 10: Пълен сценарий — оптимизация на бавна заявка *(трудно)*

Дадена е следната сложна заявка, за която се оплакват потребители, че е бавна при голям обем данни:

```sql
SELECT c.first_name || ' ' || c.last_name  AS klient,
       c.city,
       cat.name                             AS kategoriya,
       SUM(oi.quantity * oi.unit_price)     AS obshta_suma,
       COUNT(DISTINCT o.id)                 AS broi_poruchki
FROM customers      AS c
    JOIN orders         AS o   ON c.id          = o.customer_id
    JOIN order_items    AS oi  ON o.id           = oi.order_id
    JOIN products       AS p   ON oi.product_id  = p.id
    JOIN categories     AS cat ON p.category_id  = cat.id
WHERE c.city        = 'София'
  AND o.status      = 'delivered'
  AND cat.name      != 'Дрехи'
GROUP BY c.id, c.first_name, c.last_name, c.city, cat.id, cat.name
HAVING SUM(oi.quantity * oi.unit_price) > 100
ORDER BY obshta_suma DESC;
```

**Задачи:**
1. Изпълнете `EXPLAIN QUERY PLAN` за тази заявка **без допълнителни индекси** (след `DROP INDEX` на всичко, което сте създали). Отбележете кои стъпки са `SCAN`.
2. Предложете **минималния набор от индекси**, с които да елиминирате full scan-овете. Напишете `CREATE INDEX` командите.
3. Изпълнете плана отново **с** индексите — сравнете броя на сканиранията.
4. Има ли клауза в заявката, на която **индекс не може да помогне**? Коя е тя и защо?

*(Подсказка: разгледайте JOIN условията и WHERE клаузата — всяка колона, по която се JOIN-ва или филтрира, е кандидат за индекс. Внимавайте с `cat.name != 'Дрехи'` — негативното условие.)*

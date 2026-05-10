# SQL Упражнения — Лекция 7: Индекси — Задълбочено (B-Tree, Clustered, Covering)

Използвайте таблиците от **Лекция 7**. Ако не сте ги създали, изпълнете схемата от файла с лекция или от Лекция 6.

> **Важно:** Упражненията изискват `EXPLAIN QUERY PLAN` и `PRAGMA` команди, достъпни в **SQLite**. Изпълнявайте ги в DB Browser for SQLite или SQLite CLI.

> **Преди да започнете:** Изтрийте всички индекси, за да стартирате от чисто:
> ```sql
> DROP INDEX IF EXISTS idx_customers_email;
> DROP INDEX IF EXISTS idx_customers_city;
> DROP INDEX IF EXISTS idx_customers_city_email;
> DROP INDEX IF EXISTS idx_customers_city_last_first_email;
> DROP INDEX IF EXISTS idx_products_price;
> DROP INDEX IF EXISTS idx_products_category_id;
> DROP INDEX IF EXISTS idx_products_category_price;
> DROP INDEX IF EXISTS idx_orders_customer_id;
> DROP INDEX IF EXISTS idx_orders_status;
> DROP INDEX IF EXISTS idx_orders_customer_status;
> DROP INDEX IF EXISTS idx_orders_ordered_on;
> DROP INDEX IF EXISTS idx_orders_active;
> DROP INDEX IF EXISTS idx_order_items_order_id;
> DROP INDEX IF EXISTS idx_order_items_product_id;
> ```

---

## Упражнения 1–3: Full Table Scan и B-Tree — Виждаме разликата

---

### Упражнение 1: SCAN срещу SEARCH — страна преди и след индекс *(лесно)*

Изпълнете `EXPLAIN QUERY PLAN` за следните четири заявки **преди** да създадете какъвто и да е допълнителен индекс. Запишете резултата за всяка:

```sql
-- A: Точно търсене по email
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'borislav@mail.bg';

-- B: Диапазон по цена
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price BETWEEN 30 AND 150;

-- C: Сортиране по дата на поръчка
EXPLAIN QUERY PLAN
SELECT id, ordered_on, status FROM orders ORDER BY ordered_on DESC;

-- D: Търсене по PRIMARY KEY (id)
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE id = 5;
```

**Задачи:**
1. За кои заявки виждате `SCAN` и за коя виждате `SEARCH`? Защо заявка D се различава?
2. Какво означава думата `SCAN` в изхода и защо е проблем при таблица с 10 000 000 реда?
3. Каква е разликата в сложността: O(n) срещу O(log n)? Колко стъпки би направил B-Tree при 1 000 000 реда?
4. Сега създайте индекси за заявки A, B и C и изпълнете `EXPLAIN QUERY PLAN` отново. Какво се промени?

*(Подсказка: заявка D търси по PRIMARY KEY — той автоматично е Clustered Index.)*

---

### Упражнение 2: Clustered Index — разбираме PRIMARY KEY *(лесно)*

В SQLite PRIMARY KEY автоматично създава Clustered Index. Нека го видим на практика.

**Стъпка 1:** Изпълнете следните три заявки с `EXPLAIN QUERY PLAN` и запишете изхода:

```sql
-- Точно търсене по id (Clustered Index)
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE id = 7;

-- Диапазон по id (Clustered Index)
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE id BETWEEN 3 AND 10;

-- Сортиране по id (Clustered Index — вече наредено!)
EXPLAIN QUERY PLAN
SELECT id, name, price FROM products ORDER BY id;
```

**Стъпка 2:** Изпълнете същите типове заявки, но по неиндексирана колона `price`:

```sql
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price = 349.99;

EXPLAIN QUERY PLAN
SELECT * FROM products WHERE price BETWEEN 30 AND 150;

EXPLAIN QUERY PLAN
SELECT id, name, price FROM products ORDER BY price;
```

**Въпроси:**
1. Кои заявки показват `USING INTEGER PRIMARY KEY (rowid=?)`? 
2. Кои заявки правят `SCAN`? Защо?
3. Колко Clustered Index-а може да има една таблица и защо?
4. Добавете `CREATE INDEX idx_products_price ON products (price);` и изпълнете заявките по `price` отново. Сега Non-Clustered Index ли е или Clustered?

---

### Упражнение 3: B-Tree и диапазонни заявки *(лесно–средно)*

B-Tree индексите са особено ефективни при диапазонни заявки (`BETWEEN`, `>`, `<`, `LIKE 'prefix%'`), защото листата в B-Tree са свързани последователно.

1. Създайте индекс по `price` в `products`:
   ```sql
   CREATE INDEX idx_products_price ON products (price);
   ```

2. Изпълнете `EXPLAIN QUERY PLAN` за следните заявки и запишете дали се ползва индексът:

```sql
-- A: Точно съответствие
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price = 49.99;

-- B: По-голямо от
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price > 100;

-- C: BETWEEN
EXPLAIN QUERY PLAN
SELECT name, price FROM products WHERE price BETWEEN 30 AND 200;

-- D: Сортиране по цена
EXPLAIN QUERY PLAN
SELECT name, price FROM products ORDER BY price ASC;

-- E: LIKE с префикс (ако имахме текстов индекс)
EXPLAIN QUERY PLAN
SELECT first_name, last_name FROM customers WHERE last_name LIKE 'П%';
```

**Въпроси:**
1. Кои заявки ползват индекса? Кои правят SCAN?
2. Защо `LIKE 'П%'` може да ползва индекс, а `LIKE '%тров'` не може?
3. Какво означава, че листата на B-Tree са свързани — как помага при диапазонни заявки?
4. При диапазонна заявка `WHERE price > 100` — ако 90% от продуктите са над 100 лв., ще реши ли SQL Query Optimizer да ползва индекса? Защо или защо не?

---

## Упражнения 4–6: Non-Clustered и Covering индекси

---

### Упражнение 4: Non-Clustered Index — как работи вътрешно *(средно)*

Non-Clustered Index е **отделна B-Tree структура** с указатели към редовете в таблицата. Нека видим разликата в практиката.

1. Проверете с `PRAGMA index_list('customers');` — колко индекса има в момента и от какъв вид са.

2. Създайте Non-Clustered индекс по `city`:
   ```sql
   CREATE INDEX idx_customers_city ON customers (city);
   ```

3. Изпълнете следните заявки и обяснете броя на "скоковете" (operations):

```sql
-- A: Търсим само email по city — 2 скока (индекс → таблица)
EXPLAIN QUERY PLAN
SELECT email FROM customers WHERE city = 'София';

-- B: Търсим id по city — 1 скок (индекс съдържа rowid)
EXPLAIN QUERY PLAN
SELECT id FROM customers WHERE city = 'Пловдив';

-- C: JOIN с orders — колко SCAN операции?
EXPLAIN QUERY PLAN
SELECT c.first_name, o.ordered_on
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id
WHERE c.city = 'Sofia';
```

**Въпроси:**
1. Обяснете разликата между Clustered и Non-Clustered Index с думи.
2. Колко допълнителни Non-Clustered Index-а може да има дадена таблица?
3. Има ли случаи, когато Non-Clustered Index всъщност не се ползва дори ако съществува? (Подсказка: помислете за кардиналитет — колко уникални стойности има в `city`?)
4. Добавете `CREATE INDEX idx_orders_customer_id ON orders (customer_id);` и изпълнете заявка C отново. Подобрява ли се планът?

---

### Упражнение 5: Съставен индекс — ред на колоните е от значение *(средно)*

При съставен индекс (Composite Index) редът на колоните е критично важен за ефективността.

1. Създайте съставен индекс `(customer_id, status)` в таблица `orders`:
   ```sql
   CREATE INDEX idx_orders_customer_status ON orders (customer_id, status);
   ```

2. Тествайте с `EXPLAIN QUERY PLAN` дали следните заявки ползват индекса:

```sql
-- A: Двете колони — трябва да ползва индекса
EXPLAIN QUERY PLAN
SELECT id, ordered_on FROM orders
WHERE customer_id = 4 AND status = 'delivered';

-- B: Само водещата колона — трябва да ползва индекса
EXPLAIN QUERY PLAN
SELECT id, ordered_on FROM orders
WHERE customer_id = 1;

-- C: Само втората колона — може да не ползва индекса!
EXPLAIN QUERY PLAN
SELECT id, ordered_on FROM orders
WHERE status = 'pending';
```

3. За заявка C — добавете **отделен** индекс по `status` и тествайте пак:
   ```sql
   CREATE INDEX idx_orders_status ON orders (status);
   ```

**Въпроси:**
1. Защо заявка B ползва `idx_orders_customer_status`, но не и заявка C?
2. Обяснете правилото „left-prefix rule" (правило за ляв префикс) при съставни индекси.
3. Ако беше `(status, customer_id)` вместо `(customer_id, status)`, коя от заявките A, B, C щеше да работи добре и коя не?
4. Кой индекс бихте избрали за система, в която най-честата заявка е `WHERE customer_id = X AND status = Y`?

---

### Упражнение 6: Покриващ индекс (Covering Index) *(средно–трудно)*

**Покриващ индекс** е индекс, който съдържа **всички колони**, нужни за изпълнение на заявката. SQL Engine не трябва да отива до основната таблица — получава всичко директно от индекса.

Следната заявка се изпълнява много често в приложението:

```sql
SELECT first_name, last_name, email
FROM customers
WHERE city = 'София'
ORDER BY last_name;
```

1. Изпълнете `EXPLAIN QUERY PLAN` без допълнителни индекси — запишете изхода.

2. Създайте обикновен индекс само по `city`:
   ```sql
   CREATE INDEX idx_customers_city ON customers (city);
   ```
   Изпълнете `EXPLAIN QUERY PLAN` отново. Ползва ли се индексът? Вижда ли се `COVERING`?

3. Изтрийте горния индекс и създайте **покриващ индекс**:
   ```sql
   DROP INDEX IF EXISTS idx_customers_city;
   CREATE INDEX idx_customers_city_last_first_email
       ON customers (city, last_name, first_name, email);
   ```
   Изпълнете `EXPLAIN QUERY PLAN` отново.

4. Сравнете изходите от стъпки 1, 2 и 3.

**Въпроси:**
1. Кой изход показва `COVERING INDEX`? Какво означава това за броя на операциите?
2. Колко „скока" прави заявката в стъпка 2 vs. стъпка 3? (Подсказка: in стъпка 2 — 2 скока; в стъпка 3 — 1 скок.)
3. Какъв е недостатъкът на покриващ индекс с много колони?
4. При покриващ индекс `(city, last_name, first_name, email)`, може ли заявката `WHERE city = 'Варна' ORDER BY last_name` да се изпълни само с индекса?

---

## Упражнения 7–10: Напреднало — оптимизация и проектиране

---

### Упражнение 7: Частичен индекс — пестим място и подобряваме скоростта *(средно–трудно)*

Частичен индекс индексира само редовете, отговарящи на дадено условие (WHERE клауза в `CREATE INDEX`).

В реална система „доставените" поръчки (`delivered`) са архивни и **рядко се търсят**. Активните (`pending`, `shipped`) се търсят постоянно.

1. Създайте **частичен индекс** по `ordered_on`, само за активни поръчки:
   ```sql
   CREATE INDEX idx_orders_active
       ON orders (ordered_on)
       WHERE status IN ('pending', 'shipped');
   ```

2. Тествайте кои заявки ползват частичния индекс:
   ```sql
   -- A: Трябва да ползва частичния индекс
   EXPLAIN QUERY PLAN
   SELECT id, customer_id, ordered_on
   FROM orders
   WHERE status = 'pending'
   ORDER BY ordered_on;

   -- B: НЕ трябва да ползва частичния индекс
   EXPLAIN QUERY PLAN
   SELECT id, customer_id, ordered_on
   FROM orders
   WHERE status = 'delivered'
   ORDER BY ordered_on;

   -- C: Заявката ползва условие, което включва частичния индекс
   EXPLAIN QUERY PLAN
   SELECT id, customer_id, ordered_on
   FROM orders
   WHERE status = 'shipped'
     AND ordered_on > '2024-01-01';
   ```

3. Проверете размера на индексите с `PRAGMA index_list('orders');`.

**Въпроси:**
1. Защо заявка B не ползва `idx_orders_active`?
2. В кои реални сценарии е полезен частичен индекс (дайте 2 примера от реални приложения)?
3. Ако таблицата `orders` има 1 000 000 реда, от които само 50 000 са `pending` или `shipped` — с колко реда по-малко е частичният индекс в сравнение с пълния?
4. Може ли `CREATE INDEX ... WHERE status = 'pending' OR status = 'shipped'` да се замени с `WHERE status IN ('pending', 'shipped')`?

---

### Упражнение 8: Индексиране на JOIN — оптимизация на сложна заявка *(средно–трудно)*

Следната заявка е "горещата заявка" в системата — изпълнява се хиляди пъти на ден:

```sql
SELECT c.first_name || ' ' || c.last_name AS klient,
       c.city,
       p.name                              AS produkt,
       oi.quantity,
       oi.unit_price,
       o.ordered_on
FROM customers      AS c
    JOIN orders      AS o  ON c.id          = o.customer_id
    JOIN order_items AS oi ON o.id          = oi.order_id
    JOIN products    AS p  ON oi.product_id = p.id
WHERE c.city   = 'София'
  AND o.status = 'delivered'
ORDER BY o.ordered_on DESC;
```

1. Уверете се, че **нямате допълнителни индекси** (използвайте `DROP INDEX IF EXISTS ...`). Изпълнете `EXPLAIN QUERY PLAN` и запишете всички `SCAN` операции.

2. За всяка `SCAN` операция анализирайте:
   - По коя колона се филтрира или JOIN-ва?
   - Каква е подходящата `CREATE INDEX` команда?

3. Добавете индексите **по един** и след всеки проверявайте с `EXPLAIN QUERY PLAN` дали `SCAN` се е превърнал в `SEARCH`.

4. Намерете **минималния набор от индекси**, при който всички операции са `SEARCH` (или поне повечето).

**Въпроси:**
1. Защо FK колоните (като `orders.customer_id`, `order_items.order_id`) са добри кандидати за индексиране?
2. Ако добавите 10 индекса — всеки `INSERT` в коя таблица ще е най-бавен и защо?
3. Дали индекс по `products.id` помага на тази заявка? Обяснете.
4. Как се казва техниката, при която добавяте всички нужни колони (включително `ordered_on`) в индекса, за да избегнете достъпа до таблицата?

---

### Упражнение 9: Кардиналитет и избор на индекс *(трудно)*

**Кардиналитет** (cardinality) е броят на уникалните стойности в колона. Висок кардиналитет → добър кандидат за индекс. Нисък кардиналитет → индексът може да е безполезен.

1. Напишете заявки с `COUNT(DISTINCT ...)` за следните колони и запишете резултата:

```sql
SELECT COUNT(DISTINCT city)        AS unikalni_gradove  FROM customers;
SELECT COUNT(DISTINCT status)      AS unikalni_statusove FROM orders;
SELECT COUNT(DISTINCT price)       AS unikalni_ceni     FROM products;
SELECT COUNT(DISTINCT category_id) AS unikalni_kategorii FROM products;
SELECT COUNT(DISTINCT email)       AS unikalni_emaili   FROM customers;
SELECT COUNT(DISTINCT customer_id) AS unikalni_klienti  FROM orders;
```

2. Изпълнете `EXPLAIN QUERY PLAN` за тези заявки и проверете дали SQL Query Optimizer ползва индекс (ако има такъв), или прави SCAN:

```sql
-- Low cardinality — ще ползва ли индекс по status?
CREATE INDEX idx_orders_status ON orders(status);
EXPLAIN QUERY PLAN
SELECT * FROM orders WHERE status = 'cancelled';

-- High cardinality — ще ползва ли индекс по email?
CREATE INDEX idx_customers_email ON customers(email);
EXPLAIN QUERY PLAN
SELECT * FROM customers WHERE email = 'galina@mail.bg';
```

3. Помислете: ако `status` има само 4 уникални стойности и таблицата има 1 000 000 реда — `WHERE status = 'delivered'` ще върне ~250 000 реда. Ще реши ли Query Optimizer да ползва индекса?

**Въпроси:**
1. Кои колони от стъпка 1 имат **висок** кардиналитет и кои **нисък**?
2. Защо колона с нисък кардиналитет е лош кандидат за индекс?
3. Каква е разликата между `idx_customers_city` (нисък кардиналитет) и `idx_customers_email` (висок кардиналитет) по отношение на ефективността?
4. При какъв процент от таблицата може да е по-добре Query Optimizer-ът да направи Full Scan вместо да ползва индекс?

---

### Упражнение 10: Пълен сценарий — проектиране на индекси за производствена система *(трудно)*

Нов екип пое поддръжката на онлайн магазина. Потребителите се оплакват от бавни заявки. Вашата задача е да анализирате и оптимизирате.

**Изпълнете `DROP INDEX IF EXISTS ...` за всички индекси, за да стартирате чисто.**

Дадени са следните 5 „горещи заявки":

```sql
-- Заявка 1: Страница за вход — търсене на клиент по имейл
SELECT id, first_name, last_name FROM customers
WHERE email = 'martina@mail.bg';

-- Заявка 2: Каталог с продукти — по категория, наредени по цена
SELECT name, price, stock FROM products
WHERE category_id = 1
ORDER BY price ASC;

-- Заявка 3: Статус на поръчка — всички активни поръчки на клиент
SELECT id, ordered_on, status FROM orders
WHERE customer_id = 1
  AND status IN ('pending', 'shipped');

-- Заявка 4: Фактура — всички артикули в поръчка
SELECT p.name, oi.quantity, oi.unit_price
FROM order_items AS oi
    JOIN products AS p ON oi.product_id = p.id
WHERE oi.order_id = 5;

-- Заявка 5: Отчет — топ клиенти по приход (изпълнява се веднъж седмично)
SELECT c.first_name || ' ' || c.last_name AS klient,
       SUM(oi.quantity * oi.unit_price)    AS obshta_suma
FROM customers      AS c
    JOIN orders      AS o  ON c.id         = o.customer_id
    JOIN order_items AS oi ON o.id         = oi.order_id
WHERE o.status = 'delivered'
GROUP BY c.id, c.first_name, c.last_name
ORDER BY obshta_suma DESC;
```

**Задачи:**
1. За всяка заявка изпълнете `EXPLAIN QUERY PLAN` без индекси и запишете кои операции са `SCAN`.
2. Проектирайте **минималния набор от индекси** (не повече от 5–6), с който всички 5 заявки ще работят оптимално. Напишете `CREATE INDEX` командите с обосновка за всеки.
3. Добавете индексите и изпълнете `EXPLAIN QUERY PLAN` за всяка заявка отново. Сравнете.
4. Заявка 5 е отчет, изпълняван веднъж седмично. Как подходите към нея по различен начин от заявки 1–4 (изпълнявани стотици пъти на секунда)?
5. Има ли операция в заявка 5, на която **индекс не може да помогне**? Коя е тя и защо?

*(Подсказка: при заявка 3 помислете за частичен или съставен индекс. При заявка 4 — за индекс по FK. При заявка 5 — `GROUP BY` и `ORDER BY` не се ускоряват от обикновен индекс.)*

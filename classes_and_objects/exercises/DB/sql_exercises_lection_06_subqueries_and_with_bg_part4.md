# SQL Упражнения — Лекция 6, Част 4: Подзаявки и WITH (CTE) — Затвърждаване

> **Забележка:** Използвайте същите таблици и данни от **Лекция 6, Част 1**.  
> Ако не сте ги създали, изпълнете SQL скрипта от файла  
> `sql_exercises_lection_06_subqueries_and_with_bg.md` преди да започнете.

---

Тази четвърта част е специално насочена към **затвърждаване на по-трудните концепции** —
подзаявки в `WHERE`, `EXISTS`, корелирани подзаявки и `WITH` (CTE).  
Упражненията са структурирани стъпка по стъпка, с подробни подсказки и обяснения,
за да се подобри разбирането преди преминаване към по-сложен материал.

---

## Упражнения 1–3: Подзаявки в WHERE — Стъпка по Стъпка

---

### Упражнение 1: Подзаявка в WHERE с IN — клиенти от "активни" градове *(лесно)*

Искаме да намерим клиентите, живеещи в градове, в които **има склад** (warehouse).

**Стъпка 1 — Намерете градовете с склад:**
```sql
SELECT city FROM warehouses;
```
Запишете резултата. Кои градове виждате?

**Стъпка 2 — Използвайте тези градове в основната заявка с `IN`:**
```sql
SELECT first_name, last_name, city
FROM customers
WHERE city IN (SELECT city FROM warehouses)
ORDER BY city, last_name;
```

**Въпроси:**
1. Защо работи `IN (SELECT ...)` — какво всъщност прави подзаявката?
2. Ако напишете резултата от Стъпка 1 директно: `WHERE city IN ('София', 'Пловдив', 'Варна')` — ще е ли резултатът същият? Защо е по-добре да ползвате подзаявката?
3. Добавете клиент от `'Бургас'` и повторете заявката — показва ли се?

**Очакван резултат (от данните в лекцията):**
```
first_name  | last_name   | city
------------|-------------|--------
Борислав    | Неделчев    | София
Деница      | Георгиева   | Пловдив
Ивета       | Стоянова    | София
Калоян      | Тодоров     | Варна
Мартина     | Колева      | София
Радослав    | Иванов      | София
Стефан      | Димов       | Пловдив
Галина      | Пенева      | Варна
```

---

### Упражнение 2: Подзаявка в WHERE — продукти над средната цена *(лесно–средно)*

Искаме да намерим продуктите, чиято цена е **над средната цена на всички продукти**.

**Стъпка 1 — Намерете средната цена:**
```sql
SELECT AVG(price) FROM products;
```
Запишете резултата.

**Стъпка 2 — Напишете пълната заявка, като поставите Стъпка 1 като подзаявка:**
```sql
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;
```

**Стъпка 3 — Добавете и категорията, като JOIN-нете с `categories`:**
```sql
SELECT p.name, p.price, c.name AS kategoriya
FROM products AS p
    LEFT JOIN categories AS c ON p.category_id = c.id
WHERE p.price > (SELECT AVG(price) FROM products)
ORDER BY p.price DESC;
```

**Въпроси:**
1. Колко пъти се изпълнява подзаявката `(SELECT AVG(price) FROM products)` — веднъж или за всеки ред?
2. Защо ползваме `LEFT JOIN` вместо `INNER JOIN` в Стъпка 3?
3. Ако искаме продуктите **ТОЧНО** на средната цена — какъв оператор ще ползваме?

**Очакван резултат (Стъпка 2):**
```
name                   | price
-----------------------|--------
Лаптоп Dell XPS        | 2199.99
Монитор LG 27"         |  699.99
Слушалки Sony WH-1000  |  349.99
Маратонки Nike Air     |  189.99
Яке Зимно              |  149.99
Клавиатура Mechanical  |  129.99
```

*(Средна цена ≈ 123.74 лв.)*

---

### Упражнение 3: NOT IN — клиенти, които НИКОГА не са поръчвали *(средно)*

Искаме да намерим клиентите, **без нито една поръчка**.

**Стъпка 1 — Намерете всички customer_id в таблицата orders:**
```sql
SELECT DISTINCT customer_id FROM orders;
```

**Стъпка 2 — Намерете клиентите, чиито id НЕ се намират в горния списък:**
```sql
SELECT first_name, last_name, email
FROM customers
WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders)
ORDER BY last_name;
```

**Стъпка 3 — Алтернативен начин с LEFT JOIN (резултатите трябва да са еднакви):**
```sql
SELECT c.first_name, c.last_name, c.email
FROM customers AS c
    LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.id IS NULL
ORDER BY c.last_name;
```

**Въпроси:**
1. `NOT IN` и `LEFT JOIN ... WHERE IS NULL` водят ли до един и същ резултат тук?
2. Има ли случай, в който `NOT IN` може да върне **неочакван резултат** (внимавайте с `NULL` стойности в подзаявката)?
3. Кой начин (подзаявка или LEFT JOIN) е по-лесен за четене?

**Очакван резултат:**
```
first_name  | last_name   | email
------------|-------------|--------------------
Цветелина   | Атанасова   | cveta@mail.bg
```

---

## Упражнения 4–6: EXISTS и NOT EXISTS — Разбираме Логиката

---

### Упражнение 4: EXISTS — разбираме как работи *(средно)*

`EXISTS` е истина, ако подзаявката върне **поне един ред**. Не е важно какво точно — само дали има нещо.

**Пример за четене на EXISTS:**
```sql
-- "Дай ми клиентите, за които СЪЩЕСТВУВА поне една поръчка"
SELECT first_name, last_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.id   -- <-- Забележете: ползваме c.id от ОСНОВНАТА заявка
);
```

> **Ключово:** Подзаявката с `EXISTS` е **корелирана** — за всеки ред от `customers` тя се изпълнява отново с неговото `c.id`. Затова `SELECT 1` (или `SELECT *`) е достатъчно — важен е само фактът, че ред съществува.

**Задача — Напишете три версии на едно и също нещо:**

Намерете клиентите, поръчали **продукт с цена над 1000 лв.**

**Версия 1: с EXISTS**
```sql
SELECT DISTINCT c.first_name, c.last_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    WHERE o.customer_id = c.id
      AND oi.unit_price > 1000
)
ORDER BY c.last_name;
```

**Версия 2: с IN**
```sql
SELECT first_name, last_name
FROM customers
WHERE id IN (
    SELECT DISTINCT o.customer_id
    FROM orders AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    WHERE oi.unit_price > 1000
)
ORDER BY last_name;
```

**Версия 3: с JOIN**
```sql
SELECT DISTINCT c.first_name, c.last_name
FROM customers AS c
    JOIN orders AS o ON c.id = o.customer_id
    JOIN order_items AS oi ON o.id = oi.order_id
WHERE oi.unit_price > 1000
ORDER BY c.last_name;
```

**Въпроси:**
1. И трите версии дават ли един и същ резултат? Изпълнете ги и проверете.
2. Кога `EXISTS` е по-добро от `IN` (Подсказка: помислете за много голям списък от `IN (...)` стойности)?
3. Защо в `EXISTS` пишем `SELECT 1` вместо `SELECT *`?

**Очакван резултат:**
```
first_name  | last_name
------------|----------
Борислав    | Неделчев
Ивета       | Стоянова
Мартина     | Колева
```

---

### Упражнение 5: NOT EXISTS — продукти, никога не поръчвани *(средно)*

`NOT EXISTS` е истина, ако подзаявката **не върне нито един ред**.

```sql
-- "Дай ми продуктите, за които НЕ СЪЩЕСТВУВА нито една поръчка"
SELECT p.name, p.price
FROM products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_items AS oi
    WHERE oi.product_id = p.id
)
ORDER BY p.name;
```

**Задачи:**
1. Изпълнете заявката — кои продукти никога не са поръчвани? Запишете резултата.
2. Напишете **алтернативна версия** с `NOT IN`:
   ```sql
   SELECT name, price
   FROM products
   WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items)
   ORDER BY name;
   ```
3. Сравнете резултатите на двете версии — еднакви ли са?
4. Добавете нов продукт без поръчки и повторете двете заявки — появява ли се в резултата?

```sql
INSERT INTO products (name, price, stock, category_id)
VALUES ('Тест Продукт', 9.99, 5, NULL);
```

**Въпроси:**
1. Кога `NOT EXISTS` е по-безопасно от `NOT IN` (Подсказка: NULL стойности)?
2. Опишете с думи какво прави `NOT EXISTS` — как "мисли" SQL Engine при изпълнение?

---

### Упражнение 6: EXISTS с условие по дата *(средно)*

Намерете клиентите, направили поне една поръчка **след 1 март 2024 г.** (`ordered_on > '2024-03-01'`).

**Стъпка 1 — Изградете логиката:**
- Основна таблица: `customers`
- Условие: съществува поръчка на този клиент, при която `ordered_on > '2024-03-01'`

**Стъпка 2 — Напишете заявката с EXISTS:**
```sql
SELECT first_name, last_name, city
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.id
      AND o.ordered_on > '2024-03-01'
)
ORDER BY last_name;
```

**Стъпка 3 — Разширете: добавете и датата на последната поръчка (скаларна подзаявка в SELECT):**
```sql
SELECT c.first_name,
       c.last_name,
       c.city,
       (SELECT MAX(o2.ordered_on)
        FROM orders AS o2
        WHERE o2.customer_id = c.id) AS posledna_porachka
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.id
      AND o.ordered_on > '2024-03-01'
)
ORDER BY posledna_porachka DESC;
```

**Въпроси:**
1. Може ли да комбинирате `EXISTS` (в `WHERE`) и скаларна подзаявка (в `SELECT`) за един и същ клиент? Кое прави всяка от двете?
2. Защо в скаларната подзаявка в `SELECT` ползваме псевдоним `o2` вместо `o`?

**Очакван резултат (Стъпка 2):**
```
first_name  | last_name  | city
------------|------------|--------
Борислав    | Неделчев   | София
Мартина     | Колева     | София
Никола      | Петров     | Русе
Радослав    | Иванов     | София
Калоян      | Тодоров    | Варна
```

---

## Упражнения 7–10: WITH (CTE) — Изграждаме Стъпка по Стъпка

---

### Упражнение 7: Първото CTE — опростяваме сложна заявка *(лесно–средно)*

CTE (`WITH ... AS (...)`) е **именувана временна таблица**. Вместо да пишете вложена заявка, я именувате и след това я ползвате като обикновена таблица.

**Проблем без CTE (трудно за четене):**
```sql
SELECT customer_id, COUNT(*) AS broi
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

**Същото с CTE (по-ясно):**
```sql
WITH customer_orders AS (
    SELECT customer_id, COUNT(*) AS broi
    FROM orders
    GROUP BY customer_id
)
SELECT c.first_name, c.last_name, co.broi
FROM customer_orders AS co
    JOIN customers AS c ON c.id = co.customer_id
WHERE co.broi > 1
ORDER BY co.broi DESC, c.last_name;
```

**Задачи:**
1. Изпълнете и двете версии — дават ли еднакъв резултат?
2. Добавете към CTE и `SUM(oi.quantity * oi.unit_price) AS total` (трябва да JOIN-нете и `order_items`) и покажете клиентите с повече от 1 поръчка заедно с общия им разход.
3. Именувайте CTE-то подходящо — какво описва?

**Очакван резултат (Задача 1):**
```
first_name  | last_name   | broi
------------|-------------|------
Борислав    | Неделчев    | 2
Мартина     | Колева      | 2
```

---

### Упражнение 8: CTE + категория на разход *(средно)*

**Задача:** За всеки клиент пресметнете **общия разход** и го категоризирайте.

```sql
WITH spending AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS total
    FROM orders AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    GROUP BY o.customer_id
)
SELECT
    c.first_name || ' ' || c.last_name AS klient,
    ROUND(s.total, 2)                  AS razxod,
    CASE
        WHEN s.total >= 2000 THEN 'VIP'
        WHEN s.total >= 500  THEN 'Редовен'
        ELSE                      'Обикновен'
    END AS kategoriya
FROM spending AS s
    JOIN customers AS c ON c.id = s.customer_id
ORDER BY s.total DESC;
```

**Задачи:**
1. Изпълнете заявката и запишете резултата.
2. Включете и клиентите **без поръчки** (категория `'Нов'`). За целта:
   - Сменете `JOIN customers` с `RIGHT JOIN customers` (или LEFT JOIN от другата страна).
   - Използвайте `COALESCE(s.total, 0)` за нулев разход.
   - Добавете `'Нов'` като четвърти `WHEN` за `total = 0` или `IS NULL`.
3. Колко клиента попадат в категория `'VIP'`?

---

### Упражнение 9: Две CTE — сравняваме продукт с категорията му *(средно–трудно)*

Целта е за всеки продукт да се покаже как цената му се сравнява със **средната цена на категорията му**.

**Стъпка 1 — Пишем CTE за средна цена по категория:**
```sql
WITH category_avg AS (
    SELECT category_id, AVG(price) AS avg_price
    FROM products
    WHERE category_id IS NOT NULL
    GROUP BY category_id
)
SELECT * FROM category_avg;
```
Изпълнете само това и вижте как изглежда "временната таблица".

**Стъпка 2 — Добавяме второ CTE и правим сравнение:**
```sql
WITH category_avg AS (
    SELECT category_id, AVG(price) AS avg_price
    FROM products
    WHERE category_id IS NOT NULL
    GROUP BY category_id
),
product_vs_avg AS (
    SELECT
        p.name                                               AS produkt,
        p.price,
        ROUND(ca.avg_price, 2)                              AS sredna_kategoriya,
        ROUND(p.price - ca.avg_price, 2)                    AS razlika,
        CASE
            WHEN p.price > ca.avg_price THEN 'Над средното'
            WHEN p.price < ca.avg_price THEN 'Под средното'
            ELSE                             'На средното'
        END AS pozitsiya
    FROM products AS p
        JOIN category_avg AS ca ON p.category_id = ca.category_id
)
SELECT *
FROM product_vs_avg
ORDER BY razlika DESC;
```

**Въпроси:**
1. Защо сме разделили логиката на две CTE вместо в едно? Какво улеснява?
2. В Стъпка 2, `product_vs_avg` CTE ползва резултата от `category_avg` — как се нарича тази зависимост?
3. Ако имахме 3-то CTE, можем ли то да ползва резултата от двете предишни?
4. Продуктите без категория (`category_id IS NULL`) — появяват ли се в резултата? Защо?

---

### Упражнение 10: Пълен сценарий — доклад за поръчки *(средно–трудно)*

Шефът иска **ежемесечен доклад** в следния формат:
- Месец на поръчката
- Брой поръчки
- Обща стойност
- Дали е над или под средната месечна стойност за годината

**Изградете решението стъпка по стъпка:**

**Стъпка 1 — CTE `monthly` — статистика по месец:**
```sql
WITH monthly AS (
    SELECT
        strftime('%Y-%m', o.ordered_on)       AS mesec,
        COUNT(DISTINCT o.id)                  AS broi_porachki,
        SUM(oi.quantity * oi.unit_price)       AS suma
    FROM orders AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    GROUP BY mesec
)
SELECT * FROM monthly ORDER BY mesec;
```

**Стъпка 2 — Добавете CTE `avg_monthly` — средна месечна сума:**
```sql
WITH monthly AS (
    -- (същото като Стъпка 1)
    SELECT
        strftime('%Y-%m', o.ordered_on)       AS mesec,
        COUNT(DISTINCT o.id)                  AS broi_porachki,
        SUM(oi.quantity * oi.unit_price)       AS suma
    FROM orders AS o
        JOIN order_items AS oi ON o.id = oi.order_id
    GROUP BY mesec
),
avg_monthly AS (
    SELECT AVG(suma) AS avg_suma FROM monthly
)
SELECT
    m.mesec,
    m.broi_porachki,
    ROUND(m.suma, 2)                          AS suma,
    ROUND(am.avg_suma, 2)                     AS sredna_suma,
    CASE
        WHEN m.suma > am.avg_suma THEN 'Над средното'
        WHEN m.suma < am.avg_suma THEN 'Под средното'
        ELSE                          'На средното'
    END AS ocenka
FROM monthly AS m, avg_monthly AS am
ORDER BY m.mesec;
```

**Въпроси:**
1. `FROM monthly AS m, avg_monthly AS am` — защо работи без `JOIN`? Колко реда има `avg_monthly` и какво означава кръстосването?
2. Ако имаме данни за 2 години, как да сравняваме всеки месец **само с месеците от същата година**?
3. Добавете нова колона `razlika` — разликата между `suma` и `avg_suma` за всеки месец.

**Очакван резултат:**
```
mesec   | broi_porachki | suma    | sredna_suma | ocenka
--------|---------------|---------|-------------|-------------
2024-01 | 4             | 5884.89 | 2199.94     | Над средното
2024-02 | 2             |  229.96 | 2199.94     | Под средното
2024-03 | 3             |  574.97 | 2199.94     | Под средното
2024-04 | 2             |  129.95 | 2199.94     | Под средното
```

*(Средна месечна сума = (5884.89 + 229.96 + 574.97 + 129.95) / 4 ≈ 1704.94 — стойностите може да варират леко спрямо данните)*

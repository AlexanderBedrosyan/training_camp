# SQL Лекция 4: Агрегиране на данни — GROUP BY, Агрегатни функции, HAVING и CASE

Добре дошли в четвъртата лекция по SQL!

В предишните лекции работихме с **отделни редове** — извеждахме, филтрирахме и трансформирахме данни ред по ред. Сега правим крачка напред: ще се научим да **обобщаваме (агрегираме)** данни — да броим, сумираме и намираме средни стойности върху **цели групи** от редове.

---

## Подготовка: Тестови таблици

За тази лекция ще използваме две таблици — `employees` (служители) и `departments` (отдели). Изпълнете следното:

```sql
-- Изтриване на старите таблици (ако съществуват)
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- Таблица с отдели
CREATE TABLE departments (
    id    INTEGER PRIMARY KEY,
    name  TEXT
);

INSERT INTO departments (name) VALUES ('Разработка');
INSERT INTO departments (name) VALUES ('Дизайн');
INSERT INTO departments (name) VALUES ('DevOps');
INSERT INTO departments (name) VALUES ('Качество (QA)');
INSERT INTO departments (name) VALUES ('Управление');

-- Таблица със служители
CREATE TABLE employees (
    id            INTEGER PRIMARY KEY,
    name          TEXT,
    position      TEXT,
    department_id INTEGER,
    salary        REAL,
    hire_date     TEXT
);

INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Иван Петров',     'Software Engineer', 1, 4500.00, '2021-03-15');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Мария Иванова',   'Designer',          2, 3800.00, '2020-07-01');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Георги Димитров', 'Team Lead',         5, 6200.00, '2019-11-20');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Елена Стоянова',  'QA Engineer',       4, 4100.00, '2022-01-10');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Николай Тодоров', 'Software Engineer', 1, 4700.00, '2021-09-05');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Петя Коева',      'Designer',          2, 3600.00, '2023-04-18');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Стефан Боев',     'DevOps Engineer',   3, 5100.00, '2020-02-28');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Димитър Павлов',  'Software Engineer', 1, 5000.00, '2018-06-12');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Габриела Маркова','QA Engineer',       4, 3900.00, '2023-08-01');
INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES ('Антон Колев',     'DevOps Engineer',   3, 5300.00, '2020-11-15');
```

---

## 1. Групиране — GROUP BY

### Какво означава групиране?

Представете си, че имате 10 служители и искате да разберете **колко служители работят във всеки отдел**. Вместо да броите редовете на ръка, SQL може да **групира редовете по стойност в дадена колона** и да изчисли обобщени данни за всяка група.

```
Всички редове в таблицата       →  Групиране по department_id  →  Резултат
──────────────────────────────     ────────────────────────────    ──────────────────────────
Иван Петров,     department_id=1  ┐                               Отдел 1 → 3 служители
Николай Тодоров, department_id=1  ├─ Група за отдел 1            Отдел 2 → 2 служители
Димитър Павлов,  department_id=1  ┘                               Отдел 3 → 2 служители
                                                                  Отдел 4 → 2 служители
Мария Иванова,   department_id=2  ┐                               Отдел 5 → 1 служител
Петя Коева,      department_id=2  ┘─ Група за отдел 2
...
```

### Синтаксис

```sql
SELECT колона_за_групиране, АГРЕГАТНА_ФУНКЦИЯ(друга_колона)
FROM таблица
GROUP BY колона_за_групиране;
```

### Пример 1: Брой служители по позиция

```sql
SELECT position, COUNT(*) AS broi
FROM employees
GROUP BY position;
```

| position           | broi |
|--------------------|------|
| DevOps Engineer    | 2    |
| Designer           | 2    |
| QA Engineer        | 2    |
| Software Engineer  | 3    |
| Team Lead          | 1    |

> **Важно правило:** В `SELECT` можете да поставяте **само**:
> - Колоните, по които групирате (`GROUP BY` колоните)
> - Агрегатни функции (`COUNT`, `SUM`, `AVG` и т.н.)
>
> Ако опитате да добавите колона като `name` без агрегатна функция — заявката е **неправилна** (или дава неочаквани резултати).

---

## 2. Агрегатни функции

Агрегатните функции работят върху **множество редове** и връщат **един резултат** за групата.

| Функция       | Описание                                          | Пример                            |
|---------------|---------------------------------------------------|-----------------------------------|
| `COUNT(*)`    | Брои всички редове в групата                      | Колко служители има в отдела?     |
| `COUNT(col)`  | Брои редовете, в които `col` не е `NULL`          | Колко служители имат зададена позиция? |
| `SUM(col)`    | Сумира числовите стойности                        | Каква е общата сума на заплатите? |
| `AVG(col)`    | Изчислява средната стойност                       | Каква е средната заплата?         |
| `MAX(col)`    | Връща най-голямата стойност                       | Каква е най-високата заплата?     |
| `MIN(col)`    | Връща най-малката стойност                        | Каква е най-ниската заплата?      |

---

### 2.1 COUNT() — Броене

```sql
-- Общ брой служители в таблицата
SELECT COUNT(*) AS vsichki_sluzhiteli
FROM employees;
```

| vsichki_sluzhiteli |
|--------------------|
| 10                 |

```sql
-- Брой служители за всяка позиция
SELECT position, COUNT(*) AS broi
FROM employees
GROUP BY position
ORDER BY broi DESC;
```

| position           | broi |
|--------------------|------|
| Software Engineer  | 3    |
| DevOps Engineer    | 2    |
| Designer           | 2    |
| QA Engineer        | 2    |
| Team Lead          | 1    |

---

### 2.2 SUM() — Сумиране

```sql
-- Обща сума на всички заплати
SELECT SUM(salary) AS obshta_zaplata
FROM employees;
```

| obshta_zaplata |
|----------------|
| 46200.0        |

```sql
-- Обща заплата по позиция
SELECT position, SUM(salary) AS suma_zaplati
FROM employees
GROUP BY position;
```

| position           | suma_zaplati |
|--------------------|--------------|
| DevOps Engineer    | 10400.0      |
| Designer           | 7400.0       |
| QA Engineer        | 8000.0       |
| Software Engineer  | 14200.0      |
| Team Lead          | 6200.0       |

---

### 2.3 AVG() — Средна стойност

```sql
-- Средна заплата на всички служители
SELECT ROUND(AVG(salary), 2) AS sredna_zaplata
FROM employees;
```

| sredna_zaplata |
|----------------|
| 4620.0         |

```sql
-- Средна заплата по позиция, наредена от най-висока към най-ниска
SELECT position, ROUND(AVG(salary), 2) AS sredna_zaplata
FROM employees
GROUP BY position
ORDER BY sredna_zaplata DESC;
```

| position           | sredna_zaplata |
|--------------------|----------------|
| Team Lead          | 6200.0         |
| DevOps Engineer    | 5200.0         |
| Software Engineer  | 4733.33        |
| QA Engineer        | 4000.0         |
| Designer           | 3700.0         |

---

### 2.4 MAX() и MIN() — Максимум и минимум

```sql
-- Най-висока и най-ниска заплата
SELECT MAX(salary) AS max_zaplata, MIN(salary) AS min_zaplata
FROM employees;
```

| max_zaplata | min_zaplata |
|-------------|-------------|
| 6200.0      | 3600.0      |

```sql
-- Максимална и минимална заплата по позиция
SELECT position,
       MAX(salary) AS max_zaplata,
       MIN(salary) AS min_zaplata
FROM employees
GROUP BY position;
```

| position           | max_zaplata | min_zaplata |
|--------------------|-------------|-------------|
| DevOps Engineer    | 5300.0      | 5100.0      |
| Designer           | 3800.0      | 3600.0      |
| QA Engineer        | 4100.0      | 3900.0      |
| Software Engineer  | 5000.0      | 4500.0      |
| Team Lead          | 6200.0      | 6200.0      |

---

### 2.5 Комбиниране на няколко агрегатни функции

Можете да използвате **множество агрегатни функции** в една единствена заявка:

```sql
SELECT
    position,
    COUNT(*)                  AS broi_sluzhiteli,
    ROUND(AVG(salary), 2)     AS sredna_zaplata,
    SUM(salary)               AS obshta_zaplata,
    MAX(salary)               AS max_zaplata,
    MIN(salary)               AS min_zaplata
FROM employees
GROUP BY position
ORDER BY sredna_zaplata DESC;
```

| position          | broi | sredna_zaplata | obshta_zaplata | max_zaplata | min_zaplata |
|-------------------|------|----------------|----------------|-------------|-------------|
| Team Lead         | 1    | 6200.0         | 6200.0         | 6200.0      | 6200.0      |
| DevOps Engineer   | 2    | 5200.0         | 10400.0        | 5300.0      | 5100.0      |
| Software Engineer | 3    | 4733.33        | 14200.0        | 5000.0      | 4500.0      |
| QA Engineer       | 2    | 4000.0         | 8000.0         | 4100.0      | 3900.0      |
| Designer          | 2    | 3700.0         | 7400.0         | 3800.0      | 3600.0      |

---

## 3. HAVING — Филтриране на групи

### Защо не можем да ползваме WHERE с агрегатни функции?

`WHERE` филтрира **отделни редове преди** групирането. Агрегатните функции се изчисляват **след** групирането, затова `WHERE` не знае за тях.

```sql
-- ❌ ГРЕШНО — WHERE не може да работи с AGG функции
SELECT position, AVG(salary)
FROM employees
WHERE AVG(salary) > 4500   -- Грешка!
GROUP BY position;
```

### HAVING идва на помощ!

`HAVING` работи **след** `GROUP BY` и филтрира **групи** по условие — включително с агрегатни функции.

```sql
-- ✅ ПРАВИЛНО — HAVING филтрира групи след агрегирането
SELECT position, ROUND(AVG(salary), 2) AS sredna_zaplata
FROM employees
GROUP BY position
HAVING AVG(salary) > 4500;
```

| position          | sredna_zaplata |
|-------------------|----------------|
| DevOps Engineer   | 5200.0         |
| Software Engineer | 4733.33        |
| Team Lead         | 6200.0         |

### Разлика между WHERE и HAVING

| Клауза   | Кога се прилага?                  | Работи с агрегатни функции? | Работи с отделни редове? |
|----------|-----------------------------------|-----------------------------|--------------------------|
| `WHERE`  | Преди `GROUP BY` (на редовете)    | ❌ Не                       | ✅ Да                    |
| `HAVING` | След `GROUP BY` (на групите)      | ✅ Да                       | ❌ Не (обикновено)       |

### Пример: WHERE и HAVING заедно

```sql
-- Позиции с повече от 1 служител, само сред наетите след 2019 г.,
-- при средна заплата над 4000
SELECT
    position,
    COUNT(*)              AS broi,
    ROUND(AVG(salary), 2) AS sredna_zaplata
FROM employees
WHERE hire_date > '2019-12-31'        -- ← WHERE филтрира редовете ПРЕДИ групиране
GROUP BY position
HAVING COUNT(*) > 1                   -- ← HAVING филтрира групите СЛЕД агрегиране
   AND AVG(salary) > 4000
ORDER BY sredna_zaplata DESC;
```

---

## 4. Условни изрази — CASE WHEN

`CASE WHEN` е **условен израз** в SQL — подобен на `if / elif / else` в Python. Позволява ви да задавате **различни стойности** в зависимост от условие.

### Синтаксис

```sql
CASE
    WHEN условие1 THEN стойност1
    WHEN условие2 THEN стойност2
    ...
    ELSE стойност_по_подразбиране
END
```

---

### 4.1 Категоризиране на заплати

```sql
-- Класифицира всеки служител по ниво на заплатата
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 6000 THEN 'Старши'
        WHEN salary >= 4500 THEN 'Средно ниво'
        WHEN salary >= 3500 THEN 'Начинаещ'
        ELSE 'Без категория'
    END AS nivo
FROM employees
ORDER BY salary DESC;
```

| name              | salary | nivo         |
|-------------------|--------|--------------|
| Георги Димитров   | 6200.0 | Старши       |
| Антон Колев       | 5300.0 | Средно ниво  |
| Стефан Боев       | 5100.0 | Средно ниво  |
| Димитър Павлов    | 5000.0 | Средно ниво  |
| Николай Тодоров   | 4700.0 | Средно ниво  |
| Иван Петров       | 4500.0 | Средно ниво  |
| Елена Стоянова    | 4100.0 | Начинаещ     |
| Габриела Маркова  | 3900.0 | Начинаещ     |
| Мария Иванова     | 3800.0 | Начинаещ     |
| Петя Коева        | 3600.0 | Начинаещ     |

---

### 4.2 CASE WHEN вътре в агрегатна функция

Можете да **броите или сумирате** само редовете, отговарящи на дадено условие:

```sql
-- Колко служители попадат в категориите "С висока заплата" и "С ниска заплата"
SELECT
    COUNT(CASE WHEN salary >= 5000 THEN 1 END) AS visoka_zaplata,
    COUNT(CASE WHEN salary < 5000  THEN 1 END) AS niska_zaplata
FROM employees;
```

| visoka_zaplata | niska_zaplata |
|----------------|---------------|
| 3              | 7             |

```sql
-- Обща заплата по ниво (CASE + SUM)
SELECT
    CASE
        WHEN salary >= 6000 THEN 'Старши'
        WHEN salary >= 4500 THEN 'Средно ниво'
        ELSE 'Начинаещ'
    END AS nivo,
    COUNT(*)    AS broi,
    SUM(salary) AS obshta_zaplata
FROM employees
GROUP BY nivo
ORDER BY obshta_zaplata DESC;
```

| nivo         | broi | obshta_zaplata |
|--------------|------|----------------|
| Средно ниво  | 5    | 25500.0        |
| Начинаещ     | 4    | 15400.0        |
| Старши       | 1    | 6200.0         |

---

### 4.3 CASE WHEN за трансформиране на данни при извеждане

```sql
-- Показва дали служителят е нает преди или след 2021
SELECT
    name,
    hire_date,
    CASE
        WHEN hire_date < '2021-01-01' THEN 'Ветеран (преди 2021)'
        WHEN hire_date < '2023-01-01' THEN 'Опитен (2021–2022)'
        ELSE 'Нов служител (2023+)'
    END AS status_naemane
FROM employees
ORDER BY hire_date;
```

---

## 5. Пълен ред на изпълнение (Order of Execution)

Разбирането на реда, в който SQL обработва клаузите, е ключово:

```
1. FROM       ← от коя таблица четем?
2. WHERE      ← филтрираме отделните редове
3. GROUP BY   ← групираме филтрираните редове
4. HAVING     ← филтрираме групите
5. SELECT     ← избираме какво да покажем (включително CASE, агрегатни функции)
6. ORDER BY   ← наредждаме резултата
7. LIMIT      ← ограничаваме броя на резултатите
```

### Пример, демонстриращ целия ред:

```sql
SELECT
    position,
    COUNT(*)              AS broi,
    ROUND(AVG(salary), 2) AS sredna_zaplata
FROM employees                          -- 1. Четем от таблицата
WHERE hire_date >= '2020-01-01'         -- 2. Само служители наети от 2020 нагоре
GROUP BY position                       -- 3. Групираме по позиция
HAVING COUNT(*) >= 2                    -- 4. Само групи с поне 2 служителя
ORDER BY sredna_zaplata DESC            -- 6. Наредждаме по средна заплата
LIMIT 3;                                -- 7. Показваме само первите 3
```

---

## Бързо резюме

| Концепция         | Клауза/Функция                | Кога се използва?                                          |
|-------------------|-------------------------------|------------------------------------------------------------|
| Групиране         | `GROUP BY col`                | Когато искаме обобщени данни по категории                  |
| Брой редове       | `COUNT(*)`                    | Колко реда (служители, поръчки...) има в групата           |
| Сума              | `SUM(col)`                    | Обща сума (заплати, продажби...)                           |
| Средна стойност   | `AVG(col)`                    | Средна стойност за групата                                 |
| Максимум / Минимум| `MAX(col)` / `MIN(col)`       | Най-голяма / най-малка стойност в групата                  |
| Филтриране на групи | `HAVING условие`            | Показваме само групи, отговарящи на условие                |
| Условни стойности | `CASE WHEN ... THEN ... END`  | Различна стойност в зависимост от условие (като if/else)   |

---

## Упражнения

Използвайте таблицата `employees` от подготовката в началото на лекцията.

---

### Упражнение 1: Брой и обща заплата по позиция
Напишете заявка, която извежда за всяка **позиция** (`position`):
- Броя на служителите (като `broi`)
- Общата сума от заплатите (като `obshta_zaplata`)

Наредете резултата по `obshta_zaplata` **низходящо**.

---

### Упражнение 2: Средна заплата по отдел
Напишете заявка, която извежда `department_id` и **средната заплата** (закръглена до 2 знака) като `sredna_zaplata` за всеки отдел.  
Наредете по средна заплата **низходящо**.

---

### Упражнение 3: Само позиции с повече от 1 служител
Напишете заявка, която извежда позициите (`position`) и броя служители (`broi`), но **само** за позиции с **повече от 1 служател**.

*(Подсказка: `HAVING COUNT(*) > 1`)*

---

### Упражнение 4: Минимална и максимална заплата по позиция
Напишете заявка, която извежда `position`, `min_zaplata` и `max_zaplata` за всяка позиция.  
Наредете по разликата между максималната и минималната заплата **низходящо**.

*(Подсказка: `ORDER BY (MAX(salary) - MIN(salary)) DESC`)*

---

### Упражнение 5: Позиции с обща заплата над 8000
Напишете заявка, която извежда само тези позиции, при които **общата сума на заплатите** надвишава `8000`.  
Покажете `position` и `obshta_zaplata`.

---

### Упражнение 6: Брой на служителите по година на наемане
Напишете заявка, която извежда **годината** на наемане (`godina`) и **броя служители** наети в нея (`broi`).  
Наредете по година **възходящо**.

*(Подсказка: `strftime('%Y', hire_date) AS godina` в SELECT и GROUP BY)*

---

### Упражнение 7: Категоризиране на служителите
Напишете заявка, която извежда `name`, `salary` и колона `kategoriya` по следните правила:
- `salary >= 5500` → `'Топ заплата'`
- `salary >= 4500` → `'Добра заплата'`
- `salary >= 3500` → `'Стандартна заплата'`
- Иначе → `'Ниска заплата'`

Наредете резултата по `salary` **низходящо**.

---

### Упражнение 8: Брой служители по категория заплата
Използвайки `CASE WHEN` и `GROUP BY`, напишете заявка, която брои колко служители попадат в следните категории:
- `'Над 5000'` (salary > 5000)
- `'4000–5000'` (salary BETWEEN 4000 AND 5000)
- `'Под 4000'` (salary < 4000)

Покажете `kategoriya` и `broi`.

*(Подсказка: Групирайте по CASE WHEN израза)*

---

### Упражнение 9: Комбинирана заявка с WHERE и HAVING
Напишете заявка, която извежда позициите и средната им заплата, но:
- **Само** за служители наети **след 01.01.2020** (`WHERE`)
- **Само** за позиции с **поне 2 служители** (`HAVING`)

Наредете по средна заплата **низходящо**.

---

### Упражнение 10: Статус на позицията и обобщение
Напишете заявка, която извежда за всяка позиция:
- `position`
- `broi_sluzhiteli`
- `sredna_zaplata` (закръглена до 2 знака)
- `status` — колона с `CASE WHEN`:
  - Ако средната заплата е над `5000` → `'Добре платена позиция'`
  - Ако е между `4000` и `5000` → `'Средно платена позиция'`
  - Иначе → `'Ниско платена позиция'`

Наредете по `sredna_zaplata` **низходящо**.

---

*Следваща лекция: **JOIN** — свързване на данни от множество таблици.*

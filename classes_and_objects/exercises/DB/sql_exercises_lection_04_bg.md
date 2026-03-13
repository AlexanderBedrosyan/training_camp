# SQL Упражнения — Лекция 4: GROUP BY, Агрегатни функции, HAVING и CASE WHEN

Използвайте таблиците `employees` и `departments` от подготовката в **Лекция 4**. Ако не сте ги създали, изпълнете следното:

```sql
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id    INTEGER PRIMARY KEY,
    name  TEXT
);

INSERT INTO departments (name) VALUES ('Разработка');
INSERT INTO departments (name) VALUES ('Дизайн');
INSERT INTO departments (name) VALUES ('DevOps');
INSERT INTO departments (name) VALUES ('Качество (QA)');
INSERT INTO departments (name) VALUES ('Управление');

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

## Упражнения 1–7: GROUP BY, Агрегатни функции, HAVING и CASE WHEN

---

### Упражнение 1: Брой служители и обща заплата по позиция
Напишете заявка, която извежда за всяка **позиция** (`position`):
- Броя на служителите като `broi_sluzhiteli`
- Общата сума от заплатите като `obshta_zaplata`

Наредете резултата по `obshta_zaplata` **низходящо**.

---

### Упражнение 2: Средна заплата по отдел
Напишете заявка, която извежда `department_id` и **средната заплата** (закръглена до 2 десетични знака) като `sredna_zaplata` за всеки отдел.  
Наредете резултата по `sredna_zaplata` **низходящо**.

---

### Упражнение 3: Само позиции с повече от 1 служител
Напишете заявка, която извежда **позициите** (`position`) и **броя служители** (`broi`), но **само** за позиции с **повече от 1 служател**.  
Наредете по брой **низходящо**.

*(Подсказка: Използвайте `HAVING COUNT(*) > 1`)*

---

### Упражнение 4: Максимална и минимална заплата по позиция
Напишете заявка, която показва за всяка позиция:
- `position`
- Най-високата заплата като `max_zaplata`
- Най-ниската заплата като `min_zaplata`
- Разликата между тях като `razlika`

Наредете по `razlika` **низходящо**.

*(Подсказка: `MAX(salary) - MIN(salary) AS razlika`)*

---

### Упражнение 5: Комбиниране на WHERE, GROUP BY и HAVING
Напишете заявка, която извежда позициите и средната им заплата (`sredna_zaplata`, закръглена до 2 знака), но:
- Включвайте **само** служителите, наети **след 2019 г.** (`hire_date > '2019-12-31'`)
- Показвайте **само** позициите, при които средната заплата на тази подгрупа е **над 4 200 лв.**

Наредете по `sredna_zaplata` **низходящо**.

---

### Упражнение 6: Пълна статистика по позиция (множество агрегатни функции)
Напишете заявка, която дава **пълна статистика** за всяка позиция:
- `position`
- `broi_sluzhiteli` — брой служители
- `sredna_zaplata` — средна заплата (закръглена до 2 знака)
- `obshta_zaplata` — обща сума на заплатите
- `max_zaplata` — максимална заплата
- `min_zaplata` — минимална заплата

Наредете резултата по `sredna_zaplata` **низходящо**.

---

### Упражнение 7: CASE WHEN — Категоризиране на служители по ниво на заплата
Напишете заявка, която извежда `name`, `salary` и нова колона `nivo`, която категоризира всеки служител по следната схема:
- Заплата ≥ 6 000 → `'Старши'`
- Заплата ≥ 4 500 → `'Средно ниво'`
- Заплата ≥ 3 500 → `'Начинаещ'`
- Всичко останало → `'Без категория'`

Наредете резултата по `salary` **низходящо**.

*(Подсказка: Използвайте `CASE WHEN salary >= 6000 THEN ... END AS nivo`)*

---

## Упражнения 8–10: Преглед към Лекция 5 — Релации и JOIN

> Следващите 3 упражнения въвеждат концепции (**FOREIGN KEY**, **JOIN**), които ще разгледаме подробно в **Лекция 5**. Опитайте се да ги решите или да разгледате решенията — ще ги разберете напълно в следващата лекция!

---

### Упражнение 8: Брой наети служители по отдел, използвайки JOIN *(преглед — INNER JOIN)*
В момента `employees` съдържа само `department_id`. Таблицата `departments` пази истинското **наименование** на отдела.

Напишете заявка, която извежда **наименованието на отдела** (`departments.name`) и **броя на служителите** в него (`broi_sluzhiteli`).  
Наредете по брой **низходящо**.

*(Подсказка: `SELECT d.name, COUNT(*) AS broi_sluzhiteli FROM employees e INNER JOIN departments d ON e.department_id = d.id GROUP BY d.name ORDER BY broi_sluzhiteli DESC;`)*

---

### Упражнение 9: Средна заплата по наименование на отдел *(преглед — JOIN + AVG)*
Напишете заявка, която извежда за всеки отдел:
- Наименованието на отдела (`departments.name`) като `otdel`
- Средната заплата (закръглена до 2 знака) като `sredna_zaplata`

Показвайте **само отделите**, в които средната заплата е **над 4 500 лв.**  
Наредете по `sredna_zaplata` **низходящо**.

*(Подсказка: Използвайте `INNER JOIN`, `GROUP BY d.name` и `HAVING AVG(salary) > 4500`)*

---

### Упражнение 10: Пълен профил на отдела *(преглед — JOIN + множество агрегатни функции)*
Напишете заявка, която за всеки отдел показва:
- Наименованието на отдела (`departments.name`) като `otdel`
- Броя на служителите като `broi_sluzhiteli`
- Общата сума на заплатите като `obshta_zaplata`
- Максималната заплата като `max_zaplata`
- Минималната заплата като `min_zaplata`

Наредете резултата по `obshta_zaplata` **низходящо**.  
Показвайте **само отделите, в които работят поне 2 служители**.

*(Подсказка: `JOIN departments d ON e.department_id = d.id`, `GROUP BY d.name`, `HAVING COUNT(*) >= 2`)*

---

*Следваща лекция: **Проектиране на бази данни** — релации, `FOREIGN KEY`, `JOIN` (INNER, LEFT, RIGHT) и `CASCADE` операции.*

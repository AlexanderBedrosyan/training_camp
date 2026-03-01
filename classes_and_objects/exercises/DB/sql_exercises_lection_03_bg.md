# SQL Упражнения — Лекция 3: Функции, Wildcards и Работа с Текст и Числа

Използвайте таблицата `employees` от подготовката в **Лекция 3**. Ако не сте я създали, изпълнете следното:

```sql
CREATE TABLE IF NOT EXISTS employees (
    id        INTEGER PRIMARY KEY,
    name      TEXT,
    position  TEXT,
    salary    REAL,
    hire_date TEXT
);

INSERT INTO employees (name, position, salary, hire_date) VALUES ('Ivan Petrov',     'Software Engineer', 4500.50, '2021-03-15');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Maria Ivanova',   'Designer',          3800.00, '2020-07-01');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Georgi Dimitrov', 'Team Lead',         6200.00, '2019-11-20');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Elena Stoyanova', 'QA Engineer',       4100.00, '2022-01-10');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Nikolay Todorov', 'Software Engineer', 4500.50, '2021-09-05');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Petya Koeva',     'Designer',          3600.75, '2023-04-18');
INSERT INTO employees (name, position, salary, hire_date) VALUES ('Stefan Boev',     'DevOps Engineer',   5100.00, '2020-02-28');
```

---

## Упражнения 1–8: Функции, Wildcards и Дати

---

### Упражнение 1: Главни и малки букви
Напишете **две заявки**:
- Първата да извежда **всички имена с главни букви** — колоната да се казва `IME_ГЛАВНИ`.
- Втората да извежда **всички длъжности с малки букви** — колоната да се казва `poziciya_malki`.

---

### Упражнение 2: Дължина на имената
Напишете заявка, която извежда `name` и дължината на името в символи като колона `ime_daljina`.  
Наредете резултата по дължина — от **най-дългото** към **най-краткото** ime.

---

### Упражнение 3: Замяна на текст
Напишете заявка, която извежда всички длъжности, като думата `'Engineer'` е заменена с `'Инженер'`.  
Наречете колоната `poziciya_bg`.

*(Подсказка: `REPLACE(position, 'Engineer', 'Инженер')`)*

---

### Упражнение 4: Закръгляне и математика
Напишете заявка, която извежда `name`, оригиналната `salary` и нова колона `salary_plus_bonus`, в която заплатата е **увеличена с 10%** и **закръглена до 2 десетични знаци**.

*(Подсказка: `ROUND(salary * 1.10, 2)`)*

---

### Упражнение 5: Абсолютна разлика от средна заплата
Напишете заявка, която извежда `name`, `salary` и колона `razlika`, която показва **абсолютната разлика** между заплатата на служителя и числото `4500`.  
Наредете по `razlika` във **възходящ** ред.

*(Подсказка: `ABS(salary - 4500) AS razlika`)*

---

### Упражнение 6: Година и месец на наемане
Напишете заявка, която извежда `name`, **годината** от `hire_date` (като `godina`) и **месеца** (като `mesec`).  
Наредете резултата по година **низходящо**, след това по месец **възходящо**.

*(Подсказка: `strftime('%m', hire_date)` за месец)*

---

### Упражнение 7: Wildcard — Имена, съдържащи буквата 'e'
Напишете заявка, която извежда `name`, `position` и `salary` на всички служители, в чието **собствено или фамилно ime** се среща **буквата `'e'`** (малко или главно).  
Наредете по `salary` **низходящо**.

*(Подсказка: `LOWER(name) LIKE '%e%'`)*

---

### Упражнение 8: Wildcard — Специфичен формат на дата
Напишете заявка, която извежда всички служители, наети **в годините 2020 или 2021**.  
Използвайте `LIKE` оператора върху колоната `hire_date`.

*(Подсказка: `hire_date LIKE '2020%' OR hire_date LIKE '2021%'`)*

---

## Упражнения 9–10: Преглед към Лекция 4 — Агрегатни функции

> Следващите 2 упражнения въвеждат нови концепции (`COUNT`, `GROUP BY`, `HAVING`), които ще разгледаме подробно в **Лекция 4**. Опитайте се да ги решите интуитивно — ще ги разберете напълно в следващата лекция!

---

### Упражнение 9: Брой служители по длъжност *(преглед — GROUP BY)*
Напишете заявка, която брои **колко служители** има за всяка длъжност (`position`).  
Резултатът трябва да съдържа `position` и колона `broi_sluzhiteli`.  
Наредете по брой **низходящо**.

*(Подсказка: `SELECT position, COUNT(*) AS broi_sluzhiteli FROM employees GROUP BY position ORDER BY broi_sluzhiteli DESC;`)*

---

### Упражнение 10: Средна и обща заплата по длъжност *(преглед — AVG, SUM, HAVING)*
Напишете заявка, която показва за всяка длъжност:
- `position`
- Средната заплата като `sredna_zaplata` (закръглена до 2 знака)
- Общата сума от заплати като `obshta_zaplata`

Показвайте **само длъжностите**, при които средната заплата е **над 4000**.

*(Подсказка: `GROUP BY position HAVING AVG(salary) > 4000`)*

---

*Следваща лекция: **Агрегиране на данни** — `GROUP BY`, `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` и `HAVING`.*

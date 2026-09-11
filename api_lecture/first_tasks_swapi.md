# 10 задачи за работа с SWAPI (без решения)

## Задача 1 — Първата заявка

Направете GET request към:

```
https://swapi.dev/api/people/1/
```

Изведете:
- името
- ръста
- теглото
- пола

Очаквано име: `Luke Skywalker`

---

## Задача 2 — Darth Vader

Направете заявка към:

```
https://swapi.dev/api/people/4/
```

Изведете:

```
Name: ...
Height: ...
Mass: ...
Hair color: ...
Eye color: ...
```

---

## Задача 3 — Всички персонажи

Направете GET request към:

```
https://swapi.dev/api/people/
```

Изведете имената на всички персонажи, които са върнати в текущата страница.

Пример:

```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
...
```

Бонус: изведете и броя на персонажите:

```
Total: X
```

---

## Задача 4 — Търсене

Използвайте `search` параметъра на API-то.

Направете програма, която търси:

```
luke
```

Изведете името на всеки намерен персонаж.

Използвайте:

```python
params = {"search": "luke"}
```

вместо да слагате параметъра директно в URL-а.

---

## Задача 5 — Планетата на Luke

Направете заявка за Luke Skywalker (people/1).

В отговора ще има поле `homeworld`, например:

```
"homeworld": "https://swapi.dev/api/planets/1/"
```

Използвайте този URL, за да направите втора API заявка и изведете:

```
Luke Skywalker's homeworld is Tatooine
```

---

## Задача 6 — Филмова информация

Направете заявка към:

```
https://swapi.dev/api/films/1/
```

Изведете:

```
Title: ...
Director: ...
Producer: ...
Release date: ...
Episode: ...
```

Бонус: изведете първите 100 символа от `opening_crawl`.

---

## Задача 7 — Търсене на филм

Направете програма, която пита потребителя:

```
Enter movie name:
```

Например: `A New Hope`.

След това направете API request със `search` и изведете:

```
Title: A New Hope
Director: George Lucas
Release date: 1977-05-25
```

---

## Задача 8 — Най-масивният герой

Изтеглете персонажите от:

```
https://swapi.dev/api/people/
```

Намерете персонажа с най-голяма маса.

Важно: `mass` идва като string (например "77"). Преобразувайте към число с `float(mass)` и игнорирайте стойности `"unknown"`.

Изведете:

```
The heaviest character is: ...
Mass: ... kg
```

---

## Задача 9 — Кои персонажи са участвали във филма?

Направете заявка към:

```
https://swapi.dev/api/films/1/
```

В отговора има списък `characters` с URL-и, например:

```
"characters": [
  "https://swapi.dev/api/people/1/",
  "https://swapi.dev/api/people/2/",
  ...
]
```

За всеки URL направете нов GET request и изведете:

```
Characters in A New Hope:
- Luke Skywalker
- C-3PO
- R2-D2
- Darth Vader
...
```

---

## Задача 10 — Star Wars Character Explorer (конзолна програма)

Направете малка конзолна програма с меню:

```
=========================
   STAR WARS EXPLORER
=========================

1. Search character
2. Search planet
3. Search film
4. Exit

Choose:
```

1) Search character: потребителят въвежда име, прави `/people/?search=...` и показва резултатите.

2) Search planet: потребителят въвежда име, прави `/planets/?search=...` и показва:
```
Name:
Climate:
Terrain:
Population:
Gravity:
```

3) Search film: потребителят въвежда име, прави `/films/?search=...` и показва:
```
Title:
Director:
Producer:
Release date:
```

4) Exit: програмата приключва.

---

Това са условията — дайте ги на студентите без решения. Успех!

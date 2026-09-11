# Лекция: Работа с API (пример: SWAPI)

## Какво е API?
API (Application Programming Interface) е начин за комуникация между две програми. Чрез API можем да поискаме информация или да изпратим данни към друг софтуер.

Пример разговор:

```
Дай ми информация за Luke Skywalker.
```

Към публичното API на Star Wars (SWAPI) това става така:

```
GET https://swapi.dev/api/people/1/
```

API-то ни връща JSON:

```json
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "gender": "male"
}
```

SWAPI е подходящ за упражнения, защото не изисква API ключ или автентикация.

---

## Какво е GET request?
`GET` означава "Дай ми информация". Пример:

```
GET /people/1/
```

Означава: върни човека с ID 1 (в SWAPI това е Luke Skywalker).

---

## Python библиотеката `requests`

Първо импортираме библиотеката:

```python
import requests
```

След това правим заявка:

```python
response = requests.get("https://swapi.dev/api/people/1/")
```

`response` е обект с информация за HTTP отговора. Пример:

```python
print(response.status_code)  # 200 означава OK
```

### Най-важните статус кодове (за начинаещи)
- 200 — OK (всичко е наред)
- 404 — Not Found (ресурсът не съществува)
- 400 — Bad Request (невалидна заявка)
- 500 — Server Error (грешка от сървъра)

---

## Как взимаме JSON-а?
API-то връща JSON. В `requests`:

```python
data = response.json()
```

Сега `data` е Python `dict` и можем да четем полета:

```python
print(data["name"])   # Luke Skywalker
print(data["height"]) # 172
print(data["mass"])   # 77
```

---

## Как работим с URL-и и query parameters

Примерен URL за търсене:

```
https://swapi.dev/api/people/?search=luke
```

Това ще търси хора, чието име съдържа "luke".

В Python имаме два подхода.

### Вариант 1 — директно:

```python
url = "https://swapi.dev/api/people/?search=luke"
response = requests.get(url)
```

### Вариант 2 — препоръчителен (по-добър):

```python
url = "https://swapi.dev/api/people/"
params = {"search": "luke"}
response = requests.get(url, params=params)
```

`requests` ще изгради URL-а автоматично и ще кодира параметрите правилно.

---

## Какво получаваме при списък (list endpoints)

Ако отидем на `https://swapi.dev/api/people/` ще получим структура, която съдържа:
- `count` — общ брой резултати
- `next` — URL за следващата страница (ако има)
- `previous` — URL за предишна страница
- `results` — списък от намерените обекти

Пример как да изведем всички имена на текущата страница:

```python
response = requests.get("https://swapi.dev/api/people/")
data = response.json()
for person in data["results"]:
    print(person["name"])
```

Това комбинира: API request → JSON → dict → list → loop.

---

## Пълен примерен скрипт

```python
import requests

# Пример: взимаме Luke Skywalker
url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Name:", data.get("name"))
    print("Height:", data.get("height"))
    print("Mass:", data.get("mass"))
else:
    print("Error:", response.status_code)

# Пример: търсене с params
url = "https://swapi.dev/api/people/"
params = {"search": "luke"}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    for person in data.get("results", []):
        print(person.get("name"))
else:
    print("Search error:", response.status_code)
```

---

## Съвети и добри практики
- Винаги проверявайте `status_code` преди да четете `response.json()`.
- Използвайте `params=` вместо ръчно форматиране на URL.
- Обработвайте възможните `KeyError` и използвайте `dict.get()` когато е уместно.
- При нужда от всички страници, следвайте полето `next` и правете заявки рекурсивно/в цикъл.

---

## Предложени упражнения за студентите
1. Напишете скрипт, който търси всички персонажи със "Skywalker" и печата техните имена.
2. Изведете всички планети от SWAPI (endpoint: `/planets/`) и брой резултати.
3. Направете скрипт, който следва `next` и обхожда всички страници от `people`, като брои общия брой имена.

---

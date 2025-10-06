# 🧩 15 Задачи с речници и списъци (над средно ниво)

---

## Задача 1: Анализ на продажби по категории

**Условие:**  
Напиши функция `analyze_sales(data)`, която приема речник с категории и списък от продажби за всяка категория. Трябва да върне речник с:
- средна продажба за всяка категория (закръглена до 2 десетични),
- категорията с най-висока обща продажба.

**Примерен тест:**
    ```python
    def analyze_sales(data):
        averages = {cat: round(sum(vals)/len(vals), 2) for cat, vals in data.items()}
        top_category = max(data, key=lambda c: sum(data[c]))
        return {"average_sales": averages, "top_category": top_category}

    data = {
      "Електроника": [1200, 800, 950],
      "Дрехи": [300, 500, 250],
      "Храни": [150, 200, 180]
    }
    print(analyze_sales(data))
    # Очакван изход:
    # {'average_sales': {'Електроника': 983.33, 'Дрехи': 350.0, 'Храни': 176.67}, 'top_category': 'Електроника'}
    ```

---

## Задача 2: Среден успех и отличник

**Условие:**  
Функция `class_statistics(grades)` приема речник `име -> [оценки]`. Трябва да върне:
- словар с (име -> среден успех, закръглен до 2),
- името на ученика с най-висок среден успех,
- среден успех на класа.

**Примерен тест:**
    ```python
    def class_statistics(grades):
        avgs = {n: round(sum(s)/len(s), 2) for n, s in grades.items()}
        top = max(avgs, key=avgs.get)
        class_avg = round(sum(avgs.values())/len(avgs), 2)
        return {"averages": avgs, "top_student": top, "class_avg": class_avg}

    grades = {"Иван": [5,6,6], "Мария": [6,6,5], "Петър": [4,5,4]}
    print(class_statistics(grades))
    # Очакван изход:
    # {'averages': {'Иван': 5.67, 'Мария': 5.67, 'Петър': 4.33}, 'top_student': 'Иван' (или 'Мария'), 'class_avg': 5.22}
    ```

---

## Задача 3: Филтриране на ученици по праг

**Условие:**  
Функция `filter_students(data, min_grade)` връща нов речник само с учениците, чиито средни оценки са >= `min_grade`.

**Примерен тест:**
    ```python
    def filter_students(data, min_grade):
        return {n: s for n, s in data.items() if sum(s)/len(s) >= min_grade}

    students = {"Иван": [4,5], "Мария": [6,6], "Петър": [3,4]}
    print(filter_students(students, 5))
    # Очакван изход:
    # {'Мария': [6, 6]}
    ```

---

## Задача 4: Сливане на продажби (сумиране)

**Условие:**  
Функция `merge_sales(q1, q2)` обединява два речника `продукт -> продажби`. Ако продуктът е в двата речника, стойностите се сумират.

**Примерен тест:**
    ```python
    def merge_sales(q1, q2):
        res = q1.copy()
        for k, v in q2.items():
            res[k] = res.get(k, 0) + v
        return res

    sales_q1 = {"A": 100, "B": 200}
    sales_q2 = {"A": 150, "C": 300}
    print(merge_sales(sales_q1, sales_q2))
    # Очакван изход:
    # {'A': 250, 'B': 200, 'C': 300}
    ```

---

## Задача 5: Броене на гласове и победител

**Условие:**  
`vote_count(votes)` приема списък от имена и връща речник `{име: брой}` и победителя (най-много гласове). При равенство върни някой от лидерите.

**Примерен тест:**
    ```python
    def vote_count(votes):
        cnt = {}
        for v in votes:
            cnt[v] = cnt.get(v,0) + 1
        winner = max(cnt, key=cnt.get)
        return cnt, winner

    votes = ["Иван","Мария","Иван","Петър","Мария","Иван"]
    print(vote_count(votes))
    # Очакван изход:
    # ({'Иван': 3, 'Мария': 2, 'Петър': 1}, 'Иван')
    ```

---

## Задача 6: Температурни статистики

**Условие:**  
Функция `temp_stats(data)` приема речник `град -> [температури]` и връща за всеки град средна, макс и мин температура (средната закръглена до 2).

**Примерен тест:**
    ```python
    def temp_stats(data):
        res = {}
        for city, vals in data.items():
            res[city] = {"avg": round(sum(vals)/len(vals), 2), "max": max(vals), "min": min(vals)}
        return res

    temps = {"Sofia":[20,22,25], "Varna":[18,19,17]}
    print(temp_stats(temps))
    # Очакван изход:
    # {'Sofia': {'avg': 22.33, 'max': 25, 'min': 20}, 'Varna': {'avg': 18.0, 'max': 19, 'min': 17}}
    ```

---

## Задача 7: Изчисляване на сметка за покупки

**Условие:**  
Функция `calculate_bill(store, purchases)` приема `store = {артикул: цена}` и `purchases = [(артикул, количество), ...]`. Връща крайна сума (round 2).

**Примерен тест:**
    ```python
    def calculate_bill(store, purchases):
        total = 0.0
        for item, qty in purchases:
            price = store.get(item)
            if price is None:
                continue
            total += price * qty
        return round(total, 2)

    store = {"ябълки":3.5, "банани":2.8, "портокали":4.0}
    print(calculate_bill(store, [("ябълки",2),("портокали",1)]))
    # Очакван изход:
    # 11.0
    ```

---

## Задача 8: Най-добър ученик по предмет

**Условие:**  
`best_in_subject(students, subject)` приема речник `име -> {предмет: оценка}` и връща името на ученика с най-добра оценка по `subject`. Ако няма оценки за предмета върни `None`.

**Примерен тест:**
    ```python
    def best_in_subject(students, subject):
        best = None
        best_score = -1
        for name, subs in students.items():
            if subject in subs and subs[subject] > best_score:
                best, best_score = name, subs[subject]
        return best

    students = {"Иван":{"math":6,"bio":5},"Мария":{"math":5,"bio":6}}
    print(best_in_subject(students, "bio"))
    # Очакван изход:
    # 'Мария'
    ```

---

## Задача 9: Честота на символите (букви)

**Условие:**  
`char_frequency(text)` брои честотата на всеки символ, игнорира интервали и пунктуация, използвай малки букви.

**Примерен тест:**
    ```python
    import string
    def char_frequency(text):
        freq = {}
        for ch in text.lower():
            if ch in string.ascii_lowercase or ch.isalpha():
                freq[ch] = freq.get(ch,0) + 1
        return freq

    print(char_frequency("Hello, world!"))
    # Очакван изход (поредността може да е различна):
    # {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
    ```

---

## Задача 10: Топ N резултати

**Условие:**  
`top_n_scores(scores, n)` приема речник `име -> точки` и връща списък от `n` топ елемента като `(име, точки)` сортирани низходящо.

**Примерен тест:**
    ```python
    def top_n_scores(scores, n):
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]

    scores = {"Иван":85,"Мария":92,"Петър":78}
    print(top_n_scores(scores, 2))
    # Очакван изход:
    # [('Мария', 92), ('Иван', 85)]
    ```

---

## Задача 11: Сумиране по категории (транзакции)

**Условие:**  
`sum_by_category(transactions)` приема списък от речници `{"категория":..., "сума":...}` и връща агрегиране `{категория: обща сума}`.

**Примерен тест:**
    ```python
    def sum_by_category(transactions):
        res = {}
        for t in transactions:
            c = t["категория"]
            res[c] = res.get(c, 0) + t["сума"]
        return res

    transactions = [
      {"категория":"храна","сума":12},
      {"категория":"транспорт","сума":8},
      {"категория":"храна","сума":20}
    ]
    print(sum_by_category(transactions))
    # Очакван изход:
    # {'храна': 32, 'транспорт': 8}
    ```

---

## Задача 12: Търсене на книги по ключова дума

**Условие:**  
`find_book(library, keyword)` приема `library = {заглавие: автор}` и връща списък от заглавия, които съдържат `keyword` (case-insensitive).

**Примерен тест:**
    ```python
    def find_book(library, keyword):
        kw = keyword.lower()
        return [title for title in library if kw in title.lower()]

    library = {"Python Basics":"John", "Learning C":"Anna", "Advanced Python":"Maria"}
    print(find_book(library, "Python"))
    # Очакван изход:
    # ['Python Basics', 'Advanced Python']
    ```

---

## Задача 13: Групиране на ученици по клас

**Условие:**  
`group_by_class(data)` приема списък от tuples `(име, клас)` и връща речник `клас -> [име]`.

**Примерен тест:**
    ```python
    def group_by_class(data):
        res = {}
        for name, cls in data:
            res.setdefault(cls, []).append(name)
        return res

    students = [("Иван",10),("Мария",11),("Петър",10)]
    print(group_by_class(students))
    # Очакван изход:
    # {10: ['Иван','Петър'], 11: ['Мария']}
    ```

---

## Задача 14: Проверка на наличности (недостиг)

**Условие:**  
`check_stock(stock, items)` проверява дали `stock` покрива `items` (и количествата). Връща списък на недостигащи артикули.

**Примерен тест:**
    ```python
    def check_stock(stock, items):
        shortage = []
        for item, need in items.items():
            if stock.get(item, 0) < need:
                shortage.append(item)
        return shortage

    print(check_stock({"мляко":10,"хляб":5}, {"мляко":8,"хляб":6}))
    # Очакван изход:
    # ['хляб']
    ```

---

## Задача 15: Комбиниране на списъци в речник и средна стойност

**Условие:**  
`combine_to_dict(names, values)` прави `{name: value}` и връща речника + средната стойност на `values` (round 2).

**Примерен тест:**
    ```python
    def combine_to_dict(names, values):
        d = dict(zip(names, values))
        avg = round(sum(values)/len(values), 2) if values else 0
        return d, avg

    students = ["Иван","Мария","Петър"]
    scores = [85,92,78]
    print(combine_to_dict(students, scores))
    # Очакван изход:
    # ({'Иван':85,'Мария':92,'Петър':78}, 85.0)
    ```

---

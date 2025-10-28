# История:
# Онлайн библиотека събира оценки на книги. Трябва да се покажат
# само най-добрите книги.
# Очакван изход: {'Dune': 4.75, 'It': 5.0}

def top_books(ratings, min_rating):
    best = {}

    for book, scores in ratings.items():
        if scores:  # ако има оценки
            avg = sum(scores) / len(scores)
            if avg >= min_rating:
                best[book] = round(avg, 2)

    return best

# Пример
ratings = {
    "Dune": [5, 5, 4, 5],
    "1984": [4, 3],
    "It": [5, 5, 5, 5, 5]
}

print(top_books(ratings, 3))

ratings = {"Dune":[5,5,4,5],"1984":[4,3],"It":[5,5,5,5,5]}
print(top_books(ratings, 3))
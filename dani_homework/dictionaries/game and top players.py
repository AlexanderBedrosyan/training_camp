# История:
# Играчите събират точки.
# Трябва да покажеш топ 3 по общ резултат.
# Очакван изход: [('Мария',90),('Гошо',60),('Иван',60)]

def top_players(players):
    total_scores = {}

    for name, list_of_score in players.items():
        total_scores[name] = sum(list_of_score)

    sorted_players = sorted(total_scores.items(), key=lambda x: x[1],  reverse=True)
    return sorted_players [:3]

data = {"Иван": [10, 20, 30],
        "Мария": [50, 40],
        "Петър": [15, 10, 15],
        "Гошо": [60]}
print(top_players(data))
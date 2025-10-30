# grades = {
#     "Anna": [5, 6, 6],
#     "Boris": [4, 5],
#     "Ivan": [6, 6, 6],
#     "Maria": [3, 4, 5]}
# Изисквания:
# Изчисли средната оценка на всеки студент.
# Създай речник само с отличниците (среден успех ≥ 5.50).
# Подреди резултатите по успех (низходящо).

grades = {
    "Anna": [5, 6, 6],
    "Boris": [4, 5],
    "Ivan": [6, 6, 6],
    "Maria": [3, 4, 5]
}

average_grades = {name: sum(st_grades) / len(st_grades) for name, st_grades in grades.items()}

excellent_students = {name: avg for name, avg in average_grades.items() if avg >= 5.50}

sorted_excellents = dict(sorted(excellent_students.items(), key=lambda x: x[1], reverse=True))

print("Среден успех на всички:")
for name, avg in average_grades.items():
    print(f"{name}: {avg:.2f}")

print("\nОтличници (≥ 5.50):")
for name, avg in sorted_excellents.items():
    print(f"{name}: {avg:.2f}")
# Таблица оценок студентов (15 студентов, 3 предмета)
grades = [
    [4, 5, 3],  # Оценки первого студента
    [5, 5, 4],  # Оценки второго студента
    [3, 2, 4],  # ...
    [5, 5, 5],
    [4, 4, 4],
    [3, 3, 3],
    [5, 4, 5],
    [2, 2, 2],
    [4, 5, 5],
    [5, 5, 4],
    [3, 4, 5],
    [2, 3, 4],
    [5, 5, 5],
    [4, 4, 4],
    [3, 3, 3]
]

# а) Количество студентов без двоек
students_without_twos = sum(1 for student in grades if 2 not in student)

# б) Количество предметов, по которым только "5" и "4"
subjects_with_only_4_and_5 = sum(
    1 for subject in zip(*grades) if all(grade in {4, 5} for grade in subject)
)

# в) Количество двоек по каждому предмету
twos_per_subject = [sum(1 for grade in subject if grade == 2) for subject in zip(*grades)]

print("а) Студенты без двоек:", students_without_twos)
print("б) Предметы с оценками только 4 и 5:", subjects_with_only_4_and_5)
print("в) Количество двоек по предметам:", twos_per_subject)

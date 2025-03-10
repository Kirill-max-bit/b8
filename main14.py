# Таблица оценок студентов (15 студентов, 3 предмета)
grades = [
    [4, 5, 3], [5, 5, 4], [3, 2, 4], [5, 5, 5], [4, 4, 4],
    [3, 3, 3], [5, 4, 5], [2, 2, 2], [4, 5, 5], [5, 5, 4],
    [3, 4, 5], [2, 3, 4], [5, 5, 5], [4, 4, 4], [3, 3, 3]
]

# а) Количество студентов без двоек
students_without_twos = sum(2 not in student for student in grades)

# б) Количество предметов с оценками только "5" и "4"
subjects_with_only_4_and_5 = sum(
    all(grade in {4, 5} for grade in subject)
    for subject in zip(*grades)
)

# в) Количество двоек по каждому предмету
twos_per_subject = [
    sum(grade == 2 for grade in subject)
    for subject in zip(*grades)
]

# Вывод результатов
print("а) Студенты без двоек:", students_without_twos)
print("б) Предметы с оценками только 4 и 5:", subjects_with_only_4_and_5)
print("в) Количество двоек по предметам:", twos_per_subject)

# Ввод данных
students = [
    [5, 4, 3],
    [4, 4, 4],
    [3, 2, 5],
    # ... остальные студенты
]

# а) Количество студентов, сдавших сессию без двоек
no_twos = sum(1 for grades in students if 2 not in grades)
print(f"Количество студентов без двоек: {no_twos}")

# б) Количество предметов, по которым были получены только оценки "5" и "4"
only_fours_and_fives = sum(1 for subject in zip(*students) if all(grade in {4, 5} for grade in subject))
print(f"Количество предметов с только '5' и '4': {only_fours_and_fives}")

# в) Количество двоек по каждому предмету
twos_per_subject = [subject.count(2) for subject in zip(*students)]
print(f"Количество двоек по каждому предмету: {twos_per_subject}")

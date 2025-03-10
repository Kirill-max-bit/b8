# Количество учеников и предметов
num_students = 18
num_subjects = 3

# Создаем пустую таблицу для оценок
grades = [[0 for _ in range(num_subjects)] for _ in range(num_students)]

# Ввод оценок по строкам (для каждого ученика)
for student in range(num_students):
    print(f"Введите оценки для ученика {student + 1}:")
    for subject in range(num_subjects):
        grades[student][subject] = int(input(f"Предмет {subject + 1}: "))

# Вывод оценок по строкам
print("\nОценки учеников:")
for student in range(num_students):
    print(f"Ученик {student + 1}:", end=" ")
    for subject in range(num_subjects):
        print(grades[student][subject], end=" ")
    print()

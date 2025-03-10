# Количество студентов в группах (5 курсов, 6 групп)
students = [
    [20, 25, 30, 35, 40, 45],  # 1-й курс
    [22, 27, 32, 37, 42, 47],  # 2-й курс
    [24, 29, 34, 39, 44, 49],  # 3-й курс
    [26, 31, 36, 41, 46, 51],  # 4-й курс
    [28, 33, 38, 43, 48, 53]   # 5-й курс
]


# б) Какая из групп самая малочисленная (указать номер курса и группы)
min_students = min(map(min, students))  # Минимальное количество студентов
for i, group in enumerate(students):
    if min_students in group:
        course, group_num = i + 1, group.index(min_students) + 1
        break
print(f"б) Мин. группа: {course} курс, {group_num} группа")

min_groups_per_course = [group.index(min(group)) + 1 for group in students]
print("в) Минимальные группы для каждого курса:", min_groups_per_course)

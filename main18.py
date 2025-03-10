# Ввод данных
classes = [
    [23, 25, 27, 22],
    [24, 26, 25, 23],
    # ... остальные параллели
]

# а) Сколько учеников учится в самом малочисленном классе школы
min_class = min(min(parallel) for parallel in classes)
print(f"Минимальное количество учеников в классе: {min_class}")


min_parallel = min(sum(parallel) for parallel in classes)
print(f"Минимальное количество учеников в параллели: {min_parallel}")


min_total = min(sum(parallel) for parallel in zip(*classes))
print(f"Минимальное общее количество учеников в классах А, Б, В, Г:{min_total}")

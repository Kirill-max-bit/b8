def find_smallest_taxicab_number():
    sums_of_cubes = {}

    # Перебираем все пары чисел (a, b), где a <= b
    for a in range(1, 100):
        for b in range(a, 100):
            s = a**3 + b**3  # Вычисляем сумму кубов
            if s in sums_of_cubes:
                sums_of_cubes[s].append((a, b))  # Добавляем новую пару
            else:
                sums_of_cubes[s] = [(a, b)]  # Создаем запись для новой суммы

    # Ищем минимальное число с двумя различными представлениями
    for s in sorted(sums_of_cubes.keys()):
        if len(sums_of_cubes[s]) >= 2:  # Проверяем, что есть хотя бы две пары
            return s, sums_of_cubes[s]


result, representations = find_smallest_taxicab_number()
print(f"Наименьшее число: {result}")
print("Представления:", representations)

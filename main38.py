# Оптимизированная функция для подсчета суммы собственных делителей числа
def sum_proper_divisors(n):
    if n == 1:
        return 0  # У числа 1 нет собственных делителей
    divisors_sum = 1  # Начинаем с 1, так как оно всегда является делителем
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Добавляем парный делитель, если он отличается
                divisors_sum += n // i
    return divisors_sum


divisor_sums = {}

# Поиск дружественных пар чисел
friendly_pairs = []
for num in range(1, 50000):
    # Вычисляем сумму собственных делителей для текущего числа
    divisor_sums[num] = sum_proper_divisors(num)
    pair = divisor_sums[num]

    # Проверяем условие дружественности
    if pair > num and pair in divisor_sums and divisor_sums[pair] == num:
        friendly_pairs.append((num, pair))

# Вывод результата
print("Дружественные пары чисел:", friendly_pairs)

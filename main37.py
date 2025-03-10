# Функция для подсчета суммы делителей числа
def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


a, b = map(int, input("Введите a, b через пробел: ").split())

# Находим максимальную сумму делителей в диапазоне [a, b]
max_sum = max(sum_of_divisors(num) for num in range(a, b + 1))

# Находим числа с максимальной суммой делителей
result = [num for num in range(a, b + 1) if sum_of_divisors(num) == max_sum]

# Вывод результата
print("Числа с максимальной суммой делителей:", result)

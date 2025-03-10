# Функция для подсчета количества делителей числа
def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


a, b, k = map(int, input("Введите a, b, k через пробел: ").split())

# Поиск чисел с ровно k делителями в интервале [a, b]
result = [num for num in range(a, b + 1) if count_divisors(num) == k]

# Вывод результата
print(f"Числа с {k} делителями в интервале [{a}, {b}]:", result)

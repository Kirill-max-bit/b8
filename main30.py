# Функция для подсчета количества делителей числа
def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


a, b = map(int, input("Введите a, b через пробел: ").split())

# Находим все числа и их количество делителей
numbers_with_divisors = [(num, count_divisors(num)) for num in range(a, b + 1)]

# а) Максимальное число с максимальным количеством делителей
max_divisor_count = max(div for _, div in numbers_with_divisors)
max_number = max(num for num, div in numbers_with_divisors if div
                 == max_divisor_count)
print("а) Максимальное число:", max_number)

# б) Минимальное число с максимальным количеством делителей
min_number = min(num for num, div in numbers_with_divisors if div
                 == max_divisor_count)
print("б) Минимальное число:", min_number)

# Функция для подсчета суммы делителей числа
def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


result = [num for num in range(300, 601) if sum_of_divisors(num) % 10 == 0]


print("Числа с суммой делителей, кратной 10:", result)

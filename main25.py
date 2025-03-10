# Функция для подсчета количества делителей числа
def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


results = {n: count_divisors(n) for n in range(120, 141)}

# Вывод результатов
for number, divisors in results.items():
    print(f"Число {number}: {divisors} делителей")

a, b, k = map(int, input("Введите a, b, k через пробел: ").split())
result = [num for num in range(a, b + 1) if count_divisors(num) == k]
print(f"Числа с {k} делителями в интервале [{a}, {b}]:", result)

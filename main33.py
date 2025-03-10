def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


results = {num: sum_of_divisors(num) for num in range(50, 71)}
print("Суммы делителей чисел от 50 до 70:", results)

def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


result = [num for num in range(1, 301) if count_divisors(num) == 5]
print("Числа с ровно пятью делителями:", result)

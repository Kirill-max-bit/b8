def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


result = [num for num in range(200, 501) if count_divisors(num) == 6]
print("Числа с ровно шестью делителями:", result)

# Функция для разложения числа на простые множители
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


n = int(input("Введите натуральное число n: "))

# 1) Каждый простой множитель один раз
unique_factors = sorted(set(prime_factors(n)))
print("Простые множители (уникальные):", unique_factors)

# 2) Каждый простой множитель столько раз, сколько он входит
all_factors = prime_factors(n)
print("Простые множители (с повторениями):", all_factors)

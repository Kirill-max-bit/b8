def sum_of_powers(m, n):
    return sum(i**n for i in range(1, m + 1))


m, n = map(int, input("Введите m и n через пробел: ").split())
result = sum_of_powers(m, n)
print(f"Сумма {m}^{n} + ... + 1^{n} =", result)

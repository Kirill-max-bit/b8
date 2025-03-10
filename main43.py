def sum_of_self_powers(n):
    return sum(i**i for i in range(1, n + 1))


n = int(input("Введите n: "))
result = sum_of_self_powers(n)
print(f"Сумма 1^1 + 2^2 + ... + {n}^{n} =", result)

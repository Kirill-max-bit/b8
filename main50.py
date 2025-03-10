def min_bills_for_amount(amount, denominations):
    result = {}
    for denom in sorted(denominations, reverse=True):
        count = amount // denom
        if count > 0:
            result[denom] = count
            amount -= count * denom
    return result


# Доступные номиналы купюр
denominations = [1, 2, 4, 8, 16, 32, 64]

# Ввод суммы n
n = int(input("Введите сумму n: "))

# Вывод минимального количества купюр для сумм от n до n + 10
for i in range(n, n + 11):
    bills = min_bills_for_amount(i, denominations)
    print(f"Минимальное количество купюр для {i}: {bills}")

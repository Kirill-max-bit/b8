def count_payment_ways(n):
    # Создаем массив для хранения количества способов выплаты
    dp = [0] * (n + 1)
    dp[0] = 1  # Базовый случай: 0 рублей можно выплатить одним способом
    coins = [1, 2, 5, 10]  # Доступные номиналы
    for coin in coins:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
    return dp[n]


n = int(input("Введите сумму n: "))
ways = count_payment_ways(n)
print(f"Количество способов выплатить {n} рублей:", ways)

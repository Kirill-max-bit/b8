# Стоимость товаров (5 видов)
prices = [10, 20, 30, 40, 50]

# Количество проданных товаров за 6 дней (5 видов, 6 дней)
sales = [
    [5, 10, 15, 20, 25, 30],  # Продажи товара 1
    [6, 12, 18, 24, 30, 36],  # Продажи товара 2
    [7, 14, 21, 28, 35, 42],  # Продажи товара 3
    [8, 16, 24, 32, 40, 48],  # Продажи товара 4
    [9, 18, 27, 36, 45, 54]   # Продажи товара 5
]


total_per_product = [sum(sales[i]) * prices[i] for i in range(len(prices))]
print("а) Доход по товарам:", total_per_product)


# б) Общий доход за каждый день
daily_totals = [
    sum(sales[j][i] * prices[j] for j in range(len(prices)))
    for i in range(len(sales[0]))
]
print("б) Доход по дням:", daily_totals)


best_product = total_per_product.index(max(total_per_product)) + 1
print("г) Лучший товар:", best_product)


best_product = total_per_product.index(max(total_per_product)) + 1
print("г) Лучший товар:", best_product)


best_day = daily_totals.index(max(daily_totals)) + 1
print("д) Лучший день:", best_day)


a = 5000  # Пороговое значение
days_above_a = sum(1 for total in daily_totals if total > a)
print("е) Дней с доходом > a:", days_above_a)

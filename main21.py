# Доход магазинов за 10 дней (3 магазина, 10 дней)
income = [
    [1000, 1200, 1100, 1300, 1400, 1500, 1600, 1700, 1800, 1900],  # Магазин 1
    [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],  # Магазин 2
    [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900]   # Магазин 3
]

best_days_per_shop = []  # Список для хранения лучших дней

for shop in income:
    max_income = max(shop)  # Находим максимальный доход в текущем магазине
    best_day = shop.index(max_income) + 1
    best_days_per_shop.append(best_day)

print("а) Лучшие дни для каждого магазина:", best_days_per_shop)


best_shops_per_day = []  # Список для хранения лучших магазинов

# Проходим по каждому дню (столбцу)
for day_index in range(len(income[0])):
    daily_incomes = [shop[day_index] for shop in income]
    max_income = max(daily_incomes)
    best_shop = daily_incomes.index(max_income) + 1
    best_shops_per_day.append(best_shop)

print("б) Лучшие магазины для каждого дня:", best_shops_per_day)

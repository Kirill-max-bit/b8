# а) Для каждого магазина — день с максимальным доходом
best_days_per_shop = [shop.index(max(shop)) + 1 for shop in income]

# б) Для каждого дня — магазин с максимальным доходом
best_shops_per_day = [day.index(max(day)) + 1 for day in zip(*income)]

print("а) Лучшие дни для каждого магазина:", best_days_per_shop)
print("б) Лучшие магазины для каждого дня:", best_shops_per_day)

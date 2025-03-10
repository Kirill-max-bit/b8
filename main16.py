# Ввод данных
salaries = [
    [1000, 1200, 1100],
    [900, 950, 1000],
    # ... остальные работники
]

# а) Максимальная зарплата из указанных в таблице
max_salary = max(max(month) for month in salaries)
print(f"Максимальная зарплата: {max_salary}")

# б) Порядковый номер работника, получившего за квартал наибольшую сумму
max_total = max(sum(month) for month in salaries)
worker_index = [sum(month) for month in salaries].index(max_total) + 1
print(f"Работник с наибольшей зарплатой за квартал: {worker_index}")

# в) В каком месяце общая зарплата всех работников была максимальной
monthly_totals = [sum(month[i] for month in salaries) for i in range(3)]
max_month = monthly_totals.index(max(monthly_totals)) + 1
print(f"Месяц с максимальной общей зарплатой: {max_month}")

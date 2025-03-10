# Зарплата работников за квартал (12 работников, 3 месяца)
salaries = [
    [30000, 32000, 31000],  # Зарплата первого работника
    [35000, 34000, 36000],
    [40000, 41000, 42000],
    [25000, 26000, 27000],
    [50000, 52000, 51000],
    [30000, 31000, 32000],
    [35000, 36000, 37000],
    [40000, 42000, 41000],
    [25000, 27000, 26000],
    [50000, 51000, 52000],
    [30000, 32000, 31000],
    [35000, 34000, 36000]
]


# а) Максимальная зарплата
max_salary = max(max(row) for row in salaries)

# б) Номер работника с максимальной суммой за квартал
worker_with_max_total = max(range(len(salaries)), key=lambda i: sum(salaries[i]))

# в) Месяц с максимальной общей зарплатой
monthly_totals = [sum(month) for month in zip(*salaries)]
month_with_max_total = monthly_totals.index(max(monthly_totals)) + 1

print("а) Максимальная зарплата:", max_salary)
print("б) Работник с максимальной суммой:", worker_with_max_total + 1)
print("в) Месяц с максимальной зарплатой:", month_with_max_total)

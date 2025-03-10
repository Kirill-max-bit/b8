# а) Месяц с максимальной зарплатой для каждого работника
best_month_per_worker = [row.index(max(row)) + 1 for row in salaries]

# б) Работник с максимальной зарплатой в каждом месяце
best_worker_per_month = [monthly.index(max(monthly)) + 1 for monthly in zip(*salaries)]

print("а) Лучший месяц для каждого работника:", best_month_per_worker)
print("б) Лучший работник в каждом месяце:", best_worker_per_month)

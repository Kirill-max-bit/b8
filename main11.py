# Инициализация таблицы зарплат
workers = 12
months = 3

# Создаем таблицу для хранения зарплат
salary_table = [[0 for _ in range(months)] for _ in range(workers)]

# Ввод данных
for worker in range(workers):
    for month in range(months):
        prompt = f"Введите зарплату для работника {worker + 1}, месяц {month + 1}: "
        salary = int(input(prompt))
        salary_table[worker][month] = salary


total_salary_all = sum(sum(row) for row in salary_table)
print(f"\nОбщая сумма, выплаченная за квартал всем работникам: {total_salary_all}")

# б) Зарплата, полученная за квартал каждым работником
print("\nЗарплата, полученная за квартал каждым работником:")
for worker in range(workers):
    total_salary_worker = sum(salary_table[worker])
    print(f"Работник {worker + 1}: {total_salary_worker}")


print("\nОбщая зарплата всех работников за каждый месяц:")
for month in range(months):
    total_salary_month = sum(row[month] for row in salary_table)
    print(f"Месяц {month + 1}: {total_salary_month}")

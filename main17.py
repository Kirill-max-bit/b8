# а) Для каждого работника — в какой из месяцев он получил наибольшую зарплату
for i, worker in enumerate(salaries):
    max_month = worker.index(max(worker)) + 1
    print(f"Работник {i+1} получил наибольшую зарплату в месяце {max_month}")


for month in range(3):
    max_salary = max(salaries[i][month] for i in range(len(salaries)))
    worker_index = [salaries[i][month] for i in range(len(salaries))].index(max_salary) + 1
    print(f"В месяце {month+1} наибольшую зарплату получил работник {worker_index}")

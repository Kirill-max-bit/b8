workers, months = 12, 3
salary = [[0]*months for _ in range(workers)]

for w in range(workers):
    for m in range(months):
        while True:
            try:
                salary[w][m] = int(input(f"Работник {w+1}, месяц {m+1}: "))
                break
            except ValueError:
                print("Введите целое число!")

total = sum(map(sum, salary))
print(f"\nа) Общая сумма: {total}")

print("\nб) Зарплата по работникам:")
for i, s in enumerate(map(sum, salary), 1):
    print(f"Работник {i}: {s}")

print("\nв) Зарплата по месяцам:")
for i, s in enumerate(map(sum, zip(*salary)), 1):
    print(f"Месяц {i}: {s}")

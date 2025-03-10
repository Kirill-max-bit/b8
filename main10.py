sportsmen = 8
sports = 5

table = [[0 for _ in range(sports)] for _ in range(sportsmen)]

for sport_idx in range(sports):
    for sportsman_idx in range(sportsmen):
        prompt = f"Введите балл для вида {sport_idx + 1}, спортсмена {sportsman_idx + 1}: "
        value = input(prompt)
        table[sportsman_idx][sport_idx] = int(value)
        print(f"\r{prompt}{value} {value}", end='\n')

# Вывод таблицы
print("\nРезультат:")
for row in table:
    print(' '.join(map(str, row)))

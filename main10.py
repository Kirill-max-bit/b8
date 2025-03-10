sportsmen, sports = 8, 5
table = [[0]*sports for _ in range(sportsmen)]

for sport in range(sports):
    for man in range(sportsmen):
        while True:
            try:
                prompt = f"Балл вида {sport+1} для спортсмена {man+1}: "
                table[man][sport] = int(input(prompt))
                break
            except ValueError:
                print("Введите целое число!")

print("\nРезультат:")
print('\n'.join(' '.join(map(str, row)) for row in table))

grades = [[0]*3 for _ in range(18)]

for s in range(18):
    for j in range(3):
        while True:
            try:
                grades[s][j] = int(input(f"Ученик {s+1}, предмет {j+1}: "))
                break
            except ValueError:
                print("Введите целое число!")

print(f"\nа) Пятерок: {sum(r.count(5) for r in grades)}")

print("\nб) Троек у учеников:")
for i, row in enumerate(grades):
    print(f"{i+1}: {row.count(3)}")

print("\nв) Двоек по предметам:")
for i, col in enumerate(zip(*grades)):
    print(f"{i+1}: {col.count(2)}")

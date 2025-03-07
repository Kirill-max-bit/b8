for _ in range(4):
    print('5 ' * 6)

for _ in range(4):
    for i in range(1, 11):
        print(i, end=' ')
    print()

start = 41
for row in range(4):
    for num in range(start, start + 10):
        print(num, end=' ')
    print()
    start += 10

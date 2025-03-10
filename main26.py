n = int(input("Введите число n: "))

for num in range(1, n + 1):
    divisors_count = sum(1 for i in range(1, num + 1) if num % i == 0)
    print(f"{num}{'+' * divisors_count}")

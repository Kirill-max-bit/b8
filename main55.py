from math import gcd


def coprime_numbers(n):
    return [i for i in range(1, n) if gcd(i, n) == 1]


n = int(input("Введите натуральное число n: "))
print("Числа, взаимно простые с", n, ":", coprime_numbers(n))

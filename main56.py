from math import gcd


def coprime_numbers_with_p(n, p):
    return [i for i in range(1, n) if gcd(i, p) == 1]


n, p = map(int, input("Введите n и p через пробел: ").split())
print("Числа, взаимно простые с", p, "и меньшие", n, ":",
    coprime_numbers_with_p(n, p))

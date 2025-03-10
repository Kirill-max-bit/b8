from math import gcd


def coprime_numbers_with_p(n, p):
    return [i for i in range(1, n) if gcd(i, p) == 1]


try:
    n, p = map(int, input("Введите n и p через пробел: ").split())
    if n <= 0 or p <= 0:
        print("Ошибка: n и p должны быть натуральными числами (больше 0).")
    else:
        # Вычисление и вывод результата
        result = coprime_numbers_with_p(n, p)
        print(f"Числа, взаимно простые с {p} и меньшие {n}: {result}")
except ValueError:
    print("Ошибка: Введите два целых числа через пробел.")

from math import gcd


def coprime_divisors(q, p):
    divisors = [i for i in range(1, q + 1) if q % i == 0]
    return [d for d in divisors if gcd(d, p) == 1]


q, p = map(int, input("Введите q и p через пробел: ").split())
print("Делители числа", q, ", взаимно с", p, ":", coprime_divisors(q, p))

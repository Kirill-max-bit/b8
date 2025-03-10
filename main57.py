from math import gcd

# Функция для получения всех делителей числа q, взаимно простых с p
def coprime_divisors(q, p):
    divisors = [i for i in range(1, q + 1) if q % i == 0]
    return [d for d in divisors if gcd(d, p) == 1]

# Ввод чисел
q, p = map(int, input("Введите q и p через пробел: ").split())
print("Делители числа", q, ", взаимно простые с", p, ":", coprime_divisors(q, p))
from math import gcd


def irreducible_fractions(max_denominator):
    fractions = []
    for denominator in range(2, max_denominator + 1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                fractions.append((numerator, denominator))
    return fractions


max_denominator = 7
fractions = irreducible_fractions(max_denominator)
print("Простые несократимые дроби с знаменателями ≤ 7:")
for num, den in fractions:
    print(f"{num}/{den}")

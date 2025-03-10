def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


n = int(input("Введите число: "))
root = digital_root(n)
print(f"Цифровой корень числа {n}:", root)

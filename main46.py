from math import gcd


def find_gcd_of_list(numbers):
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:  # Если НОД стал 1, дальше вычислять нет смысла
            break
    return current_gcd


numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = find_gcd_of_list(numbers)
print(f"НОД чисел {numbers} =", result)

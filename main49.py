def find_numbers_with_square_digit_sum(n, m):
    results = []
    for num in range(1, n):
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum**2 == m:
            results.append(num)
    return results


n, m = map(int, input("Введите n и m через пробел: ").split())
numbers = find_numbers_with_square_digit_sum(n, m)
print(f"Числа меньше {n}, квадрат суммы цифр которых равен {m}:", numbers)

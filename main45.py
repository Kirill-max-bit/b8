def find_unique_digit_numbers():
    results = []
    for num in range(100, 1000):  # Все трехзначные числа
        digits = list(map(int, str(num)))  # Разбиваем число на цифры
        if len(set(digits)) == 3:  # Проверяем, что все цифры уникальны
            results.append(num)
    return results


numbers = find_unique_digit_numbers()
print("Трехзначные числа без повторяющихся цифр:", numbers)

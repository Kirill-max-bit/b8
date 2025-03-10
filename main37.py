a, b = map(int, input("Введите a, b через пробел: ").split())

max_sum = max(sum_of_divisors(num) for num in range(a, b + 1))
result = [num for num in range(a, b + 1) if sum_of_divisors(num) == max_sum]
print("Числа с максимальной суммой делителей:", result)

result = [num for num in range(300, 601) if sum_of_divisors(num) % 10 == 0]
print("Числа с суммой делителей, кратной 10:", result)
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


perfect_numbers = [num for num in range(1, 100000) if is_perfect(num)]
print("Совершенные числа:", perfect_numbers)

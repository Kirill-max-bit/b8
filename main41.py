# Ищем все решения уравнения x^2 + y^2 = k^2 в интервале [1, 30]
solutions = []
for k in range(1, 31):
    for x in range(1, k):  # x < k
        y_squared = k**2 - x**2
        y = int(y_squared**0.5)
        if y > 0 and y <= x and y**2 == y_squared:
            solutions.append((x, y, k))

# Вывод результатов
print("Натуральные решения (x, y, k):", solutions)

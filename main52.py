def find_combinations(total_money, total_heads):
    solutions = []
    for bulls in range(total_heads + 1):
        for cows in range(total_heads - bulls + 1):
            calves = total_heads - bulls - cows
            if bulls * 10 + cows * 5 + calves * 0.5 == total_money:
                solutions.append((bulls, cows, calves))
    return solutions


total_money = 100
total_heads = 100
solutions = find_combinations(total_money, total_heads)
print("Возможные комбинации (быки, коровы, телята):", solutions)

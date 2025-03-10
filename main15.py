# Ввод данных
athletes = [
    [10, 9, 8, 7, 6],
    [9, 8, 7, 6, 5],
    # ... остальные спортсмены
]

# а) Максимальная из оценок в таблице
max_score = max(max(scores) for scores in athletes)
print(f"Максимальная оценка: {max_score}")

# б) Сколько баллов набрал победитель соревнований
winner_score = max(sum(scores) for scores in athletes)
print(f"Баллы победителя: {winner_score}")

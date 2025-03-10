s = int(input("Введите площадь s: "))
rectangles = [(i, s // i) for i in range(1, s + 1) if s % i == 0]
print("Разные прямоугольники:", rectangles)


unique_rectangles = {(min(i, s // i), max(i, s // i)) for i in range(1, s + 1)
                     if s % i == 0}
print("Уникальные прямоугольники:", unique_rectangles)

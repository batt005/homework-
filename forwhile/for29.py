n = int(input("Введите целое число N ( > 1 ): "))
a = float(input("Введите вещественную точку A: "))
b = float(input("Введите вещественную точку B (A < B): "))
h = (b - a) / n
print(f"Длина отрезка H = {h}")
print("Набор точек разбиения:")
for i in range(n + 1):
    point = a + i * h
    print(point)

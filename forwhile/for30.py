import math
n = int(input("Введите целое число N ( > 1 ): "))
a = float(input("Введите вещественную точку A: "))
b = float(input("Введите вещественную точку B (A < B): "))
h = (b - a) / n
print(f"Длина отрезка H = {h}")
print("Значения функции F(X) в точках разбиения:")
for i in range(n + 1):
    x = a + i * h
    f = 1 - math.sin(x)
    print(f)

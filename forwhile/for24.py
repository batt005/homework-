X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))
term = 1
sum = 1
for i in range(1, N + 1):
    term = -term * X * X / ((2 * i - 1) * (2 * i))
    sum += term
print(f"Приближённое значение cos({X}): {sum}")

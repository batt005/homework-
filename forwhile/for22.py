X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))
term = 1.0
sum = 0.0
for i in range(1, N + 1):
    term *= X/i
    sum += term
print(f"Приближённое значение exp({X}): {sum}")

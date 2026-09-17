X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))
term = X
sum = X
for i in range(1, N + 1):
    term *= -(X ** 2) / ((2 * i) * (2 * i + 1)) #по реккурентной формуле
    sum += term
print(f"Приближённое значение sin({X}): {sum}")

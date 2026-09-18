X = float(input('Введите вещественное число Х ( модуль Х < 1): '))
N = int(input('Введите целое число N (N > 0): '))
total_sum = 1.0
current_term = 1.0
for i in range(1, N + 1):
    current_term = current_term * (-X) * (2 * i - 3) / (2 * i)
    total_sum += current_term
print(f"Приближенное значение выражения: {total_sum}")

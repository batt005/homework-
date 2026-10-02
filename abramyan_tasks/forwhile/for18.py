A = float(input("Введите вещественное число А: "))
N = int(input("Введите целое число N (> 0): "))
sum = 1.0
current_term = 1.0
for i in range(1, N + 1):
    current_term *= -A
    sum += current_term
print(f"Значение выражения: {sum}")

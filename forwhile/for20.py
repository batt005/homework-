N = int(input("Введите целое число N (> 0): "))
sum = 0.0
factorial = 1.0
for i in range(1, N + 1):
    factorial *= i
    sum += factorial
print(f"Сумма факториалов = {sum}")

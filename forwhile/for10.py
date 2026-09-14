N = int(input("Введите целое положительное число N: "))
sum = 0.0
for i in range(1, N + 1):
    sum += 1 / i
print(f"Сумма ряда для N = {N} равна: {sum}")
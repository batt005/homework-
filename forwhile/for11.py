N = int(input("Введите целое положительное число N: "))
sum = 0
for i in range(N, 2 * N + 1):
    sum += i ** 2
print(f"Сумма квадратов для N = {N} равна: {sum}")
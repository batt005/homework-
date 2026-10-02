n = int(input("Введите целое число N: "))
k = int(input("Введите целое число K: "))
total_sum = 0.0
for i in range(1, n + 1):
    total_sum += float(i) ** k
print(f"Сумма равна: {total_sum}")

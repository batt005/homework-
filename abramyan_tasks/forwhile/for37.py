n = int(input("Введите целое число N ( > 0 ): "))
total_sum = 0.0
for i in range(1, n + 1):
    total_sum += float(i) ** i
print(f"Сумма равна: {total_sum}")

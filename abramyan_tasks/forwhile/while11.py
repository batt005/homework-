n = int(input("Введите целое число N ( > 1 ): "))
k = 0
total_sum = 0
while total_sum < n:
    k = k + 1
    total_sum = total_sum + k
print(f"Наименьшее K = {k}")
print(f"Сумма равна = {total_sum}")

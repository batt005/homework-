n = int(input("Введите целое число N ( > 1 ): "))
k = 0
total_sum = 0
while total_sum + (k + 1) <= n:
    k = k + 1
    total_sum = total_sum + k
print(f"Наибольшее K = {k}")
print(f"Сумма равна = {total_sum}")

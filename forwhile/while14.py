a = float(input("Введите вещественное число A ( > 1 ): "))
k = 0
total_sum = 0.0
while total_sum + 1 / (k + 1) < a:
    k = k + 1
    total_sum = total_sum + 1 / k
print(f"Наибольшее K = {k}")
print(f"Сумма равна = {total_sum}")

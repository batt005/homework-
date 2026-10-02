a = float(input("Введите вещественное число A ( > 1 ): "))
k = 0
total_sum = 0.0
while total_sum <= a:
    k = k + 1
    total_sum = total_sum + 1 / k
print(f"Наименьшее K = {k}")
print(f"Сумма равна = {total_sum}")

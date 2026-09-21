n = int(input("Введите целое число N ( > 1 ): "))
k = 1
while 3 ** k <= n:
    k = k + 1
print(f"Наименьшее K = {k}")

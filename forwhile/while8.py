n = int(input("Введите целое число N ( > 0 ): "))
k = 1
while k * k <= n:
    k = k + 1
k = k - 1
print(f"Наибольшее K = {k}")

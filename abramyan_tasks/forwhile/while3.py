n = int(input("Введите целое положительное число N: "))
k = int(input("Введите целое положительное число K: "))
quotient = 0
while n >= k:
    n = n - k
    quotient = quotient + 1
print(f"Частное от деления нацело: {quotient}")
print(f"Остаток от деления: {n}")


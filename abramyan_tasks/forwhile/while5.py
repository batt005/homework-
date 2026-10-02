n = int(input("Введите целое число N ( > 0 ): "))
k = 0
while n > 1:
    n = n // 2
    k = k + 1
print(f"Показатель степени K = {k}")

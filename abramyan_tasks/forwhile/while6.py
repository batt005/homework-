n = int(input("Введите целое число N ( > 0 ): "))
result = 1.0
while n > 0:
    result = result * n
    n = n - 2
print(f"Двойной факториал N!! = {result}")

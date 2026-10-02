n = int(input("Введите целое число N ( > 0 ): "))
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10
print(f"Перевернутое число: {reversed_n}")

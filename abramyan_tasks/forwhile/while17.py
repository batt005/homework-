n = int(input("Введите целое число N ( > 0 ): "))
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

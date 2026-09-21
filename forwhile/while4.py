n = int(input("Введите целое число N ( > 0 ): "))
while n > 1 and n % 3 == 0:
    n = n // 3
if n == 1:
    print("TRUE")
else:
    print("FALSE")

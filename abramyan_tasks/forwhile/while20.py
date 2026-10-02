n = int(input("Введите целое число N ( > 0 ): "))
has_two = False
while n > 0:
    digit = n % 10
    if digit == 2:
        has_two = True
    n = n // 10
if has_two:
    print("TRUE")
else:
    print("FALSE")

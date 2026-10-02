n = int(input("Введите целое число N ( > 0 ): "))
has_odd = False
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        has_odd = True
    n = n // 10
if has_odd:
    print("TRUE")
else:
    print("FALSE")

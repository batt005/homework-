n = int(input("Введите целое число N ( > 0 ): "))
digit_sum = 0
digit_count = 0
while n > 0:
    digit = n % 10
    digit_sum = digit_sum + digit
    digit_count = digit_count + 1
    n = n // 10
print(f"Количество цифр: {digit_count}")
print(f"Сумма цифр: {digit_sum}")

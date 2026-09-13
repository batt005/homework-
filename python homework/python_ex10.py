a = float(input("Введите число: "))
b = float(input("Введите число: "))
if a==0 or b==0:
    print("Ошибка. Введите ненулевое число.")
minus = a**a - b**b
plus = a**a + b**b
product = a**a * b**b
division = a**a / b**b
print("Разность: ", minus)
print("Сумма: ", plus)
print("Произведение: ", product)
print("Частное", division)


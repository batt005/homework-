A = int(input("Введите число A: "))
B = int(input("Введите число B > A: "))
sum_sqrs = 0
for i in range(A, B + 1):
    sum_sqrs += i ** 2
print(f"Сумма квадратов чисел от {A} до {B} равна: {sum_sqrs}")
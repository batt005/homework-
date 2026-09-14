A = int(input("Введите число A: "))
B = int(input("Введите число B > A: "))
sum = 0
for i in range(A, B + 1):
    sum += i

print(f"Сумма чисел от {A} до {B} равна: {sum}")

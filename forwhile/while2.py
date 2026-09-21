a = float(input("Введите положительное число A: "))
b = float(input("Введите положительное число B (A > B): "))
count = 0
while a >= b:
    a = a - b
    count = count + 1
print(f"Количество отрезков B: {count}")

a = int(input("Введите целое положительное число A: "))
b = int(input("Введите целое положительное число B: "))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(f"Наибольший общий делитель (НОД) = {a}")

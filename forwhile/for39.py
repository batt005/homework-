a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (A < B): "))
for i in range(a, b + 1):
    for j in range(i):
        print(i)

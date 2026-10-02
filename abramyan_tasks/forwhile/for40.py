a = int(input("Введите целое число A: "))
b = int(input("Введите целое число B (A < B): "))
for i in range(a, b + 1):
    count = i - a + 1
    for j in range(count):
        print(i)

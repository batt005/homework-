n = int(input('Введите значение N: '))
k = 1
for i in range(1, 2*n):
    if i % 2 == 0:
        k += i
        print(k)

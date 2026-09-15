n = int(input('Введите значение N: '))
k = 1.0
for i in range (0, n+1):
    k *= 1 + i/10
    print(k)

A = float(input('Введите А: '))
N = int(input('Введите целое N (> 0): '))
power = 1
sum = 1
for i in range(1, N + 1):
    power *= A
    sum += power
print(f'Сумма ряда: {sum}')

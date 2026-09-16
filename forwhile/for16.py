A = float(input('Введите А: '))
N = int(input('Введите целое N (> 0): '))
power = 1
powers_list = []
for i in range(1, N + 1):
    power *= A
    powers_list.append(power)
print(powers_list)

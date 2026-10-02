A = float(input('Введите А: '))
N = int(input('Введите целое N (> 0): '))
power = [A ** i for i in range(1, N+1)]
print(power)

A = float(input('Введите А: '))
N = int(input('Введите целое N (> 0): '))
result = 1
for _ in range(N):
    result *= A
print(f'Число {A} в степени {N} равно {result}')

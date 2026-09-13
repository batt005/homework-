A = float(input('Введите число А: '))
B = float(input('Введите число В: '))
if A != 0:
    x = -B / A
    print(f'Решение {A}x + {B} = 0 is: x = {round(x, 2)}')
else:
    print("А не может быть равно нулю.")

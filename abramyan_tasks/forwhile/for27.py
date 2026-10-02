x = float(input('Введите вещественное число (модуль x < 1): '))
n = int(input('Ввелите целое число N (N > 0) :'))
sum = x
term = x
sqrd_x = x * x
for i in range(1, n + 1):
    y = ((2 * i - 1) ** 2 * sqrd_x) / ((2 * i) * (2 * i + 1))
    term = term * y
    sum = sum + term
print(f'Приближённое значение функции arcsin(x): {sum}')

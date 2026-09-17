x = float(input("Введите вещественное число Х (модуль Х < 1): "))
n = int(input('Введите целое число N ( > 0 ): '))
sum = 0
term = x
for i in range(1, n+1):
    sum += term / i
    term = -term * x
print(f'Приближенное значение функции In(1 + x) : {sum}')

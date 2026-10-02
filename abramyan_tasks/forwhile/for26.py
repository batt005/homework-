x = float(input("Введите вещественное число Х (модуль Х < 1): "))
n = int(input('Введите целое число N ( > 0 ): '))
sum = x
sign = -1
term = x
for i in range(1, n+1):
    term = sign*(x **(2*i+1)) / (2*i+1)
    sum += term
    sign = -sign
print(f'Приближенное значение функции arctg(x) : {sum}')

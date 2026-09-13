A = float(input('Введите число А: '))
B = float(input('Введите число В: '))
C = float(input('Введите число С: '))
if C > A and C < B:
    AC = (abs(C - A))
    BC = (abs(C - B))
    print('Длина отрезка АС: ', round(AC, 2))
    print('Длина отрезка ВС: ', round(BC, 2))
else:
    print('Число С должно быть между числами А и В')

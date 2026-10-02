
x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))
x3 = float(input('Введите x3: '))
y3 = float(input('Введите y3: '))
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
P = a + b + c
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('Площадь треугольника: ', round(S, 2))
print('Периметр треугольника: ', round(P, 2))

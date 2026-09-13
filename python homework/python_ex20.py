x1 = float(input('Введите х1: '))
x2 = float(input('Введите x2: '))
y1 = float(input('Введите y1: '))
y2 = float(input('Введите y2: '))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Расстояние между точками: ', round(distance, 2))

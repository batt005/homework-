X = float(input('Введите вес(X) в кг: '))
A = float(input('Введите цену: '))
Y = float(input('Введите вес(Y) в кг: '))
price_per_kg = A / X
cost_Y = price_per_kg * Y
print('Цена за 1 кг = ', round(price_per_kg, 2))
print(f'Цена за {Y} кг = ', round(cost_Y, 2))

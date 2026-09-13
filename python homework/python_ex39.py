A = float(input('Введите число А: '))
B = float(input('Введите число В: '))
C = float(input('Введите число С: '))
D = B**2 - 4*A*C
if D > 0:
    x1 = (-B + D**0.5) / (2*A)
    x2 = (-B - D**0.5) / (2*A)
    print(f'Уравнение {A}x^2 + {B}x + {C} = 0 имеет два корня: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}')
elif D == 0:
    x = -B / (2*A)
    print(f'Уравнение {A}x^2 + {B}x + {C} = 0 имеет один корень: x = {round(x, 2)}')
else:
    print(f'Уравнение {A}x^2 + {B}x + {C} = 0 не имеет корней.')

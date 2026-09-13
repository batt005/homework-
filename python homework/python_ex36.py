V1 = float(input('Скорость 1 машины (V1): '))
V2 = float(input('Скорость 2 машины (V2): '))
S = float(input('Расстояние между машинами (S): '))
T = float(input('Время между машинами (T): '))
distance = S + (V1 + V2) * T
print(f'Расстояние между машинами спустя время {T} : (distance, )')

def Minmax(X, Y):
    if X > Y:
        X, Y = Y, X
    return X, Y
A = 2
B = 1
C = 6
D = 8
print("Исходные числа:")
print(f"A = {A}, B = {B}, C = {C}, D = {D}")
A, B = Minmax(A, B)
C, D = Minmax(C, D)
A, C = Minmax(A, C)
B, D = Minmax(B, D)
print(f"Абсолют. минимум (A): {A}")
print(f"Абсолют. максимум (D): {D}")
print(f"Все переменные: A = {A}, B = {B}, C = {C}, D = {D}")

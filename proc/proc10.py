def Swap(X, Y):
    return Y, X
A = 2
B = 4
C = 6
D = 8
print("Исходные значения:")
print(f"A = {A}, B = {B}, C = {C}, D = {D}")
A, B = Swap(A, B)
C, D = Swap(C, D)
B, C = Swap(B, C)
print("Новые значения:")
print(f"A = {A}, B = {B}, C = {C}, D = {D}")

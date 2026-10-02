def AddRightDigit(D, K):
    K[0] = K[0] * 10 + D
start_number = 15
D1 = 4
D2 = 7
container = [start_number]
print(f"Исходное число K: {container[0]}")
AddRightDigit(D1, container)
print(f"После добавления D1 ({D1}): {container[0]}")
AddRightDigit(D2, container)
print(f"После добавления D2 ({D2}): {container[0]}")

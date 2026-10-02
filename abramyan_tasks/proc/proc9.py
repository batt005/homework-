def AddLeftDigit(D, K):
    digit_count = len(str(K))
    K = D * (10 ** digit_count) + K
    return K
K = 15
D1 = 7
D2 = 5
print(f"Исходное число K: {K}")
K = AddLeftDigit(D1, K)
print(f"После добавления D1 ({D1}) слева: {K}")
K = AddLeftDigit(D2, K)
print(f"После добавления D2 ({D2}) слева: {K}")

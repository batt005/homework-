def InvertDigits(K):
    K[0] = int("".join(reversed(str(K[0]))))
numbers = [12345, 607, 1245, 57, 68345]
print("Исходные числа и их инвертированные копии:")
for num in numbers:
    container = [num]
    InvertDigits(container)
    inverted_num = container[0]
    print(f"Было: {num},  Стало: {inverted_num}")

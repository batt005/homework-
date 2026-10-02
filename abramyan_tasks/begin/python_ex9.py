a = float(input("Введите число: "))
b = float(input("Введите число: "))
if a < 0 or b < 0:
    print("Ошибка. Введите неотрицательное число.")
mean_geometric = (a * b) ** 0.5
print("Среднее геометрическое: ", mean_geometric)

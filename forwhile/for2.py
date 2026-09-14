a = int(input("Введите A: "))
b = int(input("Введите B: "))
n = b - a + 1
if a >= b:
    print("Число А должно быть меньше В")
for i in range(a, b + 1):
    print(i, end=" ")
print(f"\nКол-во чисел: {n}")

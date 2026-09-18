n = int(input("Введите целое число N ( > 0 ): "))
a = 2.0
for k in range(1, n + 1):
    a = 2 + 1 / a
    print(f"A{k} = {a}")

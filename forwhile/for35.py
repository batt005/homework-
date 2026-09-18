n = int(input("Введите целое число N ( > 2 ): "))
a1 = 1.0
a2 = 2.0
a3 = 3.0
print(f"A1 = {a1}")
print(f"A2 = {a2}")
print(f"A3 = {a3}")
for k in range(4, n + 1):
    ak = a2 + a1 - 2 * a3
    print(f"A{k} = {ak}")
    a1 = a2
    a2 = a3
    a3 = ak


n = int(input("Введите целое число N ( > 1 ): "))
a1 = 1.0
a2 = 2.0
print(f"A1 = {a1}")
if n > 1:
    print(f"A2 = {a2}")
for k in range(3, n + 1):
    ak = (a1 + 2 * a2) / 3
    print(f"A{k} = {ak}")
    a1 = a2
    a2 = ak

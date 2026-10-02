n = int(input("Введите целое число N ( > 1 ): "))
f1 = 1
f2 = 1
print(f"F1 = {f1}")
if n > 1:
    print(f"F2 = {f2}")
for k in range(3, n + 1):
    fk = f1 + f2
    print(f"F{k} = {fk}")
    f1 = f2
    f2 = fk

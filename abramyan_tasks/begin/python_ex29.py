pi = 3.14
a = float(input("Введите a: "))
if a <= 0 or a >= 360:
    print("точка а должна быть в радиусе [0, 360]")
else:
    randian = pi * a / 180
    print(f"радианов = {randian}")

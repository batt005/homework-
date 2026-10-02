pi = 3.14
a = float(input("Введите a: "))
if a <= 0 or a >= 2*pi:
    print("точка а должна быть в радиусе [0, 2*pi]")
else:
    randian = pi * a / 180
    print(f"радианов = {randian}")

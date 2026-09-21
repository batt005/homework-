a = float(input("Введите сторону прямоугольника A: "))
b = float(input("Введите сторону прямоугольника B: "))
c = float(input("Введите сторону квадрата C: "))
count_a = 0
temp_a = a
while temp_a >= c:
    temp_a = temp_a - c
    count_a = count_a + 1
count_b = 0
temp_b = b
while temp_b >= c:
    temp_b = temp_b - c
    count_b = count_b + 1
total_squares = 0
for i in range(count_b):
    total_squares = total_squares + count_a
print(f"Количество квадратов, размещенных на прямоугольнике: {total_squares}")

def PowerA234(A):
    B = A ** 2
    C = A ** 3
    D = A ** 4
    return B, C, D
numbers = [2.0, 3.0, 4.0, 5.0, 6.0]
for num in numbers:
    b, c, d = PowerA234(num)
    print(f"Число: {num} -> 2 ст. : {b:.2f}, 3 ст.: {c:.2f}, 4 ст.:{d:.2f}")

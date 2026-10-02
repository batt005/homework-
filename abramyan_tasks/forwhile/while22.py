n = int(input("Введите целое число N ( > 1 ): "))
is_prime = True
divisor = 2
while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
    divisor = divisor + 1
if is_prime:
    print("TRUE")
else:
    print("FALSE")

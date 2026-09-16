def DigitCountSum(K):
    count = 0
    sum = 0
    for i in str(K):
        count+= 1
        sum += int(i)
    return count, sum
print(DigitCountSum(1234567))

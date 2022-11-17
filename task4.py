a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum1 = 0
sum2 = 0
for i in a:
    sum1 += i
    for j in b:
        sum2 += j
print(sum1, 'min a = ', min(a))
print(sum2, 'min b = ', min(b))


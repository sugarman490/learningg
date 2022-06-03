i = 0
while i <= 5:
    print(i, end="")
    if i == 3:
        break
    i += 1
print("")
a = 0
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)

b = 0
sum1 = 0
while b <= 100:
    if b % 2 == 0:
        sum1 += b
    b += 1
print(sum1)

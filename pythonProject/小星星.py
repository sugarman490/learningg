i = 1
while i <= 5:
    print("*" * i, end="|")
    i += 1
print("")
i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

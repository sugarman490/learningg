i = 1
while i <= 9:
    j = 1

    while j <= i:
        x = i * j
        print("%d*%d=%d" % (j, i, x), end="\t")
        # \t是转义字符，能使垂直列对齐
        j += 1
    print("\"")
    i += 1

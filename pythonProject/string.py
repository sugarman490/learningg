str1 = "helloelel"
str2 = '我真的会“谢”'
print(str2)
print(str1[0])
for w in str2:
    print(w)
print(len(str2))
print(str1.count("el"))
print(str2.count("a"))
print(str2.index('“'))
print(str1.index("el"))
# 判断空字符
space_str = "     "
print(space_str.isspace())
space_str = "      a"
print(space_str.isspace())
space_str = "       \t\r\n"
print(space_str.isspace())
print("#判断数字")
num_str0 = "123"
print(num_str0.isnumeric())
print(num_str0.isdecimal())
print(num_str0.isdigit())
# 小数
num_str1 = "12.3"
print(num_str1.isnumeric())
print(num_str1.isdecimal())
print(num_str1.isdigit())
# unicode
num_str2 = "\u00b2"
print(num_str2)
print(num_str2.isnumeric())
print(num_str2.isdecimal())
print(num_str2.isdigit())
# 中文数字
print("")
num_str3 = "一千"
print(num_str3.isnumeric())
print(num_str3.isdecimal())
print(num_str3.isdigit())
print("查找")
hello_str = "hello world"
print(hello_str.startswith("hello"))
print(hello_str.startswith("Hello"))
print(hello_str.endswith("world"))
print(hello_str.find("llo"))
print(hello_str.find("a"))
print("替换")
print(hello_str.replace("world", "python"))
print(hello_str)  # replace不会修改原字符串
print("文本对齐")
poem = ["\t\nabcd",
        "abc",
        "aaaaa\t\n",
        "aaaaa"
        ]
for p in poem:
    print("|%s|" % p.strip().center(10, " "))
for p in poem:
    print("|%s|" % p.ljust(10, " "))
for p in poem:
    print("|%s|" % p.rjust(10, " "))
print("去除空白字符")
str3="  a  "
print(str3)
print(str3.strip())
#拆分和拼接
print("#拆分和拼接")
poem="aaaa\taaa\naaaaa\t"
print(poem.split())
poem1=" ".join(poem.split())
print(poem1)
#切片
print("切片")
num_str4="0123456789"
print(num_str4[2:6])
print(num_str4[2:])
print(num_str4[0:6])
print(num_str4[:6])
print(num_str4[:])
print(num_str4[::2])
print(num_str4[1::2])
print(num_str4[-1:])
print(num_str4[2:-1])
print(num_str4[-2:])
print(num_str4[-1::-1])#倒序
print(num_str4[::-1])








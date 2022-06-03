a = 1  # 看到赋值语句，首先把注意力放在等号右侧
print(id(a))
print(id(1))
b=a
print(id(b))
a=2
print(id(a))
print(id(b))
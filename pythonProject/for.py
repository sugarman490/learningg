for n in [1, 2, 3]:
    print(n)
else:
    print("循环结束")
for n in [1, 2, 3]:
    print(n)
    if n == 2:
        break
else:
    print("循环结束")
students = [
    {"name": "张三"},
    {"name": "李四"}
]
name="李四"
print("-" * 100)
for s in students:
    print(s)
    if s["name"] == name:
        print("找到%s了"%name)
        break
else:
    print("没有找到%s"%name)

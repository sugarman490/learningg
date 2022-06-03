# 元组元素不可修改
info_tuple = ("lisi", 10, 1.5, 10)
print(info_tuple)
print(type(info_tuple))
print(info_tuple[1])
single_tuple = (5)  # 整型
print(type(single_tuple))
single_tuple = (5,)  # 元组
print(type(single_tuple))
print(info_tuple.count(10))
print(info_tuple.index("lisi"))
for info in info_tuple:
    print(info)
print("名字叫%s，%d岁，身高%.2f米，%d岁" % info_tuple)
# 元组和列表的转换
list1 = list(info_tuple)
print(list1)
tuple1=tuple(list1)
print(tuple1)

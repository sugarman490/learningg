name_list = ["a", "b", "c"]
name_list2 = ["li", "wang"]
print(len(name_list))
# 取值
print(name_list[0])
print(name_list.index("b"))
# 修改
name_list[2] = "x"
print(name_list[2])
# 增加
name_list.append("c")
print(name_list)
name_list.insert(2, "z")
print(name_list)
name_list.extend(name_list2)
print(name_list)
# 删除
name_list.pop(3)
name_list.pop()
print(name_list)  # pop
del name_list[0]
print(name_list)  # del
name_list.remove("z")
print(name_list)  # remove
name_list2.clear()
print(name_list2)  # clear
#统计
name_list_len=len(name_list)
print("列表长度为%d"%name_list_len)
name_list.append("c")
print(name_list)
count=name_list.count("c")
count2=name_list.count("b")
print("c个数为%d，b个数为%d"%(count,count2))
name_list.remove("c")
print("remove删除第一个出现的数据：",end="")
print(name_list)
#排序
name_list.append("1")
name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list2=[1,3,5,2,4]
name_list2.reverse()
print(name_list2)
#迭代遍历
for name in name_list:
    print(name)

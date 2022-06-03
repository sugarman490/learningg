def test(num):
    print("函数内部%d对应的内存地址是%d"%(num,id(num)))
    result="hello"
    print("函数返回值的地址是%d"%id(result))
    return result
a=10
print("a变量保存数据的内存地址是%d"%id(a))
r=test(a)
print("%s的内存地址是%d"%(r,id(r)))
a=[1,12,3]
print(id(a))
a.append(4)
print(id(a))
a.remove(1)
print(id(a))
a.clear()
print(id(a))
a=[]
print(id(a))#内存地址变化，字典同理
print(hash(1))
print(hash("hello1"))
print(hash((1,)))
print(hash[1,2])
#字典中key必须是不可变类型（即除列表和字典）


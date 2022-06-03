import keyword

a = input("请随便输入：")  # input函数返回字符串类型
print(a)
print(type(a))

# 类型转换函数
a = 10.5
b = 10
c = "123"
print(int(a))
print(float(a))
print(int(c))
print(float(c))

# 买苹果演练
price = float(input("苹果价格："))
weight = float(input("苹果重量："))
money = price * weight
i = 1
i1 = 1000
print("顾客编号为%03d，苹果%.02f一斤，重量为%.02f斤，总价为%.02f" % (i, price, weight, money))
print("顾客编号为%03d，苹果%.02f一斤，重量为%.02f斤，总价为%.02f" % (i1, price, weight, money))
scale = 0.25
print("数据比例是%.02f%%" % (scale * 100))
# 查看关键字
print(keyword.kwlist)

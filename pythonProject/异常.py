def demo1():
    return int(input("请输入一个整数"))
def demo2():
    return demo1()
try:
    print(demo2())
except Exception as result:
    print("未知错误%s"%result)
else:#没有异常才会执行
    print("没有任何错误")
finally:#无论如何都会执行
    print("无论如何都会执行")

print("-"*50)
def input_password():
    password=input("输入密码：")
    if len(password)>=8:
        return password
    print("主动抛出异常")
    ex=Exception("密码长度不够")
    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)
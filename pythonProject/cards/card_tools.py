cardlist = []


def menu():
    print("*" * 50)
    print("欢迎使用名片系统！")
    print("1.创建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出")
    print("*" * 50)


def newcard():
    """新增名片"""
    print("*" * 50)
    card_p = {}
    name_str = input("姓名：")
    age = input("年龄：")
    phone = input("电话：")
    QQ = input("qq:")
    card_p["name"] = name_str
    card_p["age"] = age
    card_p["phone"] = phone
    card_p["QQ"] = QQ
    cardlist.append(card_p)
    print("%s的名片新建完成！" % name_str)


def showall():
    print("*" * 50)
    """显示所有名片"""
    if len(cardlist) == 0:
        print("目前没有名片,请先新建名片")
        return
    # for c in cardlist:
    # print("姓名：%s" % c["name"])
    # print("年龄：%s" % c["age"])
    # print("电话：%s" % c["phone"])
    # print("QQ：%s" % c["QQ"])
    # print("-"*50)
    for name in ["姓名", "年龄", "电话", "QQ"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for c in cardlist:
        print("%s\t\t%s\t\t%s\t\t%s" % (c["name"],
                                        c["age"],
                                        c["phone"],
                                        c["QQ"]))


def changecard(dict):
    action = input("选择操作：1修改 2删除 0返回")
    if action in ["1", "2"]:
        if action == "1":
            dict["name"]=input_card(dict["name"],"姓名：")
            dict["age"]=input_card(dict["age"],"年龄：")
            dict["phone"]=input_card(dict["phone"],"电话：")
            dict["QQ"]=input_card(dict["QQ"],"QQ：")
            print("修改完成")
        if action == "2":
            cardlist.remove(dict)
            print("删除完成")
    elif action == "0":
        return

    else:
        print("抱歉，没有该功能！")

def input_card(dic_val,tip):
    #判断修改时用户输入的内容
    inp=input(tip)
    if len(inp)==0:
        return dic_val
    else:
        return inp

def serchcard():
    print("*" * 50)
    name_str = input("请输入要搜索的姓名：")
    for c in cardlist:
        if c["name"] == name_str:
            for name in ["姓名", "年龄", "电话", "QQ"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (c["name"],
                                            c["age"],
                                            c["phone"],
                                            c["QQ"]))
            # TODO 修改和删除操作
            changecard(c)
            return
    else:
        print("没有此人的名片")

    """搜索名片"""

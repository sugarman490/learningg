import card_tools
while True:
    # TODO showmenu
    card_tools.menu()

    action = input("请选择希望执行的操作：")
    print("您选择的操作是：%s" % action)
    if action in ["1", "2", "3"]:
        if action == "1":
            card_tools.newcard()
        if action == "2":
            card_tools.showall()
        if action == "3":
            card_tools.serchcard()
    elif action == "0":
        print("欢迎再次使用")
        break
    else:
        print("抱歉，没有该功能！")
